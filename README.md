


## Data Sources

This project uses publicly available datasets from the DepMap portal (https://depmap.org/portal/). Specifically:

- `OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv`: Contains batch-corrected gene expression data (log2(TPM + 1)) for protein-coding genes across cancer cell lines.
- `OmicsSomaticMutationsMatrixDamaging.csv`: Contains binary annotations of damaging somatic mutations for genes in DepMap cell lines. Values indicate presence and confidence of mutations (0 = none, 1 = likely, 2 = high-confidence).

To create the training dataset, these two files are merged on the `ModelID` column. The mutation status for the TP53 gene is extracted from the mutation matrix and used as the target variable, while the expression levels of protein-coding genes serve as features.