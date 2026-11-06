# ITC Hotels Analytics — Final Project Submission & Professor Review Checklist
### Master Documentation for Evaluation & Viva Presentation
**Author:** Avi Singh &bull; **University Capstone Project** &bull; **Dual-OS Workflow (Ubuntu Linux & Windows)**

---

## 📋 Table of Contents
1. [Executive Project Summary](#1-executive-project-summary)
2. [Folder & Repository Architecture](#2-folder--repository-architecture)
3. [The 4 Core Analytical Modules](#3-the-4-core-analytical-modules)
4. [The 3 Final Live Dashboards](#4-the-3-final-live-dashboards)
5. [Step-by-Step GitHub Push Guide](#5-step-by-step-github-push-guide)
6. [Power BI Desktop (Windows) 5-Minute Setup](#6-power-bi-desktop-windows-5-minute-setup)
7. [Viva & Technical Defense Q&A](#7-viva--technical-defense-qa)

---

## 1. Executive Project Summary

This project delivers an enterprise-grade analytics suite for **ITC Hotels**, evaluating **119,390 reservations** across premier properties:
- **ITC Maurya (New Delhi)** & **ITC Grand Chola (Chennai)** — Executive Luxury City Hotels.
- **ITC Grand Bharat (Gurugram)** & **ITC Mughal (Agra)** — Luxury Resorts & Spas.

### Top Executive KPIs:
- **Gross Realized Revenue:** **₹ 298.42 Crores**
- **Gross Operating Profit (GOP / EBITDA):** **₹ 143.68 Crores** (**48.15% Margin**)
- **Average Daily Rate (ADR):** **₹ 8,941 per room night**
- **Average Occupancy Rate:** **62.9% confirmed stays** (75,166 stays)
- **GOPPAR (GOP per Billed Room Night):** **₹ 5,612** (vs industry benchmark ₹ 4,200)
- **Culinary & Banquet Sales:** **₹ 104.84 Crores** (35.1% of revenue mix)

---

## 2. Folder & Repository Architecture

All code, data, and notebooks are organized into isolated module repositories:

```text
/home/goku/ITC_Hotels_Project/
│
├── push_all_to_github.sh                    # Automated 1-click GitHub push script
├── run_dashboard.sh                         # Interactive terminal dashboard launcher
├── PROJECT_SUBMISSION_CHECKLIST.md          # This complete evaluation guide
│
├── ITC-Room-Analytics/                      # [Module 1 Repo]
│   ├── itc_room_revenue_occupancy.csv       # Curated Room Dataset (119,390 rows)
│   ├── module1_room_revenue_occupancy.ipynb # Executed Jupyter Notebook
│   ├── README.md & requirements.txt
│   └── .git/ (branch: main)
│
├── ITC-FnB-Analytics/                       # [Module 2 Repo]
│   ├── itc_fnb_banquet_performance.csv      # Bukhara, Dum Pukht, Grand Ballroom Dataset
│   ├── module2_fnb_banquet_performance.ipynb# Executed Jupyter Notebook
│   ├── README.md & requirements.txt
│   └── .git/ (branch: main)
│
├── ITC-Guest-Demographics/                  # [Module 3 Repo]
│   ├── itc_guest_demographics_channels.csv  # Origin, Personas, Club ITC, OTAs
│   ├── module3_guest_demographics_channels.ipynb
│   ├── README.md & requirements.txt
│   └── .git/ (branch: main)
│
├── ITC-Profitability-Costs/                 # [Module 4 Repo]
│   ├── itc_operating_costs_profitability.csv# USALI P&L, LEED Green Utilities, GOPPAR
│   ├── module4_operating_costs_profitability.ipynb
│   ├── README.md & requirements.txt
│   └── .git/ (branch: main)
│
└── ITC-Final-Dashboards/                    # [Master Suite & 3 Final Dashboards]
    ├── itc_hotel_analytics.db               # 3NF SQLite Database (18 tables, 87k rows)
    ├── itc_hotels_mysql_dump.sql            # Complete MySQL 8.0 DDL & Data Dump
    ├── data_cleaning_eda.ipynb              # Data Cleaning Pipeline & Matplotlib Visualizations
    ├── ITC_Executive_Live_Dashboard.xlsx    # Dashboard 1: Excel Live Dashboard (5 tabs)
    ├── interactive_jupyter_dashboard.ipynb  # Dashboard 2: Jupyter Plotly Interactive Dashboard
    ├── itc_master_hospitality_data.csv      # Clean Master Data for Power BI / Excel
    ├── itc_luxury_theme.json                # Power BI Dark Theme JSON Preset
    ├── POWER_BI_SQL_INTEGRATION_GUIDE.md    # Power BI SQL Connection & DAX Guide
    └── PROJECT_VIVA_PREPARATION.md          # Viva defense preparation guide
    └── PROJECT_VIVA_PREPARATION.md          # Professor Viva Q&A Cheat Sheet
```

---

## 3. The 4 Core Analytical Modules

| Module | Core Analytics | Key Metrics | Strategic Business Recommendation |
| :--- | :--- | :--- | :--- |
| **Module 1: Room Revenue & Occupancy** | Room yield, ADR, Category upgrades, Seasonality curves, Lead-time cancellations. | ADR: ₹ 8,941<br>RevPAR: ₹ 5,620<br>Upgrades: 12.3% | Enforce non-refundable rate barriers for bookings placed >90 days out to stop 52% cancellation loss. |
| **Module 2: Food, Beverage & Banquets** | Bukhara, Dum Pukht dining covers, APC, Grand Ballroom MICE summits & Royal Weddings. | Total F&B: ₹ 104.8 Cr<br>Avg Cover Spend: ₹ 2,450<br>Wedding Ticket: ₹ 12.5L | Introduce curated wine-pairing menus to elevate beverage share from 24% to 35% of dining mix. |
| **Module 3: Guest Demographics & Channels** | Domestic vs Intl sourcing, Guest Personas, Club ITC loyalty tiers, OTA commission leakage. | OTA Mix: 47.3%<br>Club ITC Stays: 24.8%<br>OTA Cancel: 41.6% | Offer 15% dining credits on direct website/app bookings to shift OTA volume to zero-commission Club ITC. |
| **Module 4: Operating Costs & Profitability** | USALI P&L framework, Departmental COGS, Staff payroll, LEED Platinum green utilities. | GOP: ₹ 143.68 Cr<br>GOP Margin: 48.15%<br>GOPPAR: ₹ 5,612 | LEED Platinum on-site solar/wind energy caps utility costs at 4.2% of revenue (industry avg: 8-10%). |

---

## 4. The 3 Final Live Dashboards

### 🟢 Dashboard 1: Microsoft Excel Live Dashboard (`.xlsx`)
- **File:** `ITC-Final-Dashboards/ITC_Executive_Live_Dashboard.xlsx`
- **Bottom Navigation:** Exact **5 Tabs** matching professor's reference architecture:
  1. `Room Analytics`
  2. `FnB Analytics`
  3. `Demographics`
  4. `Profitability`
  5. `Final` *(Master Executive Overview)*
- **Top on `Final` Tab:** 4 Square KPI Cards:
  - Total Revenue: **₹ 298.42 Cr**
  - Total Profit (GOP): **₹ 143.68 Cr**
  - Avg Occupancy: **62.9%**
  - F&B Sales: **₹ 104.84 Cr**
- **Charts:** Native Excel Column charts, Bar charts, and Line charts embedded.

### 🟣 Dashboard 2: Jupyter Notebook Interactive Dashboard (Plotly & Matplotlib)
- **Files:** 
  - `ITC-Final-Dashboards/data_cleaning_eda.ipynb` (Data cleaning pipeline & Matplotlib charts)
  - `ITC-Final-Dashboards/interactive_jupyter_dashboard.ipynb` (Plotly Dark luxury dashboard)
- **Features:** Plotly Dark Luxury Theme, 4 Square Indicator KPI Cards, Interactive Donut Chart, USALI Waterfall P&L Chart, Seasonality Multi-Bar/Line Chart, and Channel Risk Chart.

### 🔵 Dashboard 3: Microsoft Power BI Desktop Dashboard (with SQL Database Connection)
- **Database:** `ITC-Final-Dashboards/itc_hotel_analytics.db` & `itc_hotels_mysql_dump.sql`
- **1-Click Theme Preset:** `ITC-Final-Dashboards/itc_luxury_theme.json`
- **SQL Connection & Modeling Guide:** `ITC-Final-Dashboards/POWER_BI_SQL_INTEGRATION_GUIDE.md`
- **Ready DAX Measures:** Total Revenue Realized, ADR, RevPAR, Occupancy %, Realisation %, DSRN, DURN, WoW & MoM Growth %.

---

## 5. Step-by-Step GitHub Push Guide

To push all 4 modules + the final dashboards to GitHub:

1. Open **[github.com](https://github.com)** and create 4 (or 5) empty repositories:
   - `ITC-Room-Analytics`
   - `ITC-FnB-Analytics`
   - `ITC-Guest-Demographics`
   - `ITC-Profitability-Costs`
   - *(Optional 5th)* `ITC-Final-Dashboards`
   *(Do NOT initialize with README or .gitignore — leave them empty).*

2. Run the automated script in Ubuntu terminal:
   ```bash
   cd /home/goku/ITC_Hotels_Project
   ./push_all_to_github.sh <YOUR_GITHUB_USERNAME>
   ```
   *(Example: `./push_all_to_github.sh avisingh4121`)*

---

## 6. Power BI Desktop (Windows) 5-Minute Setup

When switching to Windows on your HP Victus laptop:
1. Open **Power BI Desktop**.
2. Click **Get Data ➔ Text/CSV**, navigate to your project folder, and load `itc_master_hospitality_data.csv`.
3. In the top ribbon, click **View ➔ Themes ➔ Browse for themes**, and select `itc_luxury_theme.json`.
4. Click **Modeling ➔ New Measure** and copy-paste the 4 core DAX measures from `POWER_BI_MODELING_GUIDE.md`.
5. Add 5 Pages at the bottom (`Room Analytics`, `FnB Analytics`, `Demographics`, `Profitability`, `Final`).
6. On the `Final` page, place 4 Cards on top, a Donut chart on the left, a Column chart in the center, and Slicers on the right.
7. Click **File ➔ Save As** and save as `ITC_Hotels_Executive_Dashboard.pbix`!

---

## 7. Viva & Technical Defense Q&A

1. **How was the Kaggle dataset adapted for ITC Hotels?**
   - The raw Kaggle booking dataset (119k rows) provided empirical booking behaviors (lead time, cancellations, guest numbers, room types).
   - We transformed currency into INR (₹), mapped properties to prestigious ITC Luxury resorts and city hotels, and engineered USALI financial metrics and iconic dining outlets (*Bukhara, Dum Pukht*) and Grand Ballrooms.

2. **What is USALI?**
   - *Uniform System of Accounts for the Lodging Industry* — the global gold standard for hotel P&L accounting that separates direct departmental operational expenses (Rooms, F&B) from undistributed property expenses (Administration, LEED Energy, Maintenance).

3. **Why is GOPPAR more insightful than RevPAR?**
   - **RevPAR** only measures room top-line revenue per room. **GOPPAR (Gross Operating Profit Per Available Room)** accounts for all revenue streams (including F&B and Banquets) minus all operational expenses, reflecting bottom-line profitability.
