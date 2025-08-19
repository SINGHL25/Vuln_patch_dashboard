
import streamlit as st
import plotly.express as px
import pandas as pd

def management_dashboard(df):
    st.title("📊 Management Dashboard - Server Overview")

    # KPIs
    total_servers = df['ServerID'].nunique()
    total_vulns = df['Vulnerabilities'].sum()
    avg_compliance = df['Compliance'].mean()
    eos_servers = df[df['Lifecycle'] == 'End-of-Support'].shape[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Servers", total_servers)
    col2.metric("Total Vulnerabilities", total_vulns)
    col3.metric("Avg Compliance %", f"{avg_compliance:.1f}")
    col4.metric("End-of-Support Servers", eos_servers)

    st.markdown("---")

    # Vulnerabilities by Severity
    severity_count = df.groupby('Severity')['ServerID'].count().reset_index()
    fig1 = px.bar(severity_count, x='Severity', y='ServerID', color='Severity',
                  title="Servers by Vulnerability Severity", color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig1, use_container_width=True)

    # Compliance Distribution
    fig2 = px.histogram(df, x='Compliance', nbins=10, color_discrete_sequence=['#636EFA'],
                        title="Server Compliance Distribution")
    st.plotly_chart(fig2, use_container_width=True)

    # Lifecycle Status Pie Chart
    lifecycle_count = df['Lifecycle'].value_counts().reset_index()
    lifecycle_count.columns = ['Lifecycle','Count']
    fig3 = px.pie(lifecycle_count, names='Lifecycle', values='Count', color='Lifecycle',
                  title="Server Lifecycle Status", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig3, use_container_width=True)

    # Optional: Vulnerabilities vs Compliance Scatter
    fig4 = px.scatter(df, x='Compliance', y='Vulnerabilities', color='Severity',
                      hover_data=['ServerName','IP','OS_Version'], 
                      title="Vulnerabilities vs Compliance by Server")
    st.plotly_chart(fig4, use_container_width=True)
