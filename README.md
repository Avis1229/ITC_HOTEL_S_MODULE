# 🏨 ITC Hotels: Revenue & Business Performance Analysis
**Invertis University, Bareilly** | Faculty of Computer Applications  
**Bachelor of Computer Applications (BCA) — Final Year Capstone Project [2025–26]**

---

### 👨‍🎓 Project Team & Guidance
| Name | Student ID | Roll No | Role |
|------|------------|---------|------|
| **Jatin Sagar** | BC2023727 | 2311001156 | Data Engineering & SQL Schema |
| **Atul Kumar** | BC2023590 | 2310201157 | Financial & USALI Modeling |
| **Darshika Rathore** | BC2023687 | 2310101126 | F&B & Banquet Analytics |
| **Muskan Saxena** | BC2023061 | 2310201370 | Guest Demographics & Retention |

**Project Guide:** Ms. Megha Saxena, Assistant Professor, Invertis University, Bareilly  
**Head of Department (HOD):** Dr. Akash Sanghi  
**Dean:** Prof. Manish Gupta

---

## 📌 Executive Summary
ITC Hotels is one of India's premier luxury hospitality chains, known for its *Responsible Luxury* ethos. This project implements an enterprise-grade analytics suite and relational database system evaluating **119,390 reservations** across flagship luxury properties (*ITC Maurya, ITC Grand Chola, ITC Grand Bharat, and ITC Mughal*).

### 🏆 Key Business Performance Metrics (KPIs)
- **Gross Realized Portfolio Revenue:** **₹ 298.42 Crores**
- **Gross Operating Profit (GOP / EBITDA):** **₹ 143.68 Crores** (**48.15% Margin**)
- **Average Daily Rate (ADR):** **₹ 8,941 per room night**
- **Average Occupancy Rate:** **62.9% confirmed stays** (75,166 stays)
- **GOPPAR (GOP per Billed Room Night):** **₹ 5,612** (vs industry benchmark ₹ 4,200)
- **Culinary & Banquet Sales:** **₹ 104.84 Crores** (35.1% of revenue mix)

---

## 🏗️ Project Architecture & Repository Branches

This repository is organized both as a consolidated master project on `main` and as modular isolated branches:

