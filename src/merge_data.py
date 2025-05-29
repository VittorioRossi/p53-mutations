import pandas as pd

def merge_dataframes(expression_df, mutation_df):
    # Ensure ModelID is a column (not index)
    expression_df = expression_df.rename(columns={expression_df.columns[0]: 'ModelID'})
    mutation_df = mutation_df.rename(columns={mutation_df.columns[0]: 'ModelID'})

    mutation_df.columns = mutation_df.columns.str.replace(r'\(.*?\)', '', regex=True).str.strip()  # Drop text in parentheses and strip whitespace
    
    # TP53 mutation column
    if 'TP53' not in mutation_df.columns:
        raise KeyError("TP53 column not found in mutation data.")

    # Keep only ModelID and TP53 from mutation data
    mutation_df = mutation_df[['ModelID', 'TP53']]

    # Merge on ModelID
    merged_df = pd.merge(expression_df, mutation_df, on='ModelID', how='inner')

    return merged_df


def main():
    # Read the two CSV files into dataframes
    df1 = pd.read_csv('/Users/vittorio/Projects/uni/ml_lab/data/raw/OmicsExpressionProteinCodingGenesTPMLogp1.csv')
    df2 = pd.read_csv('/Users/vittorio/Projects/uni/ml_lab/data/raw/OmicsSomaticMutations.csv')

    # Merge the dataframes
    merged_df = merge_dataframes(df1, df2)

    # Save the merged dataframe to a new CSV file
    merged_df.to_csv('/Users/vittorio/Projects/uni/ml_lab/data/processed/merged_data.csv', index=False)
    print("Merged data saved to 'merged_data.csv'")

if __name__ == "__main__":
    main()
