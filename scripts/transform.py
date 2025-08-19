
import pandas as pd

def load_and_transform(qualys_file, patch_file, lifecycle_file):
    # Load CSVs
    df1 = pd.read_csv(qualys_file)
    df2 = pd.read_csv(patch_file)
    df3 = pd.read_csv(lifecycle_file)

    # Standardize column names
    df1.columns = df1.columns.str.strip().str.replace(" ", "_")
    df2.columns = df2.columns.str.strip().str.replace(" ", "_")
    df3.columns = df3.columns.str.strip().str.replace(" ", "_")

    # Merge all data on ServerID or IP
    merged_df = df1.merge(df2, on="ServerID", how="outer")
    merged_df = merged_df.merge(df3, on="ServerID", how="outer")

    # Fill missing values
    merged_df.fillna({"Vulnerabilities": 0, "Compliance": 0, "Lifecycle": "Unknown"}, inplace=True)
    
    return merged_df
