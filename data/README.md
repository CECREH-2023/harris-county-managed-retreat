# Data sources and availability

This development release includes selected aggregate evidence and model configuration snapshots. It does not distribute the complete research workspace or claim that all model variables have measured inputs. Consult the [table inventory](TABLES.csv), [source manifest](../documentation/Source_Manifest.csv), and [62-family source catalog](../reports/source_assessment/Potential_Source_Catalog.csv) for traceability.

| Included files | What they provide | Principal limits |
| --- | --- | --- |
| `Parameters.csv`, `Initial_Conditions.csv`, `Initial_Conditions_Illustrative.csv`, `Lookup_Tables.csv` | Values, missing baselines, assumed functions, and a separate illustrative profile | 26 of 30 parameters assumed; 14 of 22 empirical stock initializations unavailable |
| `Population_Housing.csv`, `ACS_2024_Estimates_MOE.csv`, `Domestic_Outmigration_2024.csv`, `Participation_Support_Equity.csv` | Census population, tenure, socioeconomic and migration context | Rolling five-year estimates; harmonized tract counts; context is not individual behavior |
| `Hazard_Inputs.csv`, `Hazard_Annual_Counts.csv` | NOAA reported flood episodes | Reported episodes are not the model's catastrophic-event frequency |
| `Fiscal_Funding.csv`, `Retreat_Program_History.csv`, `GLO_Residential_Buyout_Quarterly.csv`, `Program_Accomplishments.csv`, `Program_Beneficiary_Context.csv` | Aggregate finance, public program reports, and beneficiary context | Distinct reporting universes, overlapping finance, and the quarantined 2025 discrepancy |
| `Climate_Scenario_Reference.csv`, `Population_Housing_Projections.csv` | Climate-window and regional projection context | Scenario references, not observed future outcomes or fitted hazard multipliers |
| `Calibration_Data.csv` | Candidate historical comparison series | No fitted parameters or validation results |

## Provenance and construction

Census data were reused from the existing Harris County research panel and supplemented with official 2024 ACS tables. The population/housing panel covers 1,115 harmonized 2020 tracts across 15 observation years (16,725 rows). Census IDs are strings. Census negative sentinel estimates are treated as missing in prepared numerical tables; available published margins of error are retained. The B07403 county extract preserves both published counts and the derived domestic outmigration rate.

The climate reference retains the source model, SSP, warming level, crossing year, and event window from Harris County projection work. Population/housing projections retain the H-GAC scenario attribution. Neither series establishes a calibrated retreat response.

Public HCD reports and GLO/DRGR financial histories provide program-specific evidence. Residential GLO buyout rows exclude commercial activities. Source fiscal-quarter labels and calendar dates are both retained; negative financial adjustments are preserved. Counts and dollar amounts from overlapping programs must not be summed without reconciliation.

The source manifest retains capture hashes and acquisition metadata. Public source URLs and variable-specific methods are in the catalog and dictionary. Source captures were assessed/acquired during the September 2026 preparation; this release does not silently refresh them.

## Material retained outside this release

- Parcel/account records, precise property geometry, original raw downloads, large NFIP/IHP and spatial working tables, and selected land-use-change parcels are not distributed. Their aggregate implications may appear as explicitly labeled inputs or source references.
- Original collaborator guide and mind-map files, email correspondence, machine locations, caches, and Word lock files are omitted. The earlier published design and structured crosswalks preserve the model context.
- Survey microdata and administrative case histories requiring a request or agreement are not included. A codebook or public dashboard does not establish the right to redistribute underlying records.
- The full acquisition pipeline depends on these retained sources and is not bundled or claimed to run from this snapshot. The included standard-library tools validate the distributed version and selected calculations.

[Release coverage](../documentation/Release_Coverage.csv) distinguishes included derivatives from excluded data files. The dictionary's source-path fields refer to the broader evidence inventory; they are not file-presence assertions.

## Attribution and use

Source terms remain those of the original providers, including the US Census Bureau, NOAA, FEMA, Harris County, Texas GLO, HCAD, and H-GAC. Public availability is not a blanket reuse license for all source material. This repository grants no additional rights to third-party data. See [RIGHTS.md](../RIGHTS.md) and follow the exact source's terms for any new redistribution.
