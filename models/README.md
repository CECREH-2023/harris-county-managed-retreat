# Model design and implementation boundary

The expected executable file is `Managed_Retreat_Main.mdl`. It has not been supplied or run. No placeholder model is distributed.

The templates here and the earlier [model design](../docs/MODEL_DESIGN.md) preserve the initial architecture. Template numerical values and ordinal scales are illustrative. Use the current [300-entry dictionary](../documentation/Model_Data_Dictionary.csv), [current parameter values](../data/Parameters.csv), and [scenario records](../scenarios/Scenario_Parameters.csv) for the Harris County evidence snapshot. The dictionary retains guide expressions separately from proposed repairs; resolve those differences explicitly during implementation.

In particular, actual outside-boundary movers leave the population regardless of subsequent relocation success. Distinguish properties, occupied units, households, and people; include time constants when converting cash or area stocks to flows. The model must pass units, accounting, numerical, and empirical checks before any scenario is interpreted.
