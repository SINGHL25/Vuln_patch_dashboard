
import pandas as pd

def load_and_transform():
    # Example: merge raw CSVs into one processed CSV
    df1 = pd.read_csv("data/raw/qualys_scan.csv")
    df2 = pd.read_csv("data/raw/patch_report.csv")
    df3 = pd.read_csv("data/raw/lifecycle.csv")
    df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
    df.to_csv("data/processed/unified_data.csv", index=False)
    print("Unified data saved to data/processed/unified_data.csv")
