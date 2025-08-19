import streamlit as st
from scripts.transform import load_and_transform
from dashboards.engineer_view import engineer_dashboard

# File paths
qualys_file = "data/raw/qualys_scan.csv"
patch_file = "data/raw/patch_report.csv"
lifecycle_file = "data/raw/lifecycle.csv"

# Load & merge data
df = load_and_transform(qualys_file, patch_file, lifecycle_file)

# Engineer Dashboard
engineer_dashboard(df)

