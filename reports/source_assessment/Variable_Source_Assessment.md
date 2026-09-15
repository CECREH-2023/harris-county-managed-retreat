# Harris County Managed Retreat Model: Comprehensive Variable Source Assessment

CECREH research development source assessment | 2026-09-10

## Findings and coverage

This assessment identifies 62 external source families and maps every one of the 215 entries in the existing variable dictionary. It adds 80 guide, alias, subscript and configuration entries, producing a 295-entry source register. These are not 295 independent empirical variables: some are calculated outputs, aliases or policy labels. All 24 major mind-map branches have an evidence route or an explicit scope gap.

The strongest existing foundation is the Harris County population, housing, parcel, flood, assistance and grant material already assembled from the user’s other projects and public sources. The largest remaining empirical needs are complete program case histories, actual staffing and spending, relocation follow-up, repeated process-trust/awareness measures, and ecological monitoring. Identifying a source does not mean its data have been acquired, matched to the model or used to estimate a parameter.

Rice’s Greater Houston Community Panel is a particularly useful new lead for social measures. Its catalog lists public-use survey waves, but obtaining the files requires a request. The codebook has been obtained and inspected. Texas A&M’s OneGulf work also identifies an existing Harris County buyout origin/destination dashboard whose underlying export and reuse availability need confirmation. [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj) [S35](https://idrt.tamu.edu/policy-decision-support/)

| Assessment route | Entries | Meaning |
| --- | --- | --- |
| Direct measurement candidate | 88 | Potential direct observations; some already local, others require retrieval or records requests. |
| Proxy or operational definition | 50 | A proxy, rubric or measurement instrument must be selected and validated. |
| Calibration or new longitudinal evidence | 50 | A response, delay or coefficient needs fitted longitudinal evidence or an uncertain prior. |
| Calculated model quantity | 23 | Derive from traceable inputs and validate the resulting quantity. |
| Scenario or policy choice | 26 | Set a transparent policy, scenario or numerical choice. |
| Alias to reconcile | 29 | Reconcile the name/scale to avoid duplicate parameters. |
| Notation or category; no separate data | 29 | A category, time index or unit label has no separate dataset. |

Use the report for the research decisions and complete variable appendix. Use Variable_Source_Crosswalk.csv to filter by subsystem, priority, evidence route and source access. Potential_Source_Catalog.csv supplies URLs, geography, period, local material and limitations. Guide_Inventory_Reconciliation.csv preserves the naming audit; Mindmap_Source_Crosswalk.csv preserves the wider conceptual scope.

## Scope and evidence standard

The authoritative inputs are Ali’s “Managed Retreat System Dynamics Model.docx” and “Mind Map Oct 15 2024.pdf,” together with the existing implementation dictionary and source manifest. The literature matrix is a separate project and is excluded. The working application is Harris County, with a 2024 reference year, 2010–2024 historical calibration window and proposed 2025–2050 scenarios. Smaller communities, cities and watersheds require explicit geographic crosswalks; Harris County is not one municipal tax jurisdiction.

The review compared the full DOCX paragraphs and tables with the original dictionary, inspected the mind map visually, checked the assembled local files, and searched official agency, university and primary research sources. Searches of the relevant Harris County, Managed Retreat, Hydrologic Determinants and Texas GLO projects prioritized reuse. Absence from the inspected files is not a claim that no copy exists anywhere on the drive.

Source descriptions distinguish local files, an accessible source or codebook, a request-only route, a restricted dataset, and a research lead whose full text or export was not verified. Recommendations for scoring, fitting and linking are proposed analytical uses; they are not claims made by the source publisher. No records request or email has been submitted and no household survey has been conducted for this report.

The original inventory contains 22 stocks, 19 flows, 22 auxiliaries, 30 parameters and 122 unresolved references. The full guide contributes omitted delay outputs, lookup functions, climate and spatial extensions, scenario selectors and plain-text controls. Nineteen underscore tokens are filenames or generic placeholders and are excluded from the variable-source register while retained in the reconciliation. “caseworkers_equivalent” remains visible as a unit-label error. “Equity_Improvements” is labeled an auxiliary but is used as a flow in the conceptual equations.

## Reuse the existing Harris County package first

| Existing material | What it can supply | Important boundary |
| --- | --- | --- |
| ACS panel and 2024 extracts | Population, tenure, household size, income/housing context. | Overlapping 5-year estimates; population and household counts differ. |
| 2024 HCAD accounts and parcels | Property inventory, value, lot area and taxing-jurisdiction links. | Taxable value must reflect jurisdiction exemptions; properties are not households. |
| NFHL, NSI and physical/event files | Exposure inventory, structure characteristics and historical hazard context. | March 2026 NFHL is not a historical 2024 flood-zone map. |
| NFIP and IHP panels | Payments and applicant/insured-loss evidence. | Selected coverage; cannot stand in for all properties or total losses. |
| HCD reports, FEMA HMA and GLO QPR extracts | Acquisitions, program chronology and financial/accomplishment context. | Different reporting views may refer to the same award/property. |
| County budgets and HCFCD maintenance material | Funding and institutional context. | Authorized budgets/positions are not actual available cash, program FTE or unit costs. |
| H-GAC forecasts and changed parcels | Future growth assumptions and development context. | Forecasts are scenarios, not observed migration or new-build completions. |

The implementation report still distinguishes a prepared data package from a calibrated model: 26 of 30 parameters remain assumed and 14 of 22 stock initializations are missing. No executable .mdl was found. The prior 118-pass validation concerns the data build, not empirical adequacy of every equation. This source assessment does not change those statuses.

Retain the existing HCD 2025 Q2 acquisition discrepancy in the gap queue: the listed statuses sum to 427 while the reported total is 425. Do not use that total as a clean calibration target until the two-case difference is resolved. Likewise, preserve both spatial exposure definitions: any parcel overlap and representative-point membership answer different questions. Existing source hashes and original files should remain unchanged.

## Where the evidence is strongest by subsystem

| Subsystem | Recommended evidence route | Main unresolved need |
| --- | --- | --- |
| Hazard and risk | HCAD/NSI + dated flood maps; NOAA/HCFCD/USGS events and gauges; TWDB and LOCA2/NOAA scenarios. [S05](https://hcad.org/pdata/pdata-property-downloads.html/) [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation) [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts) [S11](https://www.twdb.texas.gov/flood/planning/data.asp) [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states) | Historical exposure and total-damage denominators; a physical climate-to-hazard relationship. |
| Community and population | ACS/PEP/IRS for stocks and flows; GHCP for social measures; program destination records. [S01](https://api.census.gov/data/2024/acs/acs5/groups.html) [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf) [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data) [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj) | Gross moves by tenure and boundary; longitudinal social-capital and attachment responses. |
| Fiscal | Taxable rolls, audited funds, grant ledgers and paid contracts. [S05](https://hcad.org/pdata/pdata-property-downloads.html/) [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports) [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County) [S29](https://purchasing.harriscountytx.gov/) | Spendable balances, source-of-funds deduplication, actual marginal costs and a common dollar year. |
| Governance | Policy milestones, case/outreach records and process-specific resident measures. [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs) [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request) [S28](https://harriscountytx.legistar.com/Calendar.aspx) [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html) | Transparent rubrics and repeat measures; public meeting counts do not identify trust or capacity effects. |
| Implementation | Complete case-stage, FTE and payment ledgers; recipient and destination follow-up. [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request) [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests) [S35](https://idrt.tamu.edu/policy-decision-support/) | Pending/withdrawn cases, actual staff effort, tenant households and durable relocation outcomes. |
| Equity and wellbeing | Household cross-tabs, GHCP, program disparities, qualitative evidence and relevant consultation. [S03](https://www.census.gov/programs-surveys/acs/microdata.html) [S17](https://www.huduser.gov/portal/datasets/cp.html) [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj) [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content) [S46](https://egis.hud.gov/TDAT/) | Nonoverlapping vulnerable households; agreed equity measures; locally meaningful cultural indicators. |
| Land and ecosystems | Acquired polygons, accepted contracts, WEB/bank monitoring, NLCD/NWI/TCEQ and physical service models. [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests) [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program) [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks) [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data) [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html) [S52](https://data.naturalcapitalproject.stanford.edu/) | Restored versus cleared hectares, comparable costs, ecological trajectories and nonoverlapping benefits. |

## Rice GHCP: specific measures worth requesting

The inspected catalog lists waves 2301, 2303, 2304, 2401, 2403 and 2404 plus an empanelment file. It does not list every wave discussed in the codebook; in particular, availability of health waves 2302 and 2402 was not confirmed. Request the listed waves required for the chosen measures, the corresponding weights and a supported respondent linkage. Confirm how Harris County respondents can be selected from public files, which omit geocodes. [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

| Model use | Verified codebook fields | Location / interpretation |
| --- | --- | --- |
| Social cohesion | g2304_ppcare; g2304_pptrusted; g2304_pphelp; g2304_closeknit; g2304_ppnotalong; g2304_italktopp | PDF pp. 129–130. Validate scale construction and reverse coding; not a ready guide-specific stock. |
| Residence and attachment | g2304_yrsneigh; g2403_hmneigh | PDF pp. 128 and 170. Duration is banded; feeling at home is a limited attachment proxy. |
| Wellbeing | g2404_satlife; g2404_sathome; g2404_satsoclife; g2404_satfinance | PDF pp. 179–180. Keep global life satisfaction distinct from domain satisfaction. |
| Psychological distress | g2404_nervous; g2404_hopeless; g2404_restless; g2404_depressed; g2404_effort; g2404_worthless | PDF pp. 180–181. K6 items; check missingness and scoring before deriving 0–24 total. |
| Social support | g2404_facetoface; g2404_emailphone; g2404_feelclose; g2404_callhelp | PDF pp. 182–183. Select a consistent support construct and retain response categories. |
| Storm and recovery context | g2403_stleavehm; g2403_stmenhlth; g2403_stmedcare; g2403_stnofood; g2403_hbrecovery | PDF pp. 159 and 166. These are storm-related self-reports, not buyout-treatment outcomes. |

Use the applicable wave weights (gYYnn_rweight or documented alternatives), not raw sample means. Treat .a/.b/.c and suppressed -2 values according to the codebook. Neighborhood trust and school/media trust must not be relabeled as trust in the buyout process. The listed park-payment willingness-to-pay fields are suppressed, so they are not a verified public source for Recreation_Value. Proposed rescalings and composite weights require validation; public survey availability alone does not calibrate the model’s causal response functions. [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

The Texas A&M/Texas Appleseed Phase 1 study contributes local qualitative evidence from interviews with 20 residents of the mandatory program. It is useful for refining process, support and fairness constructs, but it cannot supply representative participation probabilities. The separate OneGulf dashboard is a promising origin/destination data lead; request its data dictionary, coverage, linkage method and reuse terms before relying on exports. [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content) [S35](https://idrt.tamu.edu/policy-decision-support/)

## Acquisition priorities and concrete request specifications

P0 means resolve a definition, boundary, alias or scenario decision before parameterization. P1 identifies first-phase acquisition and baseline work. P2 identifies longitudinal calibration, validation and optional extensions. The register gives one priority to each entry; this is not a ranking of social importance.

### 1. Assemble the program case ledger

Request separate HCD and HCFCD exports for historical cohorts through 2024, with later status dates where needed to observe completion. Ask for stable deidentified case/property/household links; program and award identifiers; initial interest, formal application, eligibility, offer, acceptance/refusal, withdrawal/denial, closing, demolition and move dates; status and reason codes; owner-occupant/absentee-owner/renter distinctions; occupied units and resident household/person counts; assistance components and valuation basis; duplication-of-benefits amounts; and sufficiently aggregated origin/destination geography. Keep pending and failed cases. Names, contact details and exact destination addresses are not needed for the proposed register. These are proposed fields, not verified contents of an existing public export. [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request) [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

Request accompanying monthly filled FTE/allocated hours, caseloads, contractor effort, outreach dates and reach, support referrals/receipt, complaints and appeals. Link actual receipts, commitments and paid expenditures to awards and cost categories. A program data dictionary and explanation of changes in status coding are as important as the rows. Use the HCD and HCFCD official request routes and procurement records as appropriate; this report prepares the specifications without submitting them. [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request) [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests) [S29](https://purchasing.harriscountytx.gov/)

### 2. Obtain existing social and relocation research data

Request the relevant GHCP public-use waves and weights through Rice’s catalog form. Seek the OneGulf origin/destination dataset or an aggregate export with dates, program coverage, geocoding/selection rules and destination-risk definitions. Ask whether appropriate aggregate evidence from the Phase 1 buyout research is available. If no public data measure awareness, willingness or process trust for eligible households, design a targeted survey including nonparticipants and refusals. [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj) [S35](https://idrt.tamu.edu/policy-decision-support/) [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)

### 3. Complete land, cost and ecological histories

Request acquired parcel polygons with closing/restriction status; restoration treatment and accepted completion footprints; demolition, decontamination, utility/road retirement and maintenance dates; invoices by cost component; and monitoring protocols/results with reference sites. Record area in hectares after removing geometric overlap. Separate purchase, clearance, restoration and ecological maturity. Use WEB, wetland-bank and TCEQ evidence to identify relevant monitoring and compare treatments, not to presume every buyout parcel was restored. [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests) [S29](https://purchasing.harriscountytx.gov/) [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program) [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks) [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)

### 4. Acquire only missing public supplements

After matching the existing manifest, add the required ACS household tables/PUMS, PEP components, IRS migration, CHAS, appropriate price indices and tax/financial histories. Retrieve dated flood/gauge data and climate ensembles only for the defined mechanisms. NLCD, NWI, shoreline data and wildfire inputs are conditional on the land/hazard scope. USPS vacancy data require eligible access; no replacement dataset should be described as equivalent without checking its meaning. [S01](https://api.census.gov/data/2024/acs/acs5/groups.html) [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf) [S03](https://www.census.gov/programs-surveys/acs/microdata.html) [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data) [S17](https://www.huduser.gov/portal/datasets/cp.html) [S18](https://www.huduser.gov/portal/datasets/usps.html) [S31](https://www.bls.gov/cpi/data.htm) [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data) [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download) [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)

### 5. Close the remaining longitudinal gaps

A proposed baseline and 6-, 12- and 24-month household follow-up can measure housing stability, affordability, risk, ties, distress, access and satisfaction. Include appropriate comparison households, support exposure, attrition and response weights. This is a research-design proposal, not a claim that a public dataset already exists. Estimate only parameters the data can identify; keep the rest as explicitly uncertain priors and use sensitivity analysis. Do not infer causal support or displacement effects from a single cross-section.

## Definitions and equation repairs that affect data requirements

Population, households, properties and structures need distinct stocks and conversion factors. A bought-out property can contain multiple households, and a move inside Harris County does not reduce county population. Specify whether managed-retreat moves are excluded from general outmigration and whether “Relocated_Households” records moves or successful longer-term outcomes.

Use household-based vulnerability measures. B22010_003E + B22010_006E provides households with a disabled member, and B11007_002E provides households with someone aged 65 or older. These still overlap with low-income and racial/ethnic group counts. Use weighted household microdata for their union or retain separate indicators. A person-level poverty/race table is not a household count. [S01](https://api.census.gov/data/2024/acs/acs5/groups.html) [S03](https://www.census.gov/programs-surveys/acs/microdata.html)

Use a coherent fiscal perspective: annual cash flows versus cumulative balances, real versus nominal dollars, taxable value versus revenue, and social resource costs versus transfers. Avoided future damage must be measured against a counterfactual. Past disaster costs are sunk costs, and aid/insurance may finance a loss already counted elsewhere. Verify the relevant benefit-cost policy and discount convention before numerical use. [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County) [S31](https://www.bls.gov/cpi/data.htm) [S32](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)

Repair dimensional inconsistencies before fitting: funding divided by price yields properties, not properties/year, unless a budget-release interval is included. Restoration backlog yields hectares, not hectares/year, until divided by a completion time. The application equation also needs a per-year attempt-rate term. Define the conversion between support FTE/visits and changes in wellbeing or stress scores. Bound probability/score outputs and preserve stock-flow conservation.

Replace identity-conditioned attachment, trauma and inequity multipliers with relevant measured constructs, co-designed protections or transparent policy alternatives. Localize “Provincial_Funding” to state funding while separating federal pass-throughs. Align climate scenarios: CMIP6 SSP projections are not simply renamed RCP scenarios. Correct the guide’s description of 0.125 years as quarterly; a quarter-year is 0.25 years. These are specification issues rather than missing downloads.

## Files needed to turn the sources into simulation inputs

| Proposed file / existing location | Purpose and acceptance rule |
| --- | --- |
| documentation/Source_Manifest.csv (existing) | Add newly acquired artifacts only after access, provenance, reference date, checksum and licensing/terms are recorded. |
| data/processed/program_case_panel.csv (proposed) | Unique case/property/household links, stage dates and censoring; reconcile program totals and duplicate grants. |
| data/processed/program_finance_staff_panel.csv (proposed) | Period/fund/FTE/cost-category data; reconcile opening + receipts − spending to closing balances. |
| data/processed/social_measure_panel.csv (proposed) | Instrument, item, weight, geography, wave, score and uncertainty; retain missing/suppressed codes and sample limitations. |
| data/processed/land_restoration_panel.csv (proposed) | Dated acquisition, treatment, area, cost and monitoring; unique-area and cohort checks. |
| data/processed/hazard_exposure_panel.csv (proposed) | Historical dated exposure/intensity with a common property denominator; separate scenarios from observations. |
| Parameters.csv / Scenario_Parameters.csv / Lookup_Tables.xlsx (existing or proposed model inputs) | Values, units, source IDs, empirical/assumed status, uncertainty and scenario labels; no source discovery automatically overwrites parameters. |
| Calibration_Data.xlsx and stock initialization table | Observed targets and opening balances with coverage flags; missing is not zero. |
| Managed_Retreat_Main.mdl (still needed) | Executable equations, aliases and units reconciled; dimensional, extreme-condition, conservation and numerical checks before calibration. |

The accompanying registers are source-discovery deliverables. They do not certify acquisition of every dataset, resolution of every model definition, or a working simulation. Every original dictionary entry is nevertheless accounted for, including those whose honest evidence route is a records request, a newly designed measure, a calculated result or an explicit scenario choice.

## Appendix A. Complete variable and configuration source register

D direct candidate; P proxy/definition; K calibration; C calculated; S scenario; A alias; N notation/category. Source IDs link to Appendix C.

### Hazard

**Active_Hazards** — C; P2; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Count hazards exceeding defined thresholds within an explicit joint-event time and spatial window. A simple count does not estimate compounding damage or account for dependent mechanisms.

**Actual_Hazard_Risk** — C; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf)
Select a physical or expected-loss risk measure from hazard intensity, exposure and vulnerability. Define risk separately from exposure and retain uncertainty rather than imply perfect knowledge.

**Average_Damage_Fraction** — K; P1; [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Estimate loss-to-matched-value ratios by depth and building class; check uninsured losses using inspections. Claims selection and limits bias observed ratios; total destruction is a separate outcome.

**Average_Destruction_Rate** — K; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S58](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
Estimate event-specific total-loss fractions from damage inspections and exposure inventories; pool by building/event severity. Neither claims frequency nor mean loss fraction measures total destruction; preserve denominator uncertainty.

**Base_Hazard_Frequency** — D; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/)
Count independent threshold-defined historical floods divided by exposure years; compare gauge exceedances. Choose a sufficiently long reference period; the 2010–2024 window alone may not stabilize rare-event frequency.

**CC_Impact_Increase_Rate** — C; P2; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [M01]
Derive the annual change in the explicitly chosen climate driver/index from scenario trajectories. Do not extrapolate a constant index increment across scenarios without physical justification.

**CC_Impact_Rate** — A; P1; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Reconcile to CC_Impact_Increase_Rate; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**CC_Sensitivity_Parameter** — K; P2; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [S10](https://api.waterdata.usgs.gov/docs/)
Fit the relationship between the chosen climate driver and hazard frequency/intensity using scenario ensembles. Guide range is a prior; climate index scaling changes the parameter's meaning.

**Climate_Change_Impact_Index** — P; P0; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Prefer scenario-specific precipitation/extreme-flow/sea-level changes; only construct an index after documenting normalization. No public dataset measures this guide-specific 0–100 stock; warming is not automatically linear flood risk.

**Climate_Change_Multiplier** — C; P1; [S10](https://api.waterdata.usgs.gov/docs/), [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Estimate future-to-baseline hazard frequency/intensity ratios for each scenario and ensemble member. Choose the physical endpoint; do not apply a precipitation percentage directly as a damage multiplier.

**Coastal_Erosion** — D; P2; [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change), [S05](https://hcad.org/pdata/pdata-property-downloads.html/)
Use bay-shoreline transect change rates and property locations if this optional hazard is retained. Do not apply open-Gulf beach rates to Harris County bay frontage or all inland properties.

**Compounding_Effect_Multiplier** — K; P2; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Estimate joint-hazard excess losses with event dependence, spatial overlap and conditional vulnerability. Guide increment 0.3 per added hazard is illustrative and can double count correlated flood mechanisms.

**Cumulative_Hazard_Events** — C; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/)
Accumulate distinct qualifying event clusters from a declared start year; initialize with pre-baseline history if required. NOAA event rows are not independent storms; cumulative counts depend on the chosen origin.

**Current_CC_Impact** — A; P1; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Reconcile to Climate_Change_Impact_Index at the chosen reference date; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Hazard_Event_Rate** — K; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)
Estimate exceedance frequency for defined events; calibrate projected changes using climate-hydrology relationships. Separate historical random variability, exposure change and climate trend; avoid duplicate storm counts.

**Hazard_Exposure** — C; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Compute comparable hazard-specific exposed inventories with dated footprints and common property keys. Keep hazard-specific intensity and probability separate from the exposed-property count.

**Hazard_Exposure_Index** — C; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)
Compute an explicitly scaled exposed-property share and intensity measure from the selected hazard definition. Guide multiplication by a zero climate index erases baseline risk; revise before calibration.

**Hazard_Perception_Delay** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Estimate lag between documented hazard exposure/information and repeated perceived-risk reports. The guide 1–3 years is an illustrative prior; panel timing must identify the lag.

**Hazard_Severity_Factor** — P; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf)
Define severity from depth, duration, velocity or expected loss relative to a reference event. A single countywide severity factor can obscure different mechanisms and exposed structure types.

**Initial_CC_Impact** — A; P1; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Reconcile to Climate_Change_Impact_Index at the chosen reference date; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Initial_Properties** — A; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Reconcile to Properties_at_Risk at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Initial_Properties_at_Risk** — A; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Reconcile to Properties_at_Risk at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Initial_Properties_in_Hazard_Zone** — A; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Reconcile to Properties_at_Risk at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**New_Development** — A; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S15](https://www.h-gac.com/regional-growth-forecast), [S58](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
Reconcile to New_Development_in_Risk_Zone by land-user group; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**New_Development_in_Risk_Zone** — D; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S15](https://www.h-gac.com/regional-growth-forecast), [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data), [S58](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
Link dated new structures/accounts and land-use changes to contemporaneous hazard zones. Current map overlays confound historical development and subsequent mapping changes.

**Perceived_Hazard_Risk** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Use repeated flood-specific perception questions and fit the lag relative to hazard evidence. Smooth actual risk only as an explicit hypothesis; validate perception lag and score scaling.

**Properties_at_Risk** — D; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Intersect dated residential accounts/structures with the chosen hazard footprint; count distinct eligible properties at baseline. Freeze parcel/structure definitions and map vintage; any-overlap and point-in-zone counts differ.

**Properties_Destroyed** — K; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S58](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
Use validated substantial/total-damage assessments and demolition records by event with exposed-property denominators. Claims are not destruction counts; destruction need not remove a parcel permanently from the risk stock.

**Random_Variation** — K; P2; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S10](https://api.waterdata.usgs.gov/docs/), [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)
Estimate residual variability after defining event frequency/trend; store random seed and distribution choices. A normal additive draw may create negative hazard rates; use suitable bounded/count processes.

**Sea_Level_Rise** — D; P2; [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Use a dated NOAA local relative sea-level scenario as a coastal boundary driver. Avoid double counting subsidence if already incorporated in the relative scenario.

**SLR_Projection_Table** — D; P2; [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Extract official local scenario height trajectories with datum, baseline, units and scenario provenance. Do not relabel NOAA scenarios as RCP/SSP without an explicit justified mapping.

**Total_Hazard_Exposure** — C; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Union property exposure across hazards or aggregate expected losses under a joint model. Summing overlapping exposure indices double counts properties and mixes incompatible units.

**Total_Hazard_Zone_Area** — D; P0; [S06](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Union the selected dated hazard-zone polygons within the model boundary using an area-preserving projection. Do not sum overlapping flood mechanisms; distinguish regulatory zone from event footprint.

**Total_Properties** — D; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Count deduplicated in-scope residential properties using the same account/structure convention as Properties_at_Risk. Do not mix all-property denominator with residential-only exposure or structures with parcels.

### Community

**Average_Household_Size** — D; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Use B25010 for general baseline; use actual owner/renter household sizes for retreat cohorts. County average 2.73 in the retained 2024 input is not necessarily the size of households in acquired properties.

**Base_Outmigration_Rate** — D; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Estimate gross annual exits divided by the matching origin population at risk; reconcile ACS/IRS coverage. Baseline rates already reflect prevailing hazards/attachment; normalize modifiers to avoid suppressing observed flows twice.

**Births** — D; P1; [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Use county population-estimates annual births; obtain subcounty records/approved allocations if the model boundary is smaller. County totals cannot be assigned proportionally to neighborhoods without uncertainty.

**Community_Attachment_Factor** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S38](https://research.fs.usda.gov/treesearch/23746)
Fit attachment-related retention or application behavior using measured place identity/dependence and residence duration. Guide weights 0.3/0.4/0.3 are illustrative; test collinearity with social capital and bounds.

**Community_Cohesion_Preservation** — P; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S38](https://research.fs.usda.gov/treesearch/23746), [S35](https://idrt.tamu.edu/policy-decision-support/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure retention of social ties and neighborhood cohesion among relocated households and their origin networks. Co-location of destinations is a proxy, not proof of preserved relationships.

**Community_Population** — D; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Use B01001 total or county population estimates for a fixed boundary; reconcile reference date and group quarters. A retreat neighborhood and Harris County require different geographic denominators.

**Community_Social_Capital** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S34](https://www.socialcapital.org/), [S38](https://research.fs.usda.gov/treesearch/23746)
GHCP wave 2304 cohesion items: ppcare, pptrusted, pphelp, closeknit, ppnotalong and italktopp; use Atlas as a separate contextual comparator. Validate scoring, reverse coding and geographic fit; no observed guide-specific 0–100 stock exists.

**Deaths** — D; P1; [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Use annual county deaths in population-estimates components; align boundary and reference year. Do not interpret all deaths as hazard mortality; keep event deaths as a separate subset if needed.

**Displacement_Stress_Factor** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Estimate how displacement changes social cohesion after controlling baseline ties and concurrent hazard impacts. No independent public coefficient identified; guide units and model response require explicit definition.

**Hazard_Pressure_Multiplier** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data)
Relate measured perceived/actual risk to subsequent moves, controlling baseline migration and economic conditions. The factor 2 in the guide is not estimated evidence; distinguish risk perception from exposure.

**Homeowner_Outmigration** — K; P2; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data)
Use mobility microdata to benchmark household flows; seek longitudinal prior-tenure evidence to identify homeowner exits. Public ACS/PUMS current tenure does not identify prior-tenure household transitions; IRS has no tenure field.

**Homeowner_Retreat** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Count actual owner-occupant households moving through completed retreat cases. An owner can sell without residing at the property; do not infer household exits from purchases.

**Homeowners** — D; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
B25003 owner-occupied households; use occupancy/tenure records to subset the retreat population. Property owners, owner-occupied households and HCAD accounts differ; exclude absentee owners from resident counts.

**Immigration** — D; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Estimate gross incoming migration across the model boundary using ACS/IRS origin-destination data. PEP net international/domestic migration does not identify all gross arrivals.

**Initial_Homeowners** — A; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Reconcile to Homeowners at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Initial_Population** — A; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Reconcile to Community_Population at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Initial_Renters** — A; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Reconcile to Renters at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Managed_Retreat_Relocations** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S35](https://idrt.tamu.edu/policy-decision-support/)
Count actual people moving in retreat cases, with date and destination relative to the model boundary. Properties times mean household size is only a fallback; successful resettlement is distinct from moving.

**New_Homeownership** — K; P2; [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S15](https://www.h-gac.com/regional-growth-forecast)
Estimate ownership entry and tenure transitions using repeated or longitudinal housing data; benchmark net stock change. Successive ACS cross-sections do not uniquely identify gross tenure transitions.

**New_Renters** — K; P2; [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S15](https://www.h-gac.com/regional-growth-forecast)
Estimate new renter-household entries and tenure transitions using appropriate household-flow evidence. Net renter-stock change cannot distinguish new household formation, migration and tenure switching.

**Outmigration** — D; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S04](https://www.irs.gov/statistics/soi-tax-stats-migration-data), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Use origin-based ACS migration and IRS county outflows; separate moves crossing the model boundary from within-boundary moves. PEP provides net migration, not gross exits; identify retreat moves to avoid counting them twice.

**Perceived_Safety** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Collect flood-specific perceived safety at origin and destination; compare with mapped/observed risk. GHCP general housing/neighborhood safety may concern crime; use exact wording before treating it as flood safety.

**Place_Attachment_Index** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S38](https://research.fs.usda.gov/treesearch/23746), [S46](https://egis.hud.gov/TDAT/)
Use GHCP g2403_hmneigh as a limited proxy; preferably collect adapted place-identity/dependence items. Years of residence and Indigenous identity cannot justify automatic attachment coefficients.

**Population_Decline_Rate** — C; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S02](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Calculate negative population change relative to a consistent baseline, separating migration and natural change. Overlapping ACS estimates smooth changes; an algebraic decline measure is not itself a causal driver.

**Renter_Displacement** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S37](https://floodregistry.rice.edu/)
Record tenant departures, cause, timing and destination after acquisition or hazard damage. Tenant moves may precede closing and be absent from owner-only acquisition data.

**Renter_Retreat** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Count renter households actually relocating through retreat assistance, linked to property and move dates. Separate voluntary moves, eviction/displacement and program-supported relocation.

**Renters** — D; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
B25003 renter-occupied households; verify tenants per acquired structure using program records. An acquired multifamily property can house multiple renter households.

**Social_Capital** — A; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S34](https://www.socialcapital.org/)
Reconcile to Community_Social_Capital; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Social_Capital_Building** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S34](https://www.socialcapital.org/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Estimate longitudinal cohesion/network gains following local organization and support activity. Do not infer annual growth from one cross-sectional Atlas score or meeting count.

**Social_Capital_Erosion** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S37](https://floodregistry.rice.edu/)
Estimate within-person/community change in cohesion after displacement using repeated observations and comparison populations. Cross-sectional scores and qualitative interviews do not identify an annual erosion coefficient.

**Total_Households** — D; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html)
Use B25003 total occupied housing units/households for the reference geography; reconcile eligible program household denominator. Housing units include vacancies; total persons divided by a rounded household size is only an approximation.

**Years_of_Residence** — D; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html)
Use GHCP g2304_yrsneigh, ACS B25038 move-in bands or direct household residence histories. Neighborhood tenure and years in the current dwelling differ; interval-coded durations are not exact years.

### Fiscal

**Annual_Disaster_Damage_Costs** — K; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S07](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation), [S31](https://www.bls.gov/cpi/data.htm)
Estimate event losses from depth/structure curves, checked against observed claims and assessments, then annualize. Insured/applicant losses are incomplete; calibrate selection and structure-value basis.

**Average_Property_Value** — D; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S16](https://www.fhfa.gov/data/hpi/datasets), [S31](https://www.bls.gov/cpi/data.htm)
Calculate mean cohort-specific appraisal/purchase-basis value, reporting median and distribution; deflate consistently. Do not mix assessed taxable, market, replacement and post-disaster values.

**Base_Compensation_Rate** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Define the base appraisal-linked offer ratio before explicitly justified assistance supplements. Verify historical policy version and valuation basis; future ratios are scenario decisions.

**Budget_Constraint** — S; P0; [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [M01]
Specify the available budget envelope and release schedule for each scenario and funding source. Match stock versus annual flow and prevent commitments from being treated as available cash.

**Budget_Gap** — C; P1; [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Compute matched annual operating obligations minus recurring revenues for the chosen jurisdiction/fund. Do not include the same service costs again in the fiscal-stress numerator.

**Buyout_Payments** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S29](https://purchasing.harriscountytx.gov/), [S31](https://www.bls.gov/cpi/data.htm)
Sum paid acquisition compensation by payment date, separating purchase, relocation and supplemental components. Award amount is not payment; retain household/property and grant links for deduplication.

**Compensation_Rate** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Estimate historical purchase payment relative to the specified appraisal basis; define alternative policy schedules separately. A category selector cannot be multiplied as if it were a numeric compensation rate.

**Compensation_Type_Selector** — A; P1; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [M01]
Reconcile to Compensation_Rate policy schedule; use the same source, definition, baseline and units. Map each category to a documented appraisal basis/rate; do not multiply an arbitrary category number.

**Cost_Benefit_Ratio** — C; P0; [S32](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S52](https://data.naturalcapitalproject.stanford.edu/)
Compute discounted incremental avoided losses and eligible benefits divided by incremental retreat costs relative to a counterfactual. Past sunk disaster costs are not future benefits of a new buyout; prevent administrative-cost double counting.

**Cumulative_Disaster_Costs** — C; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S31](https://www.bls.gov/cpi/data.htm)
Accumulate reconciled event losses in constant dollars from a stated starting year. Do not add insurance, aid and reported property damage as independent costs; all may describe the same loss.

**Disaster_Costs** — A; P1; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf)
Reconcile to the declared annual or cumulative disaster-cost quantity; use the same source, definition, baseline and units. Specify annual versus present-value/cumulative units before adding to the objective.

**Discount_Rate** — S; P0; [S32](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf), [M01]
Choose the documented rate applicable to the analysis/award and report sensitivity across justified alternatives. Verify rule/version at use; keep real discount rates with real dollars and nominal rates with nominal dollars.

**Enhanced_Compensation_Option** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Compensation schedule categories; specify eligible components, appraisal date and rate. Category label, not a numeric observation or an extra downloadable dataset.

**Equity_Adjustment** — A; P1; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Reconcile to Equity_Adjustment_Factor; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Equity_Adjustment_Factor** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S17](https://www.huduser.gov/portal/datasets/cp.html)
Define policy assistance supplements based on documented needs/eligibility and test alternatives. Normative policy choice; do not fit identity-based compensation penalties as natural laws.

**Federal_Funding** — D; P1; [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S24](https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories), [S30](https://api.usaspending.gov/docs/endpoints), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Trace federal receipts/disbursements by award and year from grant ledgers with transaction checks. USAspending obligations and local receipts must not be pooled without reconciliation.

**Federal_Funding_Availability** — S; P1; [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S24](https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories), [S30](https://api.usaspending.gov/docs/endpoints), [S26](https://budget.harriscountytx.gov/budget.aspx)
Use award-specific historical annual receipts as baseline and explicit future funding scenarios. Future federal appropriations are uncertain policy inputs, not values recoverable from a past average alone.

**Funding** — A; P0; [S26](https://budget.harriscountytx.gov/budget.aspx), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [M01]
Resolve whether the optimization constraint means spending, required funding or available balance. Do not silently equate Funding with Funding_Available; select and document the quantity.

**Funding_Available** — A; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S26](https://budget.harriscountytx.gov/budget.aspx)
Reconcile to Retreat_Funding_Available; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Future_Disaster_Costs_NPV** — C; P1; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S32](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)
Discount scenario-specific future annual losses over the declared horizon with exposure growth and uncertainty. Model no-retreat and retreat counterfactuals separately; do not treat a gross loss forecast as avoided loss.

**Homeowner_Compensation_Avg** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Compute paid purchase and supplemental assistance separately for owner-occupants and absentee owners. Compare asset compensation and rehousing adequacy on appropriate denominators.

**Initial_Assessment_Value** — A; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Reconcile to Municipal_Tax_Base at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Insurance_Payouts** — D; P1; [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Use claims payments and case-level duplication-of-benefits accounting to allocate insurance flows to recipients. Insurance paid to households does not automatically replenish retreat-program funds.

**Land_Restoration_Costs** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S31](https://www.bls.gov/cpi/data.htm)
Sum restoration design/construction/maintenance payments by parcel/project and date with distinct cost categories. Do not count land acquisition or demolition twice in total retreat costs.

**Market_Value_Option** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Compensation schedule categories; specify eligible components, appraisal date and rate. Category label, not a numeric observation or an extra downloadable dataset.

**Municipal_Contribution** — D; P1; [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Trace actual local match and transfers allocated to the retreat program by funding year. County versus city contribution must be explicit; commitments and cash transfers differ.

**Municipal_Fiscal_Stress** — C; P0; [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Compare recurring revenue, transfers and service obligations under a transparent fund-specific deficit measure. Guide Budget_Gap plus Service_Costs can double count expenses; align annual flow units.

**Municipal_Tax_Base** — D; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Aggregate jurisdiction-specific taxable value after exemptions at the baseline date; reconcile with the audited tax roll. Specify county versus city/FCD. Market value is not taxable value; retain nominal accounting equivalents.

**New_Development_Value** — D; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S15](https://www.h-gac.com/regional-growth-forecast), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S58](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
Use new taxable improvements and newly developed parcels from consecutive rolls; verify jurisdiction membership. Separate additions from reappraisal of existing assets and from nominal inflation.

**Political_Priority_Factor** — P; P2; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S26](https://budget.harriscountytx.gov/budget.aspx), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)
Code retreat's share of eligible funding and documented priority decisions over time. Funding is partly constrained by eligibility and awards; do not infer political preference from dollars alone.

**Pre_Disaster_Value_Option** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Compensation schedule categories; specify eligible components, appraisal date and rate. Category label, not a numeric observation or an extra downloadable dataset.

**Property_Value_Appreciation** — D; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S16](https://www.fhfa.gov/data/hpi/datasets), [S31](https://www.bls.gov/cpi/data.htm)
Measure changes in continuing-property values after removing additions, removals and inflation; compare FHFA index. Appraisal rule changes, exemptions and sales composition can mimic market appreciation.

**Property_Value_Depreciation** — K; P2; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S16](https://www.fhfa.gov/data/hpi/datasets), [S25](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Separate hazard-related or structural value loss from general market movements using repeat-property comparisons. A lower roll value is not automatically a disaster effect; avoid subtracting depreciation already included elsewhere.

**Provincial_Funding** — D; P0; [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Localize to State_Funding; identify state-origin contributions separately from federal funds passed through Texas GLO. GLO administration does not make federal CDBG-DR money state-origin funding.

**Renter_Compensation_Avg** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Compute rental assistance, moving costs and supplemental payments by tenant household and eligibility class. Do not compare the total directly to a homeowner's asset purchase price as a fairness test.

**Retreat_Funding_Available** — D; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Reconstruct spendable opening balance from receipts, restricted balances, commitments, disbursements and carryover by fund. Grant allocation, obligation, appropriation and available cash are different quantities.

**Retreat_Program_Admin_Costs** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)
Allocate actual staff, legal, appraisal and overhead spending to retreat activities using transparent cost categories. Do not add administration again if Total_Retreat_Costs already includes it.

**Retreat_Program_Costs** — A; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S29](https://purchasing.harriscountytx.gov/)
Reconcile to Total_Retreat_Costs with explicit scope and time basis; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Retreat_Property_Removal** — D; P1; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
Measure taxable value leaving the selected jurisdiction's roll after acquisition, with exemption and timing checks. Property-count removal must be converted to taxable-value flow; avoid double counting in depreciation.

**Service_Costs** — D; P1; [S26](https://budget.harriscountytx.gov/budget.aspx), [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S29](https://purchasing.harriscountytx.gov/)
Use actual operating/service costs for the chosen jurisdiction and estimate marginal changes after retreat. Average county spending per resident need not equal marginal cost savings from dispersed acquisitions.

**Support_Service_Costs** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S31](https://www.bls.gov/cpi/data.htm)
Sum paid case-management, psychosocial, transport, childcare and relocation-support costs by service category. Keep these distinct from purchase payments and administrative overhead to avoid duplicate cost allocation.

**Tax_Revenue** — D; P1; [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S26](https://budget.harriscountytx.gov/budget.aspx)
Use actual tax collections for the chosen taxing jurisdiction and fiscal year; relate to taxable roll and tax rates. Tax base dollars and revenue dollars/year are different; collection lag and overlapping jurisdictions matter.

**Total_Retreat_Costs** — C; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S29](https://purchasing.harriscountytx.gov/), [S31](https://www.bls.gov/cpi/data.htm)
Aggregate nonoverlapping acquisition, relocation, administration, demolition, restoration and maintenance costs; separate annual/cumulative forms. Define scope before calculating CBA; distinguish transfers from social resource costs.

**Total_Social_Cost** — C; P1; [S32](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S52](https://data.naturalcapitalproject.stanford.edu/), [M01]
Combine consistent incremental resource costs, losses and nonoverlapping benefits; present nonmonetary outcomes alongside. Transfers, assets, annual flows and present values cannot be added without an explicit accounting convention.

**Transfer_Payments** — D; P1; [S27](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S26](https://budget.harriscountytx.gov/budget.aspx)
Trace intergovernmental transfers into the chosen fund and year with source-of-funds identifiers. Federal pass-throughs and local interfund transfers can otherwise be counted more than once.

**User_Group_Factor** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S17](https://www.huduser.gov/portal/datasets/cp.html), [S46](https://egis.hud.gov/TDAT/), [M01]
Define group-specific assistance rules based on legally eligible costs and locally agreed needs. Do not assign arbitrary numeric effects solely from social identity; tenure compensation components differ.

### Governance

**Communication_Failures** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Code missed notices, contradictory guidance, response delays and resident-reported confusion with denominators. Complaint records undercount silent nonparticipants; ensure score units match trust-erosion formulation.

**Community_Engagement_Quality** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)
Combine perceived voice, responsiveness, accessibility and influence with documented outreach practices. Participants may differ from nonparticipants; preserve subgroup and nonresponse information.

**Community_Opposition** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure opposition among eligible/affected residents using surveys, refusals and coded public testimony; fit relation to perceived inequity. Public speakers and petitioners are selected; the guide lookup is not an estimated population response.

**Community_Petition_Threshold_Met** — S; P0; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [M01]
Evaluate a documented petition count/coverage against an explicitly chosen threshold. Confirm that such a trigger exists in the actual program; otherwise it is a hypothetical scenario rule.

**Community_Trust** — A; P1; [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Reconcile to Community_Trust_in_Process; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Community_Trust_Building_Time** — K; P2; [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Fit recovery of repeated process-trust scores following defined improvements or resolved disputes. No single public Harris County time constant was found; elicit uncertain priors if longitudinal data remain unavailable.

**Community_Trust_in_Process** — P; P1; [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Collect repeated trust questions naming the buyout agency/process; use complaints and survey narratives for triangulation. GHCP media/school trust is not buyout-process trust; general trust is contextual only.

**Coordination_Quality** — P; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure interagency handoff delays, unresolved referrals and agreed responsibilities plus participant/staff accounts. Meeting frequency alone cannot measure coordination quality.

**Cultural_Appropriate_Process** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Assess language access, recognized protocols, consent practices and culturally relevant support with affected communities. Local consultation is required to define appropriateness; outside coding is only a preliminary audit.

**Cultural_Protocol_Adherence** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Document community-agreed protocol steps and actual adherence in engagement/acquisition decisions. No generic public county score exists; appropriate communities must define the criteria.

**Decision_Authority_Clarity** — P; P2; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Code formal delegation, appeal authority and consistent staff/resident understanding of who decides. Written authority and perceived clarity can differ; retain both indicators.

**Decision_Making_Approach** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [M01]
Code the legally and operationally documented decision process; construct clearly labeled scenario alternatives. Separate participation in planning from consent to acquisition; category codes carry no numeric magnitude.

**Engagement_Activities** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Record event dates, format, purpose, target groups and unique attendance; code meaningful involvement separately. Simple event counts cannot enter a 0–100 engagement stock without a conversion rule.

**Engagement_Fatigue** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Use repeat-participant dropout, stated burden and declining response in longitudinal outreach records. Time constraints and satisfaction may explain nonattendance; fatigue should not be assumed from absence alone.

**First_Nations_Engagement_Quality** — P; P1; [S46](https://egis.hud.gov/TDAT/), [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Identify relevant tribal interests and co-design indicators of process, leadership, recognition and rights with those communities. Localize Canadian terminology; do not infer engagement quality from race, ancestry or county population shares.

**Fully_Mandatory** — N; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [M01]
Retreat-process alternative: define legal authority, participation and acquisition-consent rules for the actual program. Category label, not a numeric observation or an extra downloadable dataset.

**Governance_Capacity** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S26](https://budget.harriscountytx.gov/budget.aspx), [S29](https://purchasing.harriscountytx.gov/)
Use filled staff, relevant experience, contract resources and interagency processing performance. Do not substitute authorized staff or budget for actual implementation capability without checking utilization.

**Governance_Structure_Effectiveness** — P; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Use actor coverage, interagency handoff times, resolved tasks and authority clarity with a published coding rubric. More actors need not improve effectiveness; avoid a mechanically multiplicative index without validation.

**Indigenous_Leadership_Level** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Document recognized leadership roles, decision authority and community-defined influence in the project. Leadership quality cannot be inferred from outsider demographics or a universal numeric scale.

**Land_Rights_Respect** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S55](https://www.cclerk.hctx.net/RealProperty.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Review title, tenure, consultation, consent and documented rights outcomes with relevant authorities/communities. A property database alone cannot establish respect for rights or resolve contested interests.

**Mandatory_with_Optout** — N; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [M01]
Retreat-process alternative: define legal authority, participation and acquisition-consent rules for the actual program. Category label, not a numeric observation or an extra downloadable dataset.

**Multi_Stakeholder_Participation** — P; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Measure participation across eligible stakeholder classes and documented influence at decisions. Do not equate the fraction attending with equal influence or consensus.

**Non_Market_Value_Recognition** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S38](https://research.fs.usda.gov/treesearch/23746), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Code whether valued social, cultural and place ties are elicited and reflected in assistance or design decisions. Recognition is not equivalent to assigning a dollar value to every cultural interest.

**Number_of_Actors_Engaged** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Maintain a dated stakeholder register with roles and actual participation status. Count organizations and individual households separately; duplicate representatives can inflate coverage.

**Persuasive** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)
Decision-process category; distinguish participation in planning from acquisition consent and authority. Category label, not a numeric observation or an extra downloadable dataset.

**Policy_Adopted** — D; P1; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Code formal adoption dates and distinguish ordinance, resolution, funding award and internal operating guidance. Adoption does not imply the program is operating or fully funded.

**Policy_Choice_Selector** — A; P1; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [M01]
Reconcile to Decision_Making_Approach; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Policy_Development_Rate** — C; P2; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Derive elapsed-time changes in the defined policy-progress scale and calibrate capacity relationships. The guide factor 10 and multiplicative functional form are hypotheses, not measured rates.

**Policy_Implementation_Delay** — D; P1; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Measure adoption/award-to-operational milestones by program cohort. Several different delays exist; choose the transition represented by the model flow.

**Policy_Implemented** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Code application opening, staffing, first offers and achieved policy coverage after adoption. Choose a specific implementation endpoint before estimating its delay.

**Policy_Stimulus_Present** — P; P1; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Code a qualifying new mandate, funding opportunity or adopted incentive with a dated rule. No universal stimulus measure exists; the trigger definition is a scenario/design choice.

**Political_Will** — P; P2; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S26](https://budget.harriscountytx.gov/budget.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Code votes, appropriations, policy sponsorship and persistence using an explicit dated rubric. Event proximity and rhetoric are proxies; no public 0–100 political-will series was found.

**Potential_Actors** — P; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S46](https://egis.hud.gov/TDAT/)
Define the universe of affected residents, recipients, agencies, receiving communities and relevant tribal interests. There is no ready official denominator; agree the actor categories and boundary before measuring coverage.

**Process_Delays** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Measure stage-specific elapsed time beyond a declared service benchmark, with pending-case censoring. Do not combine raw years with 0–1 inequity scores without an explicit scale conversion.

**Recent_Disaster_Events** — C; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Count defined qualifying event clusters during an explicit recent-time window. Choose window and threshold before linking to political will; events can share a disaster declaration.

**Recent_Major_Disaster** — C; P1; [S08](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Apply documented severity/declaration criteria and a recency window to the event record. Do not use an arbitrary row count to trigger program activation.

**Retreat_Policy_Development_Progress** — P; P1; [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Code dated milestones from problem recognition through approved policy, funding and operating procedures; predefine weights. Percent complete is an analyst rubric, not a directly published continuous stock.

**Stakeholder_Engagement_Level** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Track represented groups, unique eligible participants, repeat involvement and accessibility relative to an eligible denominator. Meeting counts or attendees alone do not measure representative influence or engagement quality.

**Successful_Retreat_Demonstrations** — D; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S35](https://idrt.tamu.edu/policy-decision-support/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Identify cases meeting defined outcome criteria and measure which residents actually know those examples. Program publicity or completed acquisitions alone do not establish successful outcomes or trust effects.

**Transparency_Level** — P; P1; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Code public availability, timeliness, understandable explanations, appeals and disclosure completeness; validate with resident reports. Document count alone is not transparency; a reproducible rubric is required.

**Trust_Building_Actions** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Relate logged engagement, explanation and resolved-case actions to repeated process-trust measures. The guide multiplier 5 is uncalibrated; action counts require an estimated conversion into trust change.

**Trust_Erosion** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Link measured delay, perceived unfairness and communication failures to within-person trust changes. Standardize predictors before combining; complaints are selected observations.

**Voluntary** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)
Decision-process category; distinguish participation in planning from acquisition consent and authority. Category label, not a numeric observation or an extra downloadable dataset.

**Voluntary_with_Incentives** — N; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [M01]
Retreat-process alternative: define legal authority, participation and acquisition-consent rules for the actual program. Category label, not a numeric observation or an extra downloadable dataset.

### Implementation

**Administrative_Efficiency** — P; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/)
Use processing duration, rework and output per FTE for comparable case stages. Avoid defining efficiency from the same duration it is then used to predict without independent information.

**Application_Ease_Factor** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Use incomplete/resubmitted application rates, documentation burden, accessibility and applicant feedback. Estimate its effect on application completion; do not assume process ratings are causal coefficients.

**Awareness_Half_Time** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)
Fit repeated eligible-population awareness observations to an outreach/diffusion model, allowing saturation below 100%. A launch date and website traffic alone do not identify this time constant.

**Base_Processing_Time** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Estimate baseline complete-application-to-close duration and stage-specific distributions for comparable cohorts. Include unfinished cases; separate legal, funding and administrative delays before applying multipliers.

**Capacity_Attrition** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/)
Count departures and reductions in assigned caseworker hours over time. Contract expirations, vacancies and transfers need separate coding; headcount differs from FTE.

**Capacity_Building** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/)
Track hires, allocated contract effort and training-related capacity increments by month. Training expenditure is not an observed increase in effective throughput.

**Caseworker_Throughput** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/)
Divide completed workload by actual allocated FTE-time, recording case complexity and stage. Avoid using total county staff or mixing new applications with completed cases.

**caseworkers_equivalent** — N; P0; [M01]
Unit label for Support_Services_Capacity, not a separate model variable. Remove from the empirical-variable count while retaining this audit entry.

**Communication_Effectiveness** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure message receipt, comprehension and accessibility among eligible residents using outreach logs and survey checks. Sent notices and social-media impressions do not establish understanding.

**Community_Retreat_Demand** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Aggregate formal interest, eligible applications and stated demand separately by fixed community boundaries. Observed applications are constrained by awareness and eligibility and do not equal latent demand.

**Compensation_Attractiveness** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S62](https://doi.org/10.1016/j.jebo.2024.07.008)
Fit offer/value and assistance-adequacy responses using acceptances, refusals and stated-choice evidence. Guide lookup points are assumptions; adjust for selection, timing and receiving-housing constraints.

**Compensation_Attractiveness_Lookup** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S62](https://doi.org/10.1016/j.jebo.2024.07.008)
Estimate a bounded offer-adequacy response curve and uncertainty from acceptance/refusal or stated-choice data. Guide control points remain assumptions until fitted; cannot infer the curve using only completed buyouts.

**Hazard_Perception** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Measure respondents' perceived future flooding likelihood/severity and compare with experienced/mapped risk. Flood experience alone is not perceived probability; do not substitute crime-safety questions.

**Initial_Capacity** — A; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/)
Reconcile to Support_Services_Capacity at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Legal_Complexity_Factor** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S55](https://www.cclerk.hctx.net/RealProperty.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Estimate added stage duration associated with title, probate, liens, tenant status and appeals by case type. Use case-mix adjustment and censoring; do not apply an arbitrary multiplier to all cases.

**Legal_Obstacles** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S55](https://www.cclerk.hctx.net/RealProperty.aspx), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Code unresolved title, eligibility, authority and appeal obstacles and whether they prevent participation. A count of lawsuits is an incomplete measure and cannot be subtracted from a probability without scaling.

**Proactive_Retreat_Identification** — D; P1; [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S61](https://pmc.ncbi.nlm.nih.gov/articles/PMC6785245/)
Track distinct properties newly screened for proactive retreat under documented criteria. Target-area centroids and expressions of interest are not individually identified eligible properties.

**Processing_Time** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Estimate stage-specific time distributions from complete-application to offer, close and move; include pending cases using survival methods. Completed-case averages are biased when slow cases remain open; report voluntary/involuntary cohorts separately.

**Program_Awareness** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)
Measure unaided/aided awareness in an eligible-population survey; link outreach dates and reach as supporting records. Page views, mailed notices and applications do not directly measure population awareness.

**Properties_in_Pipeline** — A; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Reconcile to Properties_in_Retreat_Pipeline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Properties_in_Retreat_Pipeline** — D; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Reconstruct active eligible cases at each date: entries minus closures, denials and withdrawals, using stable case/property IDs. State the entry stage; expressions of interest and formal applications must remain separate.

**Properties_Retreated** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S24](https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Count distinct properties closed/acquired by date and reconcile program/site/deed records. Acquisition, demolition, move and ecological restoration are different events; budget constraint requires a time interval.

**Receiving_Area_Housing_Availability** — P; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S17](https://www.huduser.gov/portal/datasets/cp.html), [S18](https://www.huduser.gov/portal/datasets/usps.html), [S35](https://idrt.tamu.edu/policy-decision-support/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Combine available/affordable housing, accessibility, hazard safety and household needs in potential destination areas. Vacancy, affordability and current availability differ; USPS access is restricted and CHAS is not an active listing inventory.

**Regional_Retreat_Pressure** — C; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S15](https://www.h-gac.com/regional-growth-forecast), [M01]
Aggregate nonoverlapping community demand, optionally normalized by available program/housing capacity. Nested community totals and multiple applications can otherwise duplicate households/properties.

**Relocated_Households** — D; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S35](https://idrt.tamu.edu/policy-decision-support/)
Count unique households with documented moves, including renters, and reconcile cumulative opening balance. A completed purchase may displace several households or no resident household; household count differs from properties.

**Relocation_Success_Rate** — K; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S35](https://idrt.tamu.edu/policy-decision-support/), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)
Estimate the share of eligible moved households meeting prespecified 6/12/24-month outcomes, with censoring and attrition checks. Administrative completion does not establish safe, affordable and stable relocation.

**Relocation_Support_Services** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S43](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles?data_collection=1178)
Record case management, housing search, moving, transport, childcare and psychosocial service delivery by household and time. Offered, referred, received and adequate support are separate measures.

**Retreat_Applications** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Count first complete formal applications by entry date; track interest, eligibility and resubmissions separately. The guide expression needs an application-attempt rate per year to produce a flow.

**Retreat_Dropouts** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Count withdrawals and failed cases by date, stage and reason; distinguish denials, refusals and reapplications. Do not omit rejected or withdrawn cases when estimating willingness or duration.

**Retreat_Program_Active** — D; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Use dated operational status and eligibility area; implement hypothetical triggers only in scenario files. A formal policy or available grant does not establish active applications and delivery.

**Retreat_Program_Eligibility** — D; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S24](https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories)
Apply year- and program-specific geographic, hazard, income, ownership and other documented criteria to the denominator. Eligibility differs across HCD, HCFCD and funding sources; population vulnerability alone does not determine it.

**Retreat_Willingness** — K; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S62](https://doi.org/10.1016/j.jebo.2024.07.008)
Estimate offer acceptance or stated willingness among all eligible households, including refusals/nonapplicants, by offer and context. Participation among completers is not willingness; the guide expression can be negative and requires bounded calibration.

**Successful_Relocations** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S35](https://idrt.tamu.edu/policy-decision-support/), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)
Define success in advance: stable housing, affordability, safety and desired support at specified follow-up; count qualifying cohorts. Current administrative relocation totals do not measure durable success; pending follow-up is censored, not failure.

**Support_Services_Capacity** — D; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S26](https://budget.harriscountytx.gov/budget.aspx), [S29](https://purchasing.harriscountytx.gov/)
Use assigned, filled caseworker FTE by month and actual hours allocated to retreat cases. Countywide authorized posts and facility counts are not available retreat-program capacity.

**Time_Since_Program_Launch** — D; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S28](https://harriscountytx.legistar.com/Calendar.aspx)
Calculate elapsed time from a clearly specified operational launch or outreach start. Policy approval, grant award, application opening and first closing are different launch candidates.

**Trust_Factor** — A; P1; [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Reconcile to a defined 0–1 transform of Community_Trust_in_Process; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Equity

**Ancestral_Land_Significance** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S38](https://research.fs.usda.gov/treesearch/23746)
Develop consented community-specific place and cultural significance indicators through consultation. Public ancestry counts or heritage markers do not measure ancestral significance.

**Community_Psychosocial_Stress** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S41](https://www.cdc.gov/places/tools/data-portal.html), [S37](https://floodregistry.rice.edu/)
GHCP 2404 nervous, hopeless, restless, depressed, effort and worthless items support a K6 distress measure. K6 is 0–24; a 0–100 rescaling is an operational choice, not the guide's calibrated state variable.

**Cultural_Heritage_Impact** — P; P2; [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S46](https://egis.hud.gov/TDAT/), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Overlay heritage resources with retreat areas and combine with community-defined significance and protection outcomes. Site counts cannot measure living heritage or place meaning; keep sensitive location data controlled.

**Cultural_Heritage_Loss** — P; P2; [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S46](https://egis.hud.gov/TDAT/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S38](https://research.fs.usda.gov/treesearch/23746)
Track loss of access, practices, places and social ties as reported by affected groups, alongside site changes. A demolished-building count does not capture cultural loss; distinguish material and living heritage.

**Cultural_Significance** — P; P2; [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S46](https://egis.hud.gov/TDAT/), [S38](https://research.fs.usda.gov/treesearch/23746)
Use community-defined significance, historic research and site assessments. Registry designation and market price are incomplete proxies for significance.

**Disabled_Households** — D; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html)
ACS B22010_003E plus B22010_006E counts households with at least one disabled person; use PUMS for overlaps. B18101 counts people, not households; disability type and accessibility needs remain heterogeneous.

**Displacement_Impact** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01)
Estimate change per displaced person/household for an explicitly chosen scale and follow-up period. Guide wellbeing-points/household coefficient depends on whether the stock is total points or mean wellbeing.

**Displacement_Rate** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S37](https://floodregistry.rice.edu/)
Count displaced households by cause, start, duration and tenure; distinguish temporary evacuation from permanent retreat. The wellbeing equation must use the same person/household exposure basis as its effect parameter.

**Elderly_Households** — D; P1; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html)
Use B11007_002E, households containing one or more people aged 65+, or a justified alternative age threshold. Older-person counts are not older-household counts; do not add to other vulnerability groups without overlap handling.

**Equity_Degradation** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Estimate worsening access, waiting-time, adequacy or outcome gaps under the chosen equity definition. Must use the same indicators/scaling as Equity_Index and avoid duplicate subtraction of wellbeing loss.

**Equity_Improvements** — K; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure changes in the selected equity indicators following documented eligibility/support/compensation reforms. Listed as auxiliary in dictionary but used as a stock flow; revise role and validate the rate relationship.

**Equity_in_Compensation** — P; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
Compare assistance adequacy relative to eligible losses and rehousing needs, disaggregating owners and renters. Equal dollar payments do not imply equity: asset purchase and tenant relocation aid compensate different things.

**Equity_Index** — P; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S17](https://www.huduser.gov/portal/datasets/cp.html), [S42](https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Define separate access, compensation adequacy, waiting-time and outcome gaps by tenure, income and other relevant groups. SVI is vulnerability, not achieved equity. Composite weights and normative targets require explicit choices.

**Equity_Policies_Implemented** — D; P1; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Code dated adoption and actual application of accessible assistance, tenant protections and need-based support. Policy text presence does not prove implementation or its effect size.

**First_Nations_Adjustment_Factor** — S; P0; [S46](https://egis.hud.gov/TDAT/), [S38](https://research.fs.usda.gov/treesearch/23746), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [M01]
Replace the generic identity-conditioned formula with community-agreed policy protections or transparent scenario choices. The guide's trauma/ancestry coefficients lack local empirical support; do not treat identity as a deterministic behavior multiplier.

**First_Nations_Community** — S; P0; [S46](https://egis.hud.gov/TDAT/), [M01]
Determine whether and how specific tribal/Indigenous communities belong in the model through appropriate consultation. Do not use ACS race counts as a substitute for tribal nation status or governance; localize terminology.

**Heritage_Protection_Measures** — D; P2; [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S46](https://egis.hud.gov/TDAT/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Code actual preservation, access agreements, documentation and community-approved commemoration actions. A planned measure is not an implemented or effective protection.

**Heritage_Sites_Affected** — D; P1; [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Overlay documented heritage resources with acquisition/demolition footprints and verify affected status. Sensitive archaeological sites require appropriate access; absence from public inventories does not imply no heritage.

**Historical_Discrimination_Index** — P; P2; [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S42](https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html), [S46](https://egis.hud.gov/TDAT/), [S60](https://dsl.richmond.edu/panorama/redlining/map/TX/Houston/areas)
Combine documented historical treatment, unequal access and place-specific histories; keep components visible. Current SVI or race composition does not directly measure historical discrimination.

**Historical_Forced_Relocation_Trauma** — P; P2; [S46](https://egis.hud.gov/TDAT/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S38](https://research.fs.usda.gov/treesearch/23746)
Use community-authorized histories and appropriately designed self-report evidence if relevant to the local scope. Do not infer trauma from identity or transform histories into automatic numeric penalties.

**Historical_Inequity_Factor** — P; P0; [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [S45](https://atlas.thc.texas.gov/Data/DataDownload), [S46](https://egis.hud.gov/TDAT/), [S60](https://dsl.richmond.edu/panorama/redlining/map/TX/Houston/areas)
Use evidence of unequal exposure, investment, access and treatment over time; develop a transparent locally reviewed rubric. Do not assign a fixed penalty or multiplier solely from racial/Indigenous identity.

**Initial_Wellbeing** — A; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01)
Reconcile to Vulnerable_Population_Wellbeing at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Low_Income_Households** — D; P1; [S17](https://www.huduser.gov/portal/datasets/cp.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html)
Use CHAS area-median-income categories or household microdata with explicit size-adjusted thresholds. B17001 poverty counts people; a fixed B19001 income cutoff differs from HUD income eligibility.

**Non_Market_Values_Weight** — S; P0; [S46](https://egis.hud.gov/TDAT/), [S38](https://research.fs.usda.gov/treesearch/23746), [S52](https://data.naturalcapitalproject.stanford.edu/), [M01]
Elicit transparent stakeholder weights for nonmarket outcomes or report them separately in multi-criteria analysis. A normative preference weight is not a Census variable; report sensitivity and disagreement.

**Perceived_Inequity** — P; P1; [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S39](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)
Ask residents about fairness of access, process, compensation and outcomes; retain dimension-specific measures. Administrative disparity and perceived unfairness are related but different constructs.

**Psychosocial_Support_Capacity** — D; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S43](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles?data_collection=1178)
Use contracted/filled counselor effort, eligible appointments and utilization; use facility data only for service context. Guide index-point units need replacement or a defined conversion from service capacity to stress change.

**Racialized_Community** — S; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Use transparent, community-appropriate race/ethnicity group definitions for disparity analysis. Do not automatically assign behavioral or inequity coefficients from a binary group flag.

**Racialized_Households** — D; P1; [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html)
Specify race/ethnicity and whether classification follows householder or any household member; use weighted household microdata. B03002 counts persons; overlapping ethnicity/race and multiracial categories need explicit treatment.

**Service_Access_Loss** — P; P2; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S43](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles?data_collection=1178), [S44](https://publichealth.harriscountytx.gov/Media/Reports-and-Dashboards), [S35](https://idrt.tamu.edu/policy-decision-support/), [S59](https://lehd.ces.census.gov/data/)
Compare pre/post travel time, eligibility, continuity and affordability of essential services using destination geography and household reports. Provider proximity is not usable access; public destination data may be aggregated or unavailable.

**Social_Disruption_Costs** — K; P2; [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S52](https://data.naturalcapitalproject.stanford.edu/)
Estimate incremental moving burden, lost time, disrupted access and social losses with transparent valuation; retain unmonetized outcomes. Do not force distress or heritage into dollars without defensible valuation, or duplicate relocation payments and lost home value.

**Stress_Accumulation** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S37](https://floodregistry.rice.edu/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Model repeated distress changes after hazard exposure, waiting and displacement using an explicit scale. Separate stock means from totals and model recovery as well as accumulation.

**Stress_Relief** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S43](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles?data_collection=1178)
Link service exposure and repeated distress scores, controlling baseline need and access; test alternative response delays. The guide 0.15 coefficient is illustrative; counseling receipt is selected by need.

**Support_Effectiveness** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Estimate longitudinal wellbeing/distress changes against an appropriate comparison, with service type and dose. Do not interpret cross-sectional service-user differences as treatment effects.

**Vulnerable_Population_Share** — P; P0; [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S17](https://www.huduser.gov/portal/datasets/cp.html)
Use household microdata to count the union of explicitly defined vulnerability conditions, or retain separate marginal indicators. Adding low-income, older, disabled and racialized household counts double counts overlapping households.

**Vulnerable_Population_Support** — P; P1; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Measure eligible vulnerable households receiving timely accessible support and adequacy relative to needs. Service counts without the eligible denominator cannot establish support coverage or equity.

**Vulnerable_Population_Wellbeing** — P; P1; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01), [S41](https://www.cdc.gov/places/tools/data-portal.html), [S44](https://publichealth.harriscountytx.gov/Media/Reports-and-Dashboards)
Use GHCP g2404_satlife or a proposed WHO-5 panel; stratify by a defensible household/person vulnerability definition. Life satisfaction, clinical distress and area-level health prevalence are different constructs.

**Wellbeing_Decline** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S36](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content), [S37](https://floodregistry.rice.edu/), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01)
Estimate within-person change after displacement, service disruption and cultural loss with repeated follow-up. Do not sum incompatible household, index and site units; association is not necessarily a displacement effect.

**Wellbeing_Improvements** — K; P2; [S33](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj), [S40](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
Estimate within-person improvements in the chosen scale and relate them to safe housing and support exposure. Natural recovery and selection into support require comparison; use consistent score/time units.

### Land

**Average_Property_Size** — D; P0; [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Compute area from acquired-property polygons and report distribution by intended treatment. County residential mean can misrepresent target buyout parcels and assemblages.

**Biodiversity_Value** — K; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download), [S52](https://data.naturalcapitalproject.stanford.edu/), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas)
Estimate marginal habitat/species benefits using local ecological change and justified valuation or keep a nonmonetary metric. No ready local annual dollar value found; avoid double counting habitat and other ecosystem benefits.

**Carbon_Sequestration_Value** — K; P2; [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data), [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download), [S52](https://data.naturalcapitalproject.stanford.edu/)
Estimate incremental annual net carbon uptake by habitat and management, then apply an explicit carbon valuation scenario. Separate carbon stock from annual sequestration and permanence; avoid claiming saleable credits without eligibility.

**Cost_Per_Hectare** — D; P1; [S29](https://purchasing.harriscountytx.gov/), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S31](https://www.bls.gov/cpi/data.htm)
Divide paid restoration-phase cost by accepted treated area; separate acquisition, demolition, design and maintenance. Credit prices and total contract awards are not comparable treatment unit costs.

**Ecosystem_Benefits** — A; P1; [S52](https://data.naturalcapitalproject.stanford.edu/), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas)
Reconcile to the appropriately discounted Ecosystem_Service_Benefits; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Ecosystem_Decline** — K; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html), [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data)
Estimate adverse changes in measured ecological condition with matched monitoring effort. A reduction in vegetation cover is only one indicator and not a complete health decline measure.

**Ecosystem_Degradation** — D; P2; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data), [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)
Track loss of qualifying restored habitat through land-cover change and site inspections. Keep loss of area distinct from declining health on habitat that remains present.

**Ecosystem_Health_Index** — P; P1; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas)
Combine measured vegetation, habitat, hydrologic and water-quality indicators against reference conditions. No universal public 0–100 ecosystem-health measure; scoring must be habitat- and scale-specific.

**Ecosystem_Improvement** — K; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Estimate recovery trajectories from repeated site and reference monitoring by treatment and years since intervention. Area restored alone cannot determine ecological improvement; hydrologic and maintenance conditions matter.

**Ecosystem_Restoration_Rate** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks)
Derive annual completed restoration area from acceptance records, constrained by treatment-specific cost and staffing. Backlog hectares must be divided by a completion time to compare with hectares/year capacity.

**Ecosystem_Restoration_Time** — K; P2; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Use treatment completion-to-reference-condition trajectories from repeated ecological monitoring. Physical construction time and ecological maturation time must be separate.

**Ecosystem_Service_Benefits** — C; P2; [S52](https://data.naturalcapitalproject.stanford.edu/), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Estimate marginal annual flood, water-quality, recreation, carbon and habitat benefits against a no-retreat counterfactual. Do not sum overlapping services, stock carbon values and annual flows or double count avoided disaster loss.

**Ecosystem_Type_Protection_Factor** — K; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S52](https://data.naturalcapitalproject.stanford.edu/)
Fit habitat/location-specific flood attenuation against hydraulic scenarios and reference sites. Generic grassland/wetland factors in the guide are not transferable Harris County measurements.

**Flood_Protection_Value** — C; P2; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf), [S52](https://data.naturalcapitalproject.stanford.edu/)
Estimate incremental expected annual damage reduction from hydrologic/hydraulic scenarios of the restored land. Avoid counting the same flood losses in both ecosystem benefits and the general avoided-loss term.

**Full_Natural_Restoration** — N; P0; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [M01]
Land-use alternative: specify permitted treatments, costs, timing and restrictions. Category label, not a numeric observation or an extra downloadable dataset.

**Green_Infrastructure** — N; P0; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [M01]
Land-use alternative: specify permitted treatments, costs, timing and restrictions. Category label, not a numeric observation or an extra downloadable dataset.

**Infrastructure_Decommissioning_Time** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Measure acquisition-to-demolition and utility/road retirement completion from work orders and accepted contracts. Parcel clearance is not necessarily complete infrastructure retirement; record each asset class.

**Initial_Ecosystem_Health** — A; P1; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Reconcile to Ecosystem_Health_Index at baseline; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Land_Acquired_Through_Retreat** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Sum unique newly acquired polygon area by period, excluding repeated ownership transfers within the program. Prefer actual areas over a single average parcel size; document projected CRS and overlap removal.

**Mature_Ecosystem** — C; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Track restoration cohorts and the share reaching habitat-specific reference conditions over time. A fixed delay of total restored area ignores treatment failure, degradation and heterogeneous maturation.

**Multi_Purpose** — N; P0; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [M01]
Land-use alternative: specify permitted treatments, costs, timing and restrictions. Category label, not a numeric observation or an extra downloadable dataset.

**Natural_Hazard_Buffer_Capacity** — K; P2; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S52](https://data.naturalcapitalproject.stanford.edu/)
Calibrate changes in flood stage, storage or expected annual damage from restoration footprints using hydrologic/hydraulic models. Area fraction alone is not protective performance; downstream location and event magnitude matter.

**Natural_Recovery_Rate** — K; P2; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Estimate untreated/reference-site ecological trajectories by habitat and hydrologic conditions. Restoration project improvements cannot automatically identify natural recovery without a comparator.

**Policy_Selection** — A; P1; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [M01]
Reconcile to Retreat_Land_Use_Strategy; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Recreation_Value** — K; P2; [S52](https://data.naturalcapitalproject.stanford.edu/), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Use park access/visitation changes and justified local valuation or report physical use metrics separately. GHCP park willingness-to-pay fields are suppressed in the codebook; do not treat them as accessible public valuation data.

**Restoration_Capacity** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks)
Estimate feasible treatment-specific annual completions from crew/contract delivery and backlog. Observed output may be funding-constrained, not a physical capacity ceiling.

**Restoration_Funding** — D; P1; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S26](https://budget.harriscountytx.gov/budget.aspx), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)
Identify restoration-specific annual funds available for release, commitments and disbursements. Acquisition awards do not necessarily include ecological restoration; stock balance versus annual flow must be explicit.

**Restored_Ecosystem_Area** — D; P0; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S29](https://purchasing.harriscountytx.gov/), [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S48](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks), [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data)
Use accepted as-built restoration footprints and completion dates; check land-cover/imagery change and monitoring. Cleared or mowed land is not necessarily ecologically restored; do not infer completion from contract award.

**Restricted_Rebuilding** — N; P0; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [M01]
Land-use alternative: specify permitted treatments, costs, timing and restrictions. Category label, not a numeric observation or an extra downloadable dataset.

**Retreat_Land_Redevelopment** — S; P0; [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Code actual legally permitted post-acquisition transfers/uses and specify eligible scenario changes. Open-space deed restrictions may prohibit generic redevelopment; not every transfer removes land from retreat status.

**Retreat_Land_Use_Strategy** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
Specify legally feasible open-space/restoration/recreation uses by parcel and funding program. Generic redevelopment or rebuilding choices may conflict with acquisition deed/funding restrictions.

**Retreat_Lands_Area** — D; P0; [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S55](https://www.cclerk.hctx.net/RealProperty.aspx)
Union acquired land polygons by closing date; initialize cumulative eligible area after ownership/restriction verification. Avoid overlapping parcels and distinguish acquisition from restored area or target-area centroids.

**Total_Ecosystem_Area** — D; P0; [S47](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program), [S49](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data), [S50](https://www.fws.gov/program/national-wetlands-inventory/data-download)
Define eligible ecosystem classes and union their area inside the fixed model boundary at baseline. Use the same habitat definition as health/restoration metrics; mosaics and source dates vary.

**Upstream_Retreat_Area** — D; P2; [S22](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Allocate unique acquisition/restoration footprints to upstream drainage catchments for each receiving reach. Administrative neighborhoods are not drainage units; restored and acquired area may differ.

**Water_Quality_Value** — K; P2; [S51](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html), [S52](https://data.naturalcapitalproject.stanford.edu/), [S53](https://www.epa.gov/enviroatlas/about-enviroatlas)
Model marginal pollutant reduction from restoration, validate with water data and apply justified valuation if available. Water-quality measurements do not directly supply economic value; avoid overlapping treatment-cost and welfare benefits.

**Watershed_Flooding_Benefit** — K; P2; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S10](https://api.waterdata.usgs.gov/docs/), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S52](https://data.naturalcapitalproject.stanford.edu/), [S56](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf)
Run watershed hydrologic/hydraulic counterfactuals with upstream retreat/restoration footprints and comparable events. A simple linear area coefficient misses location, connectivity and event-specific effects.

### Scenario

**CC_Scenario** — S; P0; [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [M01]
Select a climate ensemble/scenario family consistent with the acquired projections; document baseline and horizon. Guide RCP labels are not interchangeable with CMIP6 SSP labels; avoid unsupported one-to-one relabeling.

**Commercial** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S46](https://egis.hud.gov/TDAT/)
Land-user subscript category; define applicable local membership and reconcile overlapping interests. Category label, not a numeric observation or an extra downloadable dataset.

**Community** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Geographic subscript category; use explicit spatial units and crosswalks, not additive nested totals. Category label, not a numeric observation or an extra downloadable dataset.

**Community_Request** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Trigger categories; define observable activation rule and timing in scenario parameters. Category label, not a numeric observation or an extra downloadable dataset.

**FINAL TIME** — S; P0; [M01]
Set proposed 2050 scenario horizon and separate historical calibration period. Guide 50–100-year examples are generic; horizon is a study choice, not a measurement.

**First_Nations** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S46](https://egis.hud.gov/TDAT/)
Land-user subscript category; define applicable local membership and reconcile overlapping interests. Category label, not a numeric observation or an extra downloadable dataset.

**Flooding** — N; P0; [M01], [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S14](https://wildfirerisk.org/download/)
Hazard subscript category; underlying physical inputs are sourced separately. Category label, not a numeric observation or an extra downloadable dataset.

**Geographic_Scale** — S; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S15](https://www.h-gac.com/regional-growth-forecast), [M01]
Choose parcel, neighborhood, community and watershed units and define crosswalks and nonoverlapping aggregations. Nested units cannot be summed together; fiscal and hydrologic boundaries need distinct mappings.

**Government** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S46](https://egis.hud.gov/TDAT/)
Land-user subscript category; define applicable local membership and reconcile overlapping interests. Category label, not a numeric observation or an extra downloadable dataset.

**Hazard_Type** — S; P0; [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S11](https://www.twdb.texas.gov/flood/planning/data.asp), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change), [M01]
Retain flood-focused baseline; explicitly enable coastal erosion, sea-level rise and wildfire only where justified. Sea-level rise can be a driver of coastal flooding rather than an independent loss event.

**Hazard_Types** — A; P1; [M01], [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S14](https://wildfirerisk.org/download/), [S57](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Reconcile to Hazard_Type subscript; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Individual_Properties** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Geographic subscript category; use explicit spatial units and crosswalks, not additive nested totals. Category label, not a numeric observation or an extra downloadable dataset.

**INITIAL TIME** — S; P0; [M01]
Set reference date/calendar or relative origin consistently with opening stocks. Guide generic zero does not specify the Harris County 2024 reference date.

**INTEGRATION METHOD** — S; P0; [M01]
Choose supported integration method, verify units and numerical behavior when the .mdl is built. No executable Vensim model is present to verify a solver setting now.

**Land_User_Group** — S; P0; [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S03](https://www.census.gov/programs-surveys/acs/microdata.html), [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S46](https://egis.hud.gov/TDAT/), [M01]
Define resident owners, renters, commercial owners, government and relevant Indigenous interests with separate units. These categories can overlap; landlord ownership and resident tenure are different axes.

**Land_User_Groups** — A; P1; [M01], [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S21](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request), [S46](https://egis.hud.gov/TDAT/)
Reconcile to Land_User_Group subscript; use the same source, definition, baseline and units. Retain the original spelling in the audit, but do not create a second independently calibrated variable.

**Neighborhood** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Geographic subscript category; use explicit spatial units and crosswalks, not additive nested totals. Category label, not a numeric observation or an extra downloadable dataset.

**Proactive_Policy** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Trigger categories; define observable activation rule and timing in scenario parameters. Category label, not a numeric observation or an extra downloadable dataset.

**RCP2.6** — N; P0; [M01], [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Legacy climate-scenario label from the guide; use a compatible source family or explicitly revise scenario definitions. Category label, not a numeric observation or an extra downloadable dataset.

**RCP4.5** — N; P0; [M01], [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Legacy climate-scenario label from the guide; use a compatible source family or explicitly revise scenario definitions. Category label, not a numeric observation or an extra downloadable dataset.

**RCP8.5** — N; P0; [M01], [S12](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states), [S13](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Legacy climate-scenario label from the guide; use a compatible source family or explicitly revise scenario definitions. Category label, not a numeric observation or an extra downloadable dataset.

**Reactive_Disaster** — N; P0; [M01], [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
Trigger categories; define observable activation rule and timing in scenario parameters. Category label, not a numeric observation or an extra downloadable dataset.

**Retreat_Strategy** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S54](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf), [M01]
Define no-retreat, reactive, proactive and hybrid options with explicit triggers, scope, funding and support rules. Scenario names alone do not specify operational mechanisms or legal feasibility.

**Threshold** — S; P0; [S26](https://budget.harriscountytx.gov/budget.aspx), [S23](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports), [M01]
Specify the minimum available-funding condition for activation and its time basis. This guide token is a policy threshold, not a separately observed data series.

**TIME STEP** — S; P0; [M01]
Choose integration interval and assess numerical convergence once equations are executable. Guide labels 0.125 years quarterly; quarterly is 0.25 years. Do not inherit that inconsistency.

**Trigger_Type** — S; P0; [S19](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs), [S20](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program), [S28](https://harriscountytx.legistar.com/Calendar.aspx), [M01]
Define disaster, policy and community-request triggers with documented activation criteria and timing. Historical programs need observed triggers; hypothetical triggers must remain labeled as scenarios.

**Watershed** — N; P0; [M01], [S05](https://hcad.org/pdata/pdata-property-downloads.html/), [S01](https://api.census.gov/data/2024/acs/acs5/groups.html), [S11](https://www.twdb.texas.gov/flood/planning/data.asp)
Geographic subscript category; use explicit spatial units and crosswalks, not additive nested totals. Category label, not a numeric observation or an extra downloadable dataset.

**Wildfire** — N; P0; [M01], [S09](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts), [S14](https://wildfirerisk.org/download/)
Hazard subscript category; underlying physical inputs are sourced separately. Category label, not a numeric observation or an extra downloadable dataset.

**Year** — N; P0; [M01]
Time index for climate lookup and reporting; align 2024 baseline and 2025–2050 scenarios. The guide uses relative time elsewhere; map relative and calendar years explicitly.

## Appendix B. Mind-map branch coverage

### MM01. Decision-support tools
Benefit-cost and multi-criteria analysis; housing needs; hazard maps; climate/demographic projections; vulnerability.
Combine hazard, population, housing and cost evidence; store normative multi-criteria weights separately. No single public file provides a decision-support score; derive outputs and retain assumptions.
S01 S11 S12 S15 S17 S32 S42 S52

### MM02. Land-user groups
Government, homeowners, leased-land owners, renters, commercial users, NGOs, Indigenous interests.
Link tenure, ownership, parcel use and program eligibility; verify leasehold and community/tribal interests. Split resident households from owning entities and overlapping social groups.
S01 S03 S05 S21 S46 S55

### MM03. Indigenous considerations
Ancestral land, place, language, nonmarket values, communal tenure, land return, historic forced relocation.
Use consultation routing, relevant histories, title records and community-defined evidence. Localize the generic Canadian framing; do not infer numerical attachment/trauma effects from identity.
S46 S45 S38 S36 S55

### MM04. Maintaining the tax base
New industry, replacement housing, local rehousing, redevelopment, livelihoods.
Follow taxable rolls and jurisdiction retention; use jobs and housing-growth evidence for livelihood context. Add local rehousing and employment outcomes if required; forecast growth is not observed retention.
S05 S16 S26 S27 S15 S59

### MM05. Scope of retreat instruments
Parcel/community buyouts, leasebacks, easements, buffers, other acquisition, infrastructure realignment.
Code program instruments, recorded restrictions, acquisition footprints and infrastructure work orders. The current property-buyout flows do not fully represent easements, leasebacks or network realignment.
S19 S20 S22 S54 S55 S29

### MM06. Community support services
Caseworkers, housing search, temporary housing, real-estate hazard advice, relocation and livelihood support.
Request service delivery, staffed FTE, referrals and follow-up outcomes by household. Separate service availability, receipt and adequacy; add livelihood measures if included.
S21 S22 S29 S43 S44 S59

### MM07. Legal issues
Authority, litigation, title, acquisition, rezoning, redevelopment and compliance.
Use program rules, case-stage reasons, deed restrictions and permit records; code dated constraints. Case-record access remains unverified; legal complexity is a measured process feature, not a universal multiplier.
S19 S20 S21 S22 S54 S55 S58

### MM08. Resilience goals
Lower exposure, housing quality, social ties, tax base and ecosystem condition.
Build separate physical, housing, social, fiscal and ecological outcome indicators. Prespecify success and time horizon; no common index is implied by these distinct goals.
S05 S09 S17 S21 S33 S47 S51

### MM09. Retreat-land uses
Demolition, decontamination, planting, restoration, recreation, commemoration, maintenance and ownership transfer.
Request parcel treatment histories, accepted work, costs, restrictions and maintenance monitoring. Acquisition area is not restored area; decontamination and ongoing maintenance need their own costs.
S22 S29 S47 S48 S49 S54 S55

### MM10. Equity dimensions
Compensation, historical treatment, vulnerability, tenure, service access, heritage and intergenerational effects.
Measure access, adequacy, waiting and outcomes by relevant groups; include historical context and future cohorts. Avoid overlapping household sums and equal-dollar fairness formulas; intergenerational weights are normative.
S03 S17 S21 S36 S42 S45 S46 S60

### MM11. Time horizons
Preplanning, near-term implementation, long-term adaptation and post-retreat follow-up.
Observe separate policy, application, move, demolition and ecological timelines; choose scenario horizon explicitly. Guide 1–100-year examples are not calibrated delay distributions.
S21 S22 S28 S48 S12 M01

### MM12. Engagement approaches
Visualization, mapping, transparency, updates and community involvement.
Code outreach formats and reach, resident comprehension, perceived voice and trust over repeated contacts. No meeting-count proxy establishes engagement quality or causal trust effects.
S21 S22 S28 S36 S39

### MM13. Engagement supports
Psychosocial support, caseworkers, childcare, transport, liaisons and technical help.
Record supports offered/received, costs, accessibility and who was excluded. These services should remain separately observable even if aggregated for model capacity.
S21 S22 S29 S43 S44

### MM14. People and assets retreated
Individuals, households, communities, critical infrastructure, protective works and industrial assets.
Identify asset/occupancy classes and network retirement work, with distinct counts and units. Current residential inputs do not cover critical infrastructure or industrial relocation without extension.
S01 S05 S07 S21 S22 S29 S58

### MM15. Geographic scales
House, street, neighborhood, community, subwatershed and watershed.
Build spatial crosswalks among administrative, residential and hydrologic units. Nested totals must not be added; evaluate destination outside the model boundary.
S05 S01 S11 S15 S09

### MM16. Voluntariness
Voluntary, incentives, persuasion, opt-out and mandatory approaches.
Code documented acquisition-consent/authority rules and actual case pathways. Do not pool voluntary HCFCD and involuntary HCD outcomes without program/cohort controls.
S19 S20 S21 S54 M01

### MM17. Compensation choices
Market, tax, pre/post-disaster value, bonuses and in-kind support.
Track valuation date/basis and paid assistance components for each tenure and household type. Separate property purchase from relocation assistance; measure need-adjusted adequacy.
S05 S19 S20 S21 S22 S31

### MM18. Funding sources
Insurance, local/state/federal, multiple funders, lenders and international sources.
Build a source-of-funds ledger with awards, transfers, receipts and expenditure accounts. International and lender funding are optional scenarios until an actual relevant program is identified.
S23 S24 S25 S26 S27 S30 S21

### MM19. Planning approaches
Adaptive, participatory, top-down, multisector, phased, public-private and interjurisdiction planning.
Code governance structure, milestones and actual decision influence; specify adaptive policy rules. Method labels alone do not supply parameters; authority, timing and budgets must be explicit.
S19 S20 S28 S21 S22 S32 M01

### MM20. Governance actors
Funders, receiving communities, champions, governments, consultants, Indigenous groups, NGOs and academics.
Create a dated actor register with responsibilities, participation and handoffs. Potential-actor denominator is a design decision; organizations and households need distinct counting rules.
S21 S22 S28 S35 S46

### MM21. Language and framing
Community-preferred terms, resilience, opportunity and other framing choices.
Code actual materials and test understanding/acceptability through appropriately designed resident research. The mind map includes this mechanism but the guide lacks an explicit framing variable; do not assume an effect size.
S36 S21 S22 S39 S46

### MM22. Retreat triggers
Disaster, rebuilding costs, policy windows, community requests and proactive forecasts/vision.
Link dated events, policy/funding actions and documented community requests to program operations. Separate historical triggers from hypothetical activation thresholds.
S08 S09 S19 S20 S21 S28 S12

### MM23. Hazard focus
Flood, multiple hazards, climate drivers and compounding events.
Define physical mechanisms, exposures and joint-event dependence before aggregation. The extension requires more than summing hazard indices or adding a fixed compounding multiplier.
S09 S10 S11 S12 S13 S14 S57

### MM24. Who decides
Owners, communities, government, hazard specialists and finance experts.
Code formal authority, actual influence, appeals and community-defined participation. Planning participation and final acquisition decisions are separate constructs.
S19 S20 S21 S28 S46

## Appendix C. Source catalog and access status

### M01. Ali shared system-dynamics guide and mind map
Generic model requiring Harris County localization | DOCX guide; mind map dated October 15, 2024
Equations, stocks/flows, scenario selectors, illustrative parameters, feedbacks and additional mind-map concepts.
Both original files inspected; 215-entry dictionary reconciled against full guide.
Conceptual specification, not an executed .mdl file or empirical evidence for its constants.
Local material: sources/Managed Retreat System Dynamics Model.docx; sources/Mind Map Oct 15 2024.pdf

### S01. [Census American Community Survey, detailed tables](https://api.census.gov/data/2024/acs/acs5/groups.html)
County, tract; some block-group tables | Annual 5-year releases; target 2010–2024
B01001 population; B25003 tenure; B25010 household size; B25001/02 units and occupancy; B19001/13 income; B25064 rent; B25077 value; B25038 residence duration; B11007 older households; B22010 disability households; B07403/B07013 mobility.
Official metadata read. Many 2024 tables and a harmonized historical panel already retained; additional tables require retrieval.
Five-year estimates are overlapping periods, not annual observations. Retain margins of error and denominators; people, households and units differ.
Local material: data/raw/reused/hydro_acs.csv.gz; local_acs2024_*.csv.gz; data/raw/public/acs2024_*.dat

Additional links: https://api.census.gov/data/2024/acs/acs5/groups/B22010.html; https://api.census.gov/data/2024/acs/acs5/groups/B11007.html; https://api.census.gov/data/2024/acs/acs5/groups/B07013.html

### S02. [Census Population Estimates, county components of change](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)
Harris County | Annual; vintage 2024 for 2020–2024; earlier vintages for history
BIRTHS, DEATHS, DOMESTICMIG and INTERNATIONALMIG by year; population estimates.
Official documentation read; data not newly acquired.
Migration components are net flows. Do not substitute net migration for gross immigration or outmigration or splice revisions without reconciliation.
Local material: None identified in reviewed package.

### S03. [Census ACS Public Use Microdata Sample](https://www.census.gov/programs-surveys/acs/microdata.html)
PUMA; derive county only where boundaries support it | Annual 1-year and 5-year releases
Household/person records; household income, age, disability, tenure, race/ethnicity, migration; person and household weights.
Official access page read; microdata not acquired.
No tract identifiers. Join persons to households before counting households with any vulnerable member; harmonize changing PUMA boundaries.
Local material: None identified in reviewed package.

### S04. [IRS county-to-county migration](https://www.irs.gov/statistics/soi-tax-stats-migration-data)
County origin and destination | Annual tax-year pairs; historical series
Incoming and outgoing returns, exemptions and adjusted gross income.
Official data page read; additional acquisition candidate.
Tax filers are a selected population; returns are not all households. Account for methodology changes, including 2022–2023.
Local material: None identified in reviewed package.

### S05. [Harris Central Appraisal District account and parcel downloads](https://hcad.org/pdata/pdata-property-downloads.html/)
Parcel/account and taxing jurisdiction | 2024 retained; inspect annual historical availability
Account identifiers, land and improvement values, jurisdiction exemptions, property class, site area and parcel geometry.
Official pages checked; 2024 raw archives already retained.
Accounts, parcels, structures and households are not interchangeable. County aggregate market value is not a municipal taxable roll.
Local material: data/raw/public/hcad_2024_Real_acct_owner.zip; hcad_2024_Real_jur_exempt.zip; hcad_2024_Code_description_real.zip; hcad_parcels_2024_oct.zip

Additional links: https://hcad.org/pdata/pdata-gis-downloads.html

### S06. [FEMA National Flood Hazard Layer and map history](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf)
Flood-zone polygons | March 2026 local layer; historic effective dates must be reconstructed
Effective flood zones, special flood hazard areas, map-change dates; overlay with parcel/structure locations.
Official map-change instructions identified; existing local NFHL layer retained.
A 2026 map cannot establish 2010–2024 historical exposure. Preliminary and effective maps differ; mapped zones omit some pluvial flooding.
Local material: data/raw/reused/nfhl_20260303_harris_bbox.geojson

### S07. [USACE National Structure Inventory](https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2022/technical-documentation)
Structure points | 2022 documentation; a 2026 release also exists
Structure occupancy, population estimates, structural characteristics and replacement/depreciated value inputs.
Official technical documentation read; local SFHA extract retained.
Modeled attributes require validation. Replacement cost is not sale price; the local SFHA subset cannot be used as the all-county denominator.
Local material: data/raw/reused/nsi_sfha.csv.gz

Additional links: https://www.hec.usace.army.mil/confluence/nsi/technicalreferences/2026/technical-documentation

### S08. [NOAA Storm Events bulk files](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)
County/forecast zone and event locations | 2010–2024 files retained; longer archive available
Episode/event IDs, event type, start/end, property damage and narratives.
Bulk source used in existing package; annual files retained.
Several rows can represent one storm. Reported damage is incomplete and nominal; define event clusters and avoid adding overlapping losses.
Local material: data/raw/public/StormEvents_details*.csv.gz; data/raw/reused/harris_events.csv.gz

### S09. [HCFCD flood reports and Harris County Flood Warning System](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)
Watershed, gauge and event footprint | Event reports and gauge-specific records
Rainfall, water levels, inundation exhibits, affected structures and major-flood chronology.
Official report and gauge pages read; targeted raw series remain to acquire.
Gauge records need quality control; HCFCD riverine inundation exhibits are not all-mechanism flood footprints.
Local material: data/raw/reused/harris_climate.csv.gz; hydro_physical.csv.gz provide related existing inputs.

Additional links: https://www.harriscountyfws.org/

### S10. [USGS Water Data APIs](https://api.waterdata.usgs.gov/docs/)
Stream gauge/site | Historical and current; varies by site
Discharge, stage, peak flows and site metadata for flood-frequency analysis.
Official API documentation and 2026 migration notice read; not downloaded for this report.
Account for rating changes, regulation, missingness and nonstationarity; use the current API, not an assumed legacy endpoint.
Local material: Related hydro_physical.csv.gz already local.

Additional links: https://waterdata.usgs.gov/blog/api-updates-2026/

### S11. [Texas Water Development Board flood planning datasets](https://www.twdb.texas.gov/flood/planning/data.asp)
Statewide; extract Harris County/watersheds | Dataset-specific; 2021 floodplain compilation and planning updates
Floodplain estimates, flood exposure, regional planning GIS and flood-risk management projects.
Official download and floodplain documentation pages read; candidate additional GIS.
Compilation mixes sources and vintages. Keep pluvial, fluvial and coastal definitions and uncertainty explicit.
Local material: None newly acquired.

Additional links: https://www.twdb.texas.gov/flood/science/floodplain-dataset.asp

### S12. [USGS CMIP6 LOCA2 and National Climate Change Viewer](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)
County summaries; underlying downscaled grids | 1950–2100; historical and SSP scenarios
Temperature, precipitation and related climate summaries by model/scenario.
Official dataset and viewer pages read; candidate download.
Climate projections do not directly measure a 0–100 impact index or flood losses. Translate through a hazard model and retain ensemble uncertainty.
Local material: No LOCA2 data identified in reviewed package.

Additional links: https://www.usgs.gov/tools/national-climate-change-viewer-nccv

### S13. [NOAA relative sea-level trends and 2022 scenarios](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)
Galveston Pier 21 and coastal region | Observed station series; projected scenario horizons
Relative sea-level trend and scenario height trajectories for coastal boundary conditions.
Official pages read; scenario files not acquired. NOAA page announces a September 30, 2026 site transition.
Match vertical datum and reference period. Coastal boundary change does not supply countywide inland flood risk.
Local material: None identified in reviewed package.

Additional links: https://tidesandcurrents.noaa.gov/sltrends/sltrends_scenarios.html

### S14. [US Forest Service Wildfire Risk to Communities](https://wildfirerisk.org/download/)
National raster and community summaries | Release-specific
Burn probability, exposure and wildfire risk metrics for optional multi-hazard extension.
Official project methods/download pages read; optional source only.
Include only if wildfire is retained in Harris County scope. Do not sum incomparable wildfire and flood indices.
Local material: None identified in reviewed package.

Additional links: https://wildfirerisk.org/about/methods/

### S15. [Houston-Galveston Area Council forecasts and land cover](https://www.h-gac.com/regional-growth-forecast)
Region, tract/forecast zones and parcels | Existing forecast/land-change files; horizon varies by edition
Population, employment and household projections; development and land-use changes.
Official pages checked; local forecast and changed-parcel extracts retained; some GIS uses a request form.
Forecasts are scenario inputs, not observed demographic flows. Verify forecast edition, geography and baseline.
Local material: data/raw/reused/hgac_tracts.csv; hgac_changed_parcels.csv

Additional links: https://www.h-gac.com/regional-growth-forecast/gis-data-request; https://www.h-gac.com/land-use-and-land-cover-data

### S16. [FHFA House Price Index datasets](https://www.fhfa.gov/data/hpi/datasets)
County/metro/ZIP depending series | Historical annual or quarterly series
Repeat-sales home-price changes for appreciation and real-dollar sensitivity.
Official dataset page read; candidate acquisition.
An index is not a parcel value or disaster depreciation estimate. Mortgage/sample coverage limits representativeness.
Local material: None identified in reviewed package.

### S17. [HUD Comprehensive Housing Affordability Strategy data](https://www.huduser.gov/portal/datasets/cp.html)
County, place, tract and other published areas | ACS-based multi-year releases
Income-by-tenure counts, housing problems, cost burden and income-relative housing needs.
Official download/documentation read; bulk files available; API requires a token.
Does not identify actual affordable units currently available for relocating households.
Local material: None identified in reviewed package.

Additional links: https://www.huduser.gov/portal/datasets/cp/CHAS/data_doc_chas.html

### S18. [HUD aggregated USPS vacancy data](https://www.huduser.gov/portal/datasets/usps.html)
Census tract | Quarterly, subject to authorized access
Residential/business addresses, vacant and no-stat addresses, vacancy duration.
Official page read. Access restricted to eligible users; not an unrestricted public download.
Vacant addresses are not necessarily habitable, offered for rent, affordable or hazard-safe.
Local material: None identified in reviewed package.

### S19. [Harris County HCD buyout guidelines and performance reports](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)
HCD programs and project areas | Program-specific; 2024 Q3 and 2025 Q2 reports retained
Eligibility, assistance components, program milestones, acquisitions and relocation reporting.
Official program pages and linked June 2025 guidelines read; earlier quarterly reports retained.
Program totals require reconciliation. A 2025 Q2 two-case discrepancy remains; relocation counts do not measure durable success.
Local material: data/raw/public/hcd_buyout_2024q3.pdf; hcd_buyout_2025q2.pdf

Additional links: https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs/Involuntary-Buyout-Relocation-Program

### S20. [HCFCD voluntary home buyout program](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)
HCFCD eligible areas and participating properties | Program history/current guidance
Voluntary program rules, eligibility, application stages and buyout-area context.
Official pages read. Detailed longitudinal property records still require a request.
Interest submission is not completed application. Public buyout-area GIS gives approximate target-area centroids, not a completed-property inventory.
Local material: Existing FEMA and HCD records are related, not substitutes for this program ledger.

Additional links: https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program/Volunteer-for-a-Home-Buyout; https://services2.arcgis.com/nLl0k0Mja5hnSeSl/ArcGIS/rest/services/HCFCD_Buyout_Areas/FeatureServer

### S21. [HCD public-records access route](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)
HCD cases, staff and program finances | Request 2010–2024, with later completion dates for censoring
Proposed deidentified case-stage ledger, compensation components, support contacts, staffing, expenditures and outcome aggregates.
Official request route verified. No request submitted; responsive fields and release are unconfirmed.
This is a route to potential records, not evidence that each requested field exists. Retain rejected, withdrawn and pending cases.
Local material: No complete case ledger identified.

### S22. [HCFCD public-information access route](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)
HCFCD program, acquisition, land and infrastructure records | Request historical cohorts and 2024 opening balances
Proposed acquisition GIS, stage dates, maintenance/restoration contracts, staff effort and decommissioning records.
Official public-information request page read; no request submitted.
Requested exports and monitoring may require staff compilation or may not exist; separate observed records from proposed collection.
Local material: No complete longitudinal ledger identified.

### S23. [Texas GLO HUD DRGR quarterly performance reports](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)
Grant, activity, project and grantee | Quarterly grant histories; local Harris buyout extracts retained
Budget, obligations/disbursements, accomplishments, beneficiaries and activity narratives.
Official reporting pages read; local financial/accomplishment/narrative files retained.
Activity totals and case completions differ. Do not add GLO, HCD and FEMA representations of the same award or property.
Local material: data/raw/reused/glo_financial.csv.gz; glo_accomplishments.csv.gz; glo_beneficiaries.csv.gz; glo_narratives.csv.gz; glo_f31_1.xlsx; glo_f31_2.xlsx

Additional links: https://www.glo.texas.gov/disaster-recovery/grant-admin/buyouts-acquisitions

### S24. [OpenFEMA HMA project-site inventories](https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories)
Mitigation project/site; filter Harris County | API version-specific; retained v1 and older v4 extract
Acquisition/mitigation project records, locations, status and program funding fields where present.
Local API extracts and metadata verified in prior build; landing page returned 403 during source search.
Version changes alter coverage. Inventory rows are not necessarily completed acquisitions or distinct households; deduplicate by stable project/site keys.
Local material: data/raw/public/fema_hma_harris_v1.json; fema_hma_harris_v4.json and metadata

### S25. [OpenFEMA NFIP claims and Individual Assistance/Housing Assistance](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2)
Redacted claims/applications; local tract aggregation | Historical panel coverage varies by source
Insurance payments, claims and assistance/damage indicators in retained panel.
Local harmonized inputs retained. FEMA landing page returned 403 during this review; original lineage retained in upstream files.
Claims cover insured properties; assistance covers applicants. Neither is a complete loss denominator, and payouts are not direct retreat-program revenue.
Local material: data/raw/reused/hydro_nfip.csv.gz; hydro_ihp.csv.gz

### S26. [Harris County adopted budgets and budget volumes](https://budget.harriscountytx.gov/budget.aspx)
County departments, funds and programs | Annual; FY2025/FY2026 local documents
Appropriations, authorized positions, revenues, service costs and capital planning.
Official budget portal read; two budget PDFs already retained.
Authorized positions are not filled buyout FTE; adopted appropriations are not spending or available cash.
Local material: data/raw/public/county_budget_fy2025.pdf; county_budget_fy2026.pdf

### S27. [Harris County Auditor annual comprehensive financial reports](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)
County and reporting entities/funds | Annual audited fiscal years
Actual revenues/expenditures, fund balances, transfers, tax data and long-term fiscal context.
Official catalog and FY2024 report read; candidate acquisition.
County, city, Flood Control District and special taxing districts have different boundaries and funds. Fiscal year differs from calendar year.
Local material: Budget PDFs provide related inputs, not audited equivalents.

Additional links: https://auditor.harriscountytx.gov/portals/auditor/documents/ACFRs/HC%20Final%209-30-24.pdf

### S28. [Harris County Commissioners Court agendas, minutes and votes](https://harriscountytx.legistar.com/Calendar.aspx)
County policy decisions | Dated meetings; current and archived systems
Policy adoption, agreements, approvals, awards, public participation and decision milestones.
Official calendar/archive pages read; additional document coding candidate.
Votes and meetings can anchor milestones but are not direct measures of political will, trust or representative participation.
Local material: documentation/Governance_Program_Timeline.csv contains partial existing chronology.

Additional links: https://agenda.harriscountytx.gov/Default.aspx

### S29. [Harris County purchasing, contracts and procurement records](https://purchasing.harriscountytx.gov/)
Contract/project and vendor | Award- and invoice-specific
Scope, staffing, unit prices, demolition/restoration/relocation services and completion dates.
Official portal and linked Bonfire/GovQA routes verified; detailed invoice/effort exports not acquired.
Bid amounts, awards, modifications and paid invoices differ; match eligible hectares, tasks and contract phase.
Local material: None newly acquired.

Additional links: https://harriscountytx.bonfirehub.com; https://harriscountytxpurch.govqa.us

### S30. [USAspending API and federal award transactions](https://api.usaspending.gov/docs/endpoints)
Recipient/place of performance and award | Transaction histories by award
Award identifiers, action obligations, recipients, agencies and spending context.
Official API documentation read; candidate supplementary download.
Obligations are not cash outlays; prime/subawards can overlap. Match grants rather than sum county search results.
Local material: No new data acquired.

Additional links: https://www.usaspending.gov/data/Federal-Spending-Guide.pdf

### S31. [BLS Consumer Price Index](https://www.bls.gov/cpi/data.htm)
Houston metropolitan area or national benchmark | Monthly/bimonthly or annual series depending geography
Price index for converting nominal household/property expenditures to a common 2024-dollar convention.
Official data and Houston release pages read; deflator not yet applied.
CPI describes consumer prices, not construction/restoration input costs; test an appropriate sector deflator for contracts.
Local material: Existing monetary series remain nominal unless explicitly labeled otherwise.

### S32. [FEMA benefit-cost analysis guidance](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)
Method/policy, not local observations | Version and award-rule dependent
Discounting conventions and benefit-cost methods for eligible mitigation projects.
Official policy located; PDF fetch was unsuccessful. Applicability/current rule must be checked against the award before use.
Do not report one discount rate as universally current. Model social welfare costs and agency cash flows separately.
Local material: Guide supplies illustrative values only.

### S33. [Rice Greater Houston Community Panel (GHCP)](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)
Greater Houston adult respondents; Harris subset/weights must be established | 2023–2024 public-use waves; release listed January 9, 2026
Neighborhood cohesion/attachment, life satisfaction, psychological distress, social support and storm impacts; exact fields in report.
Catalog and 248-page codebook read; codebook downloaded. Public-use data require a request form; no request submitted. Public files omit geocodes.
Not a buyout participant panel. Confirm Harris geography, weights, longitudinal linkage and available waves. Suppressed values cannot be treated as observations.
Local material: reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

Additional links: https://assets.kinderudp.org/oxwq5xg0ewkj/GHCP23_24_Users_Guide_C.pdf; https://doi.org/10.25611/bs6g-gt03; https://forms.monday.com/forms/7ce249278f5a244ef07565a2c869822f?r=use1

### S34. [Opportunity Insights Social Capital Atlas](https://www.socialcapital.org/)
County and ZIP; some institution measures | 2022 release/cross-sectional network measures
Economic connectedness, network cohesiveness, volunteering and civic organization density.
Project/download pages and tutorial read; data not acquired.
These are distinct network/community measures, not a longitudinal 0–100 social-capital stock or a relocation-effect coefficient.
Local material: None identified in reviewed package.

Additional links: https://opportunityinsights.org/data/; https://opportunityinsights.org/wp-content/uploads/2022/07/sc_atlas_tutorial.pdf

### S35. [Texas A&M IDRT / OneGulf buyout fiscal and social implications project](https://idrt.tamu.edu/policy-decision-support/)
Historical Harris County buyouts and destination block groups | Coverage years not verified from underlying data
Public dashboard described as comparing origin/destination flood risk, vulnerability and relocation distances.
Institutional project description verified; dashboard exists but underlying exports, completeness and reuse terms are unverified.
Request data/provenance from the research team; dashboard visuals alone cannot establish relocation success or household-level longitudinal outcomes.
Local material: No dataset identified in reviewed local files.

Additional links: https://www.arcgis.com/apps/dashboards/034873f31f5e4b7995a529e97964d6ca

### S36. [Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)
Mandatory-buyout residents in Harris County | December 2025 report
Qualitative evidence on relocation, process fairness, communication, support needs, delays and social disruption.
72-page primary report read via web; local PDF download returned 403; underlying interview data access unverified.
The methods describe interviews with 20 residents. Use for construct design and mechanism checks, not representative rates or causal coefficients.
Local material: No microdata acquired.

### S37. [Rice Texas Flood Registry](https://floodregistry.rice.edu/)
Participating Houston-area residents; public aggregated products | Post-Harvey waves; product-specific
Flood exposure, displacement, recovery and health experience.
Institutional page and catalog descriptions read; underlying records/precise access need confirmation.
Self-selected participation and attrition limit population inference; separate registry aggregates from a probability sample.
Local material: None identified in reviewed package.

### S38. [Williams and Vaske place-attachment measurement study, USFS repository](https://research.fs.usda.gov/treesearch/23746)
Measurement instrument; no Harris County observations | 2003 study
Place identity and place dependence items for a locally adapted survey.
Primary research repository and PDF identified/read.
An established instrument supplies a measurement approach, not a Harris coefficient or an identity-based attachment score.
Local material: No new local survey collected.

Additional links: https://research.fs.usda.gov/download/treesearch/23746.pdf

### S39. [OECD Guidelines on Measuring Trust](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)
Survey instrument/method | 2017 guidelines
Institutional and interpersonal trust question modules; adapt specifically to buyout decision/process.
Official publication page read; method source.
General government/media trust cannot substitute for trust in this particular retreat process.
Local material: No program-trust observations acquired.

### S40. [WHO-5 Well-Being Index](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01)
Individual survey instrument | 2024 publication; two-week recall
Five-item self-reported wellbeing instrument for proposed follow-up measurement.
Official instrument page read; no local survey administered.
Choose one construct and scoring convention; do not mix WHO-5, life satisfaction and distress as if the same scale.
Local material: GHCP supplies alternative existing wellbeing measures.

### S41. [CDC PLACES](https://www.cdc.gov/places/tools/data-portal.html)
County, place and tract estimates | Annual releases; underlying survey years differ
Modeled frequent mental distress, poor health and other health indicators.
Official portal and measure definitions read; data not acquired.
Small-area modeled prevalence is an ecological baseline, not an individual K6/WHO-5 score or a buyout treatment effect.
Local material: None identified in reviewed package.

Additional links: https://www.cdc.gov/places/measure-definitions/health-status.html

### S42. [CDC/ATSDR Social Vulnerability Index](https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html)
Census tract/county | 2022 edition and historical editions
Socioeconomic, household, minority/language and housing/transportation vulnerability indicators and rankings.
Official data/documentation read; optional comparator not newly acquired.
Relative rank is not household vulnerability prevalence or an equity outcome. Harmonize historical geography and definitions.
Local material: Underlying ACS inputs already partly retained.

Additional links: https://atsdr.cdc.gov/place-health/media/pdfs/2025/01/SVI2022Documentation.pdf

### S43. [SAMHSA National Substance Use and Mental Health Services Survey](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles?data_collection=1178)
Treatment facilities and available published geographies | Annual; 2024 files listed
Facility services and capacity-related characteristics for psychosocial-service context.
Official datafiles page read; extract not acquired.
Facility counts are not available buyout counselor FTE, appointments or program effectiveness.
Local material: None identified in reviewed package.

### S44. [Harris County Public Health reports and dashboards](https://publichealth.harriscountytx.gov/Media/Reports-and-Dashboards)
Report-specific county/city/subcounty coverage | Assessment/report-specific
Community health needs, access barriers and health status for triangulation.
Official reports page read; candidate reports identified.
Confirm the population and geography of each report; a Houston-city assessment is not automatically countywide.
Local material: None newly acquired.

### S45. [Texas Historical Commission Historic Sites Atlas](https://atlas.thc.texas.gov/Data/DataDownload)
Historic sites/markers and geographic features | Current inventory with designation dates
Historic markers and National Register resources for exposure screening.
Official data download and access explanations read; GIS not acquired.
Sensitive archaeological records are restricted. Designations omit living cultural values; do not infer community significance solely from inventory presence.
Local material: None identified in reviewed package.

Additional links: https://atlas.thc.texas.gov/About/AtlasData

### S46. [HUD Tribal Directory Assessment Tool](https://egis.hud.gov/TDAT/)
County-linked tribal interests and contacts | Current tool; historical interest not a numeric time series
Identify tribes with relevant interests and appropriate consultation contacts.
Official tool and manual read; no consultation initiated.
This is a consultation-routing tool, not a measure of attachment, trauma, leadership quality or rights.
Local material: None identified in reviewed package.

Additional links: https://egis.hud.gov/tdat/docs/TDATUserManualV4.0.pdf

### S47. [HCFCD Watershed Environmental Baseline (WEB)](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)
Harris County watersheds | Survey/inventory-specific
Natural, cultural and physical watershed resources for ecological baseline and site screening.
Official program description read; underlying GIS/monitoring availability needs confirmation/request.
A program description is not an annual ecosystem-health dataset; record field protocols and survey dates.
Local material: No complete WEB export identified.

### S48. [HCFCD wetland mitigation banks and monitoring records](https://www.hcfcd.org/Activity/Additional-Programs/Wetland-Mitigation-Banks)
Specific mitigation-bank sites | Construction and monitoring cohorts
Restoration/enhancement acreage, habitat treatments and possible monitoring/contract records.
Official page read; detailed as-built costs/monitoring are request candidates.
Mitigation credits are not cost per hectare. Bank projects differ from small buyout parcels; verify transferability.
Local material: Local hcfcd_maintenance.pdf supplies qualitative context only.

### S49. [USGS Annual National Land Cover Database](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data)
30-m raster | 1985–2024 in the inspected release
Land cover, change and imperviousness for development and revegetation checks.
Official access pages read; raster not newly downloaded.
Small lots can be below effective resolution; land-cover change is not proof of funded restoration or ecological health.
Local material: Existing hydro_static.csv.gz includes related static context.

Additional links: https://www.usgs.gov/centers/eros/science/annual-nlcd-data-access

### S50. [US Fish and Wildlife Service National Wetlands Inventory](https://www.fws.gov/program/national-wetlands-inventory/data-download)
Wetland polygons | Imagery/survey date varies spatially
Wetland extent and habitat classification for ecosystem-area denominators.
Official download/mapper pages read; candidate GIS.
Not an annual health series or a regulatory jurisdiction determination; preserve source imagery dates.
Local material: None identified in reviewed package.

Additional links: https://www.fws.gov/program/national-wetlands-inventory/wetlands-mapper

### S51. [TCEQ surface-water quality data (SWQMIS)](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)
Monitoring stations/segments | Historical sample dates; site-specific coverage
Water chemistry and biological observations, station metadata and water-quality indicators.
Official download/data-management pages read; sampling-query link identified.
Sparse stations and upstream influences complicate buyout-site attribution; match hydrology and sampling effort.
Local material: No new samples acquired.

Additional links: https://www.tceq.texas.gov/waterquality/data-management/wdma_forms.html

### S52. [Natural Capital Project InVEST methods and data](https://data.naturalcapitalproject.stanford.edu/)
Model/project specific | Input-vintage and scenario specific
Carbon, habitat, water/nutrient, recreation and flood-benefit modeling inputs and methods.
Official data/method pages read; method source, not an acquired Harris valuation table.
Supply local biophysical inputs and counterfactuals. Values cannot simply be copied per hectare or added without checking overlap.
Local material: No local InVEST model identified.

Additional links: https://naturalcapitalproject.stanford.edu/publications/policy-brief/powerful-tool-map-and-value-ecosystem-services

### S53. [EPA EnviroAtlas](https://www.epa.gov/enviroatlas/about-enviroatlas)
National and community-scale indicators | Layer-specific
Ecosystem-service, access and environmental context indicators.
Official overview and ecosystem-service pages read; specific Harris layer coverage must be checked.
Indicator availability varies. An ecosystem-service proxy does not directly measure annual dollar benefits.
Local material: None newly acquired.

Additional links: https://www.epa.gov/enviroatlas/more-information-ecosystem-services-and-enviroatlas

### S54. [44 CFR Part 80, property acquisition and relocation for open space](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)
Applicable FEMA-funded acquisitions | 2025 codification; confirm award-specific applicability
Acquisition and post-acquisition land-use constraints, including open-space restrictions.
Official nine-page legal text read; use as a scenario-eligibility reference.
Rules depend on funding program and award. Redevelopment choices in the generic guide cannot be assumed feasible on every acquired parcel.
Local material: No model constraint file yet.

### S55. [Harris County Clerk real-property records](https://www.cclerk.hctx.net/RealProperty.aspx)
Recorded instrument/property | Historical recording dates
Deeds, transfers, easements and recorded restrictions to verify acquisition and title milestones.
Official search pages read; no bulk instrument acquisition performed.
Some copies/services may involve fees. Recording date is not initial application, move date or necessarily sale price.
Local material: HCAD account links provide related parcel identifiers.

Additional links: https://www.cclerk.hctx.net/Applications/WebSearch/RP.aspx

### S56. [FEMA Hazus Flood Model technical manual](https://www.fema.gov/sites/default/files/documents/fema_rsl_hazus-7-fltm_06272025_0.pdf)
Engineering loss-model methodology | Hazus 7, 2025 manual
Depth-damage and loss estimation methods for structures and occupancy classes.
Official manual located during research; local structure/depth inputs must be assembled.
Engineering loss curves are modeled priors requiring local checks; damage fraction is not probability of total destruction.
Local material: NSI and physical hazard inputs partly retained.

### S57. [UT Austin Bureau of Economic Geology bay shoreline change](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)
Galveston/Trinity/East/West Bay shorelines, including relevant Harris frontage | Historical shoreline intervals; Galveston system update through 2022
Shoreline transects, change distance and rate_myr; distinguish bay shoreline from open-Gulf projects.
Official project page and GIS service metadata read; no GIS export acquired.
Optional coastal-erosion component; local shoreline rate is not a countywide exposure index or future deterministic forecast.
Local material: None identified in reviewed package.

Additional links: https://coastal.beg.utexas.edu/arcgis/rest/services/shorelinechange_bays_2/MapServer/3

### S58. [Harris County Engineer floodplain management and permit records](https://oce.harriscountytx.gov/Services/Permits/Floodplain-Management)
County permitting jurisdiction; city jurisdictions require separate coverage | Permit/inspection-specific history
Potential development permits, elevation certificates, substantial-damage/improvement assessments and rebuilding decisions.
Official program page read; underlying historical bulk records are a request candidate, not verified downloadable data.
County permitting does not cover all incorporated municipalities; permit issuance is not construction completion or proven total destruction.
Local material: HCAD/land-change files provide existing complementary evidence.

### S59. [Census LEHD Origin-Destination Employment Statistics](https://lehd.ces.census.gov/data/)
Census block home/workplace and origin-destination pairs | Annual; coverage varies by state/year; LODES 8 uses 2020 blocks
Resident and workplace jobs, earnings/industry categories and home-work linkages for livelihood/access context.
Official data page and technical-document metadata read; no new download.
Jobs and home-work linkages are not complete individual livelihood histories, observed commuting trips or evidence of post-buyout employment effects.
Local material: H-GAC employment forecasts provide related local material.

Additional links: https://lehd.ces.census.gov/data/lodes/LODES8/LODESTechDoc8.0.pdf

### S60. [University of Richmond Mapping Inequality, Houston](https://dsl.richmond.edu/panorama/redlining/map/TX/Houston/areas)
Historically graded Houston areas, not all Harris County | Historical HOLC-era maps and area descriptions
Historical grading polygons and archival neighborhood descriptions as one component of inequity context.
Houston catalog and download metadata identified in primary-site search; interactive page did not return readable content. Exports not acquired.
Historic map coverage is incomplete and historically specific. It cannot supply a universal discrimination index or prove current individual treatment.
Local material: None identified in reviewed package.

Additional links: https://dsl.richmond.edu/panorama/redlining/whatsnew

### S61. [Mach et al., Managed retreat through voluntary buyouts of flood-prone properties](https://pmc.ncbi.nlm.nih.gov/articles/PMC6785245/)
National FEMA-funded voluntary buyouts | 2019 research; historical study period
Candidate national comparison for program geography, capacity, exposure and demographic patterns.
Primary article indexed and abstract/method excerpt located; full-page access returned a browser check. Supplement/data access not verified.
Comparison-study lead, not a locally estimated behavioral/time-delay parameter. Assess methods, dates and duplication before use.
Local material: Existing OpenFEMA data provide a related independent source.

### S62. [Addressing coordination problems in residential buyouts: experimental evidence](https://doi.org/10.1016/j.jebo.2024.07.008)
Experimental study; external to this Harris County application | 2024 Journal of Economic Behavior & Organization article
Candidate behavioral evidence on coordination in voluntary buyouts for lookup-function and mechanism review.
Publisher title/abstract metadata located; full page returned 403. No numerical effect extracted; data availability unverified.
Obtain and assess the full study before borrowing any parameter; experimental context and local field participation may differ.
Local material: None identified in reviewed package.

Additional links: https://www.sciencedirect.com/science/article/pii/S0167268124002622
