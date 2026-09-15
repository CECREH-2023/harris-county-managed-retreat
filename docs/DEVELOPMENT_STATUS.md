# Development status and next steps

Version 0.1.0 is a documented design and data release. It is suitable for examining variable definitions, tracing candidate sources, reviewing assumptions, and preparing Vensim integration.

## Completed in this release

- Documented all 300 entries in the expanded inventory: 295 source-assessment entries, four additional existing scenario settings, and one existing opposition lookup. The inventory includes aliases, categories, and settings as well as numerical variables.
- Retained 281 direct guide dependencies, 30 parameter records, 22 stock initialization records, and 24 settings across four illustrative scenarios.
- Mapped 62 external source families and one model-guide source to 295 assessed entries and 24 major mind-map branches. Source access was assessed September 10, 2026; it is not a guarantee of continuing availability.
- Included selected aggregate evidence already acquired or reused from Harris County research. No downloads are required to read or validate this snapshot.

## Remaining work before interpretable scenarios

1. Obtain the executable Vensim model and confirm its edition, variable names, import mechanisms, units, integration method, and time step. There is no `.mdl` file in this release.
2. Resolve the 14 missing baseline stock measurements and justify or estimate the 26 assumed parameters. An illustrative initial-condition profile does not close these evidence gaps.
3. Acquire or reconcile program application, closing, spending, staffing, and household destination histories. Distinguish applicants, properties, occupied units, households, and people. Do not double-count cofunded HCD, HCFCD, and FEMA projects.
4. Operationalize repeated trust, engagement, wellbeing, and social-capital measures. Rice survey source identification and codebook review do not constitute acquisition of the microdata. Validate item direction, scoring, weights, nonresponse, and population coverage before use.
5. Match restoration expenditures, hectares, and ecological monitoring to acquired land. H-GAC land-use projections do not measure completed retreat or restoration.
6. Reconcile the dictionary's proposed dimensional and accounting repairs with the model. Actual moves outside the county remove people from the population regardless of a subsequent relocation-success score. Separate financial stocks from dollar-per-year flows and area backlogs from hectare-per-year capacity.
7. Calibrate to suitable historical observations; reserve evaluation periods or cases; examine parameter identifiability and correlated uncertainty. Test units, mass balance, extreme conditions, nonnegative stocks, time-step convergence, and sensitivity before interpreting scenarios.

## Specific interpretation limits

- NOAA episode counts describe reported events; they do not directly estimate the guide's catastrophic-hazard frequency or property-destruction probability.
- ACS five-year observations overlap. Tract harmonization can yield fractional counts and does not make successive releases independent annual samples. Published county estimates are preferable to tract averages for county means and medians.
- Census domestic outmigration excludes moves abroad and uses the population age 1+ living in the area one year earlier. Applying its rate to all-age population requires a documented alignment decision.
- The June 2025 HCD table has 427 summed acquisition statuses against a reported total of 425. Preserve and quarantine that discrepancy for calibration rather than silently correcting it.
- Historical funding allocations, expenditures, disbursements, and available cash are different quantities. Retain program and quarter definitions and avoid adding overlapping finance series.
- Climate warming-window precipitation is not a dated flood-frequency multiplier. A defensible transformation remains to be fitted.
- Equity and psychosocial indices need defined observable scales and defensible subgroup comparisons. Demographic context does not directly measure willingness to participate or individual behavior.

See the [gap queue](../documentation/Gap_Queue.csv) for variable-specific follow-up and the [dictionary](../documentation/Model_Data_Dictionary.csv) for proposed repairs. No simulation, calibration, predictive validation, or cost-benefit finding is claimed by a passing release check.
