
import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.utils import load_unified_data

def engineer_dashboard():
    st.title("🛠 Engineer Dashboard - Server Drilldown")
    
    df = load_unified_data()
    servers = df['ServerID'].unique()
    
    selected_server = st.selectbox("Select Server", servers)
    server_data = df[df['ServerID']==selected_server]
    
    st.subheader(f"Details for Server: {selected_server}")
    st.table(server_data[['ServerName','IP','OS_Version','Lifecycle','Compliance']])
    
    st.subheader("Vulnerabilities by Severity")
    fig = px.bar(server_data, x='Vulnerability', y='CVSS', color='Severity', title='Vulnerabilities')
    st.plotly_chart(fig)
    
    st.subheader("Missing Patches")
    fig2 = px.pie(server_data, names='Patch', values='Status', title='Patch Status')
    st.plotly_chart(fig2)
