
import pandas as pd
import numpy as np

def load_and_transform(qualys_file, patch_file, lifecycle_file):
    # 1️⃣ Load CSVs
    df1 = pd.read_csv(qualys_file)
    df2 = pd.read_csv(patch_file)
    df3 = pd.read_csv(lifecycle_file)

    # 2️⃣ Merge CSVs on ServerID or IP
    df = df1.merge(df2, on='ServerID', how='left').merge(df3, on='ServerID', how='left')

    # 3️⃣ Rename columns to match app expectations
    df = df.rename(columns={
        'Server_Name': 'ServerName',
        'Support_Status': 'Lifecycle'
    })

    # 4️⃣ Add dummy Compliance column if not present
    if 'Compliance' not in df.columns:
        df['Compliance'] = np.random.randint(70, 100, size=len(df))

    return df

