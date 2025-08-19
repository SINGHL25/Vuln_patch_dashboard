import streamlit as st
from dashboards import engineer_view, management_view
from scripts.transform import load_and_transform



# Provide CSV file paths
qualys_file = "data/raw/qualys_scan.csv"
patch_file = "data/raw/patch_report.csv"
lifecycle_file = "data/raw/lifecycle.csv"

# Call function with arguments
df = load_and_transform(qualys_file, patch_file, lifecycle_file)


# ETL: unify raw data
load_and_transform()

# Sidebar
st.sidebar.title("Dashboard Selector")
view = st.sidebar.radio("Choose View", ["Engineer", "Management"])

if view == "Engineer":
    engineer_view.engineer_dashboard()
else:
    management_view.management_dashboard()

