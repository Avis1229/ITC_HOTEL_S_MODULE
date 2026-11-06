# Module 1: Room Revenue & Occupancy Analytics
### ITC Hotels Hospitality Management Analytics | Academic & Executive Submission
**Author:** Goku | **Property Portfolio:** ITC Maurya, ITC Grand Chola, ITC Grand Bharat, ITC Mughal

---

## 📌 Project Overview
End-to-end analytics on room inventory monetization, Average Daily Rate (ADR), RevPAR, room category upgrades, seasonality curves, and lead-time cancellation risk mitigation for ITC Hotels.

This repository forms a core module of the **ITC Hotels Comprehensive Analytics Project**, tailored to luxury hospitality standards, customer retention, and the **USALI (Uniform System of Accounts for the Lodging Industry)** framework.

---

## 🎯 Key Performance Indicators (KPIs) Tracked
- **Total Room Revenue (₹ Crores)**
- **Average Daily Rate (ADR) per room night**
- **Confirmed Stay vs Cancellation Rate (%)**
- **Room Category Upgrade Yield & Distribution**
- **Seasonal Month-over-Month Revenue Trajectory**
- **Lead Time Window vs Cancellation Probability**

---

## 📁 Repository Structure
```text
ITC-Room-Analytics/
├── README.md                               # Project documentation & business insights
├── requirements.txt                        # Python package dependencies
├── .gitignore                              # Git exclusion rules
├── itc_room_revenue_occupancy.csv                            # Curated dataset (119,390 records)
└── module1_room_revenue_occupancy.ipynb               # Interactive Jupyter Notebook with executed visualizations
```

---

### 📓 Jupyter Notebook
The exploratory and diagnostic analytics are implemented in [`module1_room_revenue_occupancy.ipynb`](module1_room_revenue_occupancy.ipynb).
To run locally:
```bash
jupyter notebook module1_room_revenue_occupancy.ipynb
```


---

## 💡 Executive Insights & Strategic Findings
- Over 70% of room revenues are concentrated in Executive Club Rooms and The Towers.
- Bookings placed >90 days in advance suffer from a >50% cancellation rate, indicating an urgent need for non-refundable rate fences.
- Peak earnings occur during Q4 and Q1 (October–April) aligning with India's luxury leisure and royal wedding seasons.

---

## 🚀 Setup & Execution Guide
1. Clone this repository:
   ```bash
   git clone <REPO_URL>
   cd ITC-Room-Analytics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Inspect and analyze the data!
