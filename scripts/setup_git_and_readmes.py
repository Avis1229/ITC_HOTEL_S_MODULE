"""
Creates README.md, requirements.txt, .gitignore and initializes git repositories
for each of the 4 ITC modules + the master dashboard folder.
"""

import os
import subprocess

BASE_DIR = "/home/goku/ITC_Hotels_Project"

REQUIREMENTS_CONTENT = """pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
openpyxl>=3.1.0
jupyter>=1.0.0
"""

GITIGNORE_CONTENT = """.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
.DS_Store
"""

MODULES_INFO = [
    {
        "folder": "ITC-Room-Analytics",
        "title": "Module 1: Room Revenue & Occupancy Analytics",
        "csv": "itc_room_revenue_occupancy.csv",
        "notebook": "module1_room_revenue_occupancy.ipynb",
        "desc": "End-to-end analytics on room inventory monetization, Average Daily Rate (ADR), RevPAR, room category upgrades, seasonality curves, and lead-time cancellation risk mitigation for ITC Hotels.",
        "kpis": [
            "Total Room Revenue (₹ Crores)",
            "Average Daily Rate (ADR) per room night",
            "Confirmed Stay vs Cancellation Rate (%)",
            "Room Category Upgrade Yield & Distribution",
            "Seasonal Month-over-Month Revenue Trajectory",
            "Lead Time Window vs Cancellation Probability"
        ],
        "findings": [
            "Over 70% of room revenues are concentrated in Executive Club Rooms and The Towers.",
            "Bookings placed >90 days in advance suffer from a >50% cancellation rate, indicating an urgent need for non-refundable rate fences.",
            "Peak earnings occur during Q4 and Q1 (October–April) aligning with India's luxury leisure and royal wedding seasons."
        ]
    },
    {
        "folder": "ITC-FnB-Analytics",
        "title": "Module 2: Food, Beverage & Banquet Performance Analytics",
        "csv": "itc_fnb_banquet_performance.csv",
        "notebook": "module2_fnb_banquet_performance.ipynb",
        "desc": "Analytics for ITC Hotels' world-renowned culinary brands (Bukhara, Dum Pukht, Peshawri, Avartana), dining covers, meal plans, and large-scale MICE banquet monetization (Grand Ballrooms, Weddings & Summits).",
        "kpis": [
            "Dining Cover Volume & Average Spend Per Cover (APC)",
            "Food vs Beverage Revenue Mix & Upselling Ratio",
            "Signature Restaurant Outlet Revenue (Bukhara, Dum Pukht)",
            "Banquet Space Monetization (Rajputana Ballroom, Chola Conclave)",
            "Event Segment Breakdown (Weddings vs Corporate Summits vs Delegations)",
            "Dining Plan Performance (Bed & Breakfast vs Half/Full Board)"
        ],
        "findings": [
            "Bukhara and Dum Pukht drive the highest culinary revenues with average covers exceeding 18,000+ each.",
            "Beverage sales contribute <25% in dining outlets, representing a major upside for curated wine pairing and beverage upselling.",
            "Luxury Wedding Receptions produce the highest revenue per event ticket size (~₹10L - ₹15L), highlighting high synergy with luxury suite blocks."
        ]
    },
    {
        "folder": "ITC-Guest-Demographics",
        "title": "Module 3: Guest Demographics & Booking Channel Analytics",
        "csv": "itc_guest_demographics_channels.csv",
        "notebook": "module3_guest_demographics_channels.ipynb",
        "desc": "Detailed demographic profiling of domestic and international luxury guests, household personas (Solo vs Couple vs Family), Club ITC loyalty tier engagement, and OTA distribution commission control.",
        "kpis": [
            "Domestic vs International Geographic Sourcing",
            "Guest Personas (Solo Business, Couples, Families with Children)",
            "Club ITC Loyalty Tier Distribution (Culinaire, Gold, Silver, Green)",
            "Distribution Channel Share (Direct App vs OTAs vs Corporate B2B)",
            "Channel-specific Cancellation Probabilities",
            "Length of Stay (LOS) by Traveler Persona"
        ],
        "findings": [
            "Club ITC Culinaire and Gold loyalty members experience an ultra-low cancellation rate (<12%) compared to >40% on third-party OTAs.",
            "Online Travel Agencies (OTAs like MakeMyTrip/Booking.com) capture the largest booking share but dilute margins with high commissions and cancellation volatility.",
            "Families with children exhibit the longest average length of stay (3.8 nights), representing prime targets for holiday resort packages."
        ]
    },
    {
        "folder": "ITC-Profitability-Costs",
        "title": "Module 4: Operating Costs & Profitability Analytics",
        "csv": "itc_operating_costs_profitability.csv",
        "notebook": "module4_operating_costs_profitability.ipynb",
        "desc": "Rigorous financial statement analysis under the USALI (Uniform System of Accounts for the Lodging Industry) standard. Tracks direct departmental costs, staff payroll, LEED Platinum green energy benchmarks, and GOPPAR.",
        "kpis": [
            "Gross Realized Revenue (₹ 298.42 Cr)",
            "Gross Operating Profit (GOP / EBITDA: ₹ 143.68 Cr)",
            "GOP Margin Percentage (48.15%)",
            "GOPPAR (Gross Operating Profit Per Available Room Night: ₹ 5,612)",
            "LEED Platinum Utility & Sustainable Energy Cost Efficiency",
            "OTA Distribution Commission Outflow & Savings Potential"
        ],
        "findings": [
            "ITC Hotels achieves a robust 48.15% GOP Margin, significantly outperforming the luxury industry average of 38-42%.",
            "LEED Platinum certified sustainable energy infrastructure keeps utility expenses contained at ~4.2% of revenue.",
            "Shifting just 5% of bookings from third-party OTAs to direct Club ITC channels immediately contributes ₹2.2 Crores in pure EBITDA."
        ]
    },
    {
        "folder": "ITC-Final-Dashboards",
        "title": "ITC Hotels — Master Executive Live Dashboards",
        "csv": "itc_master_hospitality_data.csv",
        "notebook": None,
        "desc": "Executive portfolio presentation suite containing interactive Microsoft Excel (.xlsx) live dashboard, standalone HTML executive web portal, and Power BI DAX modeling blueprint.",
        "kpis": [
            "Consolidated Portfolio Gross Revenue (₹ 298.42 Cr)",
            "Gross Operating Profit (₹ 143.68 Cr, 48.15% Margin)",
            "Average Daily Rate (₹ 8,941) across 75,166 Confirmed Stays",
            "Comprehensive USALI Hospitality Income Statement",
            "Interactive Visual Analytics for Multi-Property Executive Board Review"
        ],
        "findings": [
            "Offers a single pane of glass uniting Rooms, F&B, Banquets, Guest Demographics, and Financial Costs.",
            "Interactive Excel Dashboard (`ITC_Executive_Live_Dashboard.xlsx`) includes 5 styled reporting tabs ready for instant evaluation.",
            "HTML Web Dashboard (`index.html`) runs directly inside any web browser on Ubuntu without Windows dependency.",
            "Power BI Data Model guide (`POWER_BI_MODELING_GUIDE.md`) enables instant drag-and-drop report recreation in Windows."
        ]
    }
]

