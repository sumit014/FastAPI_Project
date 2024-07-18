import pandas as pd


def perform_data_analysis(df: pd.DataFrame):
    # Example function for data analysis
    summary = {}
    for column in df.columns:
        summary[column] = {
            "mean": df[column].mean(),
            "median": df[column].median(),
            "std": df[column].std(),
            "dtype": str(df[column].dtype)
        }

    return summary
