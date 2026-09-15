# Harris County managed retreat data dictionary

Definitions, data derivations and model contributions for all 300 documented entries. Prepared September 15, 2026.

**Scope.** 300 documented entries: all 295 source-assessment entries plus four existing scenario settings and one existing opposition lookup. Entries include stocks, flows, inputs, aliases, categories and simulation settings; they are not 300 independent numerical variables.

**How to use.** Filter Dictionary by subsystem or role. Data derivation explains preparation from observations; Equations separates guide relationships, proposed repairs and direct model connections. Sources records required fields and access. Current inputs preserves existing numeric settings and their evidence status.

**Authority.** Ali model guide and mind map define conceptual scope. The September 10 source assessment supplies potential sources. This dictionary adds interpretation and proposed operational definitions; it does not certify a completed or calibrated Vensim model.

## Hazard

### Properties_at_Risk

**Role and units:** Stock. properties.

**Definition:** In-scope properties exposed to the model's chosen hazard definition.

**How derived:** Existing proxy: count distinct residential acct with sfha_any_overlap_2026=True in Residential_Parcel_Inputs. A historical estimate requires a contemporaneous footprint. Update by new exposed development minus retreat and destruction.

**Model contribution:** Defines the population of properties eligible to generate damage, retreat applications and exposure reduction.

**Simulation relationship:** Integrate new exposed development minus retreat and destruction using a single property universe. Resolve initial-name aliases and jointly cap competing outflows by the available stock.

**Guide equation:** Guide paragraph 260: INTEG(New_Development[Land_User_Group] -
Properties_Retreated[Land_User_Group] -
Properties_Destroyed[Land_User_Group],
Initial_Properties[Land_User_Group])

**Stock balance:** `INTEG(New_Development_in_Risk_Zone - Properties_Retreated - Properties_Destroyed, Initial_Properties_in_Hazard_Zone)`

**Inputs named in guide:** Initial_Properties [guide equation reference]; Land_User_Group [guide equation reference]; New_Development [guide equation reference]; Properties_Destroyed [guide equation reference]; Properties_Retreated [guide equation reference]; New_Development_in_Risk_Zone [stock inflow]; Properties_Retreated [stock outflow]; Properties_Destroyed [stock outflow]; Initial_Properties_in_Hazard_Zone [stock initializer]

**Consumers named in guide:** Properties_Destroyed [guide equation reference]; Hazard_Exposure_Index [guide equation reference]; Annual_Disaster_Damage_Costs [guide equation reference]; Retreat_Applications [guide equation reference]

**Evidence:** Retained stock initial value: derived_proxy

**Fields or records:** acct; residential_account; geometry_matched; sfha_any_overlap_2026; sfha_representative_point_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S07: USACE National Structure Inventory; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Freeze parcel/structure definitions and map vintage; any-overlap and point-in-zone counts differ. See the simulation relationship for the required equation review.

### Cumulative_Hazard_Events

**Role and units:** Stock. events.

**Definition:** Accumulated qualifying events since the model counter's starting date.

**How derived:** Count distinct historical events for a historical opening balance, or explicitly set zero for events after model start. During simulation integrate Hazard_Event_Rate.

**Model contribution:** Records the hazard burden across scenarios and supports validation of event frequency.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Hazard_Event_Rate, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Hazard_Event_Rate, 0)`

**Inputs named in guide:** Hazard_Event_Rate [stock inflow]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: assumed

**Fields or records:** event_id; start_date; end_date; hazard_type; scope_note

**Existing evidence:** data/Hazard_Inputs.csv

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** NOAA event rows are not independent storms; cumulative counts depend on the chosen origin.

### Climate_Change_Impact_Index

**Role and units:** Stock. index or physical anomaly.

**Definition:** State of the selected climate perturbation relative to a defined reference climate.

**How derived:** Select a physically meaningful driver, such as an extreme-precipitation change. Document the transformation to the guide's index and calculate a baseline value and trajectory. Do not average incompatible physical units.

**Model contribution:** Carries the changing climate driver through time and informs hazard frequency and exposure calculations.

**Simulation relationship:** Integrate a dimensioned index-points/year change from a declared baseline, or use a direct climate time series. Do not mix an unbounded physical anomaly with an unexplained 0 to 100 scale.

**Guide equation:** Guide paragraph 357: INTEG(CC_Impact_Rate[CC_Scenario], Initial_CC_Impact)

**Stock balance:** `INTEG(CC_Impact_Increase_Rate, Current_CC_Impact)`

**Inputs named in guide:** CC_Impact_Rate [guide equation reference]; CC_Scenario [guide equation reference]; Initial_CC_Impact [guide equation reference]; CC_Impact_Increase_Rate [stock inflow]; Current_CC_Impact [stock initializer]

**Consumers named in guide:** Hazard_Exposure_Index [guide equation reference]; Climate_Change_Multiplier [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** No public dataset measures this guide-specific 0–100 stock; warming is not automatically linear flood risk. See the simulation relationship for the required equation review.

### Hazard_Event_Rate

**Role and units:** Flow. events/year.

**Definition:** Expected number of qualifying hazard events per year.

**How derived:** Estimate the baseline event rate, apply a defined climate ratio, and estimate residual variation from the event series. Use event realizations separately if discrete disasters are simulated.

**Model contribution:** Fills Cumulative_Hazard_Events and drives property destruction and annual damage costs.

**Simulation relationship:** Keep the rate nonnegative and fit the residual process. An integrated expected rate may produce fractional expected events; discrete events require a separately documented event-generation process.

**Guide equation:** Guide paragraph 47: Base_Hazard_Frequency * Climate_Change_Multiplier * (1 + Random_Variation)

**Inputs named in guide:** Base_Hazard_Frequency [guide equation reference]; Climate_Change_Multiplier [guide equation reference]; Random_Variation [guide equation reference]

**Consumers named in guide:** Properties_Destroyed [guide equation reference]; Annual_Disaster_Damage_Costs [guide equation reference]; Cumulative_Hazard_Events [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** event_id; start_date; end_date; hazard_type; scope_note; evidence_status; source_id

**Existing evidence:** data/Hazard_Inputs.csv

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** Separate historical random variability, exposure change and climate trend; avoid duplicate storm counts. See the simulation relationship for the required equation review.

### Properties_Destroyed

**Role and units:** Flow. properties/year.

**Definition:** Exposed properties becoming total losses per year.

**How derived:** Count verified total-loss properties by event and date, deduplicate accounts, and annualize. For simulation combine exposed inventory, event frequency and the event-specific destruction fraction.

**Model contribution:** Removes destroyed properties from the exposed stock and distinguishes destruction from planned retreat.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 48: Properties_at_Risk * Hazard_Event_Rate * Average_Destruction_Rate

**Inputs named in guide:** Average_Destruction_Rate [guide equation reference]; Hazard_Event_Rate [guide equation reference]; Properties_at_Risk [guide equation reference]

**Consumers named in guide:** Properties_at_Risk [guide equation reference]; Properties_at_Risk [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S21: HCD public-records access route; S22: HCFCD public-information access route; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S56: FEMA Hazus Flood Model technical manual; S58: Harris County Engineer floodplain management and permit records

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Claims are not destruction counts; destruction need not remove a parcel permanently from the risk stock.

### Hazard_Exposure_Index

**Role and units:** Auxiliary or delayed quantity. dimensionless.

**Definition:** Composite measure combining the share of properties exposed with a normalized severity measure.

**How derived:** Divide Properties_at_Risk by matching Total_Properties and multiply by the selected severity measure. Keep baseline hazard present when the climate perturbation is zero.

**Model contribution:** Influences hazard-related pressure to migrate. It needs a defined scale before entering behavioral equations.

**Simulation relationship:** Proposed baseline-preserving form: (Properties_at_Risk / Total_Properties) * Hazard_Severity_Factor. Represent additional climate effects in the hazard driver and test double counting before adding another multiplier.

**Guide equation:** Guide paragraph 50: (Properties_at_Risk / Total_Properties) * Hazard_Severity_Factor * Climate_Change_Impact_Index / 100

**Inputs named in guide:** Climate_Change_Impact_Index [guide equation reference]; Hazard_Severity_Factor [guide equation reference]; Properties_at_Risk [guide equation reference]; Total_Properties [guide equation reference]

**Consumers named in guide:** Hazard_Pressure_Multiplier [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Guide multiplication by a zero climate index erases baseline risk; revise before calibration. See the simulation relationship for the required equation review.

### Climate_Change_Multiplier

**Role and units:** Auxiliary or delayed quantity. ratio.

**Definition:** Ratio of hazard frequency or intensity under the selected climate to its baseline level.

**How derived:** Calculate comparable scenario and baseline hazard statistics and divide scenario by baseline. Fit the guide's linear approximation only if supported across the intended range.

**Model contribution:** Scales Base_Hazard_Frequency into the time-varying Hazard_Event_Rate.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 51: 1 + (Climate_Change_Impact_Index / 100) * CC_Sensitivity_Parameter

**Inputs named in guide:** CC_Sensitivity_Parameter [guide equation reference]; Climate_Change_Impact_Index [guide equation reference]

**Consumers named in guide:** Hazard_Event_Rate [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S10: USGS Water Data APIs; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://api.waterdata.usgs.gov/docs/)

**Limitation:** Choose the physical endpoint; do not apply a precipitation percentage directly as a damage multiplier.

### Average_Damage_Fraction

**Role and units:** Parameter. damage/value/event.

**Definition:** Mean fraction of exposed property value lost in a qualifying event.

**How derived:** Sum matched event damage and divide by the corresponding pre-event value at risk, including zero-loss exposed properties. Estimate by building and intensity class before aggregation.

**Model contribution:** Converts event frequency and exposed value into annual disaster damage costs.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Annual_Disaster_Damage_Costs [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S09: HCFCD flood reports and Harris County Flood Warning System; S56: FEMA Hazus Flood Model technical manual; S07: USACE National Structure Inventory

[Primary source or access page](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2)

**Limitation:** Claims selection and limits bias observed ratios; total destruction is a separate outcome.

### Average_Destruction_Rate

**Role and units:** Parameter. destroyed/exposed/event.

**Definition:** Fraction of exposed properties that become total losses during one qualifying event.

**How derived:** Divide inspected total-loss properties by all comparable exposed properties in the same event footprint. Pool events only after accounting for intensity and property type.

**Model contribution:** Determines how many properties leave Properties_at_Risk through destruction rather than retreat.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_Destroyed [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S21: HCD public-records access route; S22: HCFCD public-information access route; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S56: FEMA Hazus Flood Model technical manual; S58: Harris County Engineer floodplain management and permit records

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Neither claims frequency nor mean loss fraction measures total destruction; preserve denominator uncertainty.

### Base_Hazard_Frequency

**Role and units:** Parameter. events/year.

**Definition:** Baseline arrival rate of the particular hazardous events represented by the model.

**How derived:** Count independent events meeting a fixed severity and footprint definition and divide by years with complete observation. The current parameter remains a guide prior; NOAA episode counts use a different definition.

**Model contribution:** Sets the baseline pace of hazard events before climate and random variation are applied.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Event_Rate [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** event_id; start_date; end_date; hazard_type; scope_note; evidence_status; source_id

**Existing evidence:** data/Hazard_Inputs.csv

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** Choose a sufficiently long reference period; the 2010–2024 window alone may not stabilize rare-event frequency.

### CC_Sensitivity_Parameter

**Role and units:** Parameter. ratio response.

**Definition:** Strength of the hazard response to a one-unit change in the normalized climate driver.

**How derived:** Fit future-to-baseline event frequency or intensity ratios against the normalized climate indicator across ensemble members. Report fitted uncertainty; the current value is an assumed prior.

**Model contribution:** Controls how strongly the climate index changes Climate_Change_Multiplier.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Climate_Change_Multiplier [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios; S10: USGS Water Data APIs

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Guide range is a prior; climate index scaling changes the parameter's meaning.

### Hazard_Perception_Delay

**Role and units:** Parameter. years.

**Definition:** Average lag between changing physical risk and an associated change in perceived risk.

**How derived:** Link dated events or risk information to repeated perception surveys. Estimate the adjustment lag, accounting for baseline beliefs and incomplete follow-up.

**Model contribution:** Sets the smoothing time for the optional Perceived_Hazard_Risk relationship.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Perceived_Hazard_Risk [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** The guide 1–3 years is an illustrative prior; panel timing must identify the lag.

### Hazard_Severity_Factor

**Role and units:** Parameter. normalized intensity.

**Definition:** Intensity of the modeled hazard relative to an explicitly defined reference event.

**How derived:** Select depth, duration, velocity or damage-based severity; divide by a fixed reference value and validate across event types. The guide's 1 to 10 values remain illustrative.

**Model contribution:** Distinguishes severe events from frequent mild events in the exposure index.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Exposure_Index [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S56: FEMA Hazus Flood Model technical manual

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** A single countywide severity factor can obscure different mechanisms and exposed structure types.

### CC_Impact_Increase_Rate

**Role and units:** Flow referenced by a stock. index points/year.

**Definition:** Annual change in the chosen climate-impact index.

**How derived:** Build a scenario-specific climate indicator series, transform it using a fixed documented baseline and scale, and divide successive changes by elapsed years.

**Model contribution:** Accumulates climate change in Climate_Change_Impact_Index.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Climate_Change_Impact_Index [stock inflow]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Do not extrapolate a constant index increment across scenarios without physical justification.

### Current_CC_Impact

**Role and units:** Initial value. index or physical anomaly.

**Definition:** Baseline initializer of Climate_Change_Impact_Index retained under the guide's original name.

**How derived:** Derive Climate_Change_Impact_Index for the chosen opening date, then hold that starting value fixed as the stock initializer. Select a physically meaningful driver, such as an extreme-precipitation change. Document the transformation to the guide's index and calculate a baseline value and trajectory. Do not average incompatible physical units.

**Model contribution:** Initializes Climate_Change_Impact_Index; it is not a second independently changing stock.

**Simulation relationship:** Initializes Climate_Change_Impact_Index; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Climate_Change_Impact_Index [stock initializer]

**Evidence:** Derived from/reconciled to Climate_Change_Impact_Index

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Initial_Properties_in_Hazard_Zone

**Role and units:** Initial value. properties.

**Definition:** Baseline initializer of Properties_at_Risk retained under the guide's original name.

**How derived:** Derive Properties_at_Risk for the chosen opening date, then hold that starting value fixed as the stock initializer. Existing proxy: count distinct residential acct with sfha_any_overlap_2026=True in Residential_Parcel_Inputs. A historical estimate requires a contemporaneous footprint. Update by new exposed development minus retreat and destruction.

**Model contribution:** Initializes Properties_at_Risk; it is not a second independently changing stock.

**Simulation relationship:** Initializes Properties_at_Risk; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_at_Risk [stock initializer]

**Evidence:** Derived from/reconciled to Properties_at_Risk

**Fields or records:** acct; residential_account; geometry_matched; sfha_any_overlap_2026; sfha_representative_point_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S07: USACE National Structure Inventory

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### New_Development_in_Risk_Zone

**Role and units:** Flow referenced by a stock. properties/year.

**Definition:** Newly completed properties entering the exposed inventory per year.

**How derived:** Link consecutive parcel and improvement records with permit completion dates, identify genuinely new properties, and intersect with the chosen dated hazard zone. Divide entries by interval years.

**Model contribution:** Adds exposure to Properties_at_Risk and can offset risk reduction from retreat.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_at_Risk [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S15: Houston-Galveston Area Council forecasts and land cover; S49: USGS Annual National Land Cover Database; S58: Harris County Engineer floodplain management and permit records

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Current map overlays confound historical development and subsequent mapping changes.

### Random_Variation

**Role and units:** Proposed auxiliary or input. stochastic residual.

**Definition:** Stochastic deviation around expected hazard frequency or intensity.

**How derived:** Fit residual distribution and serial dependence after the climate and trend model. Specify a seed and resampling interval; constrain the realized hazard rate to remain nonnegative.

**Model contribution:** Creates comparable uncertain hazard paths for scenario testing.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Event_Rate [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S08: NOAA Storm Events bulk files; S10: USGS Water Data APIs; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** A normal additive draw may create negative hazard rates; use suitable bounded/count processes.

### Total_Hazard_Zone_Area

**Role and units:** Proposed auxiliary or input. hectares.

**Definition:** Area of the defined hazard-zone footprint inside the model boundary.

**How derived:** Clip the dated hazard polygons to the boundary, dissolve overlaps and compute area in an appropriate projected CRS. Convert square metres to hectares by dividing by 10000.

**Model contribution:** Normalizes restored land when estimating Natural_Hazard_Buffer_Capacity.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Natural_Hazard_Buffer_Capacity [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S06: FEMA National Flood Hazard Layer and map history; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets

[Primary source or access page](https://www.fema.gov/sites/default/files/documents/fema_flood-map-change-viewer_instructions.pdf)

**Limitation:** Do not sum overlapping flood mechanisms; distinguish regulatory zone from event footprint.

### Total_Properties

**Role and units:** Proposed auxiliary or input. properties.

**Definition:** All properties in the same geography, date and property universe as Properties_at_Risk.

**How derived:** Count distinct in-scope account or structure IDs, including exposed and unexposed units. Retain unmatched hazard status as unknown.

**Model contribution:** Provides the denominator for the exposed-property share.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Exposure_Index [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** acct; residential_account; county_tax_jurisdiction

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S07: USACE National Structure Inventory

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Do not mix all-property denominator with residential-only exposure or structures with parcels.

### Active_Hazards

**Role and units:** Proposed auxiliary or input. hazard count.

**Definition:** Number of qualifying hazards occurring together in the same modeled place and event window.

**How derived:** Define intensity thresholds and a common event window, create one exceedance flag per hazard, then sum the flags.

**Model contribution:** Activates the optional compound-hazard multiplier. A count alone does not establish a joint damage effect.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compounding_Effect_Multiplier [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S13: NOAA relative sea-level trends and 2022 scenarios; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** A simple count does not estimate compounding damage or account for dependent mechanisms.

### Actual_Hazard_Risk

**Role and units:** Proposed auxiliary or input. annual probability or expected loss.

**Definition:** A selected physical risk measure for the exposed population or property inventory.

**How derived:** Choose either annual exceedance probability or expected annual loss. For loss, combine event probabilities, spatial intensity, exposed assets and damage functions over mutually consistent events.

**Model contribution:** Supplies the objective risk signal that is delayed into Perceived_Hazard_Risk. Its scale must match that perception equation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Perceived_Hazard_Risk [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S11: Texas Water Development Board flood planning datasets; S56: FEMA Hazus Flood Model technical manual

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Define risk separately from exposure and retain uncertainty rather than imply perfect knowledge.

### CC_Impact_Rate

**Role and units:** Alias. index points/year.

**Definition:** Same quantity of CC_Impact_Increase_Rate retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as CC_Impact_Increase_Rate. Build a scenario-specific climate indicator series, transform it using a fixed documented baseline and scale, and divide successive changes by elapsed years.

**Model contribution:** Connects guide references to CC_Impact_Increase_Rate without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to CC_Impact_Increase_Rate without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Climate_Change_Impact_Index [guide equation reference]

**Evidence:** Derived from/reconciled to CC_Impact_Increase_Rate

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Coastal_Erosion

**Role and units:** Proposed auxiliary or input. m/year and exposed properties.

**Definition:** Optional shoreline-retreat hazard and the properties exposed to it.

**How derived:** Calculate shoreline displacement divided by years between surveys, retain transect uncertainty, and overlay projected erosion envelopes with property locations.

**Model contribution:** Adds an optional coastal exposure mechanism to Hazard_Type. Shoreline change is not interchangeable with flood probability.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Type [category option]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S57: UT Austin Bureau of Economic Geology bay shoreline change; S05: Harris Central Appraisal District account and parcel downloads

[Primary source or access page](https://www.beg.utexas.edu/research/programs/coastal/texas-bay-shoreline-change)

**Limitation:** Do not apply open-Gulf beach rates to Harris County bay frontage or all inland properties. This name is also used as a subscript category in the guide; resolve the naming collision.

### Compounding_Effect_Multiplier

**Role and units:** Auxiliary or delayed quantity. joint/single risk ratio.

**Definition:** Additional risk associated with interacting hazards relative to their consistently defined separate effects.

**How derived:** Compare joint-event losses with a specified single-hazard reference using matched footprints, timing and exposure. Estimate dependence rather than treating a hazard count as an empirical multiplier.

**Model contribution:** Allows optional compound events to increase hazard consequences after a downstream connection is specified.

**Simulation relationship:** The guide adds 0.3 per extra active hazard as an assumption. Estimate dependence and consequences before using this relationship.

**Guide equation:** Guide paragraph 353: IF THEN ELSE(Active_Hazards > 1,
1 + 0.3 * (Active_Hazards - 1),
1.0)

**Inputs named in guide:** Active_Hazards [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S13: NOAA relative sea-level trends and 2022 scenarios; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Guide increment 0.3 per added hazard is illustrative and can double count correlated flood mechanisms. See the simulation relationship for the required equation review.

### Hazard_Exposure

**Role and units:** Proposed auxiliary or input. exposed properties by hazard.

**Definition:** Hazard-specific inventory of properties or people inside a defined footprint.

**How derived:** Intersect dated hazard footprints with one common exposure inventory and retain a property-by-hazard flag table. Count distinct units within each hazard.

**Model contribution:** Supplies the optional multi-hazard aggregation while preserving overlaps between hazards.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Total_Hazard_Exposure [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Keep hazard-specific intensity and probability separate from the exposed-property count.

### Initial_CC_Impact

**Role and units:** Initial value. index or physical anomaly.

**Definition:** Baseline initializer of Climate_Change_Impact_Index retained under the guide's original name.

**How derived:** Derive Climate_Change_Impact_Index for the chosen opening date, then hold that starting value fixed as the stock initializer. Select a physically meaningful driver, such as an extreme-precipitation change. Document the transformation to the guide's index and calculate a baseline value and trajectory. Do not average incompatible physical units.

**Model contribution:** Initializes Climate_Change_Impact_Index; it is not a second independently changing stock.

**Simulation relationship:** Initializes Climate_Change_Impact_Index; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Climate_Change_Impact_Index [guide equation reference]

**Evidence:** Derived from/reconciled to Climate_Change_Impact_Index

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Initial_Properties

**Role and units:** Initial value. properties.

**Definition:** Baseline initializer of Properties_at_Risk retained under the guide's original name.

**How derived:** Derive Properties_at_Risk for the chosen opening date, then hold that starting value fixed as the stock initializer. Existing proxy: count distinct residential acct with sfha_any_overlap_2026=True in Residential_Parcel_Inputs. A historical estimate requires a contemporaneous footprint. Update by new exposed development minus retreat and destruction.

**Model contribution:** Initializes Properties_at_Risk; it is not a second independently changing stock.

**Simulation relationship:** Initializes Properties_at_Risk; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_at_Risk [guide equation reference]

**Evidence:** Derived from/reconciled to Properties_at_Risk

**Fields or records:** acct; residential_account; geometry_matched; sfha_any_overlap_2026; sfha_representative_point_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S07: USACE National Structure Inventory

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Initial_Properties_at_Risk

**Role and units:** Initial value. properties.

**Definition:** Baseline initializer of Properties_at_Risk retained under the guide's original name.

**How derived:** Derive Properties_at_Risk for the chosen opening date, then hold that starting value fixed as the stock initializer. Existing proxy: count distinct residential acct with sfha_any_overlap_2026=True in Residential_Parcel_Inputs. A historical estimate requires a contemporaneous footprint. Update by new exposed development minus retreat and destruction.

**Model contribution:** Initializes Properties_at_Risk; it is not a second independently changing stock.

**Simulation relationship:** Initializes Properties_at_Risk; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Derived from/reconciled to Properties_at_Risk

**Fields or records:** acct; residential_account; geometry_matched; sfha_any_overlap_2026; sfha_representative_point_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S07: USACE National Structure Inventory

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### New_Development

**Role and units:** Alias. properties/year.

**Definition:** Group-indexed alias of New_Development_in_Risk_Zone retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as New_Development_in_Risk_Zone. Link consecutive parcel and improvement records with permit completion dates, identify genuinely new properties, and intersect with the chosen dated hazard zone. Divide entries by interval years.

**Model contribution:** Connects guide references to New_Development_in_Risk_Zone without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to New_Development_in_Risk_Zone without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_at_Risk [guide equation reference]

**Evidence:** Derived from/reconciled to New_Development_in_Risk_Zone

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S15: Houston-Galveston Area Council forecasts and land cover; S58: Harris County Engineer floodplain management and permit records

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Perceived_Hazard_Risk

**Role and units:** Auxiliary or delayed quantity. subjective risk scale.

**Definition:** Residents' perceived risk after an adjustment delay.

**How derived:** Collect repeated questions on the same risk construct and scale as Actual_Hazard_Risk. Fit the smoothing delay or use observations directly for calibration.

**Model contribution:** Represents delayed recognition of hazard change. Its connection to Hazard_Perception must be explicitly reconciled.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 174: SMOOTH3(Actual_Hazard_Risk, Hazard_Perception_Delay)

**Inputs named in guide:** Actual_Hazard_Risk [guide equation reference]; Hazard_Perception_Delay [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Smooth actual risk only as an explicit hypothesis; validate perception lag and score scaling.

### SLR_Projection_Table

**Role and units:** Lookup table. relative sea level by year.

**Definition:** Time series of scenario-specific local relative sea-level projections.

**How derived:** Store year, height, scenario, site, datum and reference year. Interpolate only within the documented period and define behavior outside it.

**Model contribution:** Supplies the Sea_Level_Rise lookup.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Sea_Level_Rise [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)

**Limitation:** Do not relabel NOAA scenarios as RCP/SSP without an explicit justified mapping.

### Sea_Level_Rise

**Role and units:** Auxiliary or delayed quantity. meters relative to baseline.

**Definition:** Change in local relative sea level under a selected scenario.

**How derived:** Read the local projection by year, convert to one vertical datum and length unit, and subtract the selected reference level. Keep subsidence treatment consistent.

**Model contribution:** Provides an optional coastal boundary driver for exposure and flooding analysis.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 358: LOOKUP_TABLE(Year, SLR_Projection_Table[CC_Scenario])

**Inputs named in guide:** CC_Scenario [guide equation reference]; SLR_Projection_Table [guide equation reference]; Year [guide equation reference]

**Consumers named in guide:** Hazard_Type [category option]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S13: NOAA relative sea-level trends and 2022 scenarios

[Primary source or access page](https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8771450)

**Limitation:** Avoid double counting subsidence if already incorporated in the relative scenario. This name is also used as a subscript category in the guide; resolve the naming collision.

### Total_Hazard_Exposure

**Role and units:** Auxiliary or delayed quantity. unique exposed properties or comparable risk metric.

**Definition:** Exposure across all enabled hazards without unintended double counting.

**How derived:** For property counts, count the union of property IDs exposed to any enabled hazard. For expected loss, use a joint loss model; do not sum unlike hazard scales.

**Model contribution:** Summarizes multi-hazard exposure for scenario comparison.

**Simulation relationship:** Use a union of property IDs for exposure counts. Sum loss contributions only with a model of dependence and a consistent loss unit.

**Guide equation:** Guide paragraph 352: SUM(Hazard_Exposure[Hazard_Type])

**Inputs named in guide:** Hazard_Exposure [guide equation reference]; Hazard_Type [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Dated event ID, location/footprint, intensity, observation coverage, exposed property IDs, loss or total-loss classification; projection scenario, baseline and ensemble member where relevant.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S06: FEMA National Flood Hazard Layer and map history; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Summing overlapping exposure indices double counts properties and mixes incompatible units. See the simulation relationship for the required equation review.

## Community

### Community_Population

**Role and units:** Stock. people.

**Definition:** People residing within the fixed model boundary.

**How derived:** Existing baseline uses county B01001_E001. Historical tract sums require consistent geography. Update with births and inward migration less deaths and mutually exclusive outward moves.

**Model contribution:** Tracks community retention and provides the population denominator for migration and social impacts.

**Simulation relationship:** Use mutually exclusive gross flows. Subtract only retreat moves crossing the model boundary, and remove those people from the ordinary outmigration count.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Births + Immigration - Deaths - Outmigration - Managed_Retreat_Relocations, Initial_Population)`