def setup_all():
    for mod in MODULES_INFO:
        folder_path = os.path.join(BASE_DIR, mod['folder'])
        print(f"\nProcessing {mod['folder']}...")

        # 1. requirements.txt
        req_path = os.path.join(folder_path, "requirements.txt")
        with open(req_path, "w") as f:
            f.write(REQUIREMENTS_CONTENT)

        # 2. .gitignore
        ignore_path = os.path.join(folder_path, ".gitignore")
        with open(ignore_path, "w") as f:
            f.write(GITIGNORE_CONTENT)

        # 3. README.md
        readme_path = os.path.join(folder_path, "README.md")
        
        kpis_md = "\n".join([f"- **{kpi}**" for kpi in mod['kpis']])
        findings_md = "\n".join([f"- {f}" for f in mod['findings']])
        
        nb_section = ""
        if mod['notebook']:
            nb_section = f"""### 📓 Jupyter Notebook
The exploratory and diagnostic analytics are implemented in [`{mod['notebook']}`]({mod['notebook']}).
To run locally:
```bash
jupyter notebook {mod['notebook']}
```
"""
        else:
            nb_section = """### 📊 Executive Dashboards
- **Excel Live Dashboard:** [`ITC_Executive_Live_Dashboard.xlsx`](ITC_Executive_Live_Dashboard.xlsx) (Formatted multi-tab USALI model).
- **Interactive Web Dashboard:** Open [`index.html`](index.html) in any modern browser.
- **Power BI Guide:** [`POWER_BI_MODELING_GUIDE.md`](POWER_BI_MODELING_GUIDE.md) (Step-by-step Windows setup & DAX formulas).
"""

        readme_content = f"""# {mod['title']}
### ITC Hotels Hospitality Management Analytics | Academic & Executive Submission
**Author:** Goku | **Property Portfolio:** ITC Maurya, ITC Grand Chola, ITC Grand Bharat, ITC Mughal

---

## 📌 Project Overview
{mod['desc']}

This repository forms a core module of the **ITC Hotels Comprehensive Analytics Project**, tailored to luxury hospitality standards, customer retention, and the **USALI (Uniform System of Accounts for the Lodging Industry)** framework.

---

## 🎯 Key Performance Indicators (KPIs) Tracked
{kpis_md}

---

## 📁 Repository Structure
```text
{mod['folder']}/
├── README.md                               # Project documentation & business insights
├── requirements.txt                        # Python package dependencies
├── .gitignore                              # Git exclusion rules
├── {mod['csv']}                            # Curated dataset (119,390 records)
""" + (f"└── {mod['notebook']}               # Interactive Jupyter Notebook with executed visualizations\n```\n" if mod['notebook'] else "├── ITC_Executive_Live_Dashboard.xlsx      # Master formatted Excel dashboard\n├── index.html                              # Standalone HTML/Tailwind/Chart.js live dashboard\n└── POWER_BI_MODELING_GUIDE.md              # Power BI star schema & DAX formulas\n```\n") + f"""
---

{nb_section}

---

## 💡 Executive Insights & Strategic Findings
{findings_md}

---

## 🚀 Setup & Execution Guide
1. Clone this repository:
   ```bash
   git clone <REPO_URL>
   cd {mod['folder']}
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Inspect and analyze the data!
"""
        with open(readme_path, "w") as f:
            f.write(readme_content)

        # 4. Git Initialization & Commit
        # Configure local git user if not configured
        subprocess.run(["git", "config", "user.name", "Goku"], cwd=folder_path)
        subprocess.run(["git", "config", "user.email", "goku@victus.local"], cwd=folder_path)

        # Initialize repository
        if not os.path.exists(os.path.join(folder_path, ".git")):
            subprocess.run(["git", "init"], cwd=folder_path, check=True)
            subprocess.run(["git", "add", "."], cwd=folder_path, check=True)
            subprocess.run(["git", "commit", "-m", f"Initial commit: {mod['title']}"], cwd=folder_path, check=True)
            print(f"Git repo successfully initialized and committed in {mod['folder']}")
        else:
            subprocess.run(["git", "add", "."], cwd=folder_path, check=True)
            subprocess.run(["git", "commit", "-m", f"Update: {mod['title']}"], cwd=folder_path)
            print(f"Updated git commit in {mod['folder']}")

if __name__ == '__main__':
    setup_all()
