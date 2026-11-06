# Module 3: Guest Demographics & Booking Channel Analytics
### ITC Hotels Hospitality Management Analytics | Academic & Executive Submission
**Author:** Goku | **Property Portfolio:** ITC Maurya, ITC Grand Chola, ITC Grand Bharat, ITC Mughal

---

## 📌 Project Overview
Detailed demographic profiling of domestic and international luxury guests, household personas (Solo vs Couple vs Family), Club ITC loyalty tier engagement, and OTA distribution commission control.

This repository forms a core module of the **ITC Hotels Comprehensive Analytics Project**, tailored to luxury hospitality standards, customer retention, and the **USALI (Uniform System of Accounts for the Lodging Industry)** framework.

---

## 🎯 Key Performance Indicators (KPIs) Tracked
- **Domestic vs International Geographic Sourcing**
- **Guest Personas (Solo Business, Couples, Families with Children)**
- **Club ITC Loyalty Tier Distribution (Culinaire, Gold, Silver, Green)**
- **Distribution Channel Share (Direct App vs OTAs vs Corporate B2B)**
- **Channel-specific Cancellation Probabilities**
- **Length of Stay (LOS) by Traveler Persona**

---

## 📁 Repository Structure
```text
ITC-Guest-Demographics/
├── README.md                               # Project documentation & business insights
├── requirements.txt                        # Python package dependencies
├── .gitignore                              # Git exclusion rules
├── itc_guest_demographics_channels.csv                            # Curated dataset (119,390 records)
└── module3_guest_demographics_channels.ipynb               # Interactive Jupyter Notebook with executed visualizations
```

---

### 📓 Jupyter Notebook
The exploratory and diagnostic analytics are implemented in [`module3_guest_demographics_channels.ipynb`](module3_guest_demographics_channels.ipynb).
To run locally:
```bash
jupyter notebook module3_guest_demographics_channels.ipynb
```


---

## 💡 Executive Insights & Strategic Findings
- Club ITC Culinaire and Gold loyalty members experience an ultra-low cancellation rate (<12%) compared to >40% on third-party OTAs.
- Online Travel Agencies (OTAs like MakeMyTrip/Booking.com) capture the largest booking share but dilute margins with high commissions and cancellation volatility.
- Families with children exhibit the longest average length of stay (3.8 nights), representing prime targets for holiday resort packages.

---

## 🚀 Setup & Execution Guide
1. Clone this repository:
   ```bash
   git clone <REPO_URL>
   cd ITC-Guest-Demographics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Inspect and analyze the data!
