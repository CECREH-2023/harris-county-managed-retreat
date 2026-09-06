# Models

Use this directory for system dynamics model files and core model documentation.

## Suggested contents

- `managed_retreat_core.mdl` primary Vensim model file
- `subsystems/` optional subsystem model fragments or diagrams
- `archive/` dated snapshots of retired model versions
- `variable_dictionary_template.csv` canonical variable definitions and units
- `equation_register_template.csv` key equations with rationale and checks

## Conventions

1. Use one canonical variable name for each concept.
2. Keep units explicit and consistent in every equation.
3. Capture equation changes in the assumption change log.