**Inputs named in guide:** Births [stock inflow]; Immigration [stock inflow]; Deaths [stock outflow]; Outmigration [stock outflow]; Managed_Retreat_Relocations [stock outflow]; Initial_Population [stock initializer]

**Consumers named in guide:** Outmigration [guide equation reference]

**Evidence:** Retained stock initial value: observed

**Fields or records:** geo_id; source_field=B01001_E001; estimate; moe90; population_people

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** A retreat neighborhood and Harris County require different geographic denominators. See the simulation relationship for the required equation review.

### Homeowners

**Role and units:** Stock; also a category name. households.

**Definition:** Owner-occupied households residing within the model boundary.

**How derived:** Use B25003_E002 for the county baseline, or a corresponding smaller-area estimate. Use household IDs and prior tenure for program cohorts.

**Model contribution:** Represents the owner-household population and supports tenure-specific retreat outcomes.

**Simulation relationship:** Add explicit inward, formation and tenure-conversion components and corresponding exits if a full household balance is intended. A new owner is not necessarily a newly formed household.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(New_Homeownership - Homeowner_Retreat - Homeowner_Outmigration, Initial_Homeowners)`

**Inputs named in guide:** New_Homeownership [stock inflow]; Homeowner_Retreat [stock outflow]; Homeowner_Outmigration [stock outflow]; Initial_Homeowners [stock initializer]

**Consumers named in guide:** Land_User_Group [category option]

**Evidence:** Retained stock initial value: observed

**Fields or records:** source_field=B25003_E002; estimate; owner_households

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Property owners, owner-occupied households and HCAD accounts differ; exclude absentee owners from resident counts. This name is also used as a subscript category in the guide; resolve the naming collision. See the simulation relationship for the required equation review.

### Renters

**Role and units:** Stock; also a category name. households.

**Definition:** Renter-occupied households residing within the model boundary.

**How derived:** Use B25003_E003 for the county baseline. For acquired buildings obtain occupied-unit and household records rather than one household per property.

**Model contribution:** Tracks tenant participation, displacement and distributional outcomes.

**Simulation relationship:** Add missing ordinary renter outmigration and tenure-conversion exits if the stock covers all resident renters. Separate supported retreat from other displacement.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(New_Renters - Renter_Displacement - Renter_Retreat, Initial_Renters)`

**Inputs named in guide:** New_Renters [stock inflow]; Renter_Displacement [stock outflow]; Renter_Retreat [stock outflow]; Initial_Renters [stock initializer]

**Consumers named in guide:** Land_User_Group [category option]

**Evidence:** Retained stock initial value: observed

**Fields or records:** source_field=B25003_E003; estimate; renter_households

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** An acquired multifamily property can house multiple renter households. This name is also used as a subscript category in the guide; resolve the naming collision. See the simulation relationship for the required equation review.

### Community_Social_Capital

**Role and units:** Stock. social-capital points on a validated scale.

**Definition:** Community-level social cohesion and capacity for mutual support.

**How derived:** Proposed GHCP scoring: use the six g2304 1-to-5 cohesion items, reverse ppnotalong as 6-x, and calculate 100*(mean_item-1)/4 for complete respondents. Aggregate with g2304_rweight. Validate the composite and nonresponse before adoption.

**Model contribution:** Influences attachment and records social gains or erosion during retreat.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Social_Capital_Building - Social_Capital_Erosion, 50). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Social_Capital_Building - Social_Capital_Erosion, 50)`

**Inputs named in guide:** Social_Capital_Building [stock inflow]; Social_Capital_Erosion [stock outflow]

**Consumers named in guide:** Social_Capital_Erosion [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Candidate fields: g2304_ppcare; g2304_pptrusted; g2304_pphelp; g2304_closeknit; g2304_ppnotalong; g2304_italktopp; g2304_rweight. Codebook only; survey microdata not acquired.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S34: Opportunity Insights Social Capital Atlas; S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Validate scoring, reverse coding and geographic fit; no observed guide-specific 0–100 stock exists.

### Outmigration

**Role and units:** Flow. people/year.

**Definition:** People moving out of the boundary outside the separately counted managed-retreat flow.

**How derived:** Use gross origin-based departures, retain age and domestic/international coverage, and remove identified retreat departures. For projections apply baseline-normalized hazard and attachment modifiers.

**Model contribution:** Reduces Community_Population through ordinary or hazard-related exits.

**Simulation relationship:** Apply the observed base rate to its matching age and migration universe. Normalize hazard and attachment terms to their baseline values; use a defined limit when the baseline attachment term is zero.

**Guide equation:** Guide paragraph 64: Community_Population * Base_Outmigration_Rate * Hazard_Pressure_Multiplier * (1 - Community_Attachment_Factor)

**Inputs named in guide:** Base_Outmigration_Rate [guide equation reference]; Community_Attachment_Factor [guide equation reference]; Community_Population [guide equation reference]; Hazard_Pressure_Multiplier [guide equation reference]

**Consumers named in guide:** Community_Population [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S04: IRS county-to-county migration; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** PEP provides net migration, not gross exits; identify retreat moves to avoid counting them twice. See the simulation relationship for the required equation review.

### Managed_Retreat_Relocations

**Role and units:** Flow. people/year.

**Definition:** People leaving the model boundary through managed retreat per year.

**How derived:** Sum actual members of unique retreat households moving outside the boundary by move date. A proxy needs households per acquired property, household size and the outside-boundary share.

**Model contribution:** Removes retreat-related departures from Community_Population. Within-county moves do not drain a county population stock.

**Simulation relationship:** Preferred population outflow: count actual people moving outside the boundary. Approximation: acquired properties/year * households/property * people/household * outside-boundary share, with move timing. Do not multiply by sustainable-success probability: unsuccessful movers also leave.

**Guide equation:** Guide paragraph 65: Properties_Retreated * Average_Household_Size * Relocation_Success_Rate

**Inputs named in guide:** Average_Household_Size [guide equation reference]; Properties_Retreated [guide equation reference]; Relocation_Success_Rate [guide equation reference]

**Consumers named in guide:** Community_Population [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Properties times mean household size is only a fallback; successful resettlement is distinct from moving. See the simulation relationship for the required equation review.

### Social_Capital_Erosion

**Role and units:** Flow. scale points/year.

**Definition:** Loss of social-capital scale points per year.

**How derived:** Estimate changes in a fixed cohesion scale over elapsed time and relate them to population decline and displacement exposure. Calibrate the guide's erosion coefficient and scale.

**Model contribution:** Drains Community_Social_Capital and weakens the attachment pathway.

**Simulation relationship:** Population_Decline_Rate and Displacement_Stress_Factor must both be per-year rates when multiplied by social-capital points. Define the 0.1 coefficient and cap competing score flows consistently.

**Guide equation:** Guide paragraph 66: Community_Social_Capital * (Population_Decline_Rate + Displacement_Stress_Factor) * 0.1

**Inputs named in guide:** Community_Social_Capital [guide equation reference]; Displacement_Stress_Factor [guide equation reference]; Population_Decline_Rate [guide equation reference]

**Consumers named in guide:** Community_Social_Capital [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S37: Rice Texas Flood Registry

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Cross-sectional scores and qualitative interviews do not identify an annual erosion coefficient. See the simulation relationship for the required equation review.

### Community_Attachment_Factor

**Role and units:** Auxiliary or delayed quantity. 0–1 response modifier.

**Definition:** Modeled degree to which community attachment reduces migration.

**How derived:** Combine a documented social-capital scale and measured place attachment after normalization. Fit the relationship to observed exits; guide weights are assumptions.

**Model contribution:** Reduces Outmigration through the attachment term.

**Simulation relationship:** Use Community_Social_Capital in place of Social_Capital and bound the result to 0 to 1. Fit the 0.3, 0.4 and 0.3 weights rather than treating them as observed relationships.

**Guide equation:** Guide paragraph 68: 0.3 + 0.4 * (Social_Capital / 100) + 0.3 * Place_Attachment_Index

**Inputs named in guide:** Place_Attachment_Index [guide equation reference]; Social_Capital [guide equation reference]

**Consumers named in guide:** Outmigration [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Guide weights 0.3/0.4/0.3 are illustrative; test collinearity with social capital and bounds. See the simulation relationship for the required equation review.

### Hazard_Pressure_Multiplier

**Role and units:** Auxiliary or delayed quantity. ratio.

**Definition:** Factor increasing departure pressure when exposure is high and perceived safety is low.

**How derived:** Fit observed departures against exposure and flood-specific perceived safety, with economic and demographic controls. Normalize the fitted multiplier to one in the baseline.

**Model contribution:** Changes Outmigration in response to hazard conditions.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 69: 1 + 2 * Hazard_Exposure_Index * (1 - Perceived_Safety)

**Inputs named in guide:** Hazard_Exposure_Index [guide equation reference]; Perceived_Safety [guide equation reference]

**Consumers named in guide:** Outmigration [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S09: HCFCD flood reports and Harris County Flood Warning System; S04: IRS county-to-county migration

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** The factor 2 in the guide is not estimated evidence; distinguish risk perception from exposure.

### Place_Attachment_Index

**Role and units:** Auxiliary or delayed quantity. 0–1 or validated scale.

**Definition:** Strength of place identity and dependence for affected residents.

**How derived:** Use validated place-attachment items; GHCP g2403_hmneigh and residence duration provide limited proxies. Reverse-code as needed, handle missing responses and normalize a validated score.

**Model contribution:** Influences both community retention and Retreat_Willingness.

**Simulation relationship:** Use measured attachment with a documented transformation. Remove automatic identity-based constants; the residence-duration formula can exceed one and requires empirical validation.

**Guide equation:** Guide paragraph 70: IF THEN ELSE(First_Nations_Community = 1, 0.8 + 0.2 * Ancestral_Land_Significance,
0.4 + 0.3 * Years_of_Residence / 50)

**Inputs named in guide:** Ancestral_Land_Significance [guide equation reference]; First_Nations_Community [guide equation reference]; Years_of_Residence [guide equation reference]

**Consumers named in guide:** Community_Attachment_Factor [guide equation reference]; Retreat_Willingness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Candidate field: g2403_hmneigh; use g2403_rweight. Codebook only; limited neighborhood-satisfaction proxy, not a validated place-attachment scale.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S38: Williams and Vaske place-attachment measurement study, USFS repository; S46: HUD Tribal Directory Assessment Tool

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Years of residence and Indigenous identity cannot justify automatic attachment coefficients. See the simulation relationship for the required equation review.

### Average_Household_Size

**Role and units:** Parameter. people/household.

**Definition:** Mean number of people in an occupied household.

**How derived:** Use the published county B25010_E001 estimate for the existing baseline. For relocation, calculate people divided by households within the actual owner or renter cohort.

**Model contribution:** Converts retreat household flows into people when estimating population change.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Managed_Retreat_Relocations [guide equation reference]

**Evidence:** Retained parameter: observed

**Fields or records:** source_field=B25010_E001; estimate; moe90

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** County average 2.73 in the retained 2024 input is not necessarily the size of households in acquired properties.

### Base_Outmigration_Rate

**Role and units:** Parameter. 1/year.

**Definition:** Annual gross departure rate from the model boundary before scenario adjustments.

**How derived:** Existing proxy is (B07403_E010+B07403_E013)/B07403_E001 for domestic departures among people age one and older. Retain its universe and MOE. Estimate international departures separately.

**Model contribution:** Establishes baseline Outmigration. Normalize hazard and attachment effects at baseline to avoid applying observed influences twice.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Outmigration [guide equation reference]

**Evidence:** Retained parameter: derived_proxy

**Fields or records:** GEO_ID; B07403_E001; B07403_E010; B07403_E013; corresponding M fields; domestic_outmigration_rate

**Existing evidence:** data/Domestic_Outmigration_2024.csv

**Sources:** S01: Census American Community Survey, detailed tables; S04: IRS county-to-county migration; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Baseline rates already reflect prevailing hazards/attachment; normalize modifiers to avoid suppressing observed flows twice.

### Births

**Role and units:** Flow referenced by a stock. people/year.

**Definition:** Live births entering the resident population per year.

**How derived:** Select births for the county and consistent annual reference period from population components or vital records. Do not allocate to smaller areas without a stated method.

**Model contribution:** Adds natural population growth to Community_Population.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Population [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S02: Census Population Estimates, county components of change

[Primary source or access page](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)

**Limitation:** County totals cannot be assigned proportionally to neighborhoods without uncertainty.

### Deaths

**Role and units:** Flow referenced by a stock. people/year.

**Definition:** Resident deaths leaving the population per year.

**How derived:** Extract resident deaths for the same boundary and annual reference period used for births and population estimates.

**Model contribution:** Removes natural population loss from Community_Population.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Population [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S02: Census Population Estimates, county components of change

[Primary source or access page](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/CO-EST2024-ALLDATA.pdf)

**Limitation:** Do not interpret all deaths as hazard mortality; keep event deaths as a separate subset if needed.

### Displacement_Stress_Factor

**Role and units:** Proposed auxiliary or input. 1/year in the social-capital erosion equation.

**Definition:** Rate coefficient linking displacement to erosion of social capital.

**How derived:** Estimate repeated social-capital change after displacement, controlling prior ties and concurrent hazard experience. Convert the effect to the per-year scale required by the erosion equation.

**Model contribution:** Adds displacement-related pressure to Social_Capital_Erosion.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Social_Capital_Erosion [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** No independent public coefficient identified; guide units and model response require explicit definition.

### Homeowner_Outmigration

**Role and units:** Flow referenced by a stock. owner households/year.

**Definition:** Owner-household exits from the boundary outside the separately counted retreat flow.

**How derived:** Use linked household histories with tenure before departure and move date. Divide unique owner-household exits by years and exclude retreat exits already counted elsewhere.

**Model contribution:** Drains the Homeowners stock while preserving tenure-specific population accounting.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Homeowners [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S04: IRS county-to-county migration

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Public ACS/PUMS current tenure does not identify prior-tenure household transitions; IRS has no tenure field.

### Homeowner_Retreat

**Role and units:** Flow referenced by a stock. owner households/year.

**Definition:** Owner-occupant households leaving the modeled community through managed retreat per year.

**How derived:** Link acquisition, occupancy and household move records, identify owner-occupants and count unique households crossing the boundary by move date.

**Model contribution:** Removes participating owner households from Homeowners; property closures alone cannot supply this flow.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Homeowners [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** An owner can sell without residing at the property; do not infer household exits from purchases.

### Immigration

**Role and units:** Flow referenced by a stock. people/year.

**Definition:** Gross inward migration across the model boundary per year.

**How derived:** Count people whose prior residence was outside the boundary and current residence is inside, using origin-destination records and the correct survey universe. Separate domestic and international arrivals.

**Model contribution:** Adds arriving people to Community_Population.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Population [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S04: IRS county-to-county migration; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** PEP net international/domestic migration does not identify all gross arrivals.

### Initial_Homeowners

**Role and units:** Initial value. households.

**Definition:** Baseline initializer of Homeowners retained under the guide's original name.

**How derived:** Derive Homeowners for the chosen opening date, then hold that starting value fixed as the stock initializer. Use B25003_E002 for the county baseline, or a corresponding smaller-area estimate. Use household IDs and prior tenure for program cohorts.

**Model contribution:** Initializes Homeowners; it is not a second independently changing stock.

**Simulation relationship:** Initializes Homeowners; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Homeowners [stock initializer]

**Evidence:** Derived from/reconciled to Homeowners

**Fields or records:** source_field=B25003_E002; estimate; owner_households

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Initial_Population

**Role and units:** Initial value. people.

**Definition:** Baseline initializer of Community_Population retained under the guide's original name.

**How derived:** Derive Community_Population for the chosen opening date, then hold that starting value fixed as the stock initializer. Existing baseline uses county B01001_E001. Historical tract sums require consistent geography. Update with births and inward migration less deaths and mutually exclusive outward moves.

**Model contribution:** Initializes Community_Population; it is not a second independently changing stock.

**Simulation relationship:** Initializes Community_Population; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Population [stock initializer]

**Evidence:** Derived from/reconciled to Community_Population

**Fields or records:** geo_id; source_field=B01001_E001; estimate; moe90; population_people

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Initial_Renters

**Role and units:** Initial value. households.

**Definition:** Baseline initializer of Renters retained under the guide's original name.

**How derived:** Derive Renters for the chosen opening date, then hold that starting value fixed as the stock initializer. Use B25003_E003 for the county baseline. For acquired buildings obtain occupied-unit and household records rather than one household per property.

**Model contribution:** Initializes Renters; it is not a second independently changing stock.

**Simulation relationship:** Initializes Renters; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Renters [stock initializer]

**Evidence:** Derived from/reconciled to Renters

**Fields or records:** source_field=B25003_E003; estimate; renter_households

**Existing evidence:** data/ACS_2024_Estimates_MOE.csv; data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### New_Homeownership

**Role and units:** Flow referenced by a stock. households/year.

**Definition:** Household entries into the modeled owner-occupied population per year.

**How derived:** Use linked household histories to count owner-household formation, tenure conversion and inward moves. Keep component flows and exits mutually exclusive.

**Model contribution:** Replenishes Homeowners and permits tenure transitions to be modeled.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Homeowners [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S03: Census ACS Public Use Microdata Sample; S01: Census American Community Survey, detailed tables; S15: Houston-Galveston Area Council forecasts and land cover

[Primary source or access page](https://www.census.gov/programs-surveys/acs/microdata.html)

**Limitation:** Successive ACS cross-sections do not uniquely identify gross tenure transitions.

### New_Renters

**Role and units:** Flow referenced by a stock. households/year.

**Definition:** Household entries into the modeled renter population per year.

**How derived:** Count new renter households, inward renter moves and ownership-to-rental transitions from linked household histories. Annual net stock change alone cannot identify gross entries.

**Model contribution:** Replenishes Renters and separates formation from displacement.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Renters [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S03: Census ACS Public Use Microdata Sample; S01: Census American Community Survey, detailed tables; S15: Houston-Galveston Area Council forecasts and land cover

[Primary source or access page](https://www.census.gov/programs-surveys/acs/microdata.html)

**Limitation:** Net renter-stock change cannot distinguish new household formation, migration and tenure switching.

### Perceived_Safety

**Role and units:** Proposed auxiliary or input. survey probability/scale.

**Definition:** Residents' assessment of safety from the hazard at their location.

**How derived:** Ask flood-specific safety or likelihood questions, document direction and normalize only using a fixed scale. Measure origin and destination separately.

**Model contribution:** Moderates Hazard_Pressure_Multiplier.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Pressure_Multiplier [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** GHCP general housing/neighborhood safety may concern crime; use exact wording before treating it as flood safety.

### Population_Decline_Rate

**Role and units:** Proposed auxiliary or input. 1/year.

**Definition:** Annual proportional decrease in the resident population.

**How derived:** Calculate max(0, P_previous-P_current)/(P_previous*elapsed_years) for a nonzero baseline population, using the same boundary and population concept.

**Model contribution:** Supplies demographic pressure to Social_Capital_Erosion.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Social_Capital_Erosion [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S02: Census Population Estimates, county components of change

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Overlapping ACS estimates smooth changes; an algebraic decline measure is not itself a causal driver.

### Renter_Displacement

**Role and units:** Flow referenced by a stock. renter households/year.

**Definition:** Renter households leaving their homes or modeled area for reasons distinguished from supported retreat.

**How derived:** Link tenant departures to event or acquisition records, identify cause and destination, and count unique households by period. Define whether the stock tracks residence in the area or the origin dwelling.

**Model contribution:** Drains Renters and identifies tenant impacts that acquisition counts miss.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Renters [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S37: Rice Texas Flood Registry

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Tenant moves may precede closing and be absent from owner-only acquisition data.

### Renter_Retreat

**Role and units:** Flow referenced by a stock. renter households/year.

**Definition:** Renter households relocating through the retreat program per year.

**How derived:** Count unique tenant households with documented retreat assistance and moves; use boundary-crossing departures if Renters is a geographic resident stock.

**Model contribution:** Separates supported tenant relocation from other renter displacement.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Renters [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Separate voluntary moves, eviction/displacement and program-supported relocation.

### Social_Capital

**Role and units:** Alias. social-capital points on a validated scale.

**Definition:** Same quantity of Community_Social_Capital retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Community_Social_Capital. Proposed GHCP scoring: use the six g2304 1-to-5 cohesion items, reverse ppnotalong as 6-x, and calculate 100*(mean_item-1)/4 for complete respondents. Aggregate with g2304_rweight. Validate the composite and nonresponse before adoption.

**Model contribution:** Connects guide references to Community_Social_Capital without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Community_Social_Capital without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Attachment_Factor [guide equation reference]

**Evidence:** Derived from/reconciled to Community_Social_Capital

**Fields or records:** Candidate fields: g2304_ppcare; g2304_pptrusted; g2304_pphelp; g2304_closeknit; g2304_ppnotalong; g2304_italktopp; g2304_rweight. Codebook only; survey microdata not acquired.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S34: Opportunity Insights Social Capital Atlas

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Social_Capital_Building

**Role and units:** Flow referenced by a stock. scale points/year.

**Definition:** Increase in the chosen social-capital scale per year.

**How derived:** Estimate positive longitudinal scale change associated with networks, organizations and support, using repeated observations and a matched population definition.

**Model contribution:** Replenishes Community_Social_Capital.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Social_Capital [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S34: Opportunity Insights Social Capital Atlas; S21: HCD public-records access route

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Do not infer annual growth from one cross-sectional Atlas score or meeting count.

### Total_Households

**Role and units:** Proposed auxiliary or input. households.

**Definition:** All occupied households in the matching population and reference period.

**How derived:** Use B25003_E001 or sum owner and renter households after confirming their shared universe. Use eligible household counts for program-specific rates.

**Model contribution:** Provides denominators for vulnerability and participation measures.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Share [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** occupied_households; owner_households; renter_households; year; geoid_2020

**Existing evidence:** data/Population_Housing.csv

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Housing units include vacancies; total persons divided by a rounded household size is only an approximation.

### Years_of_Residence

**Role and units:** Proposed auxiliary or input. years or duration band.

**Definition:** Duration of residence at the place relevant to attachment.

**How derived:** Subtract move-in date from survey date, or preserve GHCP g2304_yrsneigh and ACS B25038 bands. Any midpoint conversion must be labeled an approximation.

**Model contribution:** Supplies residence-duration information for place attachment.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Place_Attachment_Index [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Candidate field: g2304_yrsneigh and g2304_rweight; ACS B25038 bands. Codebook only; neighborhood versus dwelling duration differs.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Neighborhood tenure and years in the current dwelling differ; interval-coded durations are not exact years.

### Community_Cohesion_Preservation

**Role and units:** Proposed auxiliary or input. cohesion change/network retention.

**Definition:** Extent to which relocated households retain social ties and collective connection.

**How derived:** Compare pre-move and follow-up ties, contact frequency and cohesion using the same respondents and scale. Report network retention and attrition separately.

**Model contribution:** Supplies one of the guide's conceptual determinants of relocation success.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Relocation_Success_Rate [named conceptual determinant]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Reference date, fixed geographic ID, person or household ID where available, tenure before and after moves, origin, destination, household size and survey weights or margins of error.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S38: Williams and Vaske place-attachment measurement study, USFS repository; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Co-location of destinations is a proxy, not proof of preserved relationships.

## Fiscal

### Municipal_Tax_Base

**Role and units:** Stock. USD_2024 taxable value.

**Definition:** Taxable property value within the selected taxing jurisdiction.

**How derived:** Sum jurisdiction-specific taxable values after exemptions and reconcile to the certified roll. Existing county initialization is a rounded published 2024 value, not a municipal total.

**Model contribution:** Tracks revenue-generating property value affected by development, valuation change and retreat.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(New_Development_Value + Property_Value_Appreciation - Property_Value_Depreciation - Retreat_Property_Removal, Initial_Assessment_Value). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(New_Development_Value + Property_Value_Appreciation - Property_Value_Depreciation - Retreat_Property_Removal, Initial_Assessment_Value)`

**Inputs named in guide:** New_Development_Value [stock inflow]; Property_Value_Appreciation [stock inflow]; Property_Value_Depreciation [stock outflow]; Retreat_Property_Removal [stock outflow]; Initial_Assessment_Value [stock initializer]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: observed_rounded

**Fields or records:** entity; measure; year; value; unit; source_page; amount_basis

**Existing evidence:** data/Fiscal_Funding.csv

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Specify county versus city/FCD. Market value is not taxable value; retain nominal accounting equivalents.

### Retreat_Funding_Available

**Role and units:** Stock. USD_2024.

**Definition:** Spendable program funding balance at a particular date.

**How derived:** Reconstruct opening balance plus eligible receipts less actual spending, adjusting for restrictions and committed obligations under one accounting convention. An unspent allocation is not automatically available cash.

**Model contribution:** Limits acquisition throughput and stores funding received but not yet spent.

