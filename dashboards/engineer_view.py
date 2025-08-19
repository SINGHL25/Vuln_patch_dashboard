
import streamlit as st
import plotly.express as px

def engineer_dashboard(df):
    st.title("🛠 Engineer Dashboard - Server Drilldown")

    servers = df['ServerName'].unique()
    selected_server = st.selectbox("Select Server", servers)

    server_data = df[df['ServerName'] == selected_server]

    # Show server details
    st.subheader(f"Details for Server: {selected_server}")
    st.table(server_data[['ServerName','IP','OS_Version','Lifecycle','Compliance','Vulnerabilities']])

    # --- Visuals ---

    # 1️⃣ Patch Compliance Pie Chart
    compliance = server_data['Compliance'].values[0]
    compliance_chart = px.pie(
        names=["Patched","Missing"],
        values=[compliance, 100-compliance],
        title="Patch Compliance %"
    )
    st.plotly_chart(compliance_chart)

    # 2️⃣ Vulnerabilities Bar Chart
    vulns = server_data['Vulnerabilities'].values[0]
    severity = server_data['Severity'].values[0]  # assuming Severity column exists
    # For testing, you can split High/Medium/Low
    vulns_chart = px.bar(
        x=["High","Medium","Low"],
        y=[vulns if severity=="High" else 0,
           vulns if severity=="Medium" else 0,
           vulns if severity=="Low" else 0],
        labels={"x":"Severity","y":"Count"},
        title="Vulnerabilities by Severity"
    )
    st.plotly_chart(vulns_chart)

    # 3️⃣ Lifecycle Indicator
    lifecycle = server_data['Lifecycle'].values[0]
    st.info(f"Lifecycle Status: {lifecycle}")


