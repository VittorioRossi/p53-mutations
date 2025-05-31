## How to run

1. Run data_prep.ipynb first
2. Run explore_ccle.ipynb to generate other data
3. Run other notebooks

## Data Sources

This project uses publicly available datasets from the DepMap portal (https://depmap.org/portal/). Specifically:

- `OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv`: Contains batch-corrected gene expression data (log2(TPM + 1)) for protein-coding genes across cancer cell lines.
- `OmicsSomaticMutationsMatrixDamaging.csv`: Contains binary annotations of damaging somatic mutations for genes in DepMap cell lines. Values indicate presence and confidence of mutations (0 = none, 1 = likely, 2 = high-confidence).

To create the training dataset, these two files are merged on the `ModelID` column. The mutation status for the TP53 gene is extracted from the mutation matrix and used as the target variable, while the expression levels of protein-coding genes serve as features.


cBioPortal CCLE dataset from 2 studies:

- `Cancer Cell Line Encyclopedia from the Broad Institute and Novartis, updated 2019.` : https://cbioportal-datahub.s3.amazonaws.com/ccle_broad_2019.tar.gz

- `Targeted sequencing of 1020 samples from Cancer Cell Line Encyclopedia from the Broad Institute and Novartis.` : https://cbioportal-datahub.s3.amazonaws.com/cellline_ccle_broad.tar.gz