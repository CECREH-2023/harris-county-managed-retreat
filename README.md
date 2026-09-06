# Managed Retreat Scenario Model

How can planners compare retreat strategies across risk, fiscal, equity, and implementation objectives?

A seven-subsystem system-dynamics design with explicit assumptions, parameters, and scenario definitions. The selected package is a design resource, not a calibrated simulator.

## Results and interpretation

The deliverable is a **seven-subsystem model architecture** connecting hazard and risk, community and population, fiscal conditions, governance, implementation, equity and wellbeing, and land and ecosystems. The [model design](docs/MODEL_DESIGN.md), [model registers](models/), and [scenario templates](scenarios/) make proposed stock–flow relationships and assumptions explicit.

This version contains **no calibrated executable simulator or estimated policy effects**. Example parameter values illustrate model structure and must be replaced or justified before policy scenarios are interpreted.

## Explore this repository

- [Methods](docs/METHODS.md)
- [Reproduction and dependencies](docs/REPRODUCING.md)
- [Analysis source guide](docs/CODE_MAP.md)
- [Data sources and availability](data/README.md)

## Reproduce the work

**Available reproduction:** Model design and scenario templates prepared; no calibrated executable simulator.

Start with `python scripts/check_package.py` to check the file manifest, then follow the [reproduction guide](docs/REPRODUCING.md). A file-integrity check does not rerun the research analysis. Templates and model definitions are released. Downloaded articles and private contributor notes are excluded.

## Attribution and use

The architecture and example values are research-team design resources, not empirically calibrated parameter estimates.

A research resource from [CECREH at Texas Tech University](https://www.depts.ttu.edu/cecreh/). Snapshot: September 6, 2026. For code citation, use the repository URL and the commit identifier for the version you used; see [citation guidance](CITATION.md).

No additional reuse license is granted by this snapshot. Contact the authors through CECREH about permissions; source-data terms apply separately.