| Module | Focus Area | Dedicated Branch | Folder |
|--------|------------|------------------|--------|
| **Module 1** | Room Revenue & Occupancy | [`module-1-room-analytics`](https://github.com/Avis1229/ITC_HOTEL_S_MODULE/tree/module-1-room-analytics) | `ITC-Room-Analytics/` |
| **Module 2** | Food, Beverage & Banquets | [`module-2-fnb-analytics`](https://github.com/Avis1229/ITC_HOTEL_S_MODULE/tree/module-2-fnb-analytics) | `ITC-FnB-Analytics/` |
| **Module 3** | Guest Demographics & Channels | [`module-3-guest-demographics`](https://github.com/Avis1229/ITC_HOTEL_S_MODULE/tree/module-3-guest-demographics) | `ITC-Guest-Demographics/` |
| **Module 4** | Operating Costs & Profitability | [`module-4-profitability-costs`](https://github.com/Avis1229/ITC_HOTEL_S_MODULE/tree/module-4-profitability-costs) | `ITC-Profitability-Costs/` |
| **Final Suite** | Executive Dashboards & SQL Database | [`module-5-final-dashboards`](https://github.com/Avis1229/ITC_HOTEL_S_MODULE/tree/module-5-final-dashboards) | `ITC-Final-Dashboards/` |

---

## 📁 Repository Directory Structure

```text
ITC_HOTEL_S_MODULE/
│
├── README.md                                  # Master Project Documentation
├── PROJECT_SUBMISSION_CHECKLIST.md            # Comprehensive viva & submission guide
├── run_dashboard.sh                           # Interactive terminal hub & launcher
│
├── ITC-Room-Analytics/                        # [Module 1]
│   ├── itc_room_revenue_occupancy.csv         # Room transactional dataset
│   ├── module1_room_revenue_occupancy.ipynb   # Executed Jupyter analysis (SQL + Matplotlib)
│   └── README.md
│
├── ITC-FnB-Analytics/                         # [Module 2]
│   ├── itc_fnb_banquet_performance.csv        # Bukhara, Dum Pukht, Grand Ballroom dataset
│   ├── module2_fnb_banquet_performance.ipynb  # Executed Jupyter analysis (SQL + Matplotlib)
│   └── README.md
│
├── ITC-Guest-Demographics/                    # [Module 3]
│   ├── itc_guest_demographics_channels.csv    # Origin, Personas, Club ITC, OTAs
│   ├── module3_guest_demographics_channels.ipynb
│   └── README.md
│
├── ITC-Profitability-Costs/                   # [Module 4]
│   ├── itc_operating_costs_profitability.csv  # USALI P&L, LEED Green Utilities, GOPPAR
│   ├── module4_operating_costs_profitability.ipynb
│   └── README.md
│
├── ITC-Final-Dashboards/                      # [Master Dashboards & Relational Database]
│   ├── itc_hotel_analytics.db                 # 3NF SQLite Database (18 tables, 87k rows)
│   ├── itc_hotels_mysql_dump.sql              # MySQL 8.0 DDL & Data Dump for XAMPP
│   ├── data_cleaning_eda.ipynb                # Data Cleaning Pipeline & Matplotlib Visuals
│   ├── interactive_jupyter_dashboard.ipynb    # Interactive Plotly Executive Dashboard
│   ├── ITC_Executive_Live_Dashboard.xlsx      # Master Live Excel Dashboard (5 sheets)
│   ├── itc_master_hospitality_data.csv        # Master Star-Schema Dataset
│   ├── itc_luxury_theme.json                  # Power BI Dark Luxury Theme
│   ├── POWER_BI_SQL_INTEGRATION_GUIDE.md      # Power BI SQL Connection & DAX Guide
│   └── PROJECT_VIVA_PREPARATION.md            # Viva questions & answers
│
└── scripts/                                   # Pipeline & database generation scripts
    ├── create_database.py                     # 3NF Schema & SQLite database builder
    ├── build_pdf_schema_and_mysql.py          # PDF-matched tables & MySQL dump exporter
    ├── generate_eda_notebook.py               # EDA & Matplotlib notebook builder
    ├── create_excel_dashboard.py              # Master Excel dashboard generator
    └── generate_notebooks.py                  # Module notebooks generator
```

---

## 🗄️ Relational Database (3NF Schema & Star Schema)

The project includes an **18-table relational database** normalized in Third Normal Form (3NF) according to Chapter 5.3 and Appendix B of the project report:
- **Dimension Tables:** `properties`, `rooms`, `calendar`, `room_types`, `staff`, `users`
- **Fact Tables:** `bookings` (87,396 records), `room_inventory` (Daily capacity & occupancy), `invoices`, `fnb_orders`, `banquet_events`, `operating_costs`, `payments`
- **Aggregated Analytics:** `kpi_monthly` (Pre-calculated ADR, RevPAR, GOP, Margins)

### Importing into MySQL / phpMyAdmin:
```bash
mysql -u root itc_hotels_db < ITC-Final-Dashboards/itc_hotels_mysql_dump.sql
```

---

## 📊 The 3 Final Dashboards

### 1. Microsoft Excel Live Dashboard (`.xlsx`)
- **Location:** `ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx`
- **5 Tabs:** `Room Analytics`, `FnB Analytics`, `Demographics`, `Profitability`, `Final`.
- **Top on Final Tab:** 4 Square KPI Cards (Total Revenue ₹298.42 Cr, Total Profit ₹143.68 Cr, Avg Occupancy 62.9%, F&B Sales ₹104.84 Cr).
- **Visuals:** Native embedded Excel Column, Bar, and Line charts.

### 2. Jupyter Notebook Data Cleaning & Interactive Dashboard
- **Data Cleaning & Matplotlib:** `ITC-Final-Dashboards/data_cleaning_eda.ipynb` (Nulls handling, duplicate removal, outlier capping, 7+ Matplotlib charts).
- **Interactive Plotly Suite:** `ITC-Final-Dashboards/interactive_jupyter_dashboard.ipynb` (Waterfall P&L, Donut share, KPI indicator cards).

### 3. Microsoft Power BI Desktop (Connected to SQL Database)
- **Integration Guide:** `ITC-Final-Dashboards/POWER_BI_SQL_INTEGRATION_GUIDE.md`
- **Features:** Direct connection to MySQL / SQLite ODBC, 1-to-many Star Schema relationships, official DAX measures (`RevPAR`, `ADR`, `Occupancy %`, `DSRN`, `DURN`, `WoW Growth`, `MoM Growth`).
- **Pages (Matching Appendices A.1-A.4):**
  - Page 1: Room Category Performance & Category Insights
  - Page 2: Occupancy & Capacity Analysis
  - Page 3: Cancellations & Lost Revenue Analysis
  - Page 4: Financial Overview & Performance
  - Page 5: Master Executive Dark Mode Overview

---

## 🚀 Quick Execution Guide

```bash
# Clone the repository
git clone https://github.com/Avis1229/ITC_HOTEL_S_MODULE.git
cd ITC_HOTEL_S_MODULE

# Launch interactive terminal hub
./run_dashboard.sh
```
