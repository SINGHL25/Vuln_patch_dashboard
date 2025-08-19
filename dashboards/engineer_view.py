
import streamlit as st

def engineer_dashboard(df):
    st.title("🛠 Engineer Dashboard - Server Drilldown")

    servers = df['ServerID'].unique()
    selected_server = st.selectbox("Select Server", servers)

    server_data = df[df['ServerID'] == selected_server]

    st.subheader(f"Details for Server: {selected_server}")
    st.table(server_data[['ServerName','IP','OS_Version','Lifecycle','Compliance','Vulnerabilities']])