**Simulation relationship:** Add administration and other eligible spending if not included in existing outflows. Include insurance only when received by this fund; treat reservations and disbursements consistently.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Federal_Funding + Provincial_Funding + Municipal_Contribution + Insurance_Payouts - Buyout_Payments - Support_Service_Costs - Land_Restoration_Costs, 0)`

**Inputs named in guide:** Federal_Funding [stock inflow]; Provincial_Funding [stock inflow]; Municipal_Contribution [stock inflow]; Insurance_Payouts [stock inflow]; Buyout_Payments [stock outflow]; Support_Service_Costs [stock outflow]; Land_Restoration_Costs [stock outflow]

**Consumers named in guide:** Properties_Retreated [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** entity; measure; date; value; amount_basis; grant_number; activity_number

**Existing evidence:** data/Fiscal_Funding.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S23: Texas GLO HUD DRGR quarterly performance reports; S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Grant allocation, obligation, appropriation and available cash are different quantities. See the simulation relationship for the required equation review.

### Cumulative_Disaster_Costs

**Role and units:** Stock. USD_2024.

**Definition:** Disaster damage accumulated from the counter's starting date.

**How derived:** Integrate annual damage in consistent 2024 dollars. Use zero only for a counter starting at model launch; reconstruct historical losses when legacy costs are included.

**Model contribution:** Records cumulative damage across scenarios; it is not itself the benefit of retreat.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Annual_Disaster_Damage_Costs, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Annual_Disaster_Damage_Costs, 0)`

**Inputs named in guide:** Annual_Disaster_Damage_Costs [stock inflow]

**Consumers named in guide:** Cost_Benefit_Ratio [guide equation reference]

**Evidence:** Retained stock initial value: assumed

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S56: FEMA Hazus Flood Model technical manual; S31: BLS Consumer Price Index

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** Do not add insurance, aid and reported property damage as independent costs; all may describe the same loss.

### Buyout_Payments

**Role and units:** Flow. USD_2024/year.

**Definition:** Annual acquisition compensation disbursed by the retreat program.

**How derived:** Sum dated paid acquisition transactions in constant dollars, deduplicate payment IDs and separate purchase price from tenant and supplemental assistance.

**Model contribution:** Drains Retreat_Funding_Available as properties are acquired.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 81: Properties_Retreated * Average_Property_Value * Compensation_Rate

**Inputs named in guide:** Average_Property_Value [guide equation reference]; Compensation_Rate [guide equation reference]; Properties_Retreated [guide equation reference]

