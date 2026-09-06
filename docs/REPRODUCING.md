# Reproduction guide

Model design and scenario templates prepared; no calibrated executable simulator.

## Verify the distribution

From the package root:

```bash
python scripts/check_package.py
python scripts/check_inputs.py
```

The first command verifies the shipped files and hashes. The second checks whether separately acquired inputs are present and exits with code 2 when they are missing. Neither command estimates a statistical model.

## Run the selected workflow

Start with docs/MODEL_DESIGN.md, then populate the CSV/YAML templates. No statistical run command or completed model validation is claimed.

Use a disposable working copy when running the original analysis: several original scripts overwrite their project-relative output locations. Keep the distributed reference snapshot for comparison.

Environment: `See docs/SOFTWARE.md and the dependencies imported by the chosen source modules.`

Design resources; no executable calibrated model is claimed.

## Input contract

Required paths are listed in [data/INPUTS.json](../data/INPUTS.json). Templates and model definitions are released. Downloaded articles and private contributor notes are excluded.

[Source guide](CODE_MAP.md) identifies additional acquisition, sensitivity, and rendering modules. Original modeling and uncertainty procedures are retained. Use the documented input definitions; undocumented data substitutions can change the analysis.

## Evidence

[VALIDATION.json](../VALIDATION.json) records the checks performed on this snapshot. A partial model run or a fictional demo is identified by its limited scope. Full reproduction is claimed only where that record explicitly supports it.
