# Harris County Managed Retreat System Dynamics

How could managed retreat reduce flood exposure while sustaining household wellbeing, local finances, and restored land in Harris County, Texas? This project develops a Vensim system-dynamics model to examine those connected outcomes and compare retreat policies over time.

**Version 0.1.0 — model design and data development, September 15, 2026.** The release brings together a seven-subsystem architecture, a 300-entry data dictionary, a comprehensive source assessment, and selected aggregate inputs. An executable Vensim model has not yet been supplied or run. No calibrated policy effects or simulation results are reported.

## Start here

- [Data dictionary — Excel](Harris_County_Model_Data_Dictionary.xlsx), [readable entries](documentation/Model_Data_Dictionary.md), and [CSV](documentation/Model_Data_Dictionary.csv): what each entry means, how it is derived, and what it contributes to the model.
- [Project overview and model boundary](docs/PROJECT_OVERVIEW.md): research questions, seven subsystems, geography, time horizon, and development milestones.
- [Comprehensive variable source assessment](reports/source_assessment/Variable_Source_Assessment.md): 62 external source families, 295 assessed entries, and all 24 major mind-map branches.
- [Data sources and availability](data/README.md): included inputs, excluded records, provenance, and reuse limits.
- [Reproducing and validating the release](docs/REPRODUCING.md): a portable check of the distributed files and selected input calculations.

## Current evidence

The case uses a 2024 reference year, historical evidence spanning 2010–2024, and proposed policy scenarios for 2025–2050. The population and housing panel contains 16,725 tract-year records on 2020 census tract geography. Records also cover public program finances and accomplishments, reported flood episodes, climate scenario references, and Census migration and socioeconomic measures.

The 30 parameter records contain **26 assumptions, three derived proxies, and one observed value**. Fourteen of the 22 empirical stock initializations remain unavailable; three other stock initializations are explicit accounting assumptions. The separate illustrative profile is a hypothetical program setup. Identifying a potential source does not establish that its data have been acquired or that its variable has been measured.

The model links hazard, community, fiscal, governance, implementation, equity, and land processes. Proposed equation corrections and measurement definitions are marked in the dictionary. They require review and integration into the eventual executable model.

## Repository map

| Location | Contents |
| --- | --- |
| `documentation/` | Full dictionary, dependencies, source manifest, parameter-to-source map, assumptions, and gaps |
| `reports/source_assessment/` | Source assessment and variable/mind-map crosswalks |
| `data/` | Selected aggregate input snapshots and data availability notes |
| `config/` | Harris County geography, time, currency, and model boundary |
| `models/` and `docs/MODEL_DESIGN.md` | Earlier architecture and templates, retained for design provenance |
| `scenarios/` | Current illustrative parameter records and earlier scenario templates |
| `scripts/` | Portable release validation and dictionary export |

The research scope is the Vensim model and mind map; the literature-review matrix is a separate project. Correspondence, original collaborator files, survey microdata, parcel/account records, raw downloads, private paths, and workstation files are not distributed. [Known limitations and next development steps](docs/DEVELOPMENT_STATUS.md) explain what remains before simulation.

Maintained by [CECREH at Texas Tech University](https://www.depts.ttu.edu/cecreh/). See [citation and attribution](CITATION.md), [version history](CHANGELOG.md), and [use conditions](RIGHTS.md). No reuse license has yet been designated.
