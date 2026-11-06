"""
Update all README.md files to match Invertis University BCA Project Report specifications.
Author & Team: Jatin Sagar, Atul Kumar, Darshika Rathore, Muskan Saxena
Guide: Ms. Megha Saxena
"""

import os

BASE_DIR = "/home/goku/ITC_Hotels_Project"

HEADER = """# 🏨 ITC Hotels — Revenue & Business Performance Analysis
**Invertis University, Bareilly** | Faculty of Computer Applications  
**Project Guide:** Ms. Megha Saxena, Assistant Professor  
**Student Team:**
1. Jatin Sagar (Student ID: BC2023727, Roll No: 2311001156)
2. Atul Kumar (Student ID: BC2023590, Roll No: 2310201157)
3. Darshika Rathore (Student ID: BC2023687, Roll No: 2310101126)
4. Muskan Saxena (Student ID: BC2023061, Roll No: 2310201370)

**Technology Stack:** MySQL 8.0 / SQLite 3NF Database, Python (Pandas, Matplotlib, Seaborn), Power BI Desktop, Microsoft Excel (Live Pivot Tables & Slicers).

---
"""

readmes = {
    "ITC-Room-Analytics": HEADER + """## Module 1: Room Revenue & Occupancy Analytics

### 📌 Overview
Analyzes room booking lifecycles, pricing elasticity (ADR), RevPAR maximization, room upgrades, and seasonality across ITC luxury properties (*ITC Grand Bharat & ITC Maurya*).

### 📁 Repository Structure
```
├── README.md                                  # Module documentation
├── requirements.txt                           # Python dependencies
├── .gitignore                                 # Git ignore rules
├── itc_room_revenue_occupancy.csv             # Module 1 transactional dataset
└── module1_room_revenue_occupancy.ipynb       # Executed Jupyter analysis (SQL + Matplotlib)
```

### 🧮 Key Metrics Analyzed
- **Average Daily Rate (ADR):** ₹ 8,941 per room night
- **Average Length of Stay (ALOS):** 2.76 nights
- **Average Lead Time:** 80.2 days
- **Total Room Revenue:** ₹ 192.37 Crores
- **Confirmed Stays:** 62.9%

### 🚀 How to Run
```bash
# 1. Activate environment
source ../.venv/bin/activate

# 2. Launch analysis notebook
jupyter notebook module1_room_revenue_occupancy.ipynb
```
""",

    "ITC-FnB-Analytics": HEADER + """## Module 2: Food, Beverage & Banquet Performance Analytics

### 📌 Overview
Evaluates culinary outlet performance (*Bukhara, Dum Pukht, Pavilion, Pan Asian, West View, Peshawri*), dining plan cover efficiency, beverage revenue realization, and grand banquet/MICE yields (*The Grand Ballroom, Peacock Hall*).

### 📁 Repository Structure
```
├── README.md                                  # Module documentation
├── requirements.txt                           # Python dependencies
├── .gitignore                                 # Git ignore rules
├── itc_fnb_banquet_performance.csv            # F&B and Banquet dataset
└── module2_fnb_banquet_performance.ipynb      # Executed Jupyter analysis (SQL + Matplotlib)
```

### 🧮 Key Metrics Analyzed
- **Total Dining Covers:** 121,438 covers served
- **Food Revenue:** ₹ 68.12 Crores
- **Beverage Revenue:** ₹ 16.48 Crores
- **Banquet Event Revenue:** ₹ 20.24 Crores
- **Combined Culinary Portfolio Yield:** ₹ 104.84 Crores

### 🚀 How to Run
```bash
source ../.venv/bin/activate
jupyter notebook module2_fnb_banquet_performance.ipynb
```
""",

    "ITC-Guest-Demographics": HEADER + """## Module 3: Guest Demographics & Booking Channel Analytics

### 📌 Overview
Tracks geographic distribution of guests, Club ITC loyalty engagement (Platinum, Gold, Silver), market segments (Corporate vs Transient), and OTA commission exposure across distribution channels.

### 📁 Repository Structure
```
├── README.md                                     # Module documentation
├── requirements.txt                              # Python dependencies
├── .gitignore                                    # Git ignore rules
├── itc_guest_demographics_channels.csv           # Demographics dataset
└── module3_guest_demographics_channels.ipynb     # Executed Jupyter analysis (SQL + Matplotlib)
```

### 🧮 Key Metrics Analyzed
- **Top Origin Geographies:** Domestic India (38%), Europe (34%), Americas (14%)
- **Loyalty Contribution:** Club ITC tiers drive 41% of repeat stays
- **Direct Channel Yield:** 3.2× higher margin than third-party OTAs
- **Cancellation Exposure:** Highest among high-lead-time OTA reservations

### 🚀 How to Run
```bash
source ../.venv/bin/activate
jupyter notebook module3_guest_demographics_channels.ipynb
```
""",

    "ITC-Profitability-Costs": HEADER + """## Module 4: Operating Costs & Profitability Analytics

### 📌 Overview
Adheres to the hospitality-standard **USALI (Uniform System of Accounts for the Lodging Industry)** framework to model room operating costs, F&B COGS, staff payroll, energy utilities, and property Gross Operating Profit (GOP).

### 📁 Repository Structure
```
├── README.md                                       # Module documentation
├── requirements.txt                                # Python dependencies
├── .gitignore                                      # Git ignore rules
├── itc_operating_costs_profitability.csv           # Operating expenses dataset
└── module4_operating_costs_profitability.ipynb     # Executed Jupyter analysis (SQL + Matplotlib)
```

### 🧮 Key Metrics Analyzed
- **Gross Revenue:** ₹ 298.42 Crores
- **Total Operating Expenses:** ₹ 154.74 Crores
- **Gross Operating Profit (GOP):** ₹ 143.68 Crores
- **GOP Margin:** 48.15%
- **GOPPAR (GOP Per Available Room):** ₹ 5,612

### 🚀 How to Run
```bash
source ../.venv/bin/activate
jupyter notebook module4_operating_costs_profitability.ipynb
```
""",

    "ITC-Final-Dashboards": HEADER + """## Final Executive Dashboards & SQL Integration

### 📌 Overview
Consolidates all 4 analytical modules into industry-standard deliverables:
1. **Relational SQL Database:** 18 tables/views in 3NF (`itc_hotel_analytics.db` & `itc_hotels_mysql_dump.sql`).
2. **Data Cleaning & EDA Notebook:** Matplotlib visualizations and data pipeline (`data_cleaning_eda.ipynb`).
3. **Interactive Plotly Dashboard:** 5 bottom tabs and top square KPI cards (`interactive_jupyter_dashboard.ipynb`).
4. **Master Live Excel Dashboard:** 5 sheets with native charts and KPI cards (`ITC_Executive_Live_Dashboard.xlsx`).
5. **Power BI Integration Guide:** Star-schema connection, DAX formulas, and visual layouts (`POWER_BI_SQL_INTEGRATION_GUIDE.md`).

### 📁 Repository Structure
```
├── README.md                                 # Master documentation
├── requirements.txt                          # Dependencies
├── .gitignore                                # Git rules
├── itc_hotel_analytics.db                    # 3NF SQLite Database (18 tables, 87k rows)
├── itc_hotels_mysql_dump.sql                 # Complete MySQL 8.0 DDL & Data Dump
├── data_cleaning_eda.ipynb                   # Data cleaning & Matplotlib EDA
├── interactive_jupyter_dashboard.ipynb       # Interactive Plotly executive dashboard
├── ITC_Executive_Live_Dashboard.xlsx         # Master Excel live dashboard
├── itc_luxury_theme.json                     # Power BI Luxury Theme
├── POWER_BI_SQL_INTEGRATION_GUIDE.md         # SQL connection & DAX documentation
└── PROJECT_VIVA_PREPARATION.md               # Viva defense questions & answers
```

### 🚀 Quick Launch
```bash
# Launch terminal hub
./run_dashboard.sh
```
"""
}

for folder, content in readmes.items():
    readme_path = os.path.join(BASE_DIR, folder, "README.md")
    with open(readme_path, "w") as f:
        f.write(content)
    print(f"✅ Updated README: {folder}")

print("All READMEs successfully synchronized with Invertis University BCA Report!")
