import streamlit as st
from dashboards import engineer_view, management_view
from scripts.transform import load_and_transform

# ETL: unify raw data
load_and_transform()

# Sidebar
st.sidebar.title("Dashboard Selector")
view = st.sidebar.radio("Choose View", ["Engineer", "Management"])

if view == "Engineer":
    engineer_view.engineer_dashboard()
else:
    management_view.management_dashboard()

