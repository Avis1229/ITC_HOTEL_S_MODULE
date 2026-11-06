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
## Module 3: Guest Demographics & Booking Channel Analytics

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
