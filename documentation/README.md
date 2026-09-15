# Dictionary and evidence registers

The [300-entry CSV](Model_Data_Dictionary.csv) is the editable dictionary snapshot. Its [readable Markdown](Model_Data_Dictionary.md) and [Excel workbook](../Harris_County_Model_Data_Dictionary.xlsx) explain each entry's definition, derivation, units, source requirements, limitations, and contribution to the model. The workbook has Dictionary, Equations, Sources, Current inputs, and Conventions sheets.

Data derivation describes how to construct a value from records. Simulation relationships describe how it would enter the model. Original guide equations, proposed repairs, aliases, and current evidence are separate fields. Missing measurements remain missing. Source identification is not evidence of acquisition or calibration.

The [281 dependency records](Model_Dependency_Links.csv) include stock flows, initial values, category options, and named conceptual determinants. They are a guide relationship inventory rather than proof that the model is closed or executable. Older templates in `models/` and `assumptions/` remain illustrative.

The September 15 register supersedes the earlier 215-entry inventory for interpretation. The earlier inventory remains local to the acquisition pipeline. In particular, the current dictionary corrects an earlier proposed population expression: actual outside-boundary movers leave the population even if their subsequent relocation does not meet the success criterion.

## Additional registers

- [Guide definitions](Guide_Variable_Register.csv) preserve 63 typed stock, flow, and auxiliary definitions.
- [Parameter source map](Parameter_Source_Map.csv) records source fields, transformations, geography, and time references.
- [Source manifest](Source_Manifest.csv) preserves source identifiers, acquisition metadata, and fingerprints. Raw capture paths refer to retained research material outside this distribution; workstation locations are removed.
- [Assumptions](Assumptions.csv) and [gaps](Gap_Queue.csv) make unresolved measurement and modeling decisions explicit.
- [Program timeline](Governance_Program_Timeline.csv) and [reported-table reconciliation](Reported_Table_Reconciliation.csv) retain public reporting context.

Paths in inherited `existing_file`, `existing_material`, and source-capture fields describe the research evidence inventory. They do not promise that every named file is distributed. Consult [release coverage](Release_Coverage.csv) and [data availability](../data/README.md).
