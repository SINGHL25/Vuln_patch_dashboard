# Vuln_patch_dashboard
Streamlit-ready setup with both Engineer and Management dashboards
# Vulnerability & Patch Dashboard

This is a Streamlit-based web application for monitoring server vulnerabilities, patch compliance, and lifecycle status across multiple servers (Windows 2012/2016/2022, etc.).

## Features
- Engineer view: Drill down per server for vulnerabilities, OS version, lifecycle, patches, compliance.
- Management view: High-level KPIs, vulnerable servers by severity, compliance %.
- Centralized view of multiple CSV reports: Qualys scan, patch report, lifecycle.

## Folder Structure
- `data/raw/` : CSV files (qualys_scan.csv, patch_report.csv, lifecycle.csv)
- `scripts/transform.py` : Load and merge all CSVs
- `dashboards/engineer_view.py` : Engineer dashboard UI
- `streamlit_app.py` : Main app
- `requirements.txt` : Python dependencies

## How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
