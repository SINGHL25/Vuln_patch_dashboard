import pandas as pd

def load_unified_data():
    return pd.read_csv("data/processed/unified_data.csv")

def server_summary(df, server_id):
    return df[df['ServerID'] == server_id].T

