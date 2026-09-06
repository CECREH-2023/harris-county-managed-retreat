# Using this resource

Model design and scenario templates prepared; no calibrated executable simulator.

Start with docs/MODEL_DESIGN.md, then populate the CSV/YAML templates. No statistical run command or completed model validation is claimed.

Use [MODEL_DESIGN.md](MODEL_DESIGN.md), the [model registers](../models/), [scenario templates](../scenarios/), and [assumptions register](../assumptions/). Example values are illustrative. Calibration, dimensional checks, and empirical validation belong to a future model implementation.

## Verification scope

`python scripts/check_package.py` checks the distributed file hashes. It uses only the Python standard library and does not fit a model. Run it before generating outputs; new files outside the designated generated-results directory may be reported as extras.

[VALIDATION.json](../VALIDATION.json) records the checks performed for this version and their limits. Inclusion of an analysis module is not evidence that it has been executed. The [source guide](CODE_MAP.md) identifies the distributed modules.