**Consumers named in guide:** Retreat_Funding_Available [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S23: Texas GLO HUD DRGR quarterly performance reports; S29: Harris County purchasing, contracts and procurement records; S31: BLS Consumer Price Index

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Award amount is not payment; retain household/property and grant links for deduplication.

### Annual_Disaster_Damage_Costs

**Role and units:** Flow. USD_2024/year.

**Definition:** Expected or observed hazard damage occurring in one year.

**How derived:** For history reconcile event-level physical losses and deflate to 2024 dollars. For simulation combine event probabilities, exposed values and matched damage fractions; distinguish expected losses from realized events.

**Model contribution:** Fills Cumulative_Disaster_Costs and quantifies the damage burden that retreat may avoid.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 82: Hazard_Event_Rate * Properties_at_Risk * Average_Property_Value * Average_Damage_Fraction

**Inputs named in guide:** Average_Damage_Fraction [guide equation reference]; Average_Property_Value [guide equation reference]; Hazard_Event_Rate [guide equation reference]; Properties_at_Risk [guide equation reference]

**Consumers named in guide:** Cumulative_Disaster_Costs [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S56: FEMA Hazus Flood Model technical manual; S07: USACE National Structure Inventory; S31: BLS Consumer Price Index

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Insured/applicant losses are incomplete; calibrate selection and structure-value basis.

### Federal_Funding

**Role and units:** Flow. USD_2024/year.

**Definition:** Federal-origin receipts available to the program per year.

**How derived:** Sum verified receipts by award and transaction date, track restrictions and funding origin, and remove duplicate pass-through reporting. Deflate nominal transactions consistently.

**Model contribution:** Replenishes Retreat_Funding_Available.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 83: Federal_Funding_Availability * Retreat_Program_Eligibility * Political_Priority_Factor

**Inputs named in guide:** Federal_Funding_Availability [guide equation reference]; Political_Priority_Factor [guide equation reference]; Retreat_Program_Eligibility [guide equation reference]

**Consumers named in guide:** Retreat_Funding_Available [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S23: Texas GLO HUD DRGR quarterly performance reports; S24: OpenFEMA HMA project-site inventories; S30: USAspending API and federal award transactions; S21: HCD public-records access route

[Primary source or access page](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)

**Limitation:** USAspending obligations and local receipts must not be pooled without reconciliation.

### Compensation_Rate

**Role and units:** Auxiliary or delayed quantity. payment/value ratio.

**Definition:** Ratio of total modeled acquisition compensation to the specified property-value basis.

**How derived:** For history divide matched acquisition payments by the relevant appraisal amount. For scenarios multiply the selected base schedule by explicit supplements without duplicating eligible costs.

**Model contribution:** Changes acquisition cost, funding-limited throughput and compensation attractiveness.

**Simulation relationship:** Convert the selected compensation category to a numeric base rate, then apply documented adjustments. The array alternative uses Base_Compensation_Rate * Equity_Adjustment * User_Group_Factor.

**Guide equation:** Guide paragraph 85: Compensation_Type_Selector * Equity_Adjustment_Factor

Guide paragraph 261: Base_Compensation_Rate * Equity_Adjustment[Land_User_Group] * User_Group_Factor[Land_User_Group]

**Inputs named in guide:** Compensation_Type_Selector [guide equation reference]; Equity_Adjustment_Factor [guide equation reference]; Base_Compensation_Rate [guide equation reference]; Equity_Adjustment [guide equation reference]; Land_User_Group [guide equation reference]; User_Group_Factor [guide equation reference]

**Consumers named in guide:** Buyout_Payments [guide equation reference]; Properties_Retreated [guide equation reference]; Compensation_Attractiveness [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** A category selector cannot be multiplied as if it were a numeric compensation rate. See the simulation relationship for the required equation review.

### Cost_Benefit_Ratio

**Role and units:** Auxiliary or delayed quantity. ratio.

**Definition:** Ratio of discounted incremental benefits to discounted incremental resource costs of retreat.

**How derived:** Compare retreat with a matched counterfactual over the same horizon. Discount avoided future losses and nonoverlapping benefits, then divide by incremental costs. Do not count sunk historical losses as benefits.

**Model contribution:** Supports economic comparison of retreat policies and the guide's political-will pathway.

**Simulation relationship:** Use PV(incremental avoided future losses + nonoverlapping benefits) / PV(incremental retreat resource costs). Exclude sunk historical damage and avoid counting administration twice. The guide name actually describes a benefit-to-cost ratio.

**Guide equation:** Guide paragraph 89: (Cumulative_Disaster_Costs + Future_Disaster_Costs_NPV) / (Total_Retreat_Costs + Retreat_Program_Admin_Costs)

**Inputs named in guide:** Cumulative_Disaster_Costs [guide equation reference]; Future_Disaster_Costs_NPV [guide equation reference]; Retreat_Program_Admin_Costs [guide equation reference]; Total_Retreat_Costs [guide equation reference]

**Consumers named in guide:** Political_Will [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S32: FEMA benefit-cost analysis guidance; S56: FEMA Hazus Flood Model technical manual; S21: HCD public-records access route; S23: Texas GLO HUD DRGR quarterly performance reports; S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)

**Limitation:** Past sunk disaster costs are not future benefits of a new buyout; prevent administrative-cost double counting. See the simulation relationship for the required equation review.

### Municipal_Fiscal_Stress

**Role and units:** Auxiliary or delayed quantity. ratio or documented scale.

**Definition:** Defined measure of pressure on a taxing jurisdiction's recurring finances.

**How derived:** Compare matched recurring obligations and revenues. If Budget_Gap already includes services, avoid adding Service_Costs again; preserve the underlying deficit ratio before any bounded display transform.

**Model contribution:** Reports the fiscal consequences of lost taxable value and service obligations.

**Simulation relationship:** Resolve whether Budget_Gap already includes Service_Costs. Use one matched recurring-deficit definition and a positive revenue denominator; do not double count service obligations.

**Guide equation:** Guide paragraph 90: MAX(0, MIN(1, (Budget_Gap + Service_Costs) / (Tax_Revenue + Transfer_Payments)))

**Inputs named in guide:** Budget_Gap [guide equation reference]; Service_Costs [guide equation reference]; Tax_Revenue [guide equation reference]; Transfer_Payments [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** Guide Budget_Gap plus Service_Costs can double count expenses; align annual flow units. See the simulation relationship for the required equation review.

### Average_Property_Value

**Role and units:** Parameter. USD_2024/property.

**Definition:** Mean property value on the valuation basis used for acquisition or damage calculations.

**How derived:** Existing proxy is mean positive tot_mkt_val among residential accounts overlapping the 2026 SFHA. For acquisition use the relevant cohort and appraisal basis; for damage use compatible structure and contents values.

**Model contribution:** Converts property counts into buyout spending and exposed monetary value.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Buyout_Payments [guide equation reference]; Annual_Disaster_Damage_Costs [guide equation reference]; Properties_Retreated [guide equation reference]

**Evidence:** Retained parameter: derived_proxy

**Fields or records:** acct; tot_mkt_val; sfha_any_overlap_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S16: FHFA House Price Index datasets; S31: BLS Consumer Price Index

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Do not mix assessed taxable, market, replacement and post-disaster values.

### Discount_Rate

**Role and units:** Parameter. 1/year.

**Definition:** Annual rate used to convert future costs and benefits to present values.

**How derived:** Choose a documented real rate consistent with constant-dollar cash flows and the analysis purpose. Apply PV=sum(amount_t/(1+r)^(t-reference_year)); retain sensitivity alternatives.

**Model contribution:** Makes costs and benefits occurring in different years comparable.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S32: FEMA benefit-cost analysis guidance; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)

**Limitation:** Verify rule/version at use; keep real discount rates with real dollars and nominal rates with nominal dollars.

### Federal_Funding_Availability

**Role and units:** Parameter. USD_2024/year.

**Definition:** Federal funding envelope available for the selected year and scenario.

**How derived:** Use award-specific annual schedules and receipts for history. Future amounts are policy scenarios until awards and release conditions are known.

**Model contribution:** Sets the upper funding input multiplied by eligibility and political priority in the guide.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Federal_Funding [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S23: Texas GLO HUD DRGR quarterly performance reports; S24: OpenFEMA HMA project-site inventories; S30: USAspending API and federal award transactions; S26: Harris County adopted budgets and budget volumes

[Primary source or access page](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)

**Limitation:** Future federal appropriations are uncertain policy inputs, not values recoverable from a past average alone.

### Budget_Gap

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Annual shortfall of recurring revenue relative to the selected operating obligations.

**How derived:** Calculate max(0, obligations-recurring_revenue) for the same fund and year. Define whether Service_Costs is already included before using the guide's stress equation.

**Model contribution:** Supplies fiscal pressure to Municipal_Fiscal_Stress.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Fiscal_Stress [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** Do not include the same service costs again in the fiscal-stress numerator.

### Compensation_Type_Selector

**Role and units:** Policy or scenario selector. category mapped to payment/value ratio.

**Definition:** Selector or numeric base ratio for the chosen compensation schedule.

**How derived:** Choose Market_Value_Option, Pre_Disaster_Value_Option or Enhanced_Compensation_Option and look up its documented numeric offer ratio. A text category cannot be multiplied directly.

**Model contribution:** Supplies the base ratio used by Compensation_Rate; it is not identical to the final adjusted rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Market_Value_Option [category option]; Pre_Disaster_Value_Option [category option]; Enhanced_Compensation_Option [category option]

**Consumers named in guide:** Compensation_Rate [guide equation reference]

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Map each category to a documented appraisal basis/rate; do not multiply an arbitrary category number.

### Equity_Adjustment_Factor

**Role and units:** Policy or scenario input. payment multiplier.

**Definition:** Policy multiplier or assistance adjustment based on specified eligible needs.

**How derived:** Define eligibility and assistance rules, then calculate the adjustment relative to the base offer for each group. Preserve purchase and relocation assistance components separately.

**Model contribution:** Changes compensation adequacy and the cost of equitable participation.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Rate [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S21: HCD public-records access route; S17: HUD Comprehensive Housing Affordability Strategy data

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Normative policy choice; do not fit identity-based compensation penalties as natural laws.

### Future_Disaster_Costs_NPV

**Role and units:** Proposed auxiliary or input. USD_2024 present value.

**Definition:** Present value of future disaster losses in a specified scenario.

**How derived:** Estimate annual losses over the stated horizon and sum each discounted amount. Calculate separately for retreat and counterfactual paths before taking avoided losses.

**Model contribution:** Supplies the future-loss component of economic evaluation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cost_Benefit_Ratio [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S56: FEMA Hazus Flood Model technical manual; S05: Harris Central Appraisal District account and parcel downloads; S32: FEMA benefit-cost analysis guidance

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Model no-retreat and retreat counterfactuals separately; do not treat a gross loss forecast as avoided loss.

### Homeowner_Compensation_Avg

**Role and units:** Proposed auxiliary or input. USD_2024/owner household.

**Definition:** Mean compensation received per owner household, with components separately identified.

**How derived:** Sum verified owner-household acquisition and supplemental payments and divide by unique eligible recipient households. Separate owner-occupants from absentee owners.

**Model contribution:** Supports distributional assessment of owner outcomes and compensation adequacy.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Equity_in_Compensation [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Compare asset compensation and rehousing adequacy on appropriate denominators.

### Initial_Assessment_Value

**Role and units:** Initial value. USD_2024 taxable value.

**Definition:** Baseline initializer of Municipal_Tax_Base retained under the guide's original name.

**How derived:** Derive Municipal_Tax_Base for the chosen opening date, then hold that starting value fixed as the stock initializer. Sum jurisdiction-specific taxable values after exemptions and reconcile to the certified roll. Existing county initialization is a rounded published 2024 value, not a municipal total.

**Model contribution:** Initializes Municipal_Tax_Base; it is not a second independently changing stock.

**Simulation relationship:** Initializes Municipal_Tax_Base; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Tax_Base [stock initializer]

**Evidence:** Derived from/reconciled to Municipal_Tax_Base

**Fields or records:** entity; measure; year; value; unit; source_page; amount_basis

**Existing evidence:** data/Fiscal_Funding.csv

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Insurance_Payouts

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Insurance payments received after hazard losses, allocated to the actual recipient.

**How derived:** Sum claims payments by recipient and date and reconcile duplication-of-benefits records. Include in program cash only amounts legally transferred to the program.

**Model contribution:** Represents a possible funding inflow in the guide, subject to recipient and accounting reconciliation.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Funding_Available [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S21: HCD public-records access route

[Primary source or access page](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2)

**Limitation:** Insurance paid to households does not automatically replenish retreat-program funds.

### Land_Restoration_Costs

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Annual expenditure on restoration activities after acquisition.

**How derived:** Sum dated design, treatment and maintenance payments by project and phase in 2024 dollars, keeping acquisition and demolition separate.

**Model contribution:** Drains retreat funds and contributes to the cost of ecological benefits.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Funding_Available [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S31: BLS Consumer Price Index

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Do not count land acquisition or demolition twice in total retreat costs.

### Municipal_Contribution

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Local-origin funding transferred to the retreat program per year.

**How derived:** Sum local-match and transfer transactions by funding source, fund and fiscal year. Exclude federal or state pass-through money already counted.

**Model contribution:** Adds local funding to Retreat_Funding_Available.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Funding_Available [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports; S21: HCD public-records access route

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** County versus city contribution must be explicit; commitments and cash transfers differ.

### New_Development_Value

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** New taxable value added by construction and newly developed property per year.

**How derived:** Identify newly completed taxable improvements in consecutive rolls and sum their values, separating additions from appreciation of existing assets.

**Model contribution:** Adds new value to Municipal_Tax_Base.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Tax_Base [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S15: Houston-Galveston Area Council forecasts and land cover; S27: Harris County Auditor annual comprehensive financial reports; S58: Harris County Engineer floodplain management and permit records

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Separate additions from reappraisal of existing assets and from nominal inflation.

### Political_Priority_Factor

**Role and units:** Proposed auxiliary or input. allocation share/score.

**Definition:** Share or multiplier reflecting retreat's priority in eligible funding allocation.

**How derived:** Code dated appropriations and allocation decisions against a fixed eligible-funding denominator. Use a transparent rubric only where an observed allocation share is unavailable.

**Model contribution:** Modifies federal funding entering the modeled program.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Federal_Funding [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S26: Harris County adopted budgets and budget volumes; S23: Texas GLO HUD DRGR quarterly performance reports

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Funding is partly constrained by eligibility and awards; do not infer political preference from dollars alone.

### Property_Value_Appreciation

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Annual positive value change on continuing taxable properties.

**How derived:** Compare matched continuing properties across rolls, remove new construction and boundary changes, and adjust for inflation. Sum the positive component under a declared accounting convention.

**Model contribution:** Raises Municipal_Tax_Base independently of new development.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Tax_Base [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S16: FHFA House Price Index datasets; S31: BLS Consumer Price Index

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Appraisal rule changes, exemptions and sales composition can mimic market appreciation.

### Property_Value_Depreciation

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Annual reduction in continuing-property taxable value.

**How derived:** Match repeat-property values, remove disposals and boundary changes, and distinguish ordinary market change from hazard-related loss. Use the same price basis as appreciation.

**Model contribution:** Lowers Municipal_Tax_Base outside retreat removals.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Tax_Base [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S16: FHFA House Price Index datasets; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** A lower roll value is not automatically a disaster effect; avoid subtracting depreciation already included elsewhere.

### Provincial_Funding

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** State-origin funding contribution under the guide's generic provincial label.

**How derived:** For Harris County relabel to State_Funding after model-name reconciliation. Trace state-origin receipts and distinguish them from federal dollars administered through Texas GLO.

**Model contribution:** Supplies the state-level contribution to Retreat_Funding_Available.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Funding_Available [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S23: Texas GLO HUD DRGR quarterly performance reports; S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://glo.texas.gov/disaster-recovery/grant-administration/grant-administration-reporting/hud-drgr-qpr-reports)

**Limitation:** GLO administration does not make federal CDBG-DR money state-origin funding.

### Renter_Compensation_Avg

**Role and units:** Proposed auxiliary or input. USD_2024/renter household.

**Definition:** Mean relocation and assistance payments per renter household.

**How derived:** Sum tenant moving, rental and supplemental assistance and divide by unique tenant households. Retain eligibility, household size and payment components.

**Model contribution:** Supports renter outcome and compensation-adequacy assessment.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Equity_in_Compensation [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not compare the total directly to a homeowner's asset purchase price as a fairness test.

### Retreat_Program_Admin_Costs

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Annual cost of managing the retreat program.

**How derived:** Allocate paid staff time, appraisals, legal work and overhead by activity and period. Ensure these items are not already embedded in Total_Retreat_Costs.

**Model contribution:** Measures administrative resource requirements and the full cost of retreat.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cost_Benefit_Ratio [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S23: Texas GLO HUD DRGR quarterly performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not add administration again if Total_Retreat_Costs already includes it.

### Retreat_Property_Removal

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Taxable value removed from the selected roll because of retreat acquisitions.

**How derived:** Link acquired accounts to the jurisdiction's roll and sum value actually removed or exempted in each tax year. Use effective tax dates rather than assuming immediate removal at closing.

**Model contribution:** Drains Municipal_Tax_Base through retreat.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Tax_Base [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S22: HCFCD public-information access route; S27: Harris County Auditor annual comprehensive financial reports

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** Property-count removal must be converted to taxable-value flow; avoid double counting in depreciation.

### Service_Costs

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Annual public-service obligations within the selected jurisdiction and fund.

**How derived:** Use actual expenditures and estimate the marginal portion changed by retreat. Preserve fixed costs, population served and jurisdiction scope.

**Model contribution:** Supplies the service burden used in fiscal-stress assessment.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Fiscal_Stress [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** Average county spending per resident need not equal marginal cost savings from dispersed acquisitions.

### Support_Service_Costs

**Role and units:** Flow referenced by a stock. USD_2024/year.

**Definition:** Annual cost of relocation and household support services.

**How derived:** Sum paid case-management, transport, housing-search and psychosocial service transactions by period and cost category. Exclude any administrative costs counted elsewhere.

**Model contribution:** Drains Retreat_Funding_Available and records support investment.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Funding_Available [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S31: BLS Consumer Price Index

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Keep these distinct from purchase payments and administrative overhead to avoid duplicate cost allocation.

### Tax_Revenue

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Annual tax collections received by the selected taxing jurisdiction.

**How derived:** Use audited collections for the matching fund and year. For projection apply the relevant rate and collection assumptions to taxable value, including exemptions and timing.

**Model contribution:** Supplies recurring revenue in Municipal_Fiscal_Stress.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Fiscal_Stress [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S27: Harris County Auditor annual comprehensive financial reports; S26: Harris County adopted budgets and budget volumes

[Primary source or access page](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)

**Limitation:** Tax base dollars and revenue dollars/year are different; collection lag and overlapping jurisdictions matter.

### Total_Retreat_Costs

**Role and units:** Proposed auxiliary or input. USD_2024/year for component accounting; separate PV for evaluation.

**Definition:** Combined nonoverlapping costs of the retreat policy over a stated period.

**How derived:** Sum purchase, relocation, administration, demolition, restoration and maintenance costs once. Keep annual, cumulative and discounted totals as explicitly distinct quantities.

**Model contribution:** Provides the cost side of economic and policy comparisons.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cost_Benefit_Ratio [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S23: Texas GLO HUD DRGR quarterly performance reports; S29: Harris County purchasing, contracts and procurement records; S31: BLS Consumer Price Index

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Define scope before calculating CBA; distinguish transfers from social resource costs.

### Transfer_Payments

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Intergovernmental transfers received by the selected local fund per year.

**How derived:** Aggregate receipts by origin, fund and year and reconcile pass-through amounts to avoid duplication with tax revenue or program funding.

**Model contribution:** Adds non-tax revenue to the fiscal-stress denominator.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Municipal_Fiscal_Stress [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S27: Harris County Auditor annual comprehensive financial reports; S23: Texas GLO HUD DRGR quarterly performance reports; S26: Harris County adopted budgets and budget volumes

[Primary source or access page](https://auditor.harriscountytx.gov/Reports/Annual-Comprehensive-Financial-Report-Harris-County)

**Limitation:** Federal pass-throughs and local interfund transfers can otherwise be counted more than once.

### Base_Compensation_Rate

**Role and units:** Policy or scenario input. payment/value ratio.

**Definition:** Base ratio of acquisition compensation to the selected appraisal basis.

**How derived:** Divide base purchase offers by their corresponding appraisal values for history. For a scenario specify a documented ratio before supplements.

**Model contribution:** Establishes the starting compensation offer before group or equity adjustments.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Rate [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Verify historical policy version and valuation basis; future ratios are scenario decisions.

### Budget_Constraint

**Role and units:** Policy or scenario input. USD_2024 or USD_2024/year.

**Definition:** Maximum spending or annual funding allowed in a specified scenario.

**How derived:** Select a budget envelope and time basis, allocate it to years and eligible cost categories, and document whether it constrains cash, commitments or total expenditure.

**Model contribution:** Bounds the optional policy optimization and funding scenarios.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S27: Harris County Auditor annual comprehensive financial reports; S23: Texas GLO HUD DRGR quarterly performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** Match stock versus annual flow and prevent commitments from being treated as available cash.

### Disaster_Costs

**Role and units:** Derived mapping requiring reconciliation. USD_2024 present value for the objective.

**Definition:** Unresolved aggregate disaster-loss term in the guide's optimization objective.

**How derived:** For Total_Social_Cost use the present value of residual future losses under each scenario. Reconcile this name with annual, cumulative and future-NPV loss variables.

**Model contribution:** Carries disaster losses into policy optimization without mixing annual flows and accumulated amounts.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Total_Social_Cost [guide equation reference]

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S25: OpenFEMA NFIP claims and Individual Assistance/Housing Assistance; S56: FEMA Hazus Flood Model technical manual

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Specify annual versus present-value/cumulative units before adding to the objective.

### Enhanced_Compensation_Option

**Role and units:** Category. categorical.

**Definition:** Compensation category with explicit supplements beyond the selected base valuation.

**How derived:** Specify eligible components and their valuation basis. The guide's 1.2 to 1.5 ratios are illustrative scenario values.

**Model contribution:** Selects an enhanced offer schedule through Compensation_Type_Selector.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects an enhanced offer schedule through Compensation_Type_Selector.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Type_Selector [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Equity_Adjustment

**Role and units:** Alias. payment multiplier.

**Definition:** Group-indexed alias of Equity_Adjustment_Factor retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Equity_Adjustment_Factor. Define eligibility and assistance rules, then calculate the adjustment relative to the base offer for each group. Preserve purchase and relocation assistance components separately.

**Model contribution:** Connects guide references to Equity_Adjustment_Factor without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Equity_Adjustment_Factor without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Rate [guide equation reference]

**Evidence:** Derived from/reconciled to Equity_Adjustment_Factor

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S21: HCD public-records access route

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Funding

**Role and units:** Proposed auxiliary or input. USD_2024 or USD_2024/year; resolve budget scope.

**Definition:** Unresolved funding quantity used in the guide's budget constraint.

**How derived:** Decide whether the optimization constrains annual expenditure, cumulative expenditure or available cash, and match Budget_Constraint to that same quantity and period.

**Model contribution:** Makes the optional funding constraint meaningful once its accounting scope is fixed.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S23: Texas GLO HUD DRGR quarterly performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** Do not silently equate Funding with Funding_Available; select and document the quantity.

### Funding_Available

**Role and units:** Alias. USD_2024.

**Definition:** Same quantity of Retreat_Funding_Available retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Retreat_Funding_Available. Reconstruct opening balance plus eligible receipts less actual spending, adjusting for restrictions and committed obligations under one accounting convention. An unspent allocation is not automatically available cash.

**Model contribution:** Connects guide references to Retreat_Funding_Available without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Retreat_Funding_Available without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Derived from/reconciled to Retreat_Funding_Available

**Fields or records:** entity; measure; date; value; amount_basis; grant_number; activity_number

**Existing evidence:** data/Fiscal_Funding.csv

**Sources:** S21: HCD public-records access route; S23: Texas GLO HUD DRGR quarterly performance reports; S26: Harris County adopted budgets and budget volumes

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Market_Value_Option

**Role and units:** Category. categorical.

**Definition:** Compensation category tied to a stated market-value appraisal.

**How derived:** Define appraisal date, property interest and eligible additions. The guide sets an illustrative ratio of 1.0 to that basis.

**Model contribution:** Selects a market-value offer schedule.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a market-value offer schedule.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Type_Selector [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Pre_Disaster_Value_Option

**Role and units:** Category. categorical.

**Definition:** Compensation category using an explicitly dated pre-disaster valuation basis.

**How derived:** Link the relevant pre-event appraisal and payment rules. The guide's 1.1 ratio is illustrative and does not calculate the pre-disaster valuation.

**Model contribution:** Selects an alternative offer basis for Compensation_Type_Selector.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects an alternative offer basis for Compensation_Type_Selector.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Type_Selector [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Retreat_Program_Costs

**Role and units:** Derived mapping requiring reconciliation. USD_2024 present value for the objective.

**Definition:** Cost term for the retreat program in the guide's optimization objective.

**How derived:** Use the present value of the nonoverlapping annual components defined under Total_Retreat_Costs, on the same horizon as the other objective terms.

**Model contribution:** Carries program costs into Total_Social_Cost.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Total_Social_Cost [guide equation reference]

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S23: Texas GLO HUD DRGR quarterly performance reports; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Total_Social_Cost

**Role and units:** Auxiliary or delayed quantity. USD_2024 present value.

**Definition:** Total incremental resource losses and costs of a scenario, net of compatible benefits.

**How derived:** On one present-value basis combine retreat costs, residual disaster losses and valued social disruption, then subtract nonoverlapping ecosystem benefits. Report unmonetized outcomes separately.

**Model contribution:** Defines the optional optimization objective.

**Simulation relationship:** Place all monetary terms on the same incremental present-value basis. Keep transfers distinct from resource costs and prevent duplication across disaster, ecosystem and disruption terms.

**Guide equation:** Guide paragraph 361: Retreat_Program_Costs + Disaster_Costs + Social_Disruption_Costs - Ecosystem_Benefits

**Inputs named in guide:** Disaster_Costs [guide equation reference]; Ecosystem_Benefits [guide equation reference]; Retreat_Program_Costs [guide equation reference]; Social_Disruption_Costs [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S32: FEMA benefit-cost analysis guidance; S21: HCD public-records access route; S56: FEMA Hazus Flood Model technical manual; S52: Natural Capital Project InVEST methods and data; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.fema.gov/sites/default/files/documents/fema_policy-206-23-001-bca-discount-rate-and-streamlined-approaches_april-24-2024.pdf)

**Limitation:** Transfers, assets, annual flows and present values cannot be added without an explicit accounting convention. See the simulation relationship for the required equation review.

### User_Group_Factor

**Role and units:** Policy or scenario input. documented assistance modifier.

**Definition:** Group-specific policy adjustment to the base compensation schedule.

**How derived:** Define assistance rules by tenure or other justified eligibility class, using documented needs and eligible costs. Record a scenario value rather than inferring behavior from group identity.

**Model contribution:** Allows the optional compensation array to reflect different eligible costs across land-user groups.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Rate [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Transaction or account ID, fund and jurisdiction, funding origin, eligible cost category, nominal amount, price basis, receipt/payment/effective date, restrictions and appraisal basis.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S21: HCD public-records access route; S17: HUD Comprehensive Housing Affordability Strategy data; S46: HUD Tribal Directory Assessment Tool; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Do not assign arbitrary numeric effects solely from social identity; tenure compensation components differ.

## Governance

### Community_Trust_in_Process

**Role and units:** Stock. trust points on a defined 0 to 100 scale.

**Definition:** Trust in the named agency and procedures administering retreat.

**How derived:** Collect repeated questions on competence, fairness and reliability of the actual process. Validate scoring and baseline aggregation. General institutional trust is an imperfect substitute.

**Model contribution:** Stores trust, supports willingness through Trust_Factor and records effects of delays and engagement.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Trust_Building_Actions - Trust_Erosion, 50). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Trust_Building_Actions - Trust_Erosion, 50)`

**Inputs named in guide:** Trust_Building_Actions [stock inflow]; Trust_Erosion [stock outflow]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S39: OECD Guidelines on Measuring Trust; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S21: HCD public-records access route

[Primary source or access page](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)

**Limitation:** GHCP media/school trust is not buyout-process trust; general trust is contextual only.

### Retreat_Policy_Development_Progress

**Role and units:** Stock. policy-progress points, 0 to 100.

**Definition:** Accumulated progress toward a defined operational retreat policy.

**How derived:** Code weighted milestones from recognition to approved policy, funds and procedures. The initial value must describe the actual program stage.

**Model contribution:** Tracks policy development and reduces the remaining progress in Policy_Development_Rate.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Policy_Development_Rate, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Policy_Development_Rate, 0)`

**Inputs named in guide:** Policy_Development_Rate [stock inflow]

**Consumers named in guide:** Policy_Development_Rate [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Percent complete is an analyst rubric, not a directly published continuous stock.

### Stakeholder_Engagement_Level

**Role and units:** Stock. engagement points on a defined 0 to 100 scale.

**Definition:** Current extent and depth of stakeholder involvement.

**How derived:** Construct a transparent score from representation, unique participation, repeat involvement and influence. Measure baseline and repeated changes on the same scale.

**Model contribution:** Accumulates engagement gains and fatigue; any additional influence on policy or trust must be connected explicitly.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Engagement_Activities - Engagement_Fatigue, 20). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Engagement_Activities - Engagement_Fatigue, 20)`

**Inputs named in guide:** Engagement_Activities [stock inflow]; Engagement_Fatigue [stock outflow]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Meeting counts or attendees alone do not measure representative influence or engagement quality.

### Trust_Building_Actions

**Role and units:** Flow. trust points/year.

**Definition:** Annual gain in process-trust points associated with successful and transparent engagement.

**How derived:** Link dated actions and demonstration exposure to repeated trust measurements. Estimate scale-point gains per year and a maximum attainable trust level.

**Model contribution:** Fills Community_Trust_in_Process.

**Simulation relationship:** Normalize demonstration exposure and define a gain coefficient in trust-points/year. Include a headroom or saturation condition so trust cannot grow without limit.

**Guide equation:** Guide paragraph 102: Transparency_Level * Community_Engagement_Quality * Successful_Retreat_Demonstrations * 5

**Inputs named in guide:** Community_Engagement_Quality [guide equation reference]; Successful_Retreat_Demonstrations [guide equation reference]; Transparency_Level [guide equation reference]

**Consumers named in guide:** Community_Trust_in_Process [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S39: OECD Guidelines on Measuring Trust; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** The guide multiplier 5 is uncalibrated; action counts require an estimated conversion into trust change. See the simulation relationship for the required equation review.

### Trust_Erosion

**Role and units:** Flow. trust points/year.

**Definition:** Annual loss of process-trust points due to adverse experiences.

**How derived:** Estimate within-person trust changes associated with perceived inequity, normalized delay and communication failures; calibrate the per-year response coefficients.

**Model contribution:** Drains Community_Trust_in_Process and can weaken participation through Trust_Factor.

**Simulation relationship:** Use Community_Trust_in_Process and normalize delays and other predictors before addition. Express the erosion coefficient in 1/year and estimate it from repeated observations.

**Guide equation:** Guide paragraph 103: Community_Trust * (Perceived_Inequity + Process_Delays + Communication_Failures) * 0.1

**Inputs named in guide:** Communication_Failures [guide equation reference]; Community_Trust [guide equation reference]; Perceived_Inequity [guide equation reference]; Process_Delays [guide equation reference]

**Consumers named in guide:** Community_Trust_in_Process [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S39: OECD Guidelines on Measuring Trust; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Standardize predictors before combining; complaints are selected observations. See the simulation relationship for the required equation review.

### Policy_Development_Rate

**Role and units:** Flow. milestone points/year.

**Definition:** Annual increase in a defined policy-development progress score.

**How derived:** Assign milestone weights before coding, reconstruct dated progress and divide changes by elapsed years. Calibrate the relationship to governance capacity and participation.

**Model contribution:** Fills Retreat_Policy_Development_Progress while slowing as completion approaches.

**Simulation relationship:** Use compatible 0 to 1 capacity and participation measures and Political_Will/100. The coefficient 10 must carry policy-points/year and remains uncalibrated.

**Guide equation:** Guide paragraph 104: Governance_Capacity * Multi_Stakeholder_Participation * (Political_Will / 100) * 10 * (1 - Retreat_Policy_Development_Progress / 100)

**Inputs named in guide:** Governance_Capacity [guide equation reference]; Multi_Stakeholder_Participation [guide equation reference]; Political_Will [guide equation reference]; Retreat_Policy_Development_Progress [guide equation reference]

**Consumers named in guide:** Retreat_Policy_Development_Progress [stock inflow]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** The guide factor 10 and multiplicative functional form are hypotheses, not measured rates. See the simulation relationship for the required equation review.

### Decision_Making_Approach

**Role and units:** Policy or scenario selector. categorical.

**Definition:** Selected governance and acquisition-consent approach for the program.

**How derived:** Code the adopted process from program documents and dates. Represent scenario alternatives with an explicit categorical lookup rather than multiplying text labels.

**Model contribution:** Determines the policy setting for participation and acquisition; behavioral effects require separate equations.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 106: Policy_Choice_Selector

**Inputs named in guide:** Policy_Choice_Selector [guide equation reference]; Voluntary [category option]; Voluntary_with_Incentives [category option]; Persuasive [category option]; Mandatory_with_Optout [category option]; Fully_Mandatory [category option]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S28: Harris County Commissioners Court agendas, minutes and votes; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Separate participation in planning from consent to acquisition; category codes carry no numeric magnitude.

### Governance_Structure_Effectiveness

**Role and units:** Auxiliary or delayed quantity. documented score.

**Definition:** Composite representation of actor coverage, coordination and authority clarity.

**How derived:** Divide engaged actors by the defined actor universe and multiply by compatible normalized coordination and clarity scores. Validate the composite against delivery performance.

**Model contribution:** Describes the governance structure; its downstream effect is conceptual unless an explicit equation is added.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 107: (Number_of_Actors_Engaged / Potential_Actors) * Coordination_Quality * Decision_Authority_Clarity

**Inputs named in guide:** Coordination_Quality [guide equation reference]; Decision_Authority_Clarity [guide equation reference]; Number_of_Actors_Engaged [guide equation reference]; Potential_Actors [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** More actors need not improve effectiveness; avoid a mechanically multiplicative index without validation.

### First_Nations_Engagement_Quality

**Role and units:** Auxiliary or delayed quantity. co-designed indicators.

**Definition:** Quality of engagement with relevant Indigenous communities under locally agreed criteria.

**How derived:** Establish local relevance and evaluate process, leadership, recognition of nonmarket values and rights with those communities. Normalize component scales only after agreement.

**Model contribution:** Combines the guide's four cultural-process components; downstream use remains to be specified.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 108: Cultural_Appropriate_Process * Indigenous_Leadership_Level * Non_Market_Value_Recognition * Land_Rights_Respect

**Inputs named in guide:** Cultural_Appropriate_Process [guide equation reference]; Indigenous_Leadership_Level [guide equation reference]; Land_Rights_Respect [guide equation reference]; Non_Market_Value_Recognition [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S45: Texas Historical Commission Historic Sites Atlas; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Localize Canadian terminology; do not infer engagement quality from race, ancestry or county population shares.

### Community_Engagement_Quality

**Role and units:** Parameter. rubric/survey score.

**Definition:** Quality of opportunities for affected people to understand and influence decisions.

**How derived:** Score accessibility, responsiveness, voice and influence with a prespecified rubric and resident responses. Validate coding and normalize to the guide's 0 to 1 range if retained.

**Model contribution:** Modifies trust building and the effect of engagement activities.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Building_Actions [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S39: OECD Guidelines on Measuring Trust

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Participants may differ from nonparticipants; preserve subgroup and nonresponse information.

### Community_Trust_Building_Time

**Role and units:** Parameter. years.

**Definition:** Time required for process trust to adjust after a sustained improvement.

**How derived:** Fit repeated agency-specific trust measurements following defined actions using a lagged adjustment model.

**Model contribution:** Provides a potential trust adjustment delay; the main guide trust-flow equations do not yet use it.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S39: OECD Guidelines on Measuring Trust; S21: HCD public-records access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)

**Limitation:** No single public Harris County time constant was found; elicit uncertain priors if longitudinal data remain unavailable.

### Governance_Capacity

**Role and units:** Parameter. FTE/resources or score.

**Definition:** Resources and expertise available to develop and operate retreat policy.

**How derived:** Measure filled staff effort, relevant experience, contracts and processing performance. If the guide score is retained, document its transformation from those observations.

**Model contribution:** Controls Policy_Development_Rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Policy_Development_Rate [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S26: Harris County adopted budgets and budget volumes; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not substitute authorized staff or budget for actual implementation capability without checking utilization.

### Policy_Implementation_Delay

**Role and units:** Parameter. years.

**Definition:** Elapsed time from adoption or award to the specified operating milestone.

**How derived:** Link adoption and operational dates for comparable programs; estimate durations including pending cases and define the start and end events.

**Model contribution:** Delays Policy_Adopted into Policy_Implemented.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Policy_Implemented [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Several different delays exist; choose the transition represented by the model flow.

### Political_Will

**Role and units:** Parameter; also conceptual response. coded score.

**Definition:** Measured or assumed priority assigned by decision makers to retreat.

**How derived:** Code votes, appropriations and sustained actions with a fixed 0 to 100 rubric, or explicitly set a scenario score. Fit any event-driven change separately.

**Model contribution:** Modifies Policy_Development_Rate; the guide also proposes responses to disasters and economic evaluation.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 179: f(Recent_Disaster_Events, Cost_Benefit_Ratio); conceptual function

**Inputs named in guide:** Cost_Benefit_Ratio [guide equation reference]; Recent_Disaster_Events [guide equation reference]

**Consumers named in guide:** Policy_Development_Rate [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S26: Harris County adopted budgets and budget volumes; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Event proximity and rhetoric are proxies; no public 0–100 political-will series was found.

### Transparency_Level

**Role and units:** Parameter. rubric score.

**Definition:** Accessibility, timeliness and completeness of program information and explanations.

**How derived:** Code public information, understandable decisions, appeals and disclosure practices; validate with resident experience and map to a fixed 0 to 1 scale.

**Model contribution:** Multiplies Trust_Building_Actions.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Building_Actions [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Document count alone is not transparency; a reproducible rubric is required.

### Communication_Failures

**Role and units:** Proposed auxiliary or input. rate or documented score.

**Definition:** Missed, inconsistent or inaccessible program communications.

**How derived:** Count documented failures and divide by relevant communications or households reached, or use a validated respondent scale. Separate response delay from contradictory or missing information.

**Model contribution:** Contributes to Trust_Erosion after conversion to a compatible normalized scale.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Erosion [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Complaint records undercount silent nonparticipants; ensure score units match trust-erosion formulation.

### Community_Trust

**Role and units:** Alias. trust points on a defined 0 to 100 scale.

**Definition:** Same quantity of Community_Trust_in_Process retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Community_Trust_in_Process. Collect repeated questions on competence, fairness and reliability of the actual process. Validate scoring and baseline aggregation. General institutional trust is an imperfect substitute.

**Model contribution:** Connects guide references to Community_Trust_in_Process without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Community_Trust_in_Process without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Erosion [guide equation reference]

**Evidence:** Derived from/reconciled to Community_Trust_in_Process

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S39: OECD Guidelines on Measuring Trust; S21: HCD public-records access route

[Primary source or access page](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Coordination_Quality

**Role and units:** Proposed auxiliary or input. handoff performance/score.

**Definition:** Effectiveness of handoffs and joint decisions across responsible organizations.

**How derived:** Measure completed handoffs, unresolved referrals and elapsed time relative to a stated benchmark, supported by staff and participant evidence.

**Model contribution:** Multiplies actor participation in Governance_Structure_Effectiveness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Governance_Structure_Effectiveness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Meeting frequency alone cannot measure coordination quality.

### Cultural_Appropriate_Process

**Role and units:** Proposed auxiliary or input. co-designed rubric.

**Definition:** Extent to which process design follows affected communities' agreed practices.

**How derived:** Develop indicators with the relevant community, document observed process steps and compare with agreed standards.

**Model contribution:** Contributes to the guide's optional Indigenous engagement quality measure.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Engagement_Quality [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S21: HCD public-records access route

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Local consultation is required to define appropriateness; outside coding is only a preliminary audit.

### Decision_Authority_Clarity

**Role and units:** Proposed auxiliary or input. rubric score.

**Definition:** Clarity of who can make, implement and review program decisions.

**How derived:** Compare formal delegations and appeal procedures with staff and resident understanding, using a published rubric.

**Model contribution:** Modifies Governance_Structure_Effectiveness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Governance_Structure_Effectiveness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Written authority and perceived clarity can differ; retain both indicators.

### Engagement_Activities

**Role and units:** Flow referenced by a stock. engagement points/year (raw activity counts retained separately).

**Definition:** Activity that increases the modeled stock of stakeholder engagement.

**How derived:** Retain event counts and unique attendance as raw data, then estimate their contribution to changes in the engagement score per year. Counts of meetings are not score points.

**Model contribution:** Fills Stakeholder_Engagement_Level.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Stakeholder_Engagement_Level [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Simple event counts cannot enter a 0–100 engagement stock without a conversion rule.

### Engagement_Fatigue

**Role and units:** Flow referenced by a stock. engagement points/year.

**Definition:** Decline in engagement caused by repeated burden or unsuccessful participation.

**How derived:** Estimate loss of continued participation and measured engagement over time among previously involved people; separate fatigue from relocation or ineligibility.

**Model contribution:** Drains Stakeholder_Engagement_Level.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Stakeholder_Engagement_Level [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Time constraints and satisfaction may explain nonattendance; fatigue should not be assumed from absence alone.

### Fully_Mandatory

**Role and units:** Category. categorical.

**Definition:** Category describing acquisition without an ordinary voluntary participation choice.

**How derived:** Code the actual program authority and consent rules with a defined effective period. It is a category, not a numeric willingness score.

**Model contribution:** Selects one Decision_Making_Approach alternative.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects one Decision_Making_Approach alternative.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Indigenous_Leadership_Level

**Role and units:** Proposed auxiliary or input. co-defined process indicator.

**Definition:** Recognized leadership and decision influence of relevant Indigenous communities.

**How derived:** Document formal roles, actual decision authority and community assessment against an agreed rubric.

**Model contribution:** Contributes to First_Nations_Engagement_Quality.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Engagement_Quality [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Leadership quality cannot be inferred from outsider demographics or a universal numeric scale.

### Land_Rights_Respect

**Role and units:** Proposed auxiliary or input. co-designed/legal process indicators.

**Definition:** Extent to which the process recognizes and follows applicable land and tenure rights.

**How derived:** Review documented tenure, consultation, consent and dispute outcomes with relevant communities and authorities; define evidence and scoring before aggregation.

**Model contribution:** Contributes to First_Nations_Engagement_Quality.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Engagement_Quality [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S54: 44 CFR Part 80, property acquisition and relocation for open space; S55: Harris County Clerk real-property records; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** A property database alone cannot establish respect for rights or resolve contested interests.

### Mandatory_with_Optout

**Role and units:** Category. categorical.

**Definition:** Category describing a mandatory framework with a defined exemption or opt-out mechanism.

**How derived:** Record the actual opt-out conditions, decision authority and effective dates.

**Model contribution:** Selects a Decision_Making_Approach alternative requiring distinct eligibility and participation rules.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Decision_Making_Approach alternative requiring distinct eligibility and participation rules.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Multi_Stakeholder_Participation

**Role and units:** Proposed auxiliary or input. representation/influence score.

**Definition:** Representation and substantive involvement across the defined stakeholder groups.

**How derived:** Calculate coverage of eligible groups and unique participants, and code their role in decisions. Normalize to a documented participation scale.

**Model contribution:** Modifies Policy_Development_Rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Policy_Development_Rate [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not equate the fraction attending with equal influence or consensus.

### Non_Market_Value_Recognition

**Role and units:** Proposed auxiliary or input. co-designed rubric.

**Definition:** Extent to which social, cultural and place values influence program decisions.

**How derived:** Record which values residents identify and whether resulting assistance or design decisions address them, using a transparent rubric.

**Model contribution:** Contributes to First_Nations_Engagement_Quality.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Engagement_Quality [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S38: Williams and Vaske place-attachment measurement study, USFS repository; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Recognition is not equivalent to assigning a dollar value to every cultural interest.

### Number_of_Actors_Engaged

**Role and units:** Proposed auxiliary or input. distinct actors.

**Definition:** Distinct actors with documented active participation in the process.

**How derived:** Maintain a dated registry of unique organizations or stakeholder units with participation evidence. Use the same unit of actor as Potential_Actors.

**Model contribution:** Forms the numerator of actor coverage in Governance_Structure_Effectiveness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Governance_Structure_Effectiveness [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Count organizations and individual households separately; duplicate representatives can inflate coverage.

### Policy_Choice_Selector

**Role and units:** Policy selector. category.

**Definition:** Policy selector of Decision_Making_Approach retained under the guide's original name.

**How derived:** Store the selected category that defines Decision_Making_Approach. Resolve this as the input selector rather than creating two variables that refer back to each other.

**Model contribution:** Sets the policy category used by Decision_Making_Approach.

**Simulation relationship:** Sets the policy category used by Decision_Making_Approach. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [guide equation reference]

**Evidence:** Derived from/reconciled to Decision_Making_Approach

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Potential_Actors

**Role and units:** Proposed auxiliary or input. distinct eligible actors.

**Definition:** Complete universe of actors expected to participate in the process.

**How derived:** Define eligible actor classes and construct a dated deduplicated registry before counting engagement. Avoid mixing people and organizations in one denominator.

**Model contribution:** Provides the denominator for actor coverage.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Governance_Structure_Effectiveness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S46: HUD Tribal Directory Assessment Tool

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** There is no ready official denominator; agree the actor categories and boundary before measuring coverage.

### Process_Delays

**Role and units:** Proposed auxiliary or input. years or standardized delay.

**Definition:** Delay beyond a declared processing benchmark.

**How derived:** Measure stage durations from case dates, include right-censored pending cases and compare with a stated service benchmark. Normalize delay before combining it with dimensionless indices.

**Model contribution:** Contributes to Trust_Erosion.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Erosion [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not combine raw years with 0–1 inequity scores without an explicit scale conversion.

### Successful_Retreat_Demonstrations

**Role and units:** Proposed auxiliary or input. verified examples or normalized exposure share.

**Definition:** Verified examples of satisfactory retreat outcomes known to the target population.

**How derived:** Define success criteria, verify case outcomes, and measure which eligible residents know those examples. Normalize exposure to examples if used as a multiplier.

**Model contribution:** Supports Trust_Building_Actions and the conceptual successful-retreat feedback.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Building_Actions [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Program publicity or completed acquisitions alone do not establish successful outcomes or trust effects.

### Voluntary_with_Incentives

**Role and units:** Category. categorical.

**Definition:** Category describing voluntary retreat with additional incentives.

**How derived:** Record voluntary consent rules, incentive eligibility, amounts and dates. Keep incentives separate from the consent category.

**Model contribution:** Selects a Decision_Making_Approach alternative with a distinct compensation schedule.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Decision_Making_Approach alternative with a distinct compensation schedule.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Community_Opposition

**Role and units:** Auxiliary or delayed quantity. proportion or intensity.

**Definition:** Extent of opposition to the retreat program among affected residents.

**How derived:** Measure opposition with eligible-population surveys, refusals and testimony using a defined denominator. Fit the response to perceived inequity instead of treating the guide lookup as observations.

**Model contribution:** Represents a proposed balancing response to perceived inequity; its effect on implementation still needs an equation.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 178: f(Perceived_Inequity); illustrative lookup

**Inputs named in guide:** Perceived_Inequity [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative guide lookup; not fitted

**Fields or records:** lookup_name=Community_Opposition_Lookup; input_value; output_value

**Existing evidence:** data/Lookup_Tables.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Public speakers and petitioners are selected; the guide lookup is not an estimated population response.

### Community_Opposition_Lookup

**Role and units:** Lookup table. perceived-inequity score to opposition score.

**Definition:** Existing input-table function mapping perceived inequity to an opposition score.

**How derived:** Select rows with lookup_name=Community_Opposition_Lookup, retain ordered input and output values, and apply the recorded interpolation and endpoint rules. These are illustrative guide points, not fitted responses.

**Model contribution:** Supplies a proposed implementation of the guide's Community_Opposition response to Perceived_Inequity.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative guide lookup; not fitted

**Fields or records:** lookup_name; input_value; output_value; interpolation; below_range; above_range; evidence_status

**Existing evidence:** data/Lookup_Tables.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S28: Harris County Commissioners Court agendas, minutes and votes; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Public speakers and petitioners are selected; the guide lookup is not an estimated population response.

### Community_Petition_Threshold_Met

**Role and units:** Policy or scenario input. binary.

**Definition:** Whether a documented community request meets the chosen activation rule.

**How derived:** Verify unique eligible petitioners, calculate count or share and compare with the explicit threshold and date rule.

**Model contribution:** Activates the community-request branch of Retreat_Program_Active.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S21: HCD public-records access route; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Confirm that such a trigger exists in the actual program; otherwise it is a hypothetical scenario rule.

### Cultural_Protocol_Adherence

**Role and units:** Proposed auxiliary or input. co-designed process indicators.

**Definition:** Degree to which agreed cultural protocols are actually followed.

**How derived:** Record completion of required protocol steps and community evaluation of adherence, with a fixed scoring and missing-data rule.

**Model contribution:** Enters the optional First_Nations_Adjustment_Factor after local scope and interpretation are resolved.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Adjustment_Factor [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S21: HCD public-records access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** No generic public county score exists; appropriate communities must define the criteria.

### Persuasive

**Role and units:** Category. categorical.

**Definition:** Category describing a process that uses persuasion to encourage retreat.

**How derived:** Code outreach and decision rules while distinguishing persuasion from acquisition consent or legal compulsion.

**Model contribution:** Selects a Decision_Making_Approach alternative.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Decision_Making_Approach alternative.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Policy_Adopted

**Role and units:** Proposed auxiliary or input. dated indicator/milestone.

**Definition:** Dated adoption status of a defined retreat policy.

**How derived:** Identify the formal adoption instrument and effective date, then construct a step indicator or separate milestone series.

**Model contribution:** Supplies the input to the guide's delayed Policy_Implemented relationship.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Policy_Implemented [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** Adoption does not imply the program is operating or fully funded.

### Policy_Implemented

**Role and units:** Auxiliary or delayed quantity. operational milestone/coverage.

**Definition:** Degree or status of operational implementation after adoption.

**How derived:** Code application opening, staffing and delivery milestones. A delayed binary input produces a continuous implementation trajectory in the guide; choose status versus progress explicitly.

**Model contribution:** Represents the lag between formal policy and operational action.

**Simulation relationship:** Decide whether output is a continuous implementation fraction or binary operational status. A third-order delay of an adoption step does not produce a binary opening date.

**Guide equation:** Guide paragraph 174: DELAY3(Policy_Adopted, Policy_Implementation_Delay)

**Inputs named in guide:** Policy_Adopted [guide equation reference]; Policy_Implementation_Delay [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Choose a specific implementation endpoint before estimating its delay. See the simulation relationship for the required equation review.

### Policy_Stimulus_Present

**Role and units:** Proposed auxiliary or input. binary/rubric.

**Definition:** Whether a defined mandate, funding opportunity or incentive supporting retreat is present.

**How derived:** Code dated qualifying actions against a prespecified activation rule and expiry period.

**Model contribution:** Supports the proactive-policy branch of Retreat_Program_Active.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S28: Harris County Commissioners Court agendas, minutes and votes; S23: Texas GLO HUD DRGR quarterly performance reports; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://harriscountytx.legistar.com/Calendar.aspx)

**Limitation:** No universal stimulus measure exists; the trigger definition is a scenario/design choice.

### Recent_Disaster_Events

**Role and units:** Proposed auxiliary or input. events per rolling window.

**Definition:** Number of qualifying disasters during a fixed recent interval.

**How derived:** Count distinct events meeting the model's severity rule in a rolling window ending at model time. State window length and reporting coverage.

**Model contribution:** Supplies the guide's proposed event-driven Political_Will relationship.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Political_Will [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** Choose window and threshold before linking to political will; events can share a disaster declaration.

### Recent_Major_Disaster

**Role and units:** Proposed auxiliary or input. binary or event count.

**Definition:** Indicator or count of major disasters inside a specified recency window.

**How derived:** Apply a fixed severity or declaration rule to deduplicated event records and evaluate the declared lookback window.

**Model contribution:** Activates the reactive-disaster branch of Retreat_Program_Active.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S08: NOAA Storm Events bulk files; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

**Limitation:** Do not use an arbitrary row count to trigger program activation.

### Voluntary

**Role and units:** Category. categorical.

**Definition:** Category describing retreat based on voluntary acquisition consent.

**How derived:** Code actual program consent and withdrawal rules separately from planning participation.

**Model contribution:** Selects a Decision_Making_Approach alternative.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Decision_Making_Approach alternative.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Decision_Making_Approach [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Policy/program ID, dated decision or process milestone, eligible actor universe, documented participation, stage timestamps and repeated respondent-specific process measures.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

## Implementation

### Properties_in_Retreat_Pipeline

**Role and units:** Stock. properties.

**Definition:** Active eligible property cases not yet completed or exited.

**How derived:** At each date count distinct cases entered before that date minus completed, withdrawn and otherwise exited cases. Reconcile all status transitions and repeat applications.

**Model contribution:** Stores unmet implementation workload and constrains property completions.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Retreat_Applications + Proactive_Retreat_Identification - Properties_Retreated - Retreat_Dropouts, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Retreat_Applications + Proactive_Retreat_Identification - Properties_Retreated - Retreat_Dropouts, 0)`

**Inputs named in guide:** Retreat_Applications [stock inflow]; Proactive_Retreat_Identification [stock inflow]; Properties_Retreated [stock outflow]; Retreat_Dropouts [stock outflow]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** series=pending_acquisition_status_sum; time; value; program_id; designation; quality_flag

**Existing evidence:** data/Calibration_Data.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** State the entry stage; expressions of interest and formal applications must remain separate.

### Relocated_Households

**Role and units:** Stock. households.

**Definition:** Cumulative households meeting the model's defined successful relocation criterion.

**How derived:** Count distinct qualifying household IDs, including tenants, with cohort and outcome dates. Use zero only for a counter of new post-start successes.

**Model contribution:** Records successful household outcomes separately from property acquisitions.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Successful_Relocations, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Successful_Relocations, 0)`

**Inputs named in guide:** Successful_Relocations [stock inflow]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: assumed

**Fields or records:** series=relocated_cases; time; value; program_id; observation_basis

**Existing evidence:** data/Calibration_Data.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** A completed purchase may displace several households or no resident household; household count differs from properties.

### Support_Services_Capacity

**Role and units:** Stock. caseworker FTE.

**Definition:** Productive caseworker capacity assigned to retreat at a point in time.

**How derived:** Divide assigned productive hours by standard full-time hours for the period; include filled staff and equivalent contracted effort.

**Model contribution:** Constrains Properties_Retreated through Caseworker_Throughput.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Capacity_Building - Capacity_Attrition, Initial_Capacity). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Capacity_Building - Capacity_Attrition, Initial_Capacity)`

**Inputs named in guide:** Capacity_Building [stock inflow]; Capacity_Attrition [stock outflow]; Initial_Capacity [stock initializer]

**Consumers named in guide:** Properties_Retreated [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S26: Harris County adopted budgets and budget volumes; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Countywide authorized posts and facility counts are not available retreat-program capacity.

### Retreat_Applications

**Role and units:** Flow. properties/year.

**Definition:** New formal property applications entering the program per year.

**How derived:** Count first complete applications by unique property and entry date, separating inquiries, resubmissions and ineligible cases. Divide by elapsed years.

**Model contribution:** Fills Properties_in_Retreat_Pipeline and converts willingness and awareness into workload.

**Simulation relationship:** Candidate form: eligible non-pipeline properties * bounded willingness * awareness * ease / application_interval_years. Multiply by the activation switch. Define the additional interval and avoid repeat entry.

**Guide equation:** Guide paragraph 120: Properties_at_Risk * Retreat_Willingness * Program_Awareness * Application_Ease_Factor

**Inputs named in guide:** Application_Ease_Factor [guide equation reference]; Program_Awareness [guide equation reference]; Properties_at_Risk [guide equation reference]; Retreat_Willingness [guide equation reference]

**Consumers named in guide:** Properties_in_Retreat_Pipeline [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** The guide expression needs an application-attempt rate per year to produce a flow. See the simulation relationship for the required equation review.

### Properties_Retreated

**Role and units:** Flow. properties/year.

**Definition:** Properties completing the defined acquisition or retreat milestone per year.

**How derived:** Count unique acquired property IDs by verified closing date and divide by interval years. Reconcile administrative and deed records and separate later relocation or restoration dates.

**Model contribution:** Removes hazard exposure, drains the pipeline, triggers acquisition spending and creates retreat land.

**Simulation relationship:** Candidate rate: MIN(pipeline/processing_time, spendable_funds/(cost_per_property * funding_release_time), support_FTE * throughput). Include full cost obligations, positive time constants and joint pipeline/stock depletion limits.

**Guide equation:** Guide paragraph 121: MIN(Properties_in_Pipeline / Processing_Time,
Retreat_Funding_Available / (Average_Property_Value * Compensation_Rate),
Support_Services_Capacity * Caseworker_Throughput)

**Inputs named in guide:** Average_Property_Value [guide equation reference]; Caseworker_Throughput [guide equation reference]; Compensation_Rate [guide equation reference]; Processing_Time [guide equation reference]; Properties_in_Pipeline [guide equation reference]; Retreat_Funding_Available [guide equation reference]; Support_Services_Capacity [guide equation reference]

**Consumers named in guide:** Managed_Retreat_Relocations [guide equation reference]; Buyout_Payments [guide equation reference]; Successful_Relocations [guide equation reference]; Land_Acquired_Through_Retreat [guide equation reference]; Properties_at_Risk [guide equation reference]; Properties_at_Risk [stock outflow]; Properties_in_Retreat_Pipeline [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** series=acquired_properties; time; value; program_id; designation; quality_flag

**Existing evidence:** data/Calibration_Data.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S24: OpenFEMA HMA project-site inventories; S55: Harris County Clerk real-property records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Acquisition, demolition, move and ecological restoration are different events; budget constraint requires a time interval. See the simulation relationship for the required equation review.

### Successful_Relocations

**Role and units:** Flow. households/year.

**Definition:** Households newly satisfying the chosen successful relocation outcome per year.

**How derived:** Count households reaching a prespecified follow-up outcome by cohort and date. If estimated from acquisitions, convert properties to households and represent the follow-up delay.

**Model contribution:** Fills Relocated_Households.

**Simulation relationship:** Convert acquisitions to actual household move cohorts, then apply a measured follow-up success share with an explicit delay. A property-to-household conversion and cohort linkage are required.

**Guide equation:** Guide paragraph 122: Properties_Retreated * Relocation_Success_Rate

**Inputs named in guide:** Properties_Retreated [guide equation reference]; Relocation_Success_Rate [guide equation reference]

**Consumers named in guide:** Relocated_Households [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S33: Rice Greater Houston Community Panel (GHCP)

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Current administrative relocation totals do not measure durable success; pending follow-up is censored, not failure. See the simulation relationship for the required equation review.

### Retreat_Willingness

**Role and units:** Auxiliary or delayed quantity. probability.

**Definition:** Probability or bounded propensity of an eligible household to participate under a specified offer.

**How derived:** Estimate participation or stated willingness using eligible nonapplicants, refusals and acceptances, with offer and context covariates. Validate the scale and bound probabilities.

**Model contribution:** Determines potential applications through hazard perception, compensation, attachment, trust and legal barriers.

**Simulation relationship:** Bound a validated participation response to 0 to 1. Normalize trust and legal penalties to compatible scales; multiplication of guide factors is an assumed behavioral form.

**Guide equation:** Guide paragraph 127: Hazard_Perception * Compensation_Attractiveness * (1 - Place_Attachment_Index) * Trust_Factor - Legal_Obstacles

**Inputs named in guide:** Compensation_Attractiveness [guide equation reference]; Hazard_Perception [guide equation reference]; Legal_Obstacles [guide equation reference]; Place_Attachment_Index [guide equation reference]; Trust_Factor [guide equation reference]

**Consumers named in guide:** Retreat_Applications [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S33: Rice Greater Houston Community Panel (GHCP); S62: Addressing coordination problems in residential buyouts: experimental evidence

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Participation among completers is not willingness; the guide expression can be negative and requires bounded calibration. See the simulation relationship for the required equation review.

### Processing_Time

**Role and units:** Auxiliary or delayed quantity. years.

**Definition:** Expected elapsed time to process a property case through the chosen stage.

**How derived:** Estimate complete-application-to-close and intermediate-stage duration distributions, including pending cases. Fit baseline, legal complexity and administrative efficiency effects.

**Model contribution:** Converts the pipeline stock into its processing-limited completion rate.

**Simulation relationship:** Require positive Base_Processing_Time, Legal_Complexity_Factor and Administrative_Efficiency. Preserve the duration distribution when a single mean would hide long pending cases.

**Guide equation:** Guide paragraph 128: Base_Processing_Time * Legal_Complexity_Factor / Administrative_Efficiency

**Inputs named in guide:** Administrative_Efficiency [guide equation reference]; Base_Processing_Time [guide equation reference]; Legal_Complexity_Factor [guide equation reference]

**Consumers named in guide:** Properties_Retreated [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S55: Harris County Clerk real-property records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Completed-case averages are biased when slow cases remain open; report voluntary/involuntary cohorts separately. See the simulation relationship for the required equation review.

### Program_Awareness

**Role and units:** Auxiliary or delayed quantity. eligible-population proportion.

**Definition:** Share of eligible residents aware of the retreat program.

**How derived:** Divide survey-weighted eligible respondents aware of the program by all eligible respondents, separating aided and unaided awareness. Fit the launch-time curve if needed.

**Model contribution:** Modifies Retreat_Applications.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 129: Communication_Effectiveness * Time_Since_Program_Launch / (Time_Since_Program_Launch + Awareness_Half_Time)

**Inputs named in guide:** Awareness_Half_Time [guide equation reference]; Communication_Effectiveness [guide equation reference]; Time_Since_Program_Launch [guide equation reference]

**Consumers named in guide:** Retreat_Applications [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S33: Rice Greater Houston Community Panel (GHCP)

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Page views, mailed notices and applications do not directly measure population awareness.

### Awareness_Half_Time

**Role and units:** Parameter. years.

**Definition:** Time after launch at which awareness reaches half of its modeled saturation level.

**How derived:** Fit repeated eligible-population awareness to the guide's t/(t+h) response, estimating the saturation level and positive h together.

**Model contribution:** Determines the speed at which Program_Awareness increases.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Program_Awareness [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S33: Rice Greater Houston Community Panel (GHCP)

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** A launch date and website traffic alone do not identify this time constant.

### Base_Processing_Time

**Role and units:** Parameter. years.

**Definition:** Typical complete-application-to-close duration before complexity adjustments.

**How derived:** Match case-stage timestamps, choose a baseline case mix and estimate duration with pending-case censoring. Convert days to years using one convention.

**Model contribution:** Sets the base time in Processing_Time.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Processing_Time [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S55: Harris County Clerk real-property records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Include unfinished cases; separate legal, funding and administrative delays before applying multipliers.

### Caseworker_Throughput

**Role and units:** Parameter. properties/FTE/year.

**Definition:** Number of property cases processed per caseworker FTE-year.

**How derived:** Divide completed comparable cases by the integral of actual allocated FTE over the same period. Define the stage counted and case-mix adjustment.

**Model contribution:** Sets the staffing limit on Properties_Retreated.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_Retreated [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Avoid using total county staff or mixing new applications with completed cases.

### Relocation_Success_Rate

**Role and units:** Parameter. proportion.

**Definition:** Share of the specified relocation cohort meeting defined success criteria at follow-up.

**How derived:** Divide qualifying households by the full eligible follow-up cohort at 6, 12 or 24 months, with attrition and incomplete follow-up reported. Define safety, stability and affordability in advance.

**Model contribution:** Converts relocation cohorts to Successful_Relocations; a move-completion rate is a different quantity.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Receiving_Area_Housing_Availability [named conceptual determinant]; Relocation_Support_Services [named conceptual determinant]; Community_Cohesion_Preservation [named conceptual determinant]

**Consumers named in guide:** Managed_Retreat_Relocations [guide equation reference]; Successful_Relocations [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S33: Rice Greater Houston Community Panel (GHCP)

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Administrative completion does not establish safe, affordable and stable relocation.

### Administrative_Efficiency

**Role and units:** Proposed auxiliary or input. case-mix-adjusted ratio.

**Definition:** Relative ability to process comparable cases with available administrative resources.

**How derived:** Compare stage duration, rework and completions per allocated FTE across comparable case mixes. Normalize relative to a documented baseline.

**Model contribution:** Reduces Processing_Time when efficiency increases.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Processing_Time [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Avoid defining efficiency from the same duration it is then used to predict without independent information.

### Application_Ease_Factor

**Role and units:** Proposed auxiliary or input. bounded modifier.

**Definition:** Modifier representing how application burden affects eligible participation.

**How derived:** Measure documentation burden, incomplete submissions, resubmissions and accessibility, then estimate their association with completed application attempts.

**Model contribution:** Modifies Retreat_Applications alongside awareness and willingness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Applications [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Estimate its effect on application completion; do not assume process ratings are causal coefficients.

### Capacity_Attrition

**Role and units:** Flow referenced by a stock. FTE/year.

**Definition:** Reduction in assigned caseworker capacity per year.

**How derived:** Sum lost retreat-assigned working hours from departures or reduced assignments, convert to FTE and divide by interval years.

**Model contribution:** Drains Support_Services_Capacity.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Support_Services_Capacity [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Contract expirations, vacancies and transfers need separate coding; headcount differs from FTE.

### Capacity_Building

**Role and units:** Flow referenced by a stock. FTE/year.

**Definition:** Addition to assigned caseworker capacity per year.

**How derived:** Sum newly assigned productive staff or contractor hours, convert using full-time annual hours and annualize changes. Distinguish hiring from training gains.

**Model contribution:** Fills Support_Services_Capacity.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Support_Services_Capacity [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Training expenditure is not an observed increase in effective throughput.

### Communication_Effectiveness

**Role and units:** Proposed auxiliary or input. understanding/reach proportion.

**Definition:** Proportion of eligible residents reached with understandable program information at saturation.

**How derived:** Measure receipt, comprehension and accessibility in an eligible-population survey, supported by outreach logs.

**Model contribution:** Sets the saturation level of Program_Awareness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Program_Awareness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Sent notices and social-media impressions do not establish understanding.

### Compensation_Attractiveness

**Role and units:** Auxiliary or delayed quantity. acceptance probability modifier.

**Definition:** Modeled appeal of an offer given the specified compensation and household need.

**How derived:** Estimate acceptance or stated preference over offer-to-value or adequacy ratios using both acceptances and refusals. Fit a bounded response curve.

**Model contribution:** Modifies Retreat_Willingness.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 529: Compensation_Attractiveness_Lookup(Compensation_Rate)

**Inputs named in guide:** Compensation_Attractiveness_Lookup [guide equation reference]; Compensation_Rate [guide equation reference]

**Consumers named in guide:** Retreat_Willingness [guide equation reference]

**Evidence:** Illustrative guide lookup; not fitted

**Fields or records:** lookup_name=Compensation_Attractiveness_Lookup; input_value; output_value

**Existing evidence:** data/Lookup_Tables.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S62: Addressing coordination problems in residential buyouts: experimental evidence

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Guide lookup points are assumptions; adjust for selection, timing and receiving-housing constraints.

### Hazard_Perception

**Role and units:** Proposed auxiliary or input. subjective probability/scale.

**Definition:** Perceived likelihood or seriousness of future hazard exposure among eligible residents.

**How derived:** Use repeated hazard-specific questions, document scale and direction, and relate responses to experience and objective exposure.

**Model contribution:** Modifies Retreat_Willingness. Reconcile with Perceived_Hazard_Risk before using both.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Willingness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S09: HCFCD flood reports and Harris County Flood Warning System

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Flood experience alone is not perceived probability; do not substitute crime-safety questions.

### Initial_Capacity

**Role and units:** Initial value. caseworker FTE.

**Definition:** Baseline initializer of Support_Services_Capacity retained under the guide's original name.

**How derived:** Derive Support_Services_Capacity for the chosen opening date, then hold that starting value fixed as the stock initializer. Divide assigned productive hours by standard full-time hours for the period; include filled staff and equivalent contracted effort.

**Model contribution:** Initializes Support_Services_Capacity; it is not a second independently changing stock.

**Simulation relationship:** Initializes Support_Services_Capacity; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Support_Services_Capacity [stock initializer]

**Evidence:** Derived from/reconciled to Support_Services_Capacity

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Legal_Complexity_Factor

**Role and units:** Proposed auxiliary or input. duration ratio.

**Definition:** Processing-duration multiplier associated with legal case complexity.

**How derived:** Estimate duration ratios for comparable title, lien, probate, tenant and appeal conditions, controlling case stage and administrative capacity.

**Model contribution:** Increases Processing_Time for more complex cases.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Processing_Time [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S55: Harris County Clerk real-property records; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Use case-mix adjustment and censoring; do not apply an arbitrary multiplier to all cases.

### Legal_Obstacles

**Role and units:** Proposed auxiliary or input. case proportion/severity.

**Definition:** Participation barriers associated with unresolved legal or eligibility issues.

**How derived:** Code obstacle types and whether each blocks participation or only delays processing. Estimate a bounded participation penalty separately from Legal_Complexity_Factor.

**Model contribution:** Reduces Retreat_Willingness in the guide's formulation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Willingness [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S55: Harris County Clerk real-property records; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** A count of lawsuits is an incomplete measure and cannot be subtracted from a probability without scaling.

### Proactive_Retreat_Identification

**Role and units:** Flow referenced by a stock. properties/year.

**Definition:** New properties admitted to the retreat pipeline through proactive screening per year.

**How derived:** Count distinct screened properties meeting the declared entry threshold and date. Exclude those already in the pipeline or counted as applications.

**Model contribution:** Adds properties to Properties_in_Retreat_Pipeline.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_in_Retreat_Pipeline [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S20: HCFCD voluntary home buyout program; S22: HCFCD public-information access route; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S61: Mach et al., Managed retreat through voluntary buyouts of flood-prone properties

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Home-Buyout-Program)

**Limitation:** Target-area centroids and expressions of interest are not individually identified eligible properties.

### Properties_in_Pipeline

**Role and units:** Alias. properties.

**Definition:** Same quantity of Properties_in_Retreat_Pipeline retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Properties_in_Retreat_Pipeline. At each date count distinct cases entered before that date minus completed, withdrawn and otherwise exited cases. Reconcile all status transitions and repeat applications.

**Model contribution:** Connects guide references to Properties_in_Retreat_Pipeline without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Properties_in_Retreat_Pipeline without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_Retreated [guide equation reference]

**Evidence:** Derived from/reconciled to Properties_in_Retreat_Pipeline

**Fields or records:** series=pending_acquisition_status_sum; time; value; program_id; designation; quality_flag

**Existing evidence:** data/Calibration_Data.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Retreat_Dropouts

**Role and units:** Flow referenced by a stock. properties/year.

**Definition:** Property cases leaving the pipeline without completion per year.

**How derived:** Count exits by stable property ID, stage, date and reason. Distinguish withdrawals, denials and refusals, and track re-entry without duplicate active cases.

**Model contribution:** Drains Properties_in_Retreat_Pipeline and prevents every applicant from being assumed to complete.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Properties_in_Retreat_Pipeline [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Do not omit rejected or withdrawn cases when estimating willingness or duration.

### Retreat_Program_Eligibility

**Role and units:** Proposed auxiliary or input. eligible share or indicator.

**Definition:** Eligibility indicator or eligible share for the specific funding opportunity and target universe.

**How derived:** Apply dated geographic, hazard, ownership, income and program rules to each target record. Divide eligible units by the same target universe if using a share.

**Model contribution:** Modifies Federal_Funding in the guide and defines who may participate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Federal_Funding [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route; S24: OpenFEMA HMA project-site inventories

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Eligibility differs across HCD, HCFCD and funding sources; population vulnerability alone does not determine it.

### Time_Since_Program_Launch

**Role and units:** Proposed auxiliary or input. years.

**Definition:** Years elapsed since the defined operational or outreach launch.

**How derived:** Calculate max(0, current_date-launch_date) in years, using the launch event relevant to awareness.

**Model contribution:** Supplies elapsed time to Program_Awareness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Program_Awareness [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Policy approval, grant award, application opening and first closing are different launch candidates.

### Trust_Factor

**Role and units:** Derived mapping requiring reconciliation. dimensionless proportion, 0 to 1.

**Definition:** Normalized process trust used as a participation modifier.

**How derived:** If a validated 0 to 100 Community_Trust_in_Process scale is retained, compute trust/100. Confirm the behavioral interpretation before treating the normalized score as a probability modifier.

**Model contribution:** Connects Community_Trust_in_Process to Retreat_Willingness.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Willingness [guide equation reference]

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S39: OECD Guidelines on Measuring Trust; S21: HCD public-records access route

[Primary source or access page](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-trust_9789264278219-en.html)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### caseworkers_equivalent

**Role and units:** Unit label. FTE.

**Definition:** Unit label expressing support staffing in full-time equivalents.

**How derived:** Convert assigned hours divided by the organization's full-time-hours standard; store the numeric result under Support_Services_Capacity.

**Model contribution:** Defines staffing units and prevents treating the unit token as an independent variable.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Defines staffing units and prevents treating the unit token as an independent variable.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Remove from the empirical-variable count while retaining this audit entry.

### Community_Retreat_Demand

**Role and units:** Proposed auxiliary or input. households/properties by community.

**Definition:** Number of households or properties seeking retreat within one defined community.

**How derived:** Count unique expressions of interest, eligible applications and verified need separately. Choose one matching unit and period for regional aggregation.

**Model contribution:** Supplies community-level values for Regional_Retreat_Pressure.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Regional_Retreat_Pressure [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S20: HCFCD voluntary home buyout program

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Observed applications are constrained by awareness and eligibility and do not equal latent demand.

### Compensation_Attractiveness_Lookup

**Role and units:** Lookup table. input-output table.

**Definition:** Table mapping a defined compensation ratio to an attractiveness score.

**How derived:** Store ordered ratio-score pairs and fit from observed decisions or stated-choice evidence. Existing guide points are assumed; retain interpolation and endpoint rules.

**Model contribution:** Supplies Compensation_Attractiveness.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 530: Compensation_Attractiveness_Lookup(
[(0.5,0)-(2,1)],
(0.8,0.1),(0.9,0.3),(1.0,0.5),(1.1,0.65),(1.2,0.8),(1.5,0.95))

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Compensation_Attractiveness [guide equation reference]

**Evidence:** Illustrative guide lookup; not fitted

**Fields or records:** lookup_name; input_value; output_value; interpolation; below_range; above_range; evidence_status

**Existing evidence:** data/Lookup_Tables.csv

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S62: Addressing coordination problems in residential buyouts: experimental evidence

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Guide control points remain assumptions until fitted; cannot infer the curve using only completed buyouts.

### Receiving_Area_Housing_Availability

**Role and units:** Proposed auxiliary or input. suitable units or choice ratio.

**Definition:** Supply of suitable, affordable and accessible destination housing for relocating households.

**How derived:** Match available units to household size, affordability, accessibility, location and hazard constraints. Report suitable units or units per seeking household.

**Model contribution:** Constrains the feasibility of successful relocation; the guide names the relationship without a full equation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Relocation_Success_Rate [named conceptual determinant]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S17: HUD Comprehensive Housing Affordability Strategy data; S18: HUD aggregated USPS vacancy data; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S21: HCD public-records access route

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Vacancy, affordability and current availability differ; USPS access is restricted and CHAS is not an active listing inventory.

### Regional_Retreat_Pressure

**Role and units:** Auxiliary or delayed quantity. households/properties.

**Definition:** Aggregate retreat demand across nonoverlapping communities.

**How derived:** Sum Community_Retreat_Demand after reconciling household or property IDs and geographic overlaps. Use a separate denominator if expressing pressure relative to capacity.

**Model contribution:** Supports regional coordination and receiving-area planning in the optional spatial extension.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 348: SUM(Community_Retreat_Demand[Community])

**Inputs named in guide:** Community [guide equation reference]; Community_Retreat_Demand [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S15: Houston-Galveston Area Council forecasts and land cover; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Nested community totals and multiple applications can otherwise duplicate households/properties.

### Relocation_Support_Services

**Role and units:** Proposed auxiliary or input. service units/coverage.

**Definition:** Support actually delivered to households during relocation.

**How derived:** Count dated housing-search, case-management, moving, transport and other service units by household. Calculate coverage or dose with an eligible denominator.

**Model contribution:** Supplies a conceptual determinant of Relocation_Success_Rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Relocation_Success_Rate [named conceptual determinant]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S43: SAMHSA National Substance Use and Mental Health Services Survey

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Offered, referred, received and adequate support are separate measures.

### Retreat_Program_Active

**Role and units:** Auxiliary or delayed quantity. 0 or 1 by program, place and time.

**Definition:** Whether the program is operational for the relevant place and time.

**How derived:** Build a dated operational indicator from launch and closure records. For scenarios evaluate the chosen disaster, policy or petition trigger.

**Model contribution:** Provides the program activation switch; connect it explicitly to applications and proactive entries.

**Simulation relationship:** Connect the activation result to entry flows explicitly. Translate category labels to the actual Vensim configuration and define trigger duration and reopening rules.

**Guide equation:** Guide paragraph 184: IF THEN ELSE(
Trigger_Type = "Reactive_Disaster",
IF THEN ELSE(Recent_Major_Disaster > 0, 1, 0),
IF THEN ELSE(Trigger_Type = "Proactive_Policy",
IF THEN ELSE(Policy_Stimulus_Present = 1 AND Funding_Available > Threshold, 1, 0),
IF THEN ELSE(Trigger_Type = "Community_Request",
IF THEN ELSE(Community_Petition_Threshold_Met = 1, 1, 0),
0)))

**Inputs named in guide:** Community_Petition_Threshold_Met [guide equation reference]; Funding_Available [guide equation reference]; Policy_Stimulus_Present [guide equation reference]; Recent_Major_Disaster [guide equation reference]; Threshold [guide equation reference]; Trigger_Type [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Stable property, case and household IDs, eligibility, entry and exit dates, stage/status, disposition, household move and follow-up dates, allocated staff hours and service records.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S21: HCD public-records access route; S28: Harris County Commissioners Court agendas, minutes and votes

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** A formal policy or available grant does not establish active applications and delivery. See the simulation relationship for the required equation review.

## Equity

### Equity_Index

**Role and units:** Stock. equity points on a defined 0 to 100 scale.

**Definition:** Defined summary of disparities in program access, process, assistance and outcomes.

**How derived:** Specify indicators, group comparisons, direction, normalization and weights before constructing a 0 to 100 score. Publish its components and validate interpretation with affected groups.

**Model contribution:** Tracks equity over time and supplies an optional constraint on policy choices.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Equity_Improvements - Equity_Degradation, 50). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Equity_Improvements - Equity_Degradation, 50)`

**Inputs named in guide:** Equity_Improvements [stock inflow]; Equity_Degradation [stock outflow]

**Consumers named in guide:** Equity_Improvements [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S17: HUD Comprehensive Housing Affordability Strategy data; S42: CDC/ATSDR Social Vulnerability Index; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** SVI is vulnerability, not achieved equity. Composite weights and normative targets require explicit choices.

### Vulnerable_Population_Wellbeing

**Role and units:** Stock. chosen wellbeing scale.

**Definition:** Mean wellbeing of the explicitly defined vulnerable population.

**How derived:** GHCP g2404_satlife is coded 1 to 7. Verify score direction, then a proposed 0-to-100 transform is 100*(x-1)/6. Calculate the weighted mean within the defined vulnerable group, retain missing responses and validate the choice of a single-item wellbeing proxy.

**Model contribution:** Tracks distributional outcomes as wellbeing improves or declines.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Wellbeing_Improvements - Wellbeing_Decline, Initial_Wellbeing). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Wellbeing_Improvements - Wellbeing_Decline, Initial_Wellbeing)`

**Inputs named in guide:** Wellbeing_Improvements [stock inflow]; Wellbeing_Decline [stock outflow]; Initial_Wellbeing [stock initializer]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Candidate field: g2404_satlife and g2404_rweight. Codebook only; microdata not acquired.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S40: WHO-5 Well-Being Index; S41: CDC PLACES; S44: Harris County Public Health reports and dashboards

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Life satisfaction, clinical distress and area-level health prevalence are different constructs.

### Community_Psychosocial_Stress

**Role and units:** Stock. distress score; guide 0 to 100 transformation unresolved.

**Definition:** Level of psychological distress in the defined affected population.

**How derived:** Sum the six g2404 K6 items scored 0 to 4 to obtain 0 to 24 for complete respondents; missing responses remain missing. Compute a g2404_rweight-weighted mean. If the guide needs 0 to 100, use 100*mean_K6/24 as an explicit rescaling.

**Model contribution:** Stores distress and responds to Stress_Accumulation and Stress_Relief.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Stress_Accumulation - Stress_Relief, 30). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Stress_Accumulation - Stress_Relief, 30)`

**Inputs named in guide:** Stress_Accumulation [stock inflow]; Stress_Relief [stock outflow]

**Consumers named in guide:** Stress_Relief [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Candidate fields: g2404_nervous; g2404_hopeless; g2404_restless; g2404_depressed; g2404_effort; g2404_worthless; g2404_rweight. Codebook only; microdata not acquired.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S41: CDC PLACES; S37: Rice Texas Flood Registry

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** K6 is 0–24; a 0–100 rescaling is an operational choice, not the guide's calibrated state variable.

### Equity_Improvements

**Role and units:** Flow; guide labels AUX. equity points/year.

**Definition:** Annual improvement in the selected equity score.

**How derived:** Measure narrowing of defined disparities after policy or support changes. Estimate gains in index points per year; the guide's coefficient is not an observed effect.

**Model contribution:** Fills Equity_Index even though the guide labels the variable AUX.

**Simulation relationship:** Treat as an inflow to Equity_Index despite the AUX label. Express the response coefficient in 1/year after normalizing policy coverage and support.

**Guide equation:** Guide paragraph 140: Equity_Policies_Implemented * Vulnerable_Population_Support * (100 - Equity_Index) * 0.1

**Inputs named in guide:** Equity_Index [guide equation reference]; Equity_Policies_Implemented [guide equation reference]; Vulnerable_Population_Support [guide equation reference]

**Consumers named in guide:** Equity_Index [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Listed as auxiliary in dictionary but used as a stock flow; revise role and validate the rate relationship. See the simulation relationship for the required equation review.

### Wellbeing_Decline

**Role and units:** Flow. wellbeing points/year.

**Definition:** Annual reduction in the selected wellbeing score.

**How derived:** Estimate repeated negative changes and attributable components from displacement, service-access loss and cultural loss. Convert every component to the same index-points-per-year scale.

**Model contribution:** Drains Vulnerable_Population_Wellbeing.

**Simulation relationship:** Convert displacement, service-access and cultural-loss components to the same wellbeing-points/year scale. Aggregate household impacts using the appropriate cohort denominator.

**Guide equation:** Guide paragraph 141: Displacement_Rate * Displacement_Impact + Service_Access_Loss + Cultural_Heritage_Loss

**Inputs named in guide:** Cultural_Heritage_Loss [guide equation reference]; Displacement_Impact [guide equation reference]; Displacement_Rate [guide equation reference]; Service_Access_Loss [guide equation reference]

**Consumers named in guide:** Vulnerable_Population_Wellbeing [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S37: Rice Texas Flood Registry; S40: WHO-5 Well-Being Index

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Do not sum incompatible household, index and site units; association is not necessarily a displacement effect. See the simulation relationship for the required equation review.

### Stress_Relief

**Role and units:** Flow. stress points/year.

**Definition:** Reduction in the selected distress score per year.

**How derived:** Link service dose and access to repeated distress measurements, accounting for baseline severity and time. Estimate a compatible per-year reduction relationship.

**Model contribution:** Drains Community_Psychosocial_Stress.

**Simulation relationship:** Use a defined service-coverage or dose measure and a calibrated per-year response. Do not multiply counselor FTE or appointment counts directly by an unexplained index coefficient.

**Guide equation:** Guide paragraph 142: Psychosocial_Support_Capacity * Support_Effectiveness * Community_Psychosocial_Stress * 0.15

**Inputs named in guide:** Community_Psychosocial_Stress [guide equation reference]; Psychosocial_Support_Capacity [guide equation reference]; Support_Effectiveness [guide equation reference]

**Consumers named in guide:** Community_Psychosocial_Stress [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S40: WHO-5 Well-Being Index; S21: HCD public-records access route; S43: SAMHSA National Substance Use and Mental Health Services Survey

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** The guide 0.15 coefficient is illustrative; counseling receipt is selected by need. See the simulation relationship for the required equation review.

### Equity_in_Compensation

**Role and units:** Auxiliary or delayed quantity. need-adjusted gap/ratio.

**Definition:** Comparison of assistance adequacy between owner and renter households.

**How derived:** Calculate group-specific assistance relative to eligible losses or rehousing need, then compare those adequacy ratios. Retain the guide's raw-dollar similarity only as a separately labeled descriptive measure.

**Model contribution:** Evaluates distribution of compensation without treating equal purchase and rental payments as equivalent outcomes.

**Simulation relationship:** The guide formula measures similarity of dollar amounts. For an equity outcome compare assistance-to-need ratios by group; handle a zero combined denominator explicitly.

**Guide equation:** Guide paragraph 144: 1 - ABS(Homeowner_Compensation_Avg - Renter_Compensation_Avg) / (Homeowner_Compensation_Avg + Renter_Compensation_Avg)

**Inputs named in guide:** Homeowner_Compensation_Avg [guide equation reference]; Renter_Compensation_Avg [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S19: Harris County HCD buyout guidelines and performance reports

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Equal dollar payments do not imply equity: asset purchase and tenant relocation aid compensate different things. See the simulation relationship for the required equation review.

### Vulnerable_Population_Share

**Role and units:** Auxiliary or delayed quantity. proportion.

**Definition:** Share of households meeting at least one stated vulnerability criterion.

**How derived:** In joint household data flag each condition, take the logical OR across conditions, and divide the weighted qualifying count by all eligible households. Do not sum overlapping marginals.

**Model contribution:** Quantifies the affected support-need population without double counting households.

**Simulation relationship:** Calculate the household-level union of vulnerability flags with consistent weights, or present separate marginal indicators. Adding marginals can exceed one.

**Guide equation:** Guide paragraph 145: (Low_Income_Households + Elderly_Households + Disabled_Households + Racialized_Households) / Total_Households

**Inputs named in guide:** Disabled_Households [guide equation reference]; Elderly_Households [guide equation reference]; Low_Income_Households [guide equation reference]; Racialized_Households [guide equation reference]; Total_Households [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S03: Census ACS Public Use Microdata Sample; S01: Census American Community Survey, detailed tables; S17: HUD Comprehensive Housing Affordability Strategy data

[Primary source or access page](https://www.census.gov/programs-surveys/acs/microdata.html)

**Limitation:** Adding low-income, older, disabled and racialized household counts double counts overlapping households. See the simulation relationship for the required equation review.

### Historical_Inequity_Factor

**Role and units:** Auxiliary or delayed quantity. documented indicators.

**Definition:** Representation of documented historical disadvantage relevant to retreat decisions.

**How derived:** Build context-specific indicators of exposure, investment, access and treatment. Do not assign a multiplier solely because a race or Indigenous category is present.

**Model contribution:** Adds historical context to equity assessment; the guide does not specify a downstream equation.

**Simulation relationship:** Replace identity-conditioned multipliers with explicit context-specific evidence or transparent policy scenarios. Retain group labels for disparity comparisons.

**Guide equation:** Guide paragraph 146: IF THEN ELSE(Racialized_Community = 1 OR First_Nations_Community = 1, 1.5 + Historical_Discrimination_Index, 1.0)

**Inputs named in guide:** First_Nations_Community [guide equation reference]; Historical_Discrimination_Index [guide equation reference]; Racialized_Community [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S28: Harris County Commissioners Court agendas, minutes and votes; S45: Texas Historical Commission Historic Sites Atlas; S46: HUD Tribal Directory Assessment Tool; S60: University of Richmond Mapping Inequality, Houston

[Primary source or access page](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)

**Limitation:** Do not assign a fixed penalty or multiplier solely from racial/Indigenous identity. See the simulation relationship for the required equation review.

### Cultural_Heritage_Impact

**Role and units:** Auxiliary or delayed quantity. co-designed impact indicators.

**Definition:** Effect of retreat on valued cultural places, access and practices.

**How derived:** Overlay verified heritage resources with retreat footprints, document actual effects and combine with community-defined significance and protection outcomes. Normalize site counts if a 0 to 1 score is required.

**Model contribution:** Reports cultural consequences that physical damage and financial costs omit.

**Simulation relationship:** If output must lie between zero and one, normalize the affected-site measure and all component scores. Preserve cultural outcomes that are not meaningfully represented by one scalar.

**Guide equation:** Guide paragraph 147: Heritage_Sites_Affected * Cultural_Significance * (1 - Heritage_Protection_Measures)

**Inputs named in guide:** Cultural_Significance [guide equation reference]; Heritage_Protection_Measures [guide equation reference]; Heritage_Sites_Affected [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S45: Texas Historical Commission Historic Sites Atlas; S46: HUD Tribal Directory Assessment Tool; S47: HCFCD Watershed Environmental Baseline (WEB); S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://atlas.thc.texas.gov/Data/DataDownload)

**Limitation:** Site counts cannot measure living heritage or place meaning; keep sensitive location data controlled. See the simulation relationship for the required equation review.

### Displacement_Impact

**Role and units:** Parameter. wellbeing change per exposure.

**Definition:** Change in the chosen wellbeing scale associated with displacement exposure.

**How derived:** Estimate within-person wellbeing change against an appropriate comparison, with cohort, follow-up and exposure definitions. Convert household-level effects to the aggregate index using population weights.

**Model contribution:** Translates Displacement_Rate into one component of Wellbeing_Decline.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Wellbeing_Decline [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S40: WHO-5 Well-Being Index

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Guide wellbeing-points/household coefficient depends on whether the stock is total points or mean wellbeing.

### Psychosocial_Support_Capacity

**Role and units:** Parameter. available visits/year or FTE.

**Definition:** Capacity to provide appropriate psychosocial support to the affected cohort.

**How derived:** Measure available counselor FTE, appointment slots or service hours and their eligibility coverage. Normalize capacity before using the guide's dimensionless stress-relief formulation.

**Model contribution:** Limits the potential for Stress_Relief.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Stress_Relief [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S43: SAMHSA National Substance Use and Mental Health Services Survey

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Guide index-point units need replacement or a defined conversion from service capacity to stress change.

### Support_Effectiveness

**Role and units:** Parameter. effect per service dose.

**Definition:** Effect of a defined support service dose on the selected outcome.

**How derived:** Estimate longitudinal outcome change relative to a defensible comparison, specifying service type, dose and follow-up. Rescale only with a documented unit conversion.

**Model contribution:** Determines how much available support reduces modeled distress.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Stress_Relief [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S40: WHO-5 Well-Being Index; S21: HCD public-records access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Do not interpret cross-sectional service-user differences as treatment effects.

### Ancestral_Land_Significance

**Role and units:** Proposed auxiliary or input. community-defined scale.

**Definition:** Community-defined significance of ancestral land and associated practices.

**How derived:** Develop consented indicators or qualitative evidence with the relevant community. Preserve distinct meanings instead of assigning significance from demographic identity.

**Model contribution:** Supplies the guide's optional cultural attachment and policy-adjustment relationships after local review.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Place_Attachment_Index [guide equation reference]; First_Nations_Adjustment_Factor [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S45: Texas Historical Commission Historic Sites Atlas; S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Public ancestry counts or heritage markers do not measure ancestral significance.

### Cultural_Heritage_Loss

**Role and units:** Proposed auxiliary or input. documented loss indicators.

**Definition:** Loss of valued places, access, practices or ties associated with displacement.

**How derived:** Compare baseline and follow-up community-reported access and practices, with site and process evidence. Estimate a wellbeing response separately if this enters an index-point flow.

**Model contribution:** Contributes to Wellbeing_Decline after conversion to compatible units.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Wellbeing_Decline [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S45: Texas Historical Commission Historic Sites Atlas; S46: HUD Tribal Directory Assessment Tool; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://atlas.thc.texas.gov/Data/DataDownload)

**Limitation:** A demolished-building count does not capture cultural loss; distinguish material and living heritage.

### Cultural_Significance

**Role and units:** Proposed auxiliary or input. co-designed significance scale.

**Definition:** Importance assigned to a cultural resource by the relevant community.

**How derived:** Use community-defined assessment and historical evidence to score or describe each resource. Retain criteria and disagreement rather than assigning an unexplained universal value.

**Model contribution:** Weights resources in Cultural_Heritage_Impact.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cultural_Heritage_Impact [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S45: Texas Historical Commission Historic Sites Atlas; S46: HUD Tribal Directory Assessment Tool; S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://atlas.thc.texas.gov/Data/DataDownload)

**Limitation:** Registry designation and market price are incomplete proxies for significance.

### Disabled_Households

**Role and units:** Proposed auxiliary or input. households.

**Definition:** Households containing at least one person with a disability under the chosen definition.

**How derived:** Sum ACS B22010_003E and B22010_006E for the matching household universe. Use household microdata to identify overlaps with age and income conditions.

**Model contribution:** Supplies one vulnerability component and identifies accessibility needs.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Share [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Candidate ACS fields B22010_003E + B22010_006E; household microdata needed for overlaps.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** B18101 counts people, not households; disability type and accessibility needs remain heterogeneous.

### Displacement_Rate

**Role and units:** Proposed auxiliary or input. households/year.

**Definition:** Households experiencing defined displacement per year.

**How derived:** Count unique displaced households by cause and start date, distinguishing temporary evacuation, permanent involuntary moves and supported retreat. Divide by elapsed years.

**Model contribution:** Supplies displacement exposure to Wellbeing_Decline.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Wellbeing_Decline [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S37: Rice Texas Flood Registry

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** The wellbeing equation must use the same person/household exposure basis as its effect parameter.

### Elderly_Households

**Role and units:** Proposed auxiliary or input. households.

**Definition:** Households with at least one person aged 65 or older under the selected definition.

**How derived:** Use ACS B11007_002E, or consistently apply another stated age rule. Preserve overlap with disability and income groups.

**Model contribution:** Supplies a vulnerability component and informs age-related support needs.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Share [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Candidate ACS field B11007_002E; retain corresponding MOE.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Older-person counts are not older-household counts; do not add to other vulnerability groups without overlap handling.

### Equity_Degradation

**Role and units:** Flow referenced by a stock. equity points/year.

**Definition:** Annual worsening of the selected equity score.

**How derived:** Measure deteriorating access, adequacy, waiting-time or outcome gaps over time and transform them using the same weights and direction as Equity_Index.

**Model contribution:** Drains Equity_Index.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Equity_Index [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Must use the same indicators/scaling as Equity_Index and avoid duplicate subtraction of wellbeing loss.

### Equity_Policies_Implemented

**Role and units:** Proposed auxiliary or input. coded milestones/coverage.

**Definition:** Coverage or implementation status of defined equity measures.

**How derived:** Code adoption dates and actual application of tenant, accessibility, eligibility and need-based support measures. Separate formal adoption from delivered coverage.

**Model contribution:** Modifies Equity_Improvements.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Equity_Improvements [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S28: Harris County Commissioners Court agendas, minutes and votes; S21: HCD public-records access route

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Policy text presence does not prove implementation or its effect size.

### First_Nations_Community

**Role and units:** Policy or scenario input. locally defined group flag.

**Definition:** Scope flag identifying a relevant Indigenous community under an explicit local definition.

**How derived:** Establish applicable community and geographic scope through appropriate engagement and documented criteria. Do not infer a behavioral coefficient from race or ancestry data.

**Model contribution:** Selects optional guide branches that require localization before a Harris County model uses them.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Place_Attachment_Index [guide equation reference]; Historical_Inequity_Factor [guide equation reference]; First_Nations_Adjustment_Factor [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Do not use ACS race counts as a substitute for tribal nation status or governance; localize terminology.

### Heritage_Protection_Measures

**Role and units:** Proposed auxiliary or input. documented coverage/score.

**Definition:** Extent of implemented measures protecting valued heritage resources and access.

**How derived:** Verify preservation, access agreements, documentation or agreed commemoration by resource and date. Convert to a documented coverage fraction or score.

**Model contribution:** Reduces modeled Cultural_Heritage_Impact.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cultural_Heritage_Impact [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S45: Texas Historical Commission Historic Sites Atlas; S46: HUD Tribal Directory Assessment Tool; S21: HCD public-records access route; S22: HCFCD public-information access route

[Primary source or access page](https://atlas.thc.texas.gov/Data/DataDownload)

**Limitation:** A planned measure is not an implemented or effective protection.

### Heritage_Sites_Affected

**Role and units:** Proposed auxiliary or input. sites or affected share.

**Definition:** Number or share of verified heritage sites affected by the retreat footprint.

**How derived:** Overlay heritage inventories and actual acquisition or demolition polygons, then verify site-level effects. Use affected share rather than count if the output is bounded to one.

**Model contribution:** Supplies the extent component of Cultural_Heritage_Impact.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Cultural_Heritage_Impact [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S45: Texas Historical Commission Historic Sites Atlas; S47: HCFCD Watershed Environmental Baseline (WEB); S05: Harris Central Appraisal District account and parcel downloads; S22: HCFCD public-information access route

[Primary source or access page](https://atlas.thc.texas.gov/Data/DataDownload)

**Limitation:** Sensitive archaeological sites require appropriate access; absence from public inventories does not imply no heritage.

### Historical_Discrimination_Index

**Role and units:** Proposed auxiliary or input. transparent evidence rubric.

**Definition:** Explicitly defined evidence of historical unequal treatment affecting the modeled place.

**How derived:** Code documented policies, unequal access and place-specific histories with a transparent rubric and dates. Keep indicators visible and distinguish place context from individual experience.

**Model contribution:** Informs the optional Historical_Inequity_Factor after its interpretation is revised.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Historical_Inequity_Factor [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S28: Harris County Commissioners Court agendas, minutes and votes; S42: CDC/ATSDR Social Vulnerability Index; S46: HUD Tribal Directory Assessment Tool; S60: University of Richmond Mapping Inequality, Houston

[Primary source or access page](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)

**Limitation:** Current SVI or race composition does not directly measure historical discrimination.

### Initial_Wellbeing

**Role and units:** Initial value. chosen wellbeing scale.

**Definition:** Baseline initializer of Vulnerable_Population_Wellbeing retained under the guide's original name.

**How derived:** Derive Vulnerable_Population_Wellbeing for the chosen opening date, then hold that starting value fixed as the stock initializer. GHCP g2404_satlife is coded 1 to 7. Verify score direction, then a proposed 0-to-100 transform is 100*(x-1)/6. Calculate the weighted mean within the defined vulnerable group, retain missing responses and validate the choice of a single-item wellbeing proxy.

**Model contribution:** Initializes Vulnerable_Population_Wellbeing; it is not a second independently changing stock.

**Simulation relationship:** Initializes Vulnerable_Population_Wellbeing; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Wellbeing [stock initializer]

**Evidence:** Derived from/reconciled to Vulnerable_Population_Wellbeing

**Fields or records:** Candidate field: g2404_satlife and g2404_rweight. Codebook only; microdata not acquired.

**Existing evidence:** reports/2026-09-10_Variable_Source_Assessment/research/GHCP_2023_2024_User_Guide.pdf

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S40: WHO-5 Well-Being Index

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Low_Income_Households

**Role and units:** Proposed auxiliary or input. households.

**Definition:** Households below a declared income threshold adjusted for the analysis purpose.

**How derived:** Use HUD CHAS income categories or weighted household microdata with a stated household-size adjustment. Do not substitute people below poverty for households below the threshold.

**Model contribution:** Supplies a vulnerability component and support-eligibility context.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Share [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S17: HUD Comprehensive Housing Affordability Strategy data; S03: Census ACS Public Use Microdata Sample; S01: Census American Community Survey, detailed tables

[Primary source or access page](https://www.huduser.gov/portal/datasets/cp.html)

**Limitation:** B17001 poverty counts people; a fixed B19001 income cutoff differs from HUD income eligibility.

### Perceived_Inequity

**Role and units:** Proposed auxiliary or input. survey scale.

**Definition:** Residents' perception that access, process, compensation or outcomes are unfair.

**How derived:** Ask dimension-specific fairness questions, document scale direction, and aggregate with relevant survey weights.

**Model contribution:** Contributes to Trust_Erosion and the Community_Opposition lookup.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trust_Erosion [guide equation reference]; Community_Opposition [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S21: HCD public-records access route; S39: OECD Guidelines on Measuring Trust

[Primary source or access page](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)

**Limitation:** Administrative disparity and perceived unfairness are related but different constructs.

### Racialized_Community

**Role and units:** Policy or scenario input. explicit grouping definition.

**Definition:** Explicit grouping used to assess racial or ethnic disparities in the modeled context.

**How derived:** Define the analytic grouping and geographic unit transparently using appropriate categories and local context. Use it for comparisons, not an automatic behavioral multiplier.

**Model contribution:** Identifies groups for disparity assessment and flags guide equations that require revision.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Historical_Inequity_Factor [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Do not automatically assign behavioral or inequity coefficients from a binary group flag.

### Racialized_Households

**Role and units:** Proposed auxiliary or input. households.

**Definition:** Households assigned to a stated race or ethnicity grouping rule.

**How derived:** Use household-weighted microdata and specify whether grouping follows the householder or another rule. Reconcile mutually exclusive ethnicity categories and overlap with other vulnerability conditions.

**Model contribution:** Supplies a distributional comparison group and potential vulnerability component under an explicit definition.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Share [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S03: Census ACS Public Use Microdata Sample; S01: Census American Community Survey, detailed tables

[Primary source or access page](https://www.census.gov/programs-surveys/acs/microdata.html)

**Limitation:** B03002 counts persons; overlapping ethnicity/race and multiracial categories need explicit treatment.

### Service_Access_Loss

**Role and units:** Proposed auxiliary or input. travel/access change.

**Definition:** Reduction in access to essential services following a move or disruption.

**How derived:** Compare origin and destination travel time, cost, eligibility and continuity for the same household. Estimate any conversion to wellbeing-point change separately.

**Model contribution:** Contributes to Wellbeing_Decline and identifies receiving-area needs.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Wellbeing_Decline [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S33: Rice Greater Houston Community Panel (GHCP); S43: SAMHSA National Substance Use and Mental Health Services Survey; S44: Harris County Public Health reports and dashboards; S35: Texas A&M IDRT / OneGulf buyout fiscal and social implications project; S59: Census LEHD Origin-Destination Employment Statistics

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Provider proximity is not usable access; public destination data may be aggregated or unavailable.

### Stress_Accumulation

**Role and units:** Flow referenced by a stock. stress points/year.

**Definition:** Increase in the selected distress score per year.

**How derived:** Estimate repeated score changes following hazards, waiting and displacement with consistent measurement and follow-up. Calibrate rates rather than adding event counts directly to a score.

**Model contribution:** Fills Community_Psychosocial_Stress.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Community_Psychosocial_Stress [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S37: Rice Texas Flood Registry; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Separate stock means from totals and model recovery as well as accumulation.

### Vulnerable_Population_Support

**Role and units:** Proposed auxiliary or input. service coverage/adequacy.

**Definition:** Coverage and adequacy of support provided to households with defined needs.

**How derived:** Divide households receiving timely suitable support by eligible households and report adequacy relative to assessed need. Preserve dimensions if a single index is not validated.

**Model contribution:** Modifies Equity_Improvements.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Equity_Improvements [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Service counts without the eligible denominator cannot establish support coverage or equity.

### Wellbeing_Improvements

**Role and units:** Flow referenced by a stock. wellbeing points/year.

**Definition:** Annual increase in the selected wellbeing score.

**How derived:** Measure within-person improvements associated with stable housing, safety and support, with explicit follow-up and aggregation weights.

**Model contribution:** Fills Vulnerable_Population_Wellbeing.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Vulnerable_Population_Wellbeing [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S33: Rice Greater Houston Community Panel (GHCP); S40: WHO-5 Well-Being Index; S21: HCD public-records access route

[Primary source or access page](https://www.kinderudp.org/#/datasetCatalog/oxwq5xg0ewkj)

**Limitation:** Natural recovery and selection into support require comparison; use consistent score/time units.

### First_Nations_Adjustment_Factor

**Role and units:** Auxiliary or delayed quantity. explicit policy adjustment.

**Definition:** Optional policy adjustment associated with community-agreed protections in the guide's Indigenous component.

**How derived:** Establish local relevance and replace fixed identity-conditioned coefficients with explicit agreed policy rules or named scenarios. No demographic field directly measures this multiplier.

**Model contribution:** Offers a place for cultural and rights-related policy protections; no downstream use is specified in the guide.

**Simulation relationship:** Localize scope and obtain a defensible community-defined policy interpretation. Do not use the numeric identity-conditioned coefficients as empirical evidence.

**Guide equation:** Guide paragraph 185: IF THEN ELSE(
First_Nations_Community = 1,
(1 + Non_Market_Values_Weight * 0.5) *
(1 + Ancestral_Land_Significance * 0.3) *
(1 - Historical_Forced_Relocation_Trauma * 0.4) *
Cultural_Protocol_Adherence,
1.0)

**Inputs named in guide:** Ancestral_Land_Significance [guide equation reference]; Cultural_Protocol_Adherence [guide equation reference]; First_Nations_Community [guide equation reference]; Historical_Forced_Relocation_Trauma [guide equation reference]; Non_Market_Values_Weight [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S38: Williams and Vaske place-attachment measurement study, USFS repository; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** The guide's trauma/ancestry coefficients lack local empirical support; do not treat identity as a deterministic behavior multiplier. See the simulation relationship for the required equation review.

### Historical_Forced_Relocation_Trauma

**Role and units:** Proposed auxiliary or input. community-defined qualitative/scale evidence.

**Definition:** Community-reported lasting effects of prior forced relocation where relevant.

**How derived:** Use community-authorized histories and appropriately designed self-report evidence. Define scope, interpretation and consent before any scale is constructed.

**Model contribution:** Enters an optional cultural-policy relationship in the guide; its coefficient remains unvalidated.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Adjustment_Factor [guide equation reference]

**Evidence:** Requires operational definition or validated proxy

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S38: Williams and Vaske place-attachment measurement study, USFS repository

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** Do not infer trauma from identity or transform histories into automatic numeric penalties.

### Non_Market_Values_Weight

**Role and units:** Policy or scenario input. preference weight.

**Definition:** Policy preference weight placed on nonmarket social or cultural outcomes.

**How derived:** Elicit and record stakeholder weights or present separate outcomes without aggregation. Treat alternative weights as scenarios, not empirical facts.

**Model contribution:** Modifies the optional First_Nations_Adjustment_Factor.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** First_Nations_Adjustment_Factor [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S46: HUD Tribal Directory Assessment Tool; S38: Williams and Vaske place-attachment measurement study, USFS repository; S52: Natural Capital Project InVEST methods and data; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://egis.hud.gov/TDAT/)

**Limitation:** A normative preference weight is not a Census variable; report sensitivity and disagreement.

### Social_Disruption_Costs

**Role and units:** Proposed auxiliary or input. USD_2024 or separate nonmonetary outcomes.

**Definition:** Incremental resource burden and valued social losses caused by disruption.

**How derived:** Estimate additional moving time, service-access costs and other defined burdens relative to a counterfactual. Monetize only justified components and retain nonmonetary outcomes separately.

**Model contribution:** Adds social consequences to Total_Social_Cost without duplicating relocation payments or wellbeing scores.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Total_Social_Cost [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Household/person ID, explicit group definitions, joint vulnerability flags, eligible need, assistance components, repeated outcomes, survey weights, item coding and follow-up completeness.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S36: Texas A&M / Texas Appleseed Harris County Home Buyout Study, Phase 1; S33: Rice Greater Houston Community Panel (GHCP); S21: HCD public-records access route; S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/d5d8eede-8885-4ebd-ae00-044e424fbb6f/content)

**Limitation:** Do not force distress or heritage into dollars without defensible valuation, or duplicate relocation payments and lost home value.

## Land

### Retreat_Lands_Area

**Role and units:** Stock. hectares.

**Definition:** Unique land area held within the defined retreat portfolio.

**How derived:** Union acquired parcel geometry up to the reference date, verify ownership and restrictions, and remove only changes that satisfy the stock's exit definition.

**Model contribution:** Sets the land inventory available for restoration.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Land_Acquired_Through_Retreat - Retreat_Land_Redevelopment, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Land_Acquired_Through_Retreat - Retreat_Land_Redevelopment, 0)`

**Inputs named in guide:** Land_Acquired_Through_Retreat [stock inflow]; Retreat_Land_Redevelopment [stock outflow]

**Consumers named in guide:** Ecosystem_Restoration_Rate [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S21: HCD public-records access route; S22: HCFCD public-information access route; S05: Harris Central Appraisal District account and parcel downloads; S55: Harris County Clerk real-property records

[Primary source or access page](https://hcd.harriscountytx.gov/About-Us/Public-Records-Request)

**Limitation:** Avoid overlapping parcels and distinguish acquisition from restored area or target-area centroids.

### Restored_Ecosystem_Area

**Role and units:** Stock. hectares.

**Definition:** Unique land area that has completed the defined restoration treatment and still qualifies.

**How derived:** Union accepted as-built footprints by date, verify treatment completion and subtract subsequent degradation. Acquisition or vacancy alone is not restoration.

**Model contribution:** Determines ecological benefits, recovery and potential hazard buffering.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Ecosystem_Restoration_Rate - Ecosystem_Degradation, 0). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Ecosystem_Restoration_Rate - Ecosystem_Degradation, 0)`

**Inputs named in guide:** Ecosystem_Restoration_Rate [stock inflow]; Ecosystem_Degradation [stock outflow]

**Consumers named in guide:** Ecosystem_Restoration_Rate [guide equation reference]; Ecosystem_Improvement [guide equation reference]; Ecosystem_Service_Benefits [guide equation reference]; Natural_Hazard_Buffer_Capacity [guide equation reference]; Mature_Ecosystem [guide equation reference]

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S49: USGS Annual National Land Cover Database

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Cleared or mowed land is not necessarily ecologically restored; do not infer completion from contract award.

### Ecosystem_Health_Index

**Role and units:** Stock. documented habitat-specific score.

**Definition:** Condition of the selected ecosystem relative to explicit reference criteria.

**How derived:** Combine habitat, vegetation, hydrologic and water-quality measures using published normalization, direction and weights for each ecosystem type.

**Model contribution:** Tracks ecological quality separately from the quantity of restored land.

**Simulation relationship:** Stock balance reconstructed from the guide INFLOWS, OUTFLOWS and INITIAL VALUE fields: INTEG(Ecosystem_Improvement - Ecosystem_Decline, Initial_Ecosystem_Health). Check initial scope and stock bounds.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Stock balance:** `INTEG(Ecosystem_Improvement - Ecosystem_Decline, Initial_Ecosystem_Health)`

**Inputs named in guide:** Ecosystem_Improvement [stock inflow]; Ecosystem_Decline [stock outflow]; Initial_Ecosystem_Health [stock initializer]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained stock initial value: unavailable

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Initial_Conditions.csv (opening-value record; missing values remain missing)

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S50: US Fish and Wildlife Service National Wetlands Inventory; S51: TCEQ surface-water quality data (SWQMIS); S53: EPA EnviroAtlas

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** No universal public 0–100 ecosystem-health measure; scoring must be habitat- and scale-specific.

### Land_Acquired_Through_Retreat

**Role and units:** Flow. hectares/year.

**Definition:** Newly acquired unique land area entering the retreat portfolio per year.

**How derived:** Union newly acquired polygons by closing date, exclude prior acquisitions and duplicate transfers, and annualize hectares.

**Model contribution:** Fills Retreat_Lands_Area.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 158: Properties_Retreated * Average_Property_Size

**Inputs named in guide:** Average_Property_Size [guide equation reference]; Properties_Retreated [guide equation reference]

**Consumers named in guide:** Retreat_Lands_Area [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S05: Harris Central Appraisal District account and parcel downloads; S55: Harris County Clerk real-property records

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Prefer actual areas over a single average parcel size; document projected CRS and overlap removal.

### Ecosystem_Restoration_Rate

**Role and units:** Flow. hectares/year.

**Definition:** Area completing the defined restoration treatment per year.

**How derived:** Sum accepted completed restoration polygons by completion date, remove overlap, and divide by period length. For projection constrain completions by eligible backlog, funding and delivery capacity.

**Model contribution:** Fills Restored_Ecosystem_Area.

**Simulation relationship:** Candidate rate: MIN(eligible_unrestored_hectares / restoration_delivery_time, annual_restoration_funding / cost_per_hectare, treatment_capacity). Restrict backlog to eligible land and guard overlapping treatment cohorts.

**Guide equation:** Guide paragraph 159: MIN(Retreat_Lands_Area - Restored_Ecosystem_Area,
Restoration_Funding / Cost_Per_Hectare,
Restoration_Capacity)

**Inputs named in guide:** Cost_Per_Hectare [guide equation reference]; Restoration_Capacity [guide equation reference]; Restoration_Funding [guide equation reference]; Restored_Ecosystem_Area [guide equation reference]; Retreat_Lands_Area [guide equation reference]

**Consumers named in guide:** Restored_Ecosystem_Area [stock inflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S48: HCFCD wetland mitigation banks and monitoring records

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Backlog hectares must be divided by a completion time to compare with hectares/year capacity. See the simulation relationship for the required equation review.

### Ecosystem_Improvement

**Role and units:** Flow. health points/year.

**Definition:** Annual increase in the ecosystem-health score following recovery or treatment.

**How derived:** Estimate trajectories from repeated treated and reference-site observations, with years since treatment and habitat type.

**Model contribution:** Fills Ecosystem_Health_Index.

**Simulation relationship:** Use a recovery rate in health-points/year; the factor 10 is an uncalibrated multiplier. Define saturation and reference habitat conditions.

**Guide equation:** Guide paragraph 160: (Restored_Ecosystem_Area / Total_Ecosystem_Area) * Natural_Recovery_Rate * 10

**Inputs named in guide:** Natural_Recovery_Rate [guide equation reference]; Restored_Ecosystem_Area [guide equation reference]; Total_Ecosystem_Area [guide equation reference]

**Consumers named in guide:** Ecosystem_Health_Index [stock inflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** Area restored alone cannot determine ecological improvement; hydrologic and maintenance conditions matter. See the simulation relationship for the required equation review.

### Retreat_Land_Use_Strategy

**Role and units:** Policy or scenario selector. categorical.

**Definition:** Selected post-acquisition land treatment and permitted-use policy.

**How derived:** Assign a strategy by parcel or cohort from documented decisions and restrictions. Define scenario alternatives through treatment, cost, timing and outcome parameters.

**Model contribution:** Organizes the land-management policy comparison; downstream rate effects need explicit links.

**Simulation relationship:** Guide relationship is preserved in the equation field. Reconcile units, bounds and input definitions before execution.

**Guide equation:** Guide paragraph 162: Policy_Selection

**Inputs named in guide:** Policy_Selection [guide equation reference]; Full_Natural_Restoration [category option]; Multi_Purpose [category option]; Restricted_Rebuilding [category option]; Green_Infrastructure [category option]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space; S22: HCFCD public-information access route

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Generic redevelopment or rebuilding choices may conflict with acquisition deed/funding restrictions.

### Ecosystem_Service_Benefits

**Role and units:** Auxiliary or delayed quantity. USD_2024/year.

**Definition:** Incremental annual value of ecosystem services attributable to restored land.

**How derived:** Estimate per-hectare annual marginal benefits for each service and multiply by qualifying area. Account for maturity, spatial effects and overlapping service valuations.

**Model contribution:** Reports ecological benefits and informs the optional social-cost objective.

**Simulation relationship:** Use compatible annual marginal values per hectare and avoid counting the same avoided flooding losses in both this total and disaster-loss benefits.

**Guide equation:** Guide paragraph 163: Restored_Ecosystem_Area * (Flood_Protection_Value + Water_Quality_Value + Recreation_Value + Carbon_Sequestration_Value + Biodiversity_Value)

**Inputs named in guide:** Biodiversity_Value [guide equation reference]; Carbon_Sequestration_Value [guide equation reference]; Flood_Protection_Value [guide equation reference]; Recreation_Value [guide equation reference]; Restored_Ecosystem_Area [guide equation reference]; Water_Quality_Value [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S52: Natural Capital Project InVEST methods and data; S53: EPA EnviroAtlas; S56: FEMA Hazus Flood Model technical manual; S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://data.naturalcapitalproject.stanford.edu/)

**Limitation:** Do not sum overlapping services, stock carbon values and annual flows or double count avoided disaster loss. See the simulation relationship for the required equation review.

### Natural_Hazard_Buffer_Capacity

**Role and units:** Auxiliary or delayed quantity. reduction ratio or physical capacity.

**Definition:** Modeled physical or proportional hazard-buffering effect of restored ecosystems.

**How derived:** Estimate change in storage, stage or expected damage from spatial hydrologic scenarios. Fit the guide's area-share approximation only if it reproduces those effects.

**Model contribution:** Represents the hazard-reduction benefit of restored land; the feedback to hazard or damage needs an explicit equation.

**Simulation relationship:** Validate the area-share approximation against spatial hydraulic effects. Connect it to hazard or damage explicitly if it is intended to close the restoration feedback.

**Guide equation:** Guide paragraph 164: (Restored_Ecosystem_Area / Total_Hazard_Zone_Area) * Ecosystem_Type_Protection_Factor

**Inputs named in guide:** Ecosystem_Type_Protection_Factor [guide equation reference]; Restored_Ecosystem_Area [guide equation reference]; Total_Hazard_Zone_Area [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S11: Texas Water Development Board flood planning datasets; S47: HCFCD Watershed Environmental Baseline (WEB); S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Area fraction alone is not protective performance; downstream location and event magnitude matter. See the simulation relationship for the required equation review.

### Average_Property_Size

**Role and units:** Parameter. hectares/property.

**Definition:** Mean land area per property in the relevant acquisition cohort.

**How derived:** Existing proxy is mean positive acreage for exposed A1 accounts multiplied by 0.40468564224. Prefer the unique acquired polygon area divided by acquired property count for actual retreat cohorts.

**Model contribution:** Converts property acquisition flow into Land_Acquired_Through_Retreat.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Land_Acquired_Through_Retreat [guide equation reference]

**Evidence:** Retained parameter: derived_proxy

**Fields or records:** acct; state_class; acreage; sfha_any_overlap_2026

**Existing evidence:** data/Residential_Parcel_Inputs.csv.gz

**Sources:** S05: Harris Central Appraisal District account and parcel downloads; S22: HCFCD public-information access route

[Primary source or access page](https://hcad.org/pdata/pdata-property-downloads.html/)

**Limitation:** County residential mean can misrepresent target buyout parcels and assemblages.

### Cost_Per_Hectare

**Role and units:** Parameter. USD_2024/hectare.

**Definition:** Restoration treatment cost per accepted hectare.

**How derived:** Divide paid treatment-specific cost by verified accepted area, separating acquisition, demolition, design, maintenance and restoration phases. Convert to 2024 dollars.

**Model contribution:** Converts annual Restoration_Funding into an affordable treatment rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Restoration_Rate [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S29: Harris County purchasing, contracts and procurement records; S22: HCFCD public-information access route; S48: HCFCD wetland mitigation banks and monitoring records; S31: BLS Consumer Price Index

[Primary source or access page](https://purchasing.harriscountytx.gov/)

**Limitation:** Credit prices and total contract awards are not comparable treatment unit costs.

### Ecosystem_Restoration_Time

**Role and units:** Parameter. years.

**Definition:** Delay from restoration treatment to a specified ecological maturity or condition.

**How derived:** Follow restoration cohorts to habitat-specific criteria, include incomplete recovery observations and estimate a duration distribution.

**Model contribution:** Delays restored area into Mature_Ecosystem in the optional guide equation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Mature_Ecosystem [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S22: HCFCD public-information access route; S48: HCFCD wetland mitigation banks and monitoring records; S47: HCFCD Watershed Environmental Baseline (WEB); S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Physical construction time and ecological maturation time must be separate.

### Ecosystem_Type_Protection_Factor

**Role and units:** Parameter. event-specific reduction ratio.

**Definition:** Hazard reduction attributable to a specific ecosystem type and location.

**How derived:** Compare matched hydrologic or hydraulic scenarios with and without the treatment. Estimate reduction ratios by event, habitat and location.

**Model contribution:** Converts restored area share into Natural_Hazard_Buffer_Capacity.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Natural_Hazard_Buffer_Capacity [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S09: HCFCD flood reports and Harris County Flood Warning System; S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** Generic grassland/wetland factors in the guide are not transferable Harris County measurements.

### Infrastructure_Decommissioning_Time

**Role and units:** Parameter. years.

**Definition:** Elapsed time required to retire buildings, utilities or infrastructure after acquisition.

**How derived:** Link acquisition, work-order and accepted completion dates; estimate durations separately for buildings, utilities and roads.

**Model contribution:** Provides a potential delay before land becomes available for restoration; the guide has no full connecting equation.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S55: Harris County Clerk real-property records

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Parcel clearance is not necessarily complete infrastructure retirement; record each asset class.

### Restoration_Capacity

**Role and units:** Parameter. hectares/year.

**Definition:** Maximum feasible annual delivery of the specified restoration treatment.

**How derived:** Estimate accepted treated hectares divided by years for available crews and contracts, considering backlog and habitat type. Distinguish budget limits from physical capacity.

**Model contribution:** Caps Ecosystem_Restoration_Rate.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Restoration_Rate [guide equation reference]

**Evidence:** Retained parameter: assumed

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** data/Parameters.csv (assumption/input record; measurement status shown separately)

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S48: HCFCD wetland mitigation banks and monitoring records

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Observed output may be funding-constrained, not a physical capacity ceiling.

### Biodiversity_Value

**Role and units:** Proposed auxiliary or input. USD_2024/ha/year or physical metric.

**Definition:** Incremental habitat or species benefit per restored hectare per year.

**How derived:** Estimate ecological change by habitat and treatment against a counterfactual. Apply justified local valuation only if available; otherwise report physical outcomes separately.

**Model contribution:** Supplies one component of Ecosystem_Service_Benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Service_Benefits [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S50: US Fish and Wildlife Service National Wetlands Inventory; S52: Natural Capital Project InVEST methods and data; S53: EPA EnviroAtlas

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** No ready local annual dollar value found; avoid double counting habitat and other ecosystem benefits.

### Carbon_Sequestration_Value

**Role and units:** Proposed auxiliary or input. USD_2024/ha/year.

**Definition:** Annual value of additional net carbon uptake per restored hectare.

**How derived:** Estimate additional annual carbon flux, convert carbon to CO2-equivalent consistently, and multiply by an explicit valuation scenario. Separate carbon stocks from annual sequestration.

**Model contribution:** Supplies the carbon component of Ecosystem_Service_Benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Service_Benefits [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S49: USGS Annual National Land Cover Database; S50: US Fish and Wildlife Service National Wetlands Inventory; S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://www.usgs.gov/centers/eros/how-can-i-access-and-download-annual-nlcd-data)

**Limitation:** Separate carbon stock from annual sequestration and permanence; avoid claiming saleable credits without eligibility.

### Ecosystem_Decline

**Role and units:** Flow referenced by a stock. health points/year.

**Definition:** Annual decrease in the selected ecosystem-health score.

**How derived:** Compare repeated habitat-specific monitoring to baseline and reference conditions, with consistent sampling effort and scale.

**Model contribution:** Drains Ecosystem_Health_Index.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Health_Index [stock outflow]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S51: TCEQ surface-water quality data (SWQMIS); S49: USGS Annual National Land Cover Database

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** A reduction in vegetation cover is only one indicator and not a complete health decline measure.

### Ecosystem_Degradation

**Role and units:** Flow referenced by a stock. hectares/year.

**Definition:** Area of previously qualifying restored habitat losing that status per year.

**How derived:** Compare dated accepted footprints and inspections or land-cover evidence, identify unique degraded hectares and divide by elapsed years.

**Model contribution:** Drains Restored_Ecosystem_Area; it differs from a change in health score.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Restored_Ecosystem_Area [stock outflow]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S49: USGS Annual National Land Cover Database; S50: US Fish and Wildlife Service National Wetlands Inventory; S47: HCFCD Watershed Environmental Baseline (WEB)

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Keep loss of area distinct from declining health on habitat that remains present.

### Flood_Protection_Value

**Role and units:** Proposed auxiliary or input. USD_2024/ha/year.

**Definition:** Annual avoided flood loss attributable to one hectare of restoration.

**How derived:** Model losses under matched with-restoration and counterfactual hydraulic scenarios, integrate over event probabilities, and allocate marginal avoided loss to treated area.

**Model contribution:** Supplies the flood-protection component of Ecosystem_Service_Benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Service_Benefits [guide equation reference]

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S56: FEMA Hazus Flood Model technical manual; S52: Natural Capital Project InVEST methods and data

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Avoid counting the same flood losses in both ecosystem benefits and the general avoided-loss term.

### Full_Natural_Restoration

**Role and units:** Category. categorical.

**Definition:** Land-use strategy emphasizing ecological restoration within permitted restrictions.

**How derived:** Define eligible treatments, accepted condition, cost and timing for the parcel and funding program.

**Model contribution:** Selects a Retreat_Land_Use_Strategy alternative.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Retreat_Land_Use_Strategy alternative.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Land_Use_Strategy [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Green_Infrastructure

**Role and units:** Category. categorical.

**Definition:** Land-use strategy incorporating permitted nature-based stormwater or related infrastructure.

**How derived:** Specify the treatment, design, allowed use, cost and maintenance requirements by parcel.

**Model contribution:** Selects a Retreat_Land_Use_Strategy alternative with distinct capacity and benefits.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Retreat_Land_Use_Strategy alternative with distinct capacity and benefits.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Land_Use_Strategy [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Initial_Ecosystem_Health

**Role and units:** Initial value. documented habitat-specific score.

**Definition:** Baseline initializer of Ecosystem_Health_Index retained under the guide's original name.

**How derived:** Derive Ecosystem_Health_Index for the chosen opening date, then hold that starting value fixed as the stock initializer. Combine habitat, vegetation, hydrologic and water-quality measures using published normalization, direction and weights for each ecosystem type.

**Model contribution:** Initializes Ecosystem_Health_Index; it is not a second independently changing stock.

**Simulation relationship:** Initializes Ecosystem_Health_Index; it is not a second independently changing stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Health_Index [stock initializer]

**Evidence:** Derived from/reconciled to Ecosystem_Health_Index

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Multi_Purpose

**Role and units:** Category. categorical.

**Definition:** Land-use strategy combining compatible restoration, recreation or other permitted uses.

**How derived:** Specify the allowed combination and allocate area, costs and benefits without counting shared land twice.

**Model contribution:** Selects a Retreat_Land_Use_Strategy alternative.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Retreat_Land_Use_Strategy alternative.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Land_Use_Strategy [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Natural_Recovery_Rate

**Role and units:** Proposed auxiliary or input. ecosystem-health points/year.

**Definition:** Rate of ecological condition recovery under a defined reference process.

**How derived:** Estimate annual health-score change from repeated untreated or reference-site monitoring, controlling habitat and hydrologic conditions.

**Model contribution:** Sets the recovery speed in Ecosystem_Improvement.

**Simulation relationship:** Recommended implementation unit is ecosystem-health points/year if the guide recovery equation is retained. Document the meaning of the additional factor 10.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Improvement [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** Restoration project improvements cannot automatically identify natural recovery without a comparator. See the simulation relationship for the required equation review.

### Policy_Selection

**Role and units:** Policy selector. category.

**Definition:** Policy selector of Retreat_Land_Use_Strategy retained under the guide's original name.

**How derived:** Store the selected category that defines Retreat_Land_Use_Strategy. Resolve this as the input selector rather than creating two variables that refer back to each other.

**Model contribution:** Sets the policy category used by Retreat_Land_Use_Strategy.

**Simulation relationship:** Sets the policy category used by Retreat_Land_Use_Strategy. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Land_Use_Strategy [guide equation reference]

**Evidence:** Derived from/reconciled to Retreat_Land_Use_Strategy

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Recreation_Value

**Role and units:** Proposed auxiliary or input. USD_2024/ha/year or visits.

**Definition:** Incremental recreation benefit per restored hectare per year.

**How derived:** Measure changes in visits, access or use, then apply a justified local valuation if available. GHCP suppressed park willingness-to-pay fields cannot supply estimates.

**Model contribution:** Supplies the recreation component of Ecosystem_Service_Benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Service_Benefits [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S52: Natural Capital Project InVEST methods and data; S53: EPA EnviroAtlas; S22: HCFCD public-information access route

[Primary source or access page](https://data.naturalcapitalproject.stanford.edu/)

**Limitation:** GHCP park willingness-to-pay fields are suppressed in the codebook; do not treat them as accessible public valuation data.

### Restoration_Funding

**Role and units:** Proposed auxiliary or input. USD_2024/year.

**Definition:** Annual funding released or available for the restoration phase.

**How derived:** Trace restoration-specific receipts, commitments and payments by year and funding restriction. Keep annual release distinct from the remaining cash balance.

**Model contribution:** Limits affordable restoration hectares through Cost_Per_Hectare.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Restoration_Rate [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S29: Harris County purchasing, contracts and procurement records; S26: Harris County adopted budgets and budget volumes; S23: Texas GLO HUD DRGR quarterly performance reports

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Acquisition awards do not necessarily include ecological restoration; stock balance versus annual flow must be explicit.

### Restricted_Rebuilding

**Role and units:** Category. categorical.

**Definition:** Guide category permitting only specifically restricted post-retreat rebuilding or use.

**How derived:** Verify feasibility for each parcel's funding and deed conditions, then define allowed uses and treatment rules. Exclude prohibited scenarios.

**Model contribution:** Selects a Retreat_Land_Use_Strategy alternative only where applicable.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects a Retreat_Land_Use_Strategy alternative only where applicable.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Land_Use_Strategy [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Retreat_Land_Redevelopment

**Role and units:** Flow referenced by a stock. hectares/year.

**Definition:** Area leaving the defined retreat-land stock through a qualifying change of use per year.

**How derived:** Record actual permitted changes and effective dates. If the stock means all publicly acquired land, a change of use may not remove ownership and needs another stock definition.

**Model contribution:** Drains Retreat_Lands_Area only under a consistent land-accounting rule.

**Simulation relationship:** This flow is named by a stock, but the guide provides no complete equation. Estimate it from the described records or specify a dimensioned response before simulation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Lands_Area [stock outflow]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S54: 44 CFR Part 80, property acquisition and relocation for open space; S19: Harris County HCD buyout guidelines and performance reports; S22: HCFCD public-information access route; S55: Harris County Clerk real-property records

[Primary source or access page](https://www.govinfo.gov/content/pkg/CFR-2025-title44-vol1/pdf/CFR-2025-title44-vol1-part80.pdf)

**Limitation:** Open-space deed restrictions may prohibit generic redevelopment; not every transfer removes land from retreat status.

### Total_Ecosystem_Area

**Role and units:** Proposed auxiliary or input. hectares.

**Definition:** Total area of the ecosystem classes represented by the health or recovery calculation.

**How derived:** Select classes and a fixed boundary, dissolve overlaps and calculate hectares in an appropriate projected CRS. Match the ecosystem universe to restored area.

**Model contribution:** Provides the denominator in Ecosystem_Improvement.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Improvement [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S49: USGS Annual National Land Cover Database; S50: US Fish and Wildlife Service National Wetlands Inventory

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** Use the same habitat definition as health/restoration metrics; mosaics and source dates vary.

### Water_Quality_Value

**Role and units:** Proposed auxiliary or input. USD_2024/ha/year or physical load.

**Definition:** Annual marginal water-quality benefit per restored hectare.

**How derived:** Model and validate pollutant-load or condition change under restoration and counterfactual land use. Apply a compatible valuation only where justified.

**Model contribution:** Supplies the water-quality component of Ecosystem_Service_Benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Ecosystem_Service_Benefits [guide equation reference]

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S51: TCEQ surface-water quality data (SWQMIS); S52: Natural Capital Project InVEST methods and data; S53: EPA EnviroAtlas

[Primary source or access page](https://www.tceq.texas.gov/agency/data/lookup-data/download-data.html)

**Limitation:** Water-quality measurements do not directly supply economic value; avoid overlapping treatment-cost and welfare benefits.

### Ecosystem_Benefits

**Role and units:** Derived mapping requiring reconciliation. USD_2024 present value.

**Definition:** Ecosystem benefit term in the guide's optimization objective.

**How derived:** Discount annual incremental Ecosystem_Service_Benefits over the common horizon, accounting for maturity and avoiding overlap with avoided-disaster benefits.

**Model contribution:** Reduces Total_Social_Cost through compatible ecological benefits.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Total_Social_Cost [guide equation reference]

**Evidence:** Name or accounting scope requires reconciliation

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S52: Natural Capital Project InVEST methods and data; S53: EPA EnviroAtlas

[Primary source or access page](https://data.naturalcapitalproject.stanford.edu/)

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Mature_Ecosystem

**Role and units:** Auxiliary or delayed quantity. hectares meeting maturity criteria.

**Definition:** Restored area that has reached defined ecological maturity.

**How derived:** Track restoration cohorts and the share meeting reference criteria by age. A delay of area is an approximation requiring cohort and degradation checks.

**Model contribution:** Supports benefits that depend on maturity rather than immediate treatment completion.

**Simulation relationship:** Track restoration age cohorts and survival to maturity. The guide delay of the area stock is an approximation that may overstate mature area after degradation.

**Guide equation:** Guide paragraph 174: DELAY3(Restored_Ecosystem_Area, Ecosystem_Restoration_Time)

**Inputs named in guide:** Ecosystem_Restoration_Time [guide equation reference]; Restored_Ecosystem_Area [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Calculated once compatible inputs and definitions are supplied

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S47: HCFCD Watershed Environmental Baseline (WEB); S48: HCFCD wetland mitigation banks and monitoring records; S51: TCEQ surface-water quality data (SWQMIS)

[Primary source or access page](https://www.hcfcd.org/Activity/Additional-Programs/Watershed-Environmental-Baseline-WEB-Program)

**Limitation:** A fixed delay of total restored area ignores treatment failure, degradation and heterogeneous maturation. See the simulation relationship for the required equation review.

### Upstream_Retreat_Area

**Role and units:** Proposed auxiliary or input. hectares by drainage unit.

**Definition:** Retreat or restored area located upstream of a specified receiving reach.

**How derived:** Assign unique acquired or restored polygons to drainage catchments, calculate hectares and retain which treatment stage is represented.

**Model contribution:** Supplies the spatial input to Watershed_Flooding_Benefit.

**Simulation relationship:** No complete standalone equation is supplied. Use the stated data derivation as a proposed input method and specify any dynamic response separately.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Watershed_Flooding_Benefit [guide equation reference]

**Evidence:** Measurement route identified; exact model input not certified

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S22: HCFCD public-information access route; S05: Harris Central Appraisal District account and parcel downloads; S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets

[Primary source or access page](https://www.hcfcd.org/Community/Contact-Us/Public-Information-Requests)

**Limitation:** Administrative neighborhoods are not drainage units; restored and acquired area may differ.

### Watershed_Flooding_Benefit

**Role and units:** Auxiliary or delayed quantity. stage/storage/loss reduction.

**Definition:** Downstream flooding reduction attributable to upstream retreat or restoration.

**How derived:** Run comparable watershed and hydraulic scenarios with and without the specified upstream treatment, then compare stage, storage or expected losses.

**Model contribution:** Captures cross-community benefits in the optional spatial extension.

**Simulation relationship:** Guide relationship is preserved in the equation field. Its coefficients or scales require validation against the derivation described here.

**Guide equation:** Guide paragraph 348: f(Upstream_Retreat_Area[Neighborhood]); conceptual function

**Inputs named in guide:** Neighborhood [guide equation reference]; Upstream_Retreat_Area [guide equation reference]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Requires calibration or longitudinal evidence

**Fields or records:** Required records: Unique parcel/project geometry, ownership and restriction dates, treatment type, accepted completion, cost phase, monitoring dates and reference condition; spatial scenario results for benefits.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S10: USGS Water Data APIs; S11: Texas Water Development Board flood planning datasets; S52: Natural Capital Project InVEST methods and data; S56: FEMA Hazus Flood Model technical manual

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** A simple linear area coefficient misses location, connectivity and event-specific effects.

## Scenario

### Annual_Base_Funding

**Role and units:** Policy or scenario input. USD_2024/year.

**Definition:** Scheduled yearly funding for the scenario's additional retreat program.

**How derived:** Read the scenario amount and effective years; convert it into an annual receipt schedule with stated restrictions. It is an assumed policy input.

**Model contribution:** Supplies the non-event-contingent funding scenario.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative scenario setting

**Fields or records:** scenario_id; variable; value; unit; start_time; end_time; trigger; evidence_status

**Existing evidence:** scenarios/Scenario_Parameters.csv

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Existing illustrative scenario setting; no executed or calibrated model is implied.

### Annual_Post_Disaster_Funding

**Role and units:** Policy or scenario input. USD_2024/year.

**Definition:** Additional annual funding conditional on the scenario's disaster trigger.

**How derived:** Read the scenario amount and define the qualifying event, release date and duration. Avoid repeating the amount indefinitely without an explicit duration rule.

**Model contribution:** Supplies the event-contingent funding scenario.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative scenario setting

**Fields or records:** scenario_id; variable; value; unit; start_time; end_time; trigger; evidence_status

**Existing evidence:** scenarios/Scenario_Parameters.csv

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Existing illustrative scenario setting; no executed or calibrated model is implied.

### CC_Scenario

**Role and units:** Policy or scenario selector. categorical.

**Definition:** Selected climate projection family and trajectory.

**How derived:** Store the source ensemble, scenario label, baseline, member and horizon. Retain RCP labels only with compatible projections; do not relabel SSP projections as RCPs.

**Model contribution:** Selects climate-impact rates and sea-level trajectories.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** RCP2.6 [category option]; RCP4.5 [category option]; RCP8.5 [category option]

**Consumers named in guide:** Climate_Change_Impact_Index [guide equation reference]; Sea_Level_Rise [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.usgs.gov/data/cmip6-loca2-spatial-summaries-counties-tiger-2023-1950-2100-contiguous-united-states)

**Limitation:** Guide RCP labels are not interchangeable with CMIP6 SSP labels; avoid unsupported one-to-one relabeling.

### Commercial

**Role and units:** Category. categorical.

**Definition:** Land-user category representing specified commercial property interests.

**How derived:** Define eligible businesses, property owners and units, retaining occupancy and ownership separately.

**Model contribution:** Partitions Land_User_Group where commercial retreat is included.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Partitions Land_User_Group where commercial retreat is included.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Land_User_Group [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S46: HUD Tribal Directory Assessment Tool

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Community

**Role and units:** Category. categorical.

**Definition:** Geographic category for an explicitly defined community boundary.

**How derived:** Assign stable boundary IDs and versioned geographic membership. Define overlaps with neighborhoods and watersheds.

**Model contribution:** Indexes Community_Retreat_Demand and geographic comparisons.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Indexes Community_Retreat_Demand and geographic comparisons.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Regional_Retreat_Pressure [guide equation reference]; Geographic_Scale [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S01: Census American Community Survey, detailed tables; S11: Texas Water Development Board flood planning datasets

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Community_Request

**Role and units:** Category. categorical.

**Definition:** Trigger category based on a qualifying community request.

**How derived:** Apply the chosen petition or request criterion and effective date.

**Model contribution:** Selects the petition branch of Retreat_Program_Active.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects the petition branch of Retreat_Program_Active.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trigger_Type [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### FINAL TIME

**Role and units:** Simulation setting. year.

**Definition:** Calendar year or elapsed model time at which a simulation ends.

**How derived:** Set the proposed scenario end to 2050 if calendar time is used, or its matching elapsed-time value. Document the initial-time convention.

**Model contribution:** Determines the simulation and comparison horizon.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Guide 50–100-year examples are generic; horizon is a study choice, not a measurement.

### First_Nations

**Role and units:** Category. categorical.

**Definition:** Guide land-user category requiring a locally applicable Indigenous scope.

**How derived:** Establish community relevance, property interests and representation with the appropriate communities. It is not automatically inferred from Census race categories.

**Model contribution:** Partitions the optional Land_User_Group array after localization.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Partitions the optional Land_User_Group array after localization.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Land_User_Group [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S46: HUD Tribal Directory Assessment Tool

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Flooding

**Role and units:** Category. categorical.

**Definition:** Hazard category for the chosen flood mechanisms and event definition.

**How derived:** Specify riverine, rainfall or coastal flooding and the required physical footprints and thresholds.

**Model contribution:** Selects the baseline hazard inputs and exposure records.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects the baseline hazard inputs and exposure records.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Type [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S09: HCFCD flood reports and Harris County Flood Warning System; S14: US Forest Service Wildfire Risk to Communities

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Geographic_Scale

**Role and units:** Subscript definition. spatial index.

**Definition:** Spatial indexing scheme used for property, neighborhood, community and watershed analysis.

**How derived:** Define stable geographic units, dated crosswalks and aggregation rules. Nested levels must not be added as if they were disjoint observations.

**Model contribution:** Organizes spatial heterogeneity and inter-community effects.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Individual_Properties [category option]; Neighborhood [category option]; Community [category option]; Watershed [category option]

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S05: Harris Central Appraisal District account and parcel downloads; S11: Texas Water Development Board flood planning datasets; S15: Houston-Galveston Area Council forecasts and land cover; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** Nested units cannot be summed together; fiscal and hydrologic boundaries need distinct mappings.

### Government

**Role and units:** Category. categorical.

**Definition:** Land-user category for public property interests or facilities.

**How derived:** Identify public ownership and facility type using dated records, distinguishing the owner from the regulator or funding agency.

**Model contribution:** Partitions Land_User_Group where public property is in scope.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Partitions Land_User_Group where public property is in scope.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Land_User_Group [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S46: HUD Tribal Directory Assessment Tool

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Hazard_Type

**Role and units:** Subscript definition. hazard subscript.

**Definition:** Set of enabled hazards and their distinct physical input definitions.

**How derived:** Define a subscript with the included hazard labels and a separate intensity, frequency and exposure record for each.

**Model contribution:** Organizes optional multi-hazard calculations.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Flooding [category option]; Coastal_Erosion [category option]; Wildfire [category option]; Sea_Level_Rise [category option]

**Consumers named in guide:** Total_Hazard_Exposure [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S09: HCFCD flood reports and Harris County Flood Warning System; S11: Texas Water Development Board flood planning datasets; S13: NOAA relative sea-level trends and 2022 scenarios; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://www.hcfcd.org/About/Harris-Countys-Flooding-History/Countywide-Impacts)

**Limitation:** Sea-level rise can be a driver of coastal flooding rather than an independent loss event.

### Hazard_Types

**Role and units:** Subscript alias. hazard subscript.

**Definition:** Subscript alias of Hazard_Type retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Hazard_Type. Define a subscript with the included hazard labels and a separate intensity, frequency and exposure record for each.

**Model contribution:** Connects guide references to Hazard_Type without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Hazard_Type without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Derived from/reconciled to Hazard_Type

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S09: HCFCD flood reports and Harris County Flood Warning System; S14: US Forest Service Wildfire Risk to Communities; S57: UT Austin Bureau of Economic Geology bay shoreline change

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### INITIAL TIME

**Role and units:** Simulation setting. year.

**Definition:** Starting calendar time or elapsed origin for a simulation.

**How derived:** Match opening stocks to a precise reference date and map the 2024 baseline to subsequent 2025 to 2050 scenarios. If elapsed time starts at zero, retain its calendar mapping.

**Model contribution:** Aligns initial conditions, lookups and historical validation.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Guide generic zero does not specify the Harris County 2024 reference date.

### INTEGRATION METHOD

**Role and units:** Simulation setting. solver choice.

**Definition:** Numerical method used to integrate stock-and-flow equations.

**How derived:** Select a supported solver and compare trajectories across smaller time steps. Record the chosen algorithm and settings with each run.

**Model contribution:** Controls numerical approximation; it does not resolve data or structural uncertainty.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** No executable Vensim model is present to verify a solver setting now.

### Individual_Properties

**Role and units:** Category. categorical.

**Definition:** Geographic category representing individual property records.

**How derived:** Use stable account, parcel or structure IDs and explicitly relate multiple structures or households to each property.

**Model contribution:** Provides the finest exposure and acquisition accounting level.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Provides the finest exposure and acquisition accounting level.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Geographic_Scale [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S01: Census American Community Survey, detailed tables; S11: Texas Water Development Board flood planning datasets

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Land_User_Group

**Role and units:** Subscript definition. group subscript.

**Definition:** Set of land-user or tenure categories used to distinguish outcomes.

**How derived:** Define categories and their membership rules. Homeowners and Renters are also stock names in the guide, so resolve category-versus-variable naming before implementation.

**Model contribution:** Allows group-specific compensation, exposure and equity reporting.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Homeowners [category option]; Renters [category option]; Commercial [category option]; First_Nations [category option]; Government [category option]

**Consumers named in guide:** Compensation_Rate [guide equation reference]; Properties_at_Risk [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S01: Census American Community Survey, detailed tables; S03: Census ACS Public Use Microdata Sample; S05: Harris Central Appraisal District account and parcel downloads; S21: HCD public-records access route; S46: HUD Tribal Directory Assessment Tool; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://api.census.gov/data/2024/acs/acs5/groups.html)

**Limitation:** These categories can overlap; landlord ownership and resident tenure are different axes.

### Land_User_Groups

**Role and units:** Subscript alias. group subscript.

**Definition:** Subscript alias of Land_User_Group retained under the guide's original name.

**How derived:** Use the same definition, units and measurement as Land_User_Group. Define categories and their membership rules. Homeowners and Renters are also stock names in the guide, so resolve category-versus-variable naming before implementation.

**Model contribution:** Connects guide references to Land_User_Group without creating a duplicate input or stock.

**Simulation relationship:** Connects guide references to Land_User_Group without creating a duplicate input or stock. Select one canonical name or input mapping before implementation.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Derived from/reconciled to Land_User_Group

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S01: Census American Community Survey, detailed tables; S21: HCD public-records access route; S46: HUD Tribal Directory Assessment Tool

**Limitation:** Retain the original spelling in the audit, but do not create a second independently calibrated variable.

### Neighborhood

**Role and units:** Category. categorical.

**Definition:** Geographic category representing a fixed neighborhood boundary.

**How derived:** Assign versioned neighborhood IDs and parcel membership. Document overlapping community and drainage units.

**Model contribution:** Supports spatially differentiated exposure, demand and upstream treatment.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Supports spatially differentiated exposure, demand and upstream treatment.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Watershed_Flooding_Benefit [guide equation reference]; Geographic_Scale [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S01: Census American Community Survey, detailed tables; S11: Texas Water Development Board flood planning datasets

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### New_Retreat_Program_Enabled

**Role and units:** Policy or scenario input. 0 or 1.

**Definition:** Scenario switch for the additional retreat program being compared.

**How derived:** Read the explicit 0 or 1 setting by scenario and effective years from Scenario_Parameters.csv. Preserve any shared legacy-program baseline separately.

**Model contribution:** Enables or disables new retreat activity when mapped to Retreat_Program_Active.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative scenario setting

**Fields or records:** scenario_id; variable; value; unit; start_time; end_time; trigger; evidence_status

**Existing evidence:** scenarios/Scenario_Parameters.csv

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Existing illustrative scenario setting; no executed or calibrated model is implied.

### Planned_Caseworker_Capacity

**Role and units:** Policy or scenario input. caseworker FTE.

**Definition:** Target caseworker FTE for the scenario's program.

**How derived:** Read the planned staffing setting and specify hiring and attrition timing to reach the target. Planned FTE is distinct from observed filled FTE.

**Model contribution:** Provides the staffing target for Support_Services_Capacity.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Illustrative scenario setting

**Fields or records:** scenario_id; variable; value; unit; start_time; end_time; trigger; evidence_status

**Existing evidence:** scenarios/Scenario_Parameters.csv

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Existing illustrative scenario setting; no executed or calibrated model is implied.

### Proactive_Policy

**Role and units:** Category. categorical.

**Definition:** Trigger category based on policy stimulus and sufficient funding.

**How derived:** Evaluate the dated policy-stimulus rule and the declared funding threshold.

**Model contribution:** Selects the proactive branch of Retreat_Program_Active.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects the proactive branch of Retreat_Program_Active.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trigger_Type [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### RCP2.6

**Role and units:** Category. categorical.

**Definition:** Legacy low-forcing climate-scenario label included in the guide.

**How derived:** Select projections explicitly produced for RCP2.6 or revise the scenario taxonomy to match acquired data.

**Model contribution:** Chooses a climate trajectory within CC_Scenario.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Chooses a climate trajectory within CC_Scenario.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** CC_Scenario [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### RCP4.5

**Role and units:** Category. categorical.

**Definition:** Legacy intermediate-forcing climate-scenario label included in the guide.

**How derived:** Select projections explicitly produced for RCP4.5 or revise the scenario taxonomy to match acquired data.

**Model contribution:** Chooses a climate trajectory within CC_Scenario.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Chooses a climate trajectory within CC_Scenario.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** CC_Scenario [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### RCP8.5

**Role and units:** Category. categorical.

**Definition:** Legacy high-forcing climate-scenario label included in the guide.

**How derived:** Select projections explicitly produced for RCP8.5 or revise the scenario taxonomy to match acquired data.

**Model contribution:** Chooses a climate trajectory within CC_Scenario.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Chooses a climate trajectory within CC_Scenario.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** CC_Scenario [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S12: USGS CMIP6 LOCA2 and National Climate Change Viewer; S13: NOAA relative sea-level trends and 2022 scenarios

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Reactive_Disaster

**Role and units:** Category. categorical.

**Definition:** Trigger category based on a recent qualifying major disaster.

**How derived:** Apply the severity and recency rules for Recent_Major_Disaster.

**Model contribution:** Selects the reactive branch of Retreat_Program_Active.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Selects the reactive branch of Retreat_Program_Active.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Trigger_Type [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Retreat_Strategy

**Role and units:** Policy or scenario selector. categorical by place.

**Definition:** Overall retreat policy package for a place or scenario.

**How derived:** Specify no-retreat, reactive, proactive or hybrid rules with activation, funding, assistance, staffing and land-use settings.

**Model contribution:** Defines the policy comparisons to be simulated.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S54: 44 CFR Part 80, property acquisition and relocation for open space; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Scenario names alone do not specify operational mechanisms or legal feasibility.

### TIME STEP

**Role and units:** Simulation setting. years.

**Definition:** Time interval between numerical updates in the simulation.

**How derived:** Select an interval in years and test progressively smaller values. The guide's 0.125 years is one eighth of a year; a quarter-year is 0.25.

**Model contribution:** Controls numerical resolution and helps define feasible stock-depletion limits.

**Simulation relationship:** Correct the guide annotation: 0.125 years is not quarterly. Select and test a numerical time step rather than infer a reporting frequency from that text.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** No downstream equation specified in the guide

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** Guide labels 0.125 years quarterly; quarterly is 0.25 years. Do not inherit that inconsistency. See the simulation relationship for the required equation review.

### Threshold

**Role and units:** Policy or scenario input. USD_2024.

**Definition:** Minimum funding amount required by the proactive activation rule.

**How derived:** Select and document the funding balance threshold in the same unit and accounting scope as Funding_Available.

**Model contribution:** Determines whether funding is sufficient to activate proactive retreat.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S26: Harris County adopted budgets and budget volumes; S23: Texas GLO HUD DRGR quarterly performance reports; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://budget.harriscountytx.gov/budget.aspx)

**Limitation:** This guide token is a policy threshold, not a separately observed data series.

### Trigger_Type

**Role and units:** Policy or scenario selector. categorical.

**Definition:** Selected rule for starting or activating retreat.

**How derived:** Store one of the explicitly defined trigger categories and its required threshold, event or petition settings.

**Model contribution:** Chooses the conditional branch in Retreat_Program_Active.

**Simulation relationship:** Set the documented policy/scenario input; map its effects to the relevant model equation explicitly.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** Reactive_Disaster [category option]; Proactive_Policy [category option]; Community_Request [category option]

**Consumers named in guide:** Retreat_Program_Active [guide equation reference]

**Evidence:** Policy/scenario definition; no fitted value certified

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** S19: Harris County HCD buyout guidelines and performance reports; S20: HCFCD voluntary home buyout program; S28: Harris County Commissioners Court agendas, minutes and votes; M01: Ali shared system-dynamics guide and mind map

[Primary source or access page](https://hcd.harriscountytx.gov/Disaster-Recovery/Buyout-Relocation-Programs)

**Limitation:** Historical programs need observed triggers; hypothetical triggers must remain labeled as scenarios.

### Watershed

**Role and units:** Category. categorical.

**Definition:** Geographic category defined by drainage boundaries.

**How derived:** Use versioned catchment IDs and upstream-downstream connectivity, with explicit property and treatment crosswalks.

**Model contribution:** Supports hydrologic spillovers and watershed benefit calculations.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Supports hydrologic spillovers and watershed benefit calculations.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Geographic_Scale [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S05: Harris Central Appraisal District account and parcel downloads; S01: Census American Community Survey, detailed tables; S11: Texas Water Development Board flood planning datasets

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Wildfire

**Role and units:** Category. categorical.

**Definition:** Optional hazard category representing the defined wildfire mechanism.

**How derived:** Specify hazard probability or intensity and exposure using compatible spatial and temporal units before inclusion.

**Model contribution:** Adds an optional hazard to Hazard_Type.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Adds an optional hazard to Hazard_Type.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Hazard_Type [category option]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map; S09: HCFCD flood reports and Harris County Flood Warning System; S14: US Forest Service Wildfire Risk to Communities

**Limitation:** Category label, not a numeric observation or an extra downloadable dataset.

### Year

**Role and units:** Time index. calendar year.

**Definition:** Time index used to select calendar-based observations or projection values.

**How derived:** Map model time to a calendar year and use a consistent interpolation rule between observations.

**Model contribution:** Aligns Sea_Level_Rise and other time-varying lookup inputs.

**Simulation relationship:** Category, unit or time-index entry; no separate dynamic equation. Aligns Sea_Level_Rise and other time-varying lookup inputs.

**Guide equation:** No standalone equation captured; see stock balance where applicable

**Inputs named in guide:** No direct guide input identified

**Consumers named in guide:** Sea_Level_Rise [guide equation reference]

**Evidence:** Category or notation; no independent measurement

**Fields or records:** Required records: Scenario ID, exact setting name, category or numeric value, units, effective dates, trigger rule, geographic scope and reproducible run settings.

**Existing evidence:** No exact usable input file certified; see source assessment

**Sources:** M01: Ali shared system-dynamics guide and mind map

**Limitation:** The guide uses relative time elsewhere; map relative and calendar years explicitly.
