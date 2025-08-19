import streamlit as st
from scripts.transform import load_and_transform
from dashboards.engineer_view import engineer_dashboard
from dashboards.management_view import management_dashboard

# File paths
qualys_file = "data/raw/qualys_scan.csv"
patch_file = "data/raw/patch_report.csv"
lifecycle_file = "data/raw/lifecycle.csv"

# Load & merge data
df = load_and_transform(qualys_file, patch_file, lifecycle_file)

# Sidebar for navigation
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.selectbox("Select Page", ["Management View", "Engineer View"])

if page == "Management View":
    management_dashboard(df)
else:
    engineer_dashboard(df)

