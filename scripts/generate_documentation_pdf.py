"""
ITC Hotels Project — Comprehensive File-by-File Documentation Generator
Outputs:
1. documentation/ITC_Hotels_Project_Complete_Documentation.html
2. documentation/ITC_Hotels_Project_Complete_Documentation.pdf
3. documentation/ITC_Hotels_Project_Complete_Documentation.md
"""

import os
import subprocess

BASE_DIR = "/home/goku/ITC_Hotels_Project"
DOCS_DIR = os.path.join(BASE_DIR, "documentation")
os.makedirs(DOCS_DIR, exist_ok=True)

HTML_PATH = os.path.join(DOCS_DIR, "ITC_Hotels_Project_Complete_Documentation.html")
PDF_PATH = os.path.join(DOCS_DIR, "ITC_Hotels_Project_Complete_Documentation.pdf")
MD_PATH = os.path.join(DOCS_DIR, "ITC_Hotels_Project_Complete_Documentation.md")

print("Generating Comprehensive Project Documentation...")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ITC Hotels Analytics — Complete Technical & File Documentation</title>
<style>
    @page {
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
        @bottom-right {
            content: counter(page);
        }
    }
    body {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        color: #1e293b;
        line-height: 1.55;
        font-size: 10pt;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }
    .cover {
        text-align: center;
        padding: 60px 20px 40px 20px;
        page-break-after: always;
        border-bottom: 4px solid #1e3a8a;
    }
    .university-header {
        font-size: 15pt;
        font-weight: 700;
        color: #1e3a8a;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .dept-sub {
        font-size: 11pt;
        color: #475569;
        margin-bottom: 30px;
    }
    .logo-badge {
        display: inline-block;
        padding: 8px 24px;
        background: #f1f5f9;
        border: 2px solid #cbd5e1;
        border-radius: 30px;
        font-size: 11pt;
        font-weight: 600;
        color: #0f172a;
        margin-bottom: 25px;
    }
    .project-title {
        font-size: 22pt;
        font-weight: 800;
        color: #0f172a;
        margin: 15px 0 10px 0;
        line-height: 1.25;
    }
    .project-subtitle {
        font-size: 13pt;
        color: #d97706;
        font-weight: 600;
        margin-bottom: 35px;
    }
    .meta-box {
        margin: 0 auto;
        max-width: 650px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 18px;
        text-align: left;
        display: flex;
        justify-content: space-between;
    }
    .meta-col h4 {
        margin: 0 0 8px 0;
        font-size: 10pt;
        color: #1e3a8a;
        text-transform: uppercase;
        border-bottom: 2px solid #cbd5e1;
        padding-bottom: 4px;
    }
    .meta-col p {
        margin: 3px 0;
        font-size: 9pt;
        color: #334155;
    }
    .session-tag {
        margin-top: 35px;
        font-size: 10pt;
        font-weight: 600;
        color: #64748b;
    }

    /* Headings */
    h1 {
        font-size: 17pt;
        color: #0f172a;
        border-bottom: 2px solid #1e3a8a;
        padding-bottom: 6px;
        margin-top: 26px;
        page-break-after: avoid;
    }
    h2 {
        font-size: 13pt;
        color: #1e3a8a;
        margin-top: 18px;
        margin-bottom: 8px;
        page-break-after: avoid;
        border-left: 4px solid #d97706;
        padding-left: 8px;
    }
    h3 {
        font-size: 11pt;
        color: #334155;
        margin-top: 14px;
        margin-bottom: 6px;
        page-break-after: avoid;
    }

    /* Cards & Callouts */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin: 14px 0;
    }
    .kpi-card {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-top: 3px solid #1e3a8a;
        border-radius: 6px;
        padding: 10px;
        text-align: center;
    }
    .kpi-card.gold { border-top-color: #d97706; }
    .kpi-card.green { border-top-color: #059669; }
    .kpi-card.blue { border-top-color: #0284c7; }
    .kpi-title {
        font-size: 7.5pt;
        font-weight: 700;
        text-transform: uppercase;
        color: #64748b;
    }
    .kpi-value {
        font-size: 13pt;
        font-weight: 800;
        color: #0f172a;
        margin: 4px 0;
    }
    .kpi-sub {
        font-size: 7pt;
        color: #059669;
        font-weight: 600;
    }

    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0 18px 0;
        font-size: 8.5pt;
        page-break-inside: auto;
    }
    tr {
        page-break-inside: avoid;
        page-break-after: auto;
    }
    thead {
        display: table-header-group;
    }
    th {
        background: #1e293b;
        color: #ffffff;
        text-align: left;
        padding: 7px 9px;
        font-weight: 600;
        font-size: 8pt;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    td {
        padding: 6px 9px;
        border-bottom: 1px solid #e2e8f0;
        vertical-align: top;
    }
    tr:nth-child(even) td {
        background-color: #f8fafc;
    }
    .file-name {
        font-family: 'Consolas', 'Courier New', monospace;
        font-weight: 700;
        color: #0f172a;
        font-size: 8.5pt;
    }
    .badge {
        display: inline-block;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 7pt;
        font-weight: 600;
        text-transform: uppercase;
    }
    .badge-code { background: #e0f2fe; color: #0369a1; }
    .badge-data { background: #fef3c7; color: #b45309; }
    .badge-db   { background: #dcfce7; color: #15803d; }
    .badge-doc  { background: #ede9fe; color: #6d28d9; }
    .badge-dash { background: #ffe4e6; color: #be123c; }

    .file-detail-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 12px 14px;
        margin-bottom: 14px;
        page-break-inside: avoid;
    }
    .file-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 6px;
        margin-bottom: 8px;
    }
    .file-path {
        font-family: 'Consolas', monospace;
        font-weight: 700;
        font-size: 10pt;
        color: #1e3a8a;
    }
    .desc-text {
        font-size: 9pt;
        color: #334155;
        margin: 4px 0 8px 0;
    }
    .specs-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        background: #f8fafc;
        padding: 8px 10px;
        border-radius: 4px;
        font-size: 8pt;
    }
    .specs-item strong {
        color: #475569;
        display: block;
        font-size: 7pt;
        text-transform: uppercase;
    }
    pre {
        background: #0f172a;
        color: #f8fafc;
        padding: 10px;
        border-radius: 5px;
        font-size: 8pt;
        font-family: 'Consolas', monospace;
        overflow-x: auto;
        margin: 8px 0;
        page-break-inside: avoid;
    }
    .page-break {
        page-break-after: always;
    }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="cover">
    <div class="university-header">Invertis University, Bareilly (U.P.)</div>
    <div class="dept-sub">Faculty of Computer Applications &bull; Department of BCA</div>
    
    <div class="logo-badge">🎓 FINAL YEAR CAPSTONE PROJECT DOCUMENTATION</div>
    
    <div class="project-title">ITC Hotels: Revenue &amp; Business Performance Analysis</div>
    <div class="project-subtitle">Complete Technical Architecture &amp; File-by-File Documentation Manual</div>
    
    <div class="meta-box">
        <div class="meta-col" style="width: 48%;">
            <h4>Submitted By:</h4>
            <p><strong>1. Jatin Sagar</strong> (Roll: 2311001156 | ID: BC2023727)</p>
            <p><strong>2. Atul Kumar</strong> (Roll: 2310201157 | ID: BC2023590)</p>
            <p><strong>3. Darshika Rathore</strong> (Roll: 2310101126 | ID: BC2023687)</p>
            <p><strong>4. Muskan Saxena</strong> (Roll: 2310201370 | ID: BC2023061)</p>
            <p><em>Lead Developer: Avi Singh (avisingh4121@gmail.com)</em></p>
        </div>
        <div class="meta-col" style="width: 48%;">
            <h4>Under The Guidance Of:</h4>
            <p><strong>Ms. Megha Saxena</strong><br>Assistant Professor<br>Faculty of Computer Applications</p>
            <h4 style="margin-top: 10px;">Academic Leadership:</h4>
            <p><strong>Dr. Akash Sanghi</strong> &mdash; Head of Department (HOD)</p>
            <p><strong>Prof. Manish Gupta</strong> &mdash; Dean, Invertis University</p>
        </div>
    </div>
    
    <div class="session-tag">
        Academic Session: [2025–26] &bull; Repository: https://github.com/Avis1229/ITC_HOTEL_S_MODULE
    </div>
</div>

<!-- ================= SECTION 1: EXECUTIVE SUMMARY ================= -->
<h1>1. Executive Summary &amp; Key Business Metrics</h1>
<p>
This project delivers a full-stack, enterprise-grade business intelligence and database system modeled around 
<strong>ITC Hotels</strong>, India's premier luxury chain renowned for its <em>Responsible Luxury</em> ethos. 
Analyzing <strong>119,390 historical reservations</strong> across luxury city hotels (<em>ITC Maurya, ITC Grand Chola</em>) 
and resorts (<em>ITC Grand Bharat, ITC Mughal</em>), the project bridges transactional relational database operations with 
advanced analytics across 4 core business domains.
</p>

<div class="kpi-grid">
    <div class="kpi-card gold">
        <div class="kpi-title">Gross Revenue</div>
        <div class="kpi-value">&#8377; 298.42 Cr</div>
        <div class="kpi-sub">&bull; 119k Total Bookings</div>
    </div>
    <div class="kpi-card green">
        <div class="kpi-title">Gross Operating Profit</div>
        <div class="kpi-value">&#8377; 143.68 Cr</div>
        <div class="kpi-sub">48.15% Margin (USALI)</div>
    </div>
    <div class="kpi-card blue">
        <div class="kpi-title">Average Daily Rate</div>
        <div class="kpi-value">&#8377; 8,941</div>
        <div class="kpi-sub">Per Room Night Realized</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-title">F&amp;B + Banquets</div>
        <div class="kpi-value">&#8377; 104.84 Cr</div>
        <div class="kpi-sub">Bukhara / Dum Pukht / MICE</div>
    </div>
</div>

<p>
The system completely replaces legacy, manual registers with a <strong>3NF Normalized Relational Database</strong> 
(18 tables &amp; views, 87,396 cleaned transactions), a transparent <strong>Python data cleaning &amp; exploratory data analysis (EDA) pipeline</strong> 
with high-resolution Matplotlib visualizations, a <strong>Master Microsoft Excel live dashboard</strong> with 5 tabs and square KPI cards, 
and an enterprise <strong>Power BI Direct SQL Integration Model</strong> with industry-standard DAX measures.
</p>

<!-- ================= SECTION 2: FILE DIRECTORY OVERVIEW ================= -->
<h1>2. Master Project File Directory &amp; Role Index</h1>
<p>Below is the complete inventory of all 42 files across the project workspace, categorized by operational role:</p>

<table>
    <thead>
        <tr>
            <th>Directory / File Path</th>
            <th>Type</th>
            <th>Primary Function &amp; Purpose</th>
        </tr>
    </thead>
    <tbody>
        <!-- Root -->
        <tr>
            <td class="file-name">README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Master GitHub landing page containing project abstract, team details, architecture diagram, and branch index.</td>
        </tr>
        <tr>
            <td class="file-name">PROJECT_SUBMISSION_CHECKLIST.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Academic evaluation rubric, viva defense questions, file inventory, and submission verification steps.</td>
        </tr>
        <tr>
            <td class="file-name">run_dashboard.sh</td>
            <td><span class="badge badge-code">Automation</span></td>
            <td>Interactive terminal launcher menu (Jupyter EDA, Plotly dashboard, Excel, SQLite shell, table verification).</td>
        </tr>
        <tr>
            <td class="file-name">push_all_to_github.sh</td>
            <td><span class="badge badge-code">Automation</span></td>
            <td>Bash automation script for configuring Git remotes and pushing all 5 isolated module branches to GitHub.</td>
        </tr>
        <tr>
            <td class="file-name">.gitignore</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Protects repository integrity by ignoring <code>.venv/</code>, Python bytecode, OS lock files, and raw dumps.</td>
        </tr>
        <!-- Archive -->
        <tr>
            <td class="file-name">archive/hotel_bookings.csv</td>
            <td><span class="badge badge-data">Raw Data</span></td>
            <td>Original Kaggle Hotel Booking Demand dataset (119,390 rows &times; 32 columns) used as the ingestion baseline.</td>
        </tr>
        <!-- Module 1 -->
        <tr>
            <td class="file-name">ITC-Room-Analytics/itc_room_revenue_occupancy.csv</td>
            <td><span class="badge badge-data">Curated Data</span></td>
            <td>Module 1 dataset (119k rows &times; 21 cols): room category mapping, ADR in INR, length of stay, lead times.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Room-Analytics/module1_room_revenue_occupancy.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Executed Module 1 analysis notebook: direct SQL database connection, RevPAR curves, category yield, Matplotlib charts.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Room-Analytics/README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Module 1 specification, academic headers, KPI summaries, and reproduction instructions.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Room-Analytics/requirements.txt</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Python dependencies for running Module 1 (pandas, numpy, matplotlib, seaborn).</td>
        </tr>
        <!-- Module 2 -->
        <tr>
            <td class="file-name">ITC-FnB-Analytics/itc_fnb_banquet_performance.csv</td>
            <td><span class="badge badge-data">Curated Data</span></td>
            <td>Module 2 dataset (119k rows &times; 17 cols): restaurant outlets (Bukhara, Dum Pukht), dining covers, banquet events.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-FnB-Analytics/module2_fnb_banquet_performance.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Executed Module 2 analysis notebook: SQL query loading, covers revenue, dining plan margins, banquet event yields.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-FnB-Analytics/README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Module 2 specification, culinary outlet benchmarks, and execution steps.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-FnB-Analytics/requirements.txt</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Python dependencies for running Module 2.</td>
        </tr>
        <!-- Module 3 -->
        <tr>
            <td class="file-name">ITC-Guest-Demographics/itc_guest_demographics_channels.csv</td>
            <td><span class="badge badge-data">Curated Data</span></td>
            <td>Module 3 dataset (119k rows &times; 22 cols): guest origin country, personas, Club ITC loyalty tiers, distribution channels.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Guest-Demographics/module3_guest_demographics_channels.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Executed Module 3 analysis notebook: SQL queries, channel risk analysis, repeat guest loyalty retention.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Guest-Demographics/README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Module 3 specification, customer segmentation overview, and run guide.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Guest-Demographics/requirements.txt</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Python dependencies for running Module 3.</td>
        </tr>
        <!-- Module 4 -->
        <tr>
            <td class="file-name">ITC-Profitability-Costs/itc_operating_costs_profitability.csv</td>
            <td><span class="badge badge-data">Curated Data</span></td>
            <td>Module 4 dataset (119k rows &times; 21 cols): USALI hotel P&L accounting, departmental COGS, staff payroll, utilities, GOP.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Profitability-Costs/module4_operating_costs_profitability.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Executed Module 4 notebook: SQL aggregation, USALI cost center breakdown, GOP margin benchmarking.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Profitability-Costs/README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Module 4 specification, USALI standard definitions, and KPI calculations.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Profitability-Costs/requirements.txt</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Python dependencies for running Module 4.</td>
        </tr>
        <!-- Final Dashboards -->
        <tr>
            <td class="file-name">ITC-Final-Dashboards/itc_hotel_analytics.db</td>
            <td><span class="badge badge-db">Database</span></td>
            <td>3NF Normalized SQLite enterprise database (81 MB, 18 tables &amp; views, 87,396 cleaned transactions).</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/itc_hotels_mysql_dump.sql</td>
            <td><span class="badge badge-db">Database</span></td>
            <td>Complete MySQL 8.0 DDL &amp; Data Dump script ready for instant import into XAMPP, phpMyAdmin, or cloud MySQL.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/itc_master_hospitality_data.csv</td>
            <td><span class="badge badge-data">Master Data</span></td>
            <td>Consolidated 74-column master dataset combining room, F&amp;B, banquet, demographics, and USALI financial metrics.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/data_cleaning_eda.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Comprehensive data cleaning pipeline &amp; Matplotlib EDA notebook with live SQL query integration.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/interactive_jupyter_dashboard.ipynb</td>
            <td><span class="badge badge-dash">Jupyter</span></td>
            <td>Interactive executive dashboard in Plotly Dark Theme featuring 5 tabs, 4 KPI cards, and waterfall charts.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx</td>
            <td><span class="badge badge-dash">Excel</span></td>
            <td>Master Microsoft Excel live dashboard featuring 5 bottom tabs, top square KPI cards, and native embedded charts.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/itc_luxury_theme.json</td>
            <td><span class="badge badge-code">Theme</span></td>
            <td>Official Power BI Dark Theme JSON preset styled with ITC luxury colors (Slate, Gold, Emerald, Ice Blue).</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/POWER_BI_SQL_INTEGRATION_GUIDE.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Comprehensive guide to connecting Power BI to the SQL database, Star Schema modeling, and official DAX measures.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/POWER_BI_MODELING_GUIDE.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Step-by-step layout guide for creating the 5 visual pages matching the university report screenshots.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/PROJECT_VIVA_PREPARATION.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>High-yield viva revision guide with expected technical and domain questions, answers, and formulas.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/README.md</td>
            <td><span class="badge badge-doc">Documentation</span></td>
            <td>Executive suite documentation overview, repository layout, and usage instructions.</td>
        </tr>
        <tr>
            <td class="file-name">ITC-Final-Dashboards/requirements.txt</td>
            <td><span class="badge badge-code">Config</span></td>
            <td>Dependencies for running the master dashboards (plotly, openpyxl, ipywidgets, matplotlib).</td>
        </tr>
        <!-- Scripts -->
        <tr>
            <td class="file-name">scripts/process_data.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>ETL pipeline converting raw Kaggle data into INR luxury context and generating the 4 module CSVs.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/create_database.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Cleans raw data (nulls, duplicates, outliers), constructs the 12 core 3NF tables, and populates SQLite.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/build_pdf_schema_and_mysql.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Adds PDF-matched tables (properties, rooms, bookings, inventory) and exports <code>itc_hotels_mysql_dump.sql</code>.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/generate_eda_notebook.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Generates the standalone <code>data_cleaning_eda.ipynb</code> notebook showing data cleaning and Matplotlib plots.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/generate_notebooks.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Builds all 4 module notebooks with SQL queries, Invertis academic headers, and Seaborn/Matplotlib plots.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/create_excel_dashboard.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Automates Openpyxl creation of the 5-sheet live Microsoft Excel executive dashboard with native charts.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/generate_jupyter_dashboard.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Generates the Plotly dark-themed interactive executive dashboard notebook with tabbed widgets.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/setup_git_and_readmes.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Configures git author information, initializes module repositories, and sets up branch structures.</td>
        </tr>
        <tr>
            <td class="file-name">scripts/update_readmes.py</td>
            <td><span class="badge badge-code">Script</span></td>
            <td>Synchronizes project team names, Invertis University metadata, and guide details across all README files.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<!-- ================= SECTION 3: FILE-BY-FILE DETAILED ANALYSIS ================= -->
<h1>3. File-by-File Technical Deep Dive</h1>

<!-- File 1: README.md -->
<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">1. README.md (Root Project Landing Page)</span>
        <span class="badge badge-doc">Documentation</span>
    </div>
    <div class="desc-text">
        The master entrypoint for the GitHub repository. It presents a comprehensive overview of the capstone project, 
        formally crediting the Invertis University student team and guide Ms. Megha Saxena. It features executive KPI highlights, 
        an interactive branch navigation table, an ASCII directory tree, database architectural highlights, and local quick-start instructions.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>File Size:</strong> 6.2 KB</div>
        <div class="specs-item"><strong>Language:</strong> Markdown (GFM)</div>
        <div class="specs-item"><strong>Audience:</strong> Evaluators, Recruiters, Faculty</div>
    </div>
</div>

<!-- File 2: PROJECT_SUBMISSION_CHECKLIST.md -->
<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">2. PROJECT_SUBMISSION_CHECKLIST.md</span>
        <span class="badge badge-doc">Academic Evaluation</span>
    </div>
    <div class="desc-text">
        Serves as an exhaustive self-audit checklist and evaluation guide for academic presentation. 
        It outlines the 4 analytical modules, summarizes core metrics, cross-references files with the university project report, 
        and details high-priority viva questions (e.g., USALI cost modeling, RevPAR formulas, star schema benefits, and data hygiene rules).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>File Size:</strong> 9.8 KB</div>
        <div class="specs-item"><strong>Key Focus:</strong> Viva Readiness &amp; Verification</div>
        <div class="specs-item"><strong>Sections:</strong> 7 Structured Evaluation Units</div>
    </div>
</div>

<!-- File 3: run_dashboard.sh -->
<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">3. run_dashboard.sh (Terminal Hub)</span>
        <span class="badge badge-code">Bash Shell Script</span>
    </div>
    <div class="desc-text">
        A menu-driven interactive terminal hub written in Bash. Designed specifically for the Ubuntu development environment, 
        it allows the user or examiner to launch any component with a single keystroke:
        (1) Launch Data Cleaning &amp; Matplotlib EDA in Jupyter; 
        (2) Launch Plotly Executive Dashboard; 
        (3) Open Excel Live Dashboard via LibreOffice/Excel; 
        (4) Open Interactive SQLite CLI Shell on <code>itc_hotel_analytics.db</code>; 
        (5) Display Real-time Table Record Counts across all 18 database entities.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Permissions:</strong> Executable (755)</div>
        <div class="specs-item"><strong>Interpreter:</strong> <code>/usr/bin/env bash</code></div>
        <div class="specs-item"><strong>Dependencies:</strong> python3, jupyter, sqlite3</div>
    </div>
</div>

<!-- File 4: push_all_to_github.sh -->
<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">4. push_all_to_github.sh</span>
        <span class="badge badge-code">Git Automation</span>
    </div>
    <div class="desc-text">
        Automates multi-module branch pushing to GitHub. When provided with the target GitHub username 
        (e.g., <code>./push_all_to_github.sh Avis1229</code>), it systematically iterates through all module directories, 
        attaches the appropriate remote origin URL, sets the default branch to <code>main</code>, and pushes isolated commits.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Permissions:</strong> Executable (755)</div>
        <div class="specs-item"><strong>Target Repo:</strong> <code>ITC_HOTEL_S_MODULE.git</code></div>
        <div class="specs-item"><strong>Error Handling:</strong> <code>set -e</code> Strict Mode</div>
    </div>
</div>

<!-- File 5: archive/hotel_bookings.csv -->
<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">5. archive/hotel_bookings.csv (Raw Master Data)</span>
        <span class="badge badge-data">CSV Dataset</span>
    </div>
    <div class="desc-text">
        The raw, unmodified benchmark Kaggle dataset containing 119,390 hotel booking records spanning 2015 to 2017. 
        It comprises 32 original attributes including arrival dates, lead times, customer segments, room types, ADR in Euros, 
        and cancellation flags. This file serves as the raw immutable ground truth from which all downstream pipelines derive.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Record Count:</strong> 119,390 rows &times; 32 cols</div>
        <div class="specs-item"><strong>File Size:</strong> 16.8 MB</div>
        <div class="specs-item"><strong>Origin:</strong> Kaggle (Jesse Mostipak)</div>
    </div>
</div>

<div class="page-break"></div>

<!-- Module 1 Files -->
<h2>3.1 Module 1: Room Revenue &amp; Occupancy Analytics (`ITC-Room-Analytics`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">6. ITC-Room-Analytics/itc_room_revenue_occupancy.csv</span>
        <span class="badge badge-data">Module Dataset</span>
    </div>
    <div class="desc-text">
        Cleaned transactional dataset specifically tailored for room revenue operations. 
        Raw ADR in Euros is transformed to INR (conversion factor &times; 85), room categories are mapped to authentic ITC suites 
        (<em>ITC One Luxury Room, Towers Club, Executive Suite, Presidential Suite</em>), and total stay nights are computed.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Dimensions:</strong> 119,390 rows &times; 21 cols</div>
        <div class="specs-item"><strong>Key Columns:</strong> adr_inr, room_revenue_inr, total_nights</div>
        <div class="specs-item"><strong>File Size:</strong> 22.1 MB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">7. ITC-Room-Analytics/module1_room_revenue_occupancy.ipynb</span>
        <span class="badge badge-dash">Jupyter Notebook</span>
    </div>
    <div class="desc-text">
        Executed diagnostic analytics notebook. It first executes a direct SQL query against 
        <code>itc_hotel_analytics.db</code> to retrieve reservations and invoices, performs dataset hygiene checks, 
        and generates publication-quality Seaborn and Matplotlib figures:
        (1) Room Revenue by Property Type (City Hotel vs Luxury Resort); 
        (2) ADR Distribution Boxplot; 
        (3) Revenue by Assigned Room Category; 
        (4) Monthly Demand &amp; Cancellation Seasonality Dual-Axis Curves.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution State:</strong> Fully Pre-Executed</div>
        <div class="specs-item"><strong>Visuals:</strong> Bar, Boxplot, Dual-Axis Line</div>
        <div class="specs-item"><strong>Output Size:</strong> 279 KB</div>
    </div>
</div>

<!-- Module 2 Files -->
<h2>3.2 Module 2: Food, Beverage &amp; Banquet Performance (`ITC-FnB-Analytics`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">8. ITC-FnB-Analytics/itc_fnb_banquet_performance.csv</span>
        <span class="badge badge-data">Module Dataset</span>
    </div>
    <div class="desc-text">
        Hospitality dining and banquet performance dataset. It models realistic covers and spending across 
        ITC's legendary signature restaurants (<em>Bukhara, Dum Pukht, Pavilion, Pan Asian, West View, Peshawri</em>) 
        and MICE venues (<em>The Grand Ballroom, Peacock Hall, Mughal Hall</em>). It separates food sales, beverage sales, 
        and banquet attendee yields.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Dimensions:</strong> 119,390 rows &times; 17 cols</div>
        <div class="specs-item"><strong>Key Outlets:</strong> Bukhara, Dum Pukht, Pavilion</div>
        <div class="specs-item"><strong>Total Portfolio Yield:</strong> &#8377; 104.84 Crores</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">9. ITC-FnB-Analytics/module2_fnb_banquet_performance.ipynb</span>
        <span class="badge badge-dash">Jupyter Notebook</span>
    </div>
    <div class="desc-text">
        Analyzes dining plan profitability and banquet event yields. Connects directly to SQLite via SQL 
        <code>JOIN</code> queries across <code>fnb_orders</code>, <code>reservations</code>, and <code>banquet_events</code>. 
        Visualizes food vs beverage breakdown by signature brand and revenue contribution by event type (Weddings vs Corporate Summits).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution State:</strong> Fully Pre-Executed</div>
        <div class="specs-item"><strong>Covers Analyzed:</strong> 121,438 covers</div>
        <div class="specs-item"><strong>Output Size:</strong> 165 KB</div>
    </div>
</div>

<div class="page-break"></div>

<!-- Module 3 Files -->
<h2>3.3 Module 3: Guest Demographics &amp; Booking Channels (`ITC-Guest-Demographics`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">10. ITC-Guest-Demographics/itc_guest_demographics_channels.csv</span>
        <span class="badge badge-data">Module Dataset</span>
    </div>
    <div class="desc-text">
        Focuses on guest acquisition and loyalty dynamics. Categorizes guest nationalities into macro geographic regions 
        (Europe, South Asia, Americas, Middle East), maps guest personas (Business/Solo, Family, Group/MICE), 
        and segments loyalty participation across Club ITC Silver, Gold, and Platinum tiers.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Dimensions:</strong> 119,390 rows &times; 22 cols</div>
        <div class="specs-item"><strong>Loyalty Tiers:</strong> Club ITC Platinum/Gold/Silver</div>
        <div class="specs-item"><strong>Channels:</strong> Direct, Corporate, OTA, GDS</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">11. ITC-Guest-Demographics/module3_guest_demographics_channels.ipynb</span>
        <span class="badge badge-dash">Jupyter Notebook</span>
    </div>
    <div class="desc-text">
        Diagnostic analysis evaluating channel acquisition costs and cancellation risks. 
        Demonstrates that third-party Online Travel Agencies (OTAs) carry a 41.6% cancellation rate and 15–18% commission leakage, 
        whereas direct Club ITC loyalists display under 12% cancellations, providing a strategic foundation for direct-booking promotions.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution State:</strong> Fully Pre-Executed</div>
        <div class="specs-item"><strong>Key Insights:</strong> Customer Acquisition Cost (CAC) vs Loyalty</div>
        <div class="specs-item"><strong>Output Size:</strong> 145 KB</div>
    </div>
</div>

<!-- Module 4 Files -->
<h2>3.4 Module 4: Operating Costs &amp; Profitability (`ITC-Profitability-Costs`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">12. ITC-Profitability-Costs/itc_operating_costs_profitability.csv</span>
        <span class="badge badge-data">Module Dataset</span>
    </div>
    <div class="desc-text">
        Full financial P&amp;L dataset conforming to the global <strong>USALI (Uniform System of Accounts for the Lodging Industry)</strong> framework. 
        Computes departmental expenses: room operations, F&amp;B cost of goods sold (COGS at 31%), distribution commissions, 
        LEED Platinum green energy/utility costs, staff payroll, property maintenance, and marketing expenses to derive Gross Operating Profit (GOP).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Dimensions:</strong> 119,390 rows &times; 21 cols</div>
        <div class="specs-item"><strong>Accounting Standard:</strong> USALI 11th Edition</div>
        <div class="specs-item"><strong>Calculated GOP:</strong> &#8377; 143.68 Crores (48.15%)</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">13. ITC-Profitability-Costs/module4_operating_costs_profitability.ipynb</span>
        <span class="badge badge-dash">Jupyter Notebook</span>
    </div>
    <div class="desc-text">
        Presents executive financial analytics. Uses SQL aggregation to compute GOPPAR (Gross Operating Profit Per Available Room), 
        depicts departmental cost distributions via horizontal bar charts, and models the profitability impact of ITC's on-site 
        wind and solar renewable energy investments.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution State:</strong> Fully Pre-Executed</div>
        <div class="specs-item"><strong>GOPPAR Realized:</strong> &#8377; 5,612 per room night</div>
        <div class="specs-item"><strong>Output Size:</strong> 83 KB</div>
    </div>
</div>

<div class="page-break"></div>

<!-- Final Suite Files -->
<h2>3.5 Master Dashboards &amp; Database Suite (`ITC-Final-Dashboards`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">14. ITC-Final-Dashboards/itc_hotel_analytics.db</span>
        <span class="badge badge-db">Relational Database</span>
    </div>
    <div class="desc-text">
        Production-grade SQLite 3NF relational database. Contains 18 tables and views, including 87,396 cleaned transactions 
        with all foreign keys, unique constraints, and high-performance B-tree indexes enabled. Houses both transactional tables 
        (<code>reservations, invoices, payments</code>) and Star Schema analytical entities (<code>bookings, room_inventory, calendar, properties</code>).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>File Size:</strong> 80.5 MB (Vacuumed)</div>
        <div class="specs-item"><strong>Table Count:</strong> 18 Tables &amp; Views</div>
        <div class="specs-item"><strong>Cleaned Records:</strong> 87,396 Bookings</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">15. ITC-Final-Dashboards/itc_hotels_mysql_dump.sql</span>
        <span class="badge badge-db">MySQL 8.0 Script</span>
    </div>
    <div class="desc-text">
        Complete standalone MySQL 8.0 DDL and sample data dump script. Formatted with <code>InnoDB</code> engine parameters, 
        foreign key definitions, and table structures exactly matching Figures D1 and D2 of the Invertis University project report. 
        Allows 1-click import into XAMPP, phpMyAdmin, or cloud MySQL instances.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Compatibility:</strong> MySQL 8.0 / MariaDB 10.4+</div>
        <div class="specs-item"><strong>Import Command:</strong> <code>mysql -u root &lt; dump.sql</code></div>
        <div class="specs-item"><strong>File Size:</strong> 87.6 KB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">16. ITC-Final-Dashboards/data_cleaning_eda.ipynb</span>
        <span class="badge badge-dash">Jupyter / Matplotlib</span>
    </div>
    <div class="desc-text">
        The core academic data engineering notebook. Step-by-step documentation of:
        (1) Null value detection and imputation; 
        (2) 31,994 duplicate removal; 
        (3) Anomaly resolution (negative ADR and extreme outliers capped via boxplots); 
        (4) Feature engineering; 
        (5) 7+ Matplotlib visualizations; 
        (6) Demonstration of live SQL aggregation queries using the Python <code>sqlite3</code> driver.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution State:</strong> Fully Pre-Executed with Plots</div>
        <div class="specs-item"><strong>Charts Embedded:</strong> 8 High-Res Figures</div>
        <div class="specs-item"><strong>Output Size:</strong> 591 KB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">17. ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx</span>
        <span class="badge badge-dash">Microsoft Excel</span>
    </div>
    <div class="desc-text">
        The official Master Live Excel Dashboard. Built following the professor's strict UI/UX criteria:
        Features <strong>5 bottom navigation tabs</strong>: <code>Room Analytics</code>, <code>FnB Analytics</code>, 
        <code>Demographics</code>, <code>Profitability</code>, and <code>Final</code>. 
        The <code>Final</code> sheet features 4 square executive KPI cards at the top (Total Revenue, Total Profit, Avg Occupancy, F&amp;B Sales) 
        and embedded native Excel charts formatted with currency symbols and auto-fitted columns.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Sheet Count:</strong> 5 Formatted Tabs</div>
        <div class="specs-item"><strong>Chart Engine:</strong> Native Openpyxl XML</div>
        <div class="specs-item"><strong>File Size:</strong> 19.5 KB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">18. ITC-Final-Dashboards/interactive_jupyter_dashboard.ipynb</span>
        <span class="badge badge-dash">Interactive Plotly</span>
    </div>
    <div class="desc-text">
        Interactive web-app style executive dashboard embedded in Jupyter Notebook. Uses Plotly Dark Theme to render 
        4 indicator KPI cards, an interactive Donut chart for room category mix, a USALI Waterfall chart depicting revenue-to-profit conversion, 
        and multi-bar seasonality curves.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Theme:</strong> Plotly Dark Luxury Palette</div>
        <div class="specs-item"><strong>Interactivity:</strong> Hover, Zoom, Pan, Toggle</div>
        <div class="specs-item"><strong>Output Size:</strong> 115 KB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">19. ITC-Final-Dashboards/POWER_BI_SQL_INTEGRATION_GUIDE.md</span>
        <span class="badge badge-doc">BI Architecture</span>
    </div>
    <div class="desc-text">
        Architectural documentation for connecting Power BI to the relational SQL database. 
        Specifies connection options (MySQL localhost, SQLite ODBC 64-bit, and direct Python query import), 
        the Star Schema relationship matrix (1-to-many cardinality), the complete repository of official DAX measures 
        (ADR, RevPAR, Occupancy %, Realisation %, DSRN, DURN, MoM &amp; WoW Growth), and blueprints for the 5 dashboard pages.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Measures Documented:</strong> 15+ Production DAX Formulas</div>
        <div class="specs-item"><strong>Diagrams:</strong> Star Schema Entity Map</div>
        <div class="specs-item"><strong>File Size:</strong> 11.2 KB</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">20. ITC-Final-Dashboards/itc_luxury_theme.json</span>
        <span class="badge badge-code">Power BI Theme</span>
    </div>
    <div class="desc-text">
        Custom JSON theme preset for Power BI Desktop. Configures the visual canvas with ITC's signature luxury color palette: 
        Deep Slate Background (<code>#0F172A</code>), Visual Card Fill (<code>#1E293B</code>), Imperial Gold Accent (<code>#D4AF37</code>), 
        Emerald Profit Green (<code>#10B981</code>), and Sky Blue (<code>#38BDF8</code>).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Usage:</strong> View &rarr; Themes &rarr; Browse for themes</div>
        <div class="specs-item"><strong>Format:</strong> Power BI Theme JSON Specification</div>
        <div class="specs-item"><strong>File Size:</strong> 1.0 KB</div>
    </div>
</div>

<div class="page-break"></div>

<!-- Pipeline Scripts -->
<h2>3.6 Backend Pipeline &amp; Code Generation Scripts (`scripts/`)</h2>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">21. scripts/process_data.py</span>
        <span class="badge badge-code">Python ETL Script</span>
    </div>
    <div class="desc-text">
        The primary data engineering ETL script. Ingests raw <code>archive/hotel_bookings.csv</code>, performs currency conversion, 
        derives realistic F&amp;B and banquet records, applies the USALI operating expense model, and splits the data into 
        the 4 module CSV files and the 74-column master dataset.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Input:</strong> archive/hotel_bookings.csv</div>
        <div class="specs-item"><strong>Outputs:</strong> 4 Module CSVs + 1 Master CSV</div>
        <div class="specs-item"><strong>Execution Time:</strong> ~4.8 seconds</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">22. scripts/create_database.py</span>
        <span class="badge badge-code">Python Database Builder</span>
    </div>
    <div class="desc-text">
        Constructs the Third Normal Form (3NF) relational database. Performs data cleaning (missing values, 31k duplicates removed, 
        outlier capping), creates 12 relational tables with foreign keys and unique constraints, and computes monthly aggregated 
        KPIs in the <code>kpi_monthly</code> table using pure SQL aggregation.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Database Engine:</strong> Python SQLite3</div>
        <div class="specs-item"><strong>Output File:</strong> itc_hotel_analytics.db</div>
        <div class="specs-item"><strong>Record Ingestion:</strong> 87,396 Transactions</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">23. scripts/build_pdf_schema_and_mysql.py</span>
        <span class="badge badge-code">Python Schema Alignment</span>
    </div>
    <div class="desc-text">
        Aligns the database schema directly with the university report appendices (Figures D1, D2, and B1). 
        Creates indexes on <code>booking_id</code> for sub-second query performance, populates <code>properties, rooms, calendar, bookings, room_inventory</code>, 
        and generates the production-ready <code>itc_hotels_mysql_dump.sql</code> script for MySQL/phpMyAdmin.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Execution Speed:</strong> 0.39 seconds (Optimized indexed JOINs)</div>
        <div class="specs-item"><strong>Output Files:</strong> itc_hotels_mysql_dump.sql, SQLite tables</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">24. scripts/create_excel_dashboard.py</span>
        <span class="badge badge-code">Python Excel Builder</span>
    </div>
    <div class="desc-text">
        Leverages the <code>openpyxl</code> library to programmatically generate the 5-sheet live Microsoft Excel dashboard. 
        It writes structured KPI tables, formats cells with Indian Rupee currency styling (<code>&#8377;</code>), computes formulas, 
        and embeds native Excel Bar, Column, and Line chart XML objects into the workbook without requiring Microsoft Office.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Library:</strong> openpyxl</div>
        <div class="specs-item"><strong>Output File:</strong> ITC_Executive_Live_Dashboard.xlsx</div>
        <div class="specs-item"><strong>Automation:</strong> 100% Code Generated</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">25. scripts/generate_eda_notebook.py</span>
        <span class="badge badge-code">Python Notebook Generator</span>
    </div>
    <div class="desc-text">
        Generates the standalone <code>data_cleaning_eda.ipynb</code> notebook JSON structure. 
        Configures cells for null imputation, duplicate detection, boxplot outlier capping, and 7 Matplotlib charts, 
        ensuring strict compatibility with Matplotlib 3.9+ (using <code>tick_labels</code> instead of deprecated parameters).
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Output:</strong> data_cleaning_eda.ipynb</div>
        <div class="specs-item"><strong>Execution Engine:</strong> jupyter nbconvert</div>
    </div>
</div>

<div class="file-detail-box">
    <div class="file-header">
        <span class="file-path">26. scripts/generate_notebooks.py</span>
        <span class="badge badge-code">Python Notebook Generator</span>
    </div>
    <div class="desc-text">
        Generates the 4 individual module Jupyter Notebooks. Automatically injects Invertis University metadata, 
        student team roll numbers, guide credentials, direct SQL query logic via <code>sqlite3</code>, and Seaborn/Matplotlib 
        plotting code into each module repository.
    </div>
    <div class="specs-grid">
        <div class="specs-item"><strong>Targets:</strong> Modules 1, 2, 3, and 4</div>
        <div class="specs-item"><strong>Integrity:</strong> Embedded SQL + Pandas + Matplotlib</div>
    </div>
</div>

<div class="page-break"></div>

<!-- ================= SECTION 4: RELATIONAL DATABASE & 3NF SCHEMA ================= -->
<h1>4. Relational Database Architecture &amp; 3NF Normalization</h1>
<p>
The database for the ITC Hotels Analytics suite conforms to <strong>Third Normal Form (3NF)</strong>, 
ensuring zero data redundancy and full referential integrity enforced via foreign keys:
</p>

<table>
    <thead>
        <tr>
            <th>Table / Entity Name</th>
            <th>Type</th>
            <th>Row Count</th>
            <th>Key Attributes &amp; Relationships</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="file-name">properties</td>
            <td>Dimension</td>
            <td>5</td>
            <td><code>property_id (PK)</code>, property_name, category, city. Defines ITC luxury hotels.</td>
        </tr>
        <tr>
            <td class="file-name">rooms</td>
            <td>Dimension</td>
            <td>5</td>
            <td><code>room_id (PK)</code>, room_class (Standard, Elite, Premium, Presidential, Luxury).</td>
        </tr>
        <tr>
            <td class="file-name">room_types</td>
            <td>Dimension</td>
            <td>11</td>
            <td><code>room_type_id (PK)</code>, category_name, base_rate_inr, gst_rate_pct (12% / 18% slab).</td>
        </tr>
        <tr>
            <td class="file-name">calendar</td>
            <td>Dimension</td>
            <td>1,461</td>
            <td><code>date_val (PK)</code>, day_name, day_of_week, month_name, month_no, quarter, year_val.</td>
        </tr>
        <tr>
            <td class="file-name">hotels</td>
            <td>Dimension</td>
            <td>2</td>
            <td><code>hotel_id (PK)</code>, hotel_name, hotel_type (City / Resort), location, total_rooms.</td>
        </tr>
        <tr>
            <td class="file-name">staff</td>
            <td>Dimension</td>
            <td>10</td>
            <td><code>staff_id (PK)</code>, name, role, department, hotel_name (FK), salary_inr.</td>
        </tr>
        <tr>
            <td class="file-name">users</td>
            <td>Dimension</td>
            <td>5</td>
            <td><code>user_id (PK)</code>, username, role (Admin, Manager, Receptionist), staff_id (FK).</td>
        </tr>
        <tr>
            <td class="file-name">bookings</td>
            <td>Fact (Analytics)</td>
            <td>87,396</td>
            <td><code>booking_id (PK)</code>, property_id (FK), check_in_date (FK), room_category, status, revenue.</td>
        </tr>
        <tr>
            <td class="file-name">room_inventory</td>
            <td>Fact (Capacity)</td>
            <td>9,170</td>
            <td><code>(property_id, check_in_date, room_category) (Composite PK)</code>, successful_bookings, capacity.</td>
        </tr>
        <tr>
            <td class="file-name">reservations</td>
            <td>Fact (Core)</td>
            <td>87,396</td>
            <td><code>reservation_id (PK)</code>, booking_id (UQ), hotel_name (FK), arrival_date, is_canceled, lead_time.</td>
        </tr>
        <tr>
            <td class="file-name">guests</td>
            <td>Fact (Demographic)</td>
            <td>87,396</td>
            <td><code>guest_id (PK)</code>, booking_id (FK), country_code, region, persona, loyalty_tier.</td>
        </tr>
        <tr>
            <td class="file-name">invoices</td>
            <td>Fact (Financial)</td>
            <td>87,396</td>
            <td><code>invoice_id (PK)</code>, booking_id (FK UQ), adr_inr, room_revenue, fnb_revenue, gross_revenue.</td>
        </tr>
        <tr>
            <td class="file-name">fnb_orders</td>
            <td>Fact (Dining)</td>
            <td>87,396</td>
            <td><code>order_id (PK)</code>, booking_id (FK), restaurant_outlet, dining_covers, food_revenue, beverage_revenue.</td>
        </tr>
        <tr>
            <td class="file-name">banquet_events</td>
            <td>Fact (MICE)</td>
            <td>69,679</td>
            <td><code>event_id (PK)</code>, booking_id (FK), banquet_hall, event_type, attendees, banquet_revenue_inr.</td>
        </tr>
        <tr>
            <td class="file-name">operating_costs</td>
            <td>Fact (USALI)</td>
            <td>87,396</td>
            <td><code>cost_id (PK)</code>, booking_id (FK), rooms_cost, fnb_cogs, energy_cost, payroll, expenses, GOP.</td>
        </tr>
        <tr>
            <td class="file-name">payments</td>
            <td>Fact (Billing)</td>
            <td>63,371</td>
            <td><code>payment_id (PK)</code>, booking_id (FK), payment_method (UPI, Card, Cash), amount_paid, status.</td>
        </tr>
        <tr>
            <td class="file-name">kpi_monthly</td>
            <td>Aggregate</td>
            <td>26</td>
            <td><code>kpi_id (PK)</code>, year, month, occupancy_rate_pct, adr_inr, revpar_inr, gross_revenue, GOP, margin.</td>
        </tr>
    </tbody>
</table>

<!-- ================= SECTION 5: DATA CLEANING PIPELINE ================= -->
<h1>5. Data Cleaning &amp; Preprocessing Pipeline</h1>
<p>
To ensure strict academic rigor, the data cleaning pipeline was executed in Python and recorded in 
<code>ITC-Final-Dashboards/data_cleaning_eda.ipynb</code>:
</p>
<table>
    <thead>
        <tr>
            <th>Cleaning Stage</th>
            <th>Raw Condition</th>
            <th>Methodology Applied</th>
            <th>Records Corrected</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Missing Children</strong></td>
            <td>4 null entries in <code>children</code></td>
            <td>Imputed with <code>0</code> (assumed solo/couple traveler without children).</td>
            <td>4 records</td>
        </tr>
        <tr>
            <td><strong>Missing Country</strong></td>
            <td>488 null entries in <code>country</code></td>
            <td>Imputed with <code>'Unknown'</code> to preserve reservation financial totals.</td>
            <td>488 records</td>
        </tr>
        <tr>
            <td><strong>String 'NULL' Flags</strong></td>
            <td>128,933 string 'NULL' tokens in <code>agent</code> &amp; <code>company</code></td>
            <td>Replaced with proper IEEE <code>np.nan</code> values for correct SQL null handling.</td>
            <td>128,933 cells</td>
        </tr>
        <tr>
            <td><strong>Duplicate Transactions</strong></td>
            <td>31,994 identical duplicate rows</td>
            <td>Removed via <code>df.drop_duplicates()</code>, reducing dataset to 87,396 unique stays.</td>
            <td>31,994 rows removed</td>
        </tr>
        <tr>
            <td><strong>Negative ADR Error</strong></td>
            <td>1 transaction with ADR &lt; 0</td>
            <td>Data entry error replaced with column median (&#8377; 8,075 / &euro;95).</td>
            <td>1 record</td>
        </tr>
        <tr>
            <td><strong>Extreme Outliers</strong></td>
            <td>1 booking with ADR &gt; &euro;5,000/night</td>
            <td>Capped at &euro;5,000 threshold to prevent artificial skewing of variance.</td>
            <td>1 record</td>
        </tr>
        <tr>
            <td><strong>Date Synthesizing</strong></td>
            <td>Split into year, month, day columns</td>
            <td>Synthesized into ISO-8601 <code>YYYY-MM-DD</code> format for temporal SQL indexing.</td>
            <td>All 87,396 records</td>
        </tr>
        <tr>
            <td><strong>Currency Harmonization</strong></td>
            <td>Historical ADR quoted in Euros</td>
            <td>Converted to Indian National Rupee (INR) via standard baseline factor &times; 85.</td>
            <td>All 87,396 records</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<!-- ================= SECTION 6: THE 3 DASHBOARDS ================= -->
<h1>6. The 3 Final Dashboards &amp; Visual Architectures</h1>

<h2>6.1 Dashboard 1: Microsoft Excel Live Executive Dashboard (`.xlsx`)</h2>
<ul>
    <li><strong>File:</strong> <code>ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx</code></li>
    <li><strong>Architecture:</strong> Exactly 5 bottom tabs matching the professor's requirement:
        <code>Room Analytics</code>, <code>FnB Analytics</code>, <code>Demographics</code>, <code>Profitability</code>, and <code>Final</code>.
    </li>
    <li><strong>Executive KPI Cards:</strong> The <code>Final</code> tab highlights 4 square cards at the top:
        <strong>Total Revenue (&#8377; 298.42 Cr)</strong>, 
        <strong>Total Profit / GOP (&#8377; 143.68 Cr)</strong>, 
        <strong>Avg Occupancy (62.9%)</strong>, and 
        <strong>F&amp;B + Banquet Sales (&#8377; 104.84 Cr)</strong>.
    </li>
    <li><strong>Visuals:</strong> Native Openpyxl XML chart objects (Column charts for seasonality, Bar charts for room yield, Line charts for trend lines).</li>
</ul>

<h2>6.2 Dashboard 2: Jupyter Notebook Matplotlib &amp; Plotly Analytics Suite</h2>
<ul>
    <li><strong>Files:</strong> <code>ITC-Final-Dashboards/data_cleaning_eda.ipynb</code> &amp; <code>interactive_jupyter_dashboard.ipynb</code></li>
    <li><strong>Matplotlib Visualizations:</strong> Boxplots of ADR by room category, dual-axis bar and line plots for monthly cancellations, horizontal bar charts for country distribution, and Year &times; Month revenue heatmaps.</li>
    <li><strong>Interactive Plotly Elements:</strong> USALI Waterfall chart visualizing Gross Revenue &rarr; Departmental Costs &rarr; Gross Operating Profit (GOP).</li>
</ul>

<h2>6.3 Dashboard 3: Microsoft Power BI Desktop (Connected to SQL Database)</h2>
<ul>
    <li><strong>Files:</strong> <code>POWER_BI_SQL_INTEGRATION_GUIDE.md</code> &amp; <code>itc_luxury_theme.json</code></li>
    <li><strong>Connection Engine:</strong> Connects directly to MySQL (<code>itc_hotels_db</code>) or SQLite ODBC (<code>itc_hotel_analytics.db</code>).</li>
    <li><strong>Star Schema Model:</strong> 1-to-many relationships connecting <code>dim_properties</code>, <code>dim_rooms</code>, and <code>dim_calendar</code> to <code>fact_bookings</code> and <code>fact_room_inventory</code>.</li>
    <li><strong>DAX Formulas Implemented:</strong>
        <pre><code>-- Occupancy Rate %
Occupancy % = DIVIDE(SUM(room_inventory[successful_bookings]), SUM(room_inventory[capacity]), 0)

-- Average Daily Rate (ADR)
ADR = DIVIDE([Total Revenue Realized], [Total Successful Bookings], 0)

-- Revenue Per Available Room (RevPAR)
RevPAR = DIVIDE([Total Revenue Realized], [Total Capacity], 0)

-- Realisation Rate %
Realisation % = DIVIDE([Total Revenue Realized], [Total Revenue Generated], 0)</code></pre>
    </li>
</ul>

<!-- ================= SECTION 7: VIVA & EXECUTION INSTRUCTIONS ================= -->
<h1>7. System Execution &amp; Viva Defense Guide</h1>

<h2>7.1 Quick Launch Commands on Ubuntu</h2>
<pre><code># 1. Navigate to Project Root
cd /home/goku/ITC_Hotels_Project

# 2. Launch Interactive Terminal Hub
./run_dashboard.sh

# 3. Quick Database Inspection via SQLite CLI
sqlite3 ITC-Final-Dashboards/itc_hotel_analytics.db "SELECT count(*) FROM bookings;"

# 4. View Git Branch Structure
git branch -a</code></pre>

<h2>7.2 High-Yield Viva Q&amp;A Defense Points</h2>
<p>
<strong>Q1: Why did you split the Kaggle dataset into 4 separate module repositories?</strong><br>
<em>Answer:</em> In enterprise hospitality environments, room revenue, culinary operations, guest CRM, and corporate accounting operate under distinct business units. Modularizing into separate repositories enforces domain separation of concerns, enables independent versioning, and complies directly with the faculty's project requirements.
</p>

<p>
<strong>Q2: Why use a 3NF Relational Database instead of querying a single flat CSV file?</strong><br>
<em>Answer:</em> A flat CSV incurs massive data redundancy, lacks foreign key integrity constraints, and slows analytical query performance. Our 3NF schema separates dimensions (Hotels, Rooms, Calendar) from transactional facts (Bookings, Invoices, Orders), eliminating update anomalies and allowing Power BI to utilize lightning-fast Star Schema 1-to-many relationships.
</p>

<p>
<strong>Q3: How is ITC's 'Responsible Luxury' reflected in the financial USALI module?</strong><br>
<em>Answer:</em> ITC Hotels is the first hotel chain globally to have all its luxury properties LEED Platinum certified. In Module 4, on-site solar and wind renewable generation caps energy/utility costs at 4.2% of revenue compared to the industry average of 8–10%, directly expanding the Gross Operating Profit (GOP) margin to a superior 48.15%.
</p>

<div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #cbd5e1; font-size: 8pt; color: #64748b;">
    &copy; 2025–26 Faculty of Computer Applications, Invertis University, Bareilly (U.P.) &bull; ITC Hotels Analytics Project
</div>

</body>
</html>
"""

with open(HTML_PATH, "w") as f:
    f.write(html_content)
print(f"✅ HTML documentation written: {HTML_PATH}")

# Convert HTML to PDF using Chrome Headless
print("Converting HTML to PDF via Google Chrome Headless...")
cmd = [
    "google-chrome",
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={PDF_PATH}",
    HTML_PATH
]

try:
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    pdf_size = os.path.getsize(PDF_PATH)
    print(f"✅ PDF successfully generated: {PDF_PATH} ({pdf_size / (1024*1024):.2f} MB)")
except Exception as e:
    print(f"Error compiling PDF: {e}")

# Also generate clean Markdown version
print("Generating Markdown documentation...")
md_content = """# 🏨 ITC Hotels: Revenue & Business Performance Analysis
## Complete Technical Architecture & File-by-File Documentation Manual
**Invertis University, Bareilly (U.P.)** | Faculty of Computer Applications  
**Bachelor of Computer Applications (BCA) — Final Year Capstone Project [Session 2025–26]**

---

### 👨‍🎓 Project Team & Guidance
- **Jatin Sagar** (Student ID: BC2023727, Roll No: 2311001156) &mdash; Data Engineering & SQL Schema
- **Atul Kumar** (Student ID: BC2023590, Roll No: 2310201157) &mdash; Financial & USALI Modeling
- **Darshika Rathore** (Student ID: BC2023687, Roll No: 2310101126) &mdash; F&B & Banquet Analytics
- **Muskan Saxena** (Student ID: BC2023061, Roll No: 2310201370) &mdash; Guest Demographics & Retention
- *Lead Developer:* Avi Singh (`avisingh4121@gmail.com`)
- **Project Guide:** Ms. Megha Saxena, Assistant Professor, Faculty of Computer Applications
- **Head of Department (HOD):** Dr. Akash Sanghi
- **Dean:** Prof. Manish Gupta
- **Official GitHub Repository:** [https://github.com/Avis1229/ITC_HOTEL_S_MODULE](https://github.com/Avis1229/ITC_HOTEL_S_MODULE)

---

## 1. Executive Summary & Key Performance Indicators (KPIs)

Analyzing **119,390 historical reservations** across luxury city hotels (*ITC Maurya, ITC Grand Chola*) and resorts (*ITC Grand Bharat, ITC Mughal*), the project delivers:
- **Gross Realized Portfolio Revenue:** **₹ 298.42 Crores**
- **Gross Operating Profit (GOP / EBITDA):** **₹ 143.68 Crores** (**48.15% Margin**)
- **Average Daily Rate (ADR):** **₹ 8,941 per room night**
- **Average Occupancy Rate:** **62.9% confirmed stays** (75,166 stays)
- **GOPPAR (GOP per Billed Room Night):** **₹ 5,612** (Industry benchmark ₹ 4,200)
- **Culinary & Banquet Sales:** **₹ 104.84 Crores** (35.1% of revenue mix)

---

## 2. Master Project File Directory & Role Index

| Directory / File Path | Type | Primary Function & Purpose |
|-----------------------|------|----------------------------|
| `README.md` | Doc | Master GitHub landing page with team credentials, KPIs, and branch index. |
| `PROJECT_SUBMISSION_CHECKLIST.md` | Doc | Academic evaluation rubric, viva defense questions, and file verification. |
| `run_dashboard.sh` | Shell | Interactive terminal hub (Jupyter EDA, Plotly, Excel, SQLite CLI). |
| `push_all_to_github.sh` | Shell | Automated multi-branch push script to GitHub. |
| `.gitignore` | Config | Protects repository by ignoring `.venv/`, bytecode, and checkpoints. |
| `archive/hotel_bookings.csv` | Raw Data | Original Kaggle dataset (119,390 rows × 32 columns). |
| `ITC-Room-Analytics/itc_room_revenue_occupancy.csv` | Data | Module 1 dataset (119k rows × 21 cols): room category mapping, ADR in INR. |
| `ITC-Room-Analytics/module1_room_revenue_occupancy.ipynb` | Notebook | Executed Module 1 notebook with direct SQL database connection and Matplotlib charts. |
| `ITC-Room-Analytics/README.md` | Doc | Module 1 documentation and execution steps. |
| `ITC-Room-Analytics/requirements.txt` | Config | Python dependencies for Module 1. |
| `ITC-FnB-Analytics/itc_fnb_banquet_performance.csv` | Data | Module 2 dataset (119k rows × 17 cols): Bukhara, Dum Pukht, Grand Ballroom. |
| `ITC-FnB-Analytics/module2_fnb_banquet_performance.ipynb` | Notebook | Executed Module 2 notebook: SQL query loading, covers revenue, banquet yields. |
| `ITC-FnB-Analytics/README.md` | Doc | Module 2 documentation and culinary benchmarks. |
| `ITC-FnB-Analytics/requirements.txt` | Config | Python dependencies for Module 2. |
| `ITC-Guest-Demographics/itc_guest_demographics_channels.csv` | Data | Module 3 dataset (119k rows × 22 cols): origin, personas, Club ITC tiers. |
| `ITC-Guest-Demographics/module3_guest_demographics_channels.ipynb` | Notebook | Executed Module 3 notebook: SQL queries, channel risk, repeat guest loyalty. |
| `ITC-Guest-Demographics/README.md` | Doc | Module 3 documentation and customer segmentation. |
| `ITC-Guest-Demographics/requirements.txt` | Config | Python dependencies for Module 3. |
| `ITC-Profitability-Costs/itc_operating_costs_profitability.csv` | Data | Module 4 dataset (119k rows × 21 cols): USALI hotel P&L accounting, GOP, GOPPAR. |
| `ITC-Profitability-Costs/module4_operating_costs_profitability.ipynb` | Notebook | Executed Module 4 notebook: SQL aggregation, USALI cost center breakdown. |
| `ITC-Profitability-Costs/README.md` | Doc | Module 4 documentation and USALI definitions. |
| `ITC-Profitability-Costs/requirements.txt` | Config | Python dependencies for Module 4. |
| `ITC-Final-Dashboards/itc_hotel_analytics.db` | DB | 3NF SQLite database (81 MB, 18 tables & views, 87,396 cleaned transactions). |
| `ITC-Final-Dashboards/itc_hotels_mysql_dump.sql` | DB | Complete MySQL 8.0 DDL & Data Dump ready for XAMPP / phpMyAdmin. |
| `ITC-Final-Dashboards/itc_master_hospitality_data.csv` | Data | Consolidated 74-column master dataset combining all module metrics. |
| `ITC-Final-Dashboards/data_cleaning_eda.ipynb` | Notebook | Comprehensive data cleaning pipeline & Matplotlib EDA with live SQL queries. |
| `ITC-Final-Dashboards/interactive_jupyter_dashboard.ipynb` | Notebook | Interactive executive dashboard in Plotly Dark Theme (5 tabs, 4 KPI cards). |
| `ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx` | Excel | Master Microsoft Excel live dashboard (5 bottom tabs, top square KPI cards). |
| `ITC-Final-Dashboards/itc_luxury_theme.json` | Theme | Power BI Dark Theme JSON preset styled with ITC luxury colors. |
| `ITC-Final-Dashboards/POWER_BI_SQL_INTEGRATION_GUIDE.md` | Doc | Power BI SQL connection, Star Schema modeling, and DAX measures. |
| `ITC-Final-Dashboards/POWER_BI_MODELING_GUIDE.md` | Doc | Step-by-step layout guide for creating the 5 dashboard pages. |
| `ITC-Final-Dashboards/PROJECT_VIVA_PREPARATION.md` | Doc | High-yield viva revision guide with technical and domain questions/answers. |
| `ITC-Final-Dashboards/README.md` | Doc | Executive suite documentation overview and usage instructions. |
| `ITC-Final-Dashboards/requirements.txt` | Config | Dependencies for running the master dashboards. |
| `scripts/process_data.py` | Script | Ingests raw Kaggle data and generates the 4 module CSVs and master data. |
| `scripts/create_database.py` | Script | Cleans raw data and builds the 12 core 3NF tables in SQLite. |
| `scripts/build_pdf_schema_and_mysql.py` | Script | Adds PDF-matched tables and exports `itc_hotels_mysql_dump.sql`. |
| `scripts/generate_eda_notebook.py` | Script | Generates the standalone `data_cleaning_eda.ipynb` notebook. |
| `scripts/generate_notebooks.py` | Script | Builds all 4 module notebooks with SQL queries and Matplotlib plots. |
| `scripts/create_excel_dashboard.py` | Script | Builds the 5-sheet live Microsoft Excel executive dashboard. |
| `scripts/generate_jupyter_dashboard.py` | Script | Generates the Plotly dark-themed interactive executive dashboard notebook. |
| `scripts/setup_git_and_readmes.py` | Script | Configures git author information and initializes repositories. |
| `scripts/update_readmes.py` | Script | Synchronizes team names and university metadata across all README files. |

---

## 3. Relational Database Architecture (3NF Schema)

The SQLite database (`itc_hotel_analytics.db`) and MySQL dump (`itc_hotels_mysql_dump.sql`) feature 18 tables:
- **Dimension Tables:** `properties`, `rooms`, `calendar`, `room_types`, `hotels`, `staff`, `users`
- **Fact Tables:** `bookings` (87,396 records), `room_inventory` (Daily capacity & occupancy), `reservations`, `guests`, `invoices`, `fnb_orders`, `banquet_events`, `operating_costs`, `payments`
- **Aggregated Analytics:** `kpi_monthly` (Pre-calculated ADR, RevPAR, GOP, Margins)

---

## 4. The 3 Final Dashboards

1. **Microsoft Excel Live Dashboard (`.xlsx`):** 5 bottom tabs (`Room Analytics`, `FnB Analytics`, `Demographics`, `Profitability`, `Final`) with 4 square KPI cards and native charts.
2. **Jupyter Notebook Matplotlib & Plotly Analytics:** Complete data cleaning, missing value handling, outlier capping, and waterfall P&L.
3. **Microsoft Power BI Desktop (SQL Connected):** Direct connection via ODBC/MySQL to Star Schema tables with official DAX measures (`RevPAR`, `ADR`, `Occupancy %`, `Realisation %`).
"""

with open(MD_PATH, "w") as f:
    f.write(md_content)
print(f"✅ Markdown documentation written: {MD_PATH}")

print("\nAll documentation formats generated successfully!")
"""
with open("/home/goku/ITC_Hotels_Project/scripts/generate_documentation_pdf.py", "w") as f:
    f.write(code_str)
"""
