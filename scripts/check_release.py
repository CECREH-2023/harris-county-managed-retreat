"""Validate the distributed development snapshot, not an executable model."""
from pathlib import Path
import csv
import json
import math
import sys
import zipfile
from collections import Counter
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
checks = []


def read(name):
    with (ROOT / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def check(name, condition):
    checks.append({'check': name, 'passed': bool(condition)})


def close(a, b):
    return math.isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-8)


dictionary = read('documentation/Model_Data_Dictionary.csv')
names = {r['variable'] for r in dictionary}
check('300 unique dictionary entries', len(dictionary) == len(names) == 300)
check('all entries have definition, derivation, contribution and evidence',
      all(all(r[k].strip() for k in ['definition', 'data_derivation', 'contribution_to_model', 'evidence_status']) for r in dictionary))
cross = read('reports/source_assessment/Variable_Source_Crosswalk.csv')
cross_names = {r['variable'] for r in cross}
check('all 295 assessment entries are covered', len(cross) == len(cross_names) == 295 and cross_names <= names)
check('five additional configuration entries', names - cross_names == {
    'Annual_Base_Funding', 'Annual_Post_Disaster_Funding', 'New_Retreat_Program_Enabled',
    'Planned_Caseworker_Capacity', 'Community_Opposition_Lookup'})
check('alias targets resolve', all(not r['alias_target'] or r['alias_target'] in names for r in dictionary))
links = read('documentation/Model_Dependency_Links.csv')
check('281 guide dependency records', len(links) == 281)
check('guide dependency endpoints resolve', all(r['input_variable'] in names and r['affected_variable'] in names for r in links))
catalog = read('reports/source_assessment/Potential_Source_Catalog.csv')
source_ids = {r['source_id'] for r in catalog}
check('62 external source families and one guide', len(catalog) == len(source_ids) == 63 and 'M01' in source_ids)
check('24 mind-map branches', len(read('reports/source_assessment/Mindmap_Source_Crosswalk.csv')) == 24)

parameters = read('data/Parameters.csv')
initials = read('data/Initial_Conditions.csv')
scenarios = read('scenarios/Scenario_Parameters.csv')
p = {r['variable']: r for r in parameters}
s = {r['variable']: r for r in initials}
check('30 parameters retain the documented evidence mix', len(parameters) == len(p) == 30 and Counter(r['evidence_status'] for r in parameters) == {'assumed':26, 'derived_proxy':3, 'observed':1})
check('22 stocks with 14 unavailable initial values', len(initials) == len(s) == 22 and sum(r['value'] == '' for r in initials) == 14 and all((r['value'] == '') == (r['evidence_status'] == 'unavailable') for r in initials))
check('24 settings across four scenarios', len(scenarios) == 24 and len({r['scenario_id'] for r in scenarios}) == 4)
check('all current inputs resolve to dictionary entries', all(r['variable'] in names for r in parameters + initials + scenarios))
check('parameter values fall inside retained sensitivity bounds', all(float(r['lower_bound']) <= float(r['value']) <= float(r['upper_bound']) for r in parameters))

panel = read('data/Population_Housing.csv')
keys = {(r['geoid_2020'],r['year']) for r in panel}
check('16725 unique tract-year observations', len(panel) == len(keys) == 16725)
check('1115 Harris County tract identifiers remain strings', len({r['geoid_2020'] for r in panel}) == 1115 and all(len(r['geoid_2020']) == 11 and r['geoid_2020'].startswith('48201') for r in panel))
check('2010 to 2024 panel years', {int(r['year']) for r in panel} == set(range(2010,2025)))

acs = {r['source_field']:r for r in read('data/ACS_2024_Estimates_MOE.csv') if r['geoid_2020'] == '48201'}
for variable, code in [('Community_Population','B01001_E001'),('Homeowners','B25003_E002'),('Renters','B25003_E003')]:
    check(variable + ' matches published county ACS estimate', close(s[variable]['value'], acs[code]['estimate']))
check('average household size matches published county estimate', close(p['Average_Household_Size']['value'],acs['B25010_E001']['estimate']))
migration = read('data/Domestic_Outmigration_2024.csv')[0]
numerator = float(migration['B07403_E010']) + float(migration['B07403_E013'])
rate = numerator / float(migration['B07403_E001'])
check('domestic outmigration derives from county B07403 counts', close(numerator,migration['domestic_outmigrants_people']) and close(rate,migration['domestic_outmigration_rate']) and close(rate,p['Base_Outmigration_Rate']['value']))

book = ROOT / 'Harris_County_Model_Data_Dictionary.xlsx'
with zipfile.ZipFile(book) as z:
    check('Excel ZIP integrity', z.testzip() is None)
    ns = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    wb = ET.fromstring(z.read('xl/workbook.xml'))
    sheet_names = [e.attrib['name'] for e in wb.findall('s:sheets/s:sheet',ns)]
    check('five documented workbook sheets', sheet_names == ['Dictionary','Equations','Sources','Current inputs','Conventions'])
    xml_text = '\n'.join(z.read(n).decode() for n in z.namelist() if n.endswith('.xml'))
    check('all dictionary names appear in the saved workbook', all(v in xml_text for v in names))
    check('workbook contains no executable spreadsheet formulas', all(b'<f>' not in z.read(n) and b'<f ' not in z.read(n) for n in z.namelist() if n.startswith('xl/worksheets/') and n.endswith('.xml')))

boundary = json.loads((ROOT / 'config/model_boundary.json').read_text())
check('model status remains unexecuted', boundary['vensim_run_completed'] is False and not list((ROOT / 'models').glob('*.mdl')))
result = {'version': '0.1.0', 'passed': sum(r['passed'] for r in checks), 'failed': [r['check'] for r in checks if not r['passed']], 'checks':checks,
          'scope':'Distribution, metadata consistency, and five selected Census/ACS derivations only; no Vensim, full upstream-data, calibration, or simulation validation.'}
print(json.dumps(result,indent=2))
sys.exit(bool(result['failed']))
