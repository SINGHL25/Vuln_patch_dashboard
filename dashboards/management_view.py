
import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.utils import load_unified_data

def management_dashboard():
    st.title("📊 Management Dashboard - KPIs & Compliance")
    
    df = load_unified_data()
    
    st.subheader("Server Compliance Summary")
    compliance_counts = df['Compliance'].value_counts()
    fig = px.pie(names=compliance_counts.index, values=compliance_counts.values, title='Compliance %')
    st.plotly_chart(fig)
    
    st.subheader("Vulnerable Servers by Severity")
    severity_counts = df.groupby('Severity')['ServerID'].nunique().reset_index()
    fig2 = px.bar(severity_counts, x='Severity', y='ServerID', color='Severity', title='Vulnerable Servers')
    st.plotly_chart(fig2)
    
    st.subheader("End-of-Support Risks")
    eos_counts = df['Lifecycle'].value_counts()
    fig3 = px.bar(eos_counts, x=eos_counts.index, y=eos_counts.values, color=eos_counts.index, title='EOL / Support Risk')
    st.plotly_chart(fig3)
