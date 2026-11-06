# 🏨 ITC Hotels — Revenue & Business Performance Analysis
**Invertis University, Bareilly** | Faculty of Computer Applications  
**Project Guide:** Ms. Megha Saxena, Assistant Professor  
**Student Team:**
1. Jatin Sagar (Student ID: BC2023727, Roll No: 2311001156)
2. Atul Kumar (Student ID: BC2023590, Roll No: 2310201157)
3. Darshika Rathore (Student ID: BC2023687, Roll No: 2310101126)
4. Muskan Saxena (Student ID: BC2023061, Roll No: 2310201370)

**Technology Stack:** MySQL 8.0 / SQLite 3NF Database, Python (Pandas, Matplotlib, Seaborn), Power BI Desktop, Microsoft Excel (Live Pivot Tables & Slicers).

---
## Module 1: Room Revenue & Occupancy Analytics

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
