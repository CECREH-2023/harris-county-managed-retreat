# Scenarios

Use this directory to define and version scenario configurations.

## Files

- `scenario_catalog_template.csv` high-level scenario definitions
- `baseline_scenarios_template.yaml` default parameter bundles
- `bundles/` reusable policy bundles
- `overrides/` run-specific override files

## Recommended process

1. Register every scenario in the catalog.
2. Keep baseline bundles stable.
3. Put temporary run tweaks in `overrides/`.
4. Link each model run to a scenario ID.
