
import pandas as pd

def load_and_transform(qualys_file, patch_file, lifecycle_file):
    # Load raw CSVs
    df_qualys = pd.read_csv(qualys_file)
    df_patch = pd.read_csv(patch_file)
    df_lifecycle = pd.read_csv(lifecycle_file)

    # Merge on ServerID or IP
    df = df_qualys.merge(df_patch, on='ServerID', how='left')
    df = df.merge(df_lifecycle, on='ServerID', how='left')

    # Ensure required columns exist
    if 'Compliance' not in df.columns:
        # Example: compute compliance % = patched / total updates
        df['Compliance'] = df['PatchedUpdates'] / df['TotalUpdates'] * 100

    if 'Lifecycle' not in df.columns:
        df['Lifecycle'] = df['OS_Version'].apply(
            lambda x: 'End-of-Support' if '2012' in x else 'Supported'
        )

    return df
