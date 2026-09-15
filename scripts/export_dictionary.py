"""Export the distributed dictionary to a standalone searchable HTML file."""
from pathlib import Path
import csv
import html

root = Path(__file__).resolve().parents[1]
with (root/'documentation/Model_Data_Dictionary.csv').open(encoding='utf-8-sig',newline='') as f:
    rows = list(csv.DictReader(f))
cards = []
fields = [('definition','Definition'),('data_derivation','How it is derived'),
          ('contribution_to_model','What it provides to the model'),('recommended_unit','Units'),
          ('evidence_status','Evidence status'),('simulation_relationship','Simulation relationship and proposed repairs'),
          ('required_record_content','Required records'),('model_limit','Limitations'),('primary_source_url','Source URL')]
for row in rows:
    parts = ''.join('<dt>'+label+'</dt><dd>'+html.escape(row[key])+'</dd>' for key,label in fields)
    cards.append('<details><summary>'+html.escape(row['variable'])+' <small>'+html.escape(row['subsystem'])+'</small></summary><dl>'+parts+'</dl></details>')
page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Harris County Managed Retreat System Dynamics — Data Dictionary</title>
<style>body{font:17px/1.55 system-ui,sans-serif;color:#172a3a;background:#f4f6f8;max-width:1050px;margin:40px auto;padding:0 22px}h1{line-height:1.15}input{font:inherit;padding:12px;width:95%;border:1px solid #8293a3;border-radius:6px}details{background:white;padding:14px;margin:10px 0;border:1px solid #d8dfe5;border-radius:6px}summary{cursor:pointer;font-weight:650;overflow-wrap:anywhere}small{font-weight:400;color:#526575}dt{font-weight:650;margin-top:16px}dd{margin:3px 0;white-space:pre-wrap;overflow-wrap:anywhere}#count{color:#526575}</style>
<h1>Harris County Managed Retreat System Dynamics</h1><h2>Data dictionary · Version 0.1.0</h2>
<p>300 documented entries: definitions, derivations, model contributions, and evidence limits. Includes aliases, categories and settings. No executable or calibrated model is represented.</p>
<label for="search">Find a variable, subsystem, source, or concept</label><p><input id="search" type="search" placeholder="Search all entries…"></p><p id="count">300 entries</p><main>'''+''.join(cards)+'''</main>
<script>const cards=[...document.querySelectorAll('details')];document.querySelector('#search').addEventListener('input',e=>{const q=e.target.value.toLowerCase().trim();let n=0;for(const c of cards){c.hidden=!c.textContent.toLowerCase().includes(q);if(!c.hidden)n++;}document.querySelector('#count').textContent=n+' entries';});</script></html>'''
out = root/'results/generated/Model_Data_Dictionary.html'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(page)
print(out)
