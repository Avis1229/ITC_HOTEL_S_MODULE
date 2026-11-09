# 🏨 ITC Hotels: Revenue & Business Performance Analysis
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
