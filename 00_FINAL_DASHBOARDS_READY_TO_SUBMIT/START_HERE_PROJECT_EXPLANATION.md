# 🏨 ITC Hotels Analytics — Project Samajhne Ka Sabse Aasaan Guide
**Invertis University, Bareilly | BCA Final Year Project**

Bhai, agar project me thoda bhi confusion hai, toh bas is 2-minute ke page ko padh lo. Pura project crystal-clear ho jayega!

---

## 🎯 1. Ye Project Asal Me Hai Kya? (In Simple Words)

- **Scenario:** Humne India ki luxury hotel chain **"ITC Hotels"** (ITC Maurya, ITC Grand Bharat, etc.) ka 1 saal ka data analyze kiya hai.
- **Source Data:** Kaggle se hotel booking ka master dataset liya (1,19,390 bookings).
- **Transformation:** Humne us data ko clean kiya, Euro ko Indian Rupee (₹) me convert kiya, ITC ke famous restaurants (Bukhara, Dum Pukht) aur grand banquets ke realistic sales add kiye.
- **Main Goal:** Hotel ke 4 main hisson (Rooms, F&B, Demographics, Profit) ka analysis karke **3 alag tools me LIVE Dashboards** banana:
  1. **Excel me Live Dashboard**
  2. **Jupyter Notebook me Interactive Dashboard**
  3. **Power BI me Executive Dashboard**

---

## 📁 2. Saari Final Files Ek Jagah (Is Folder Me Kya Hai)

Tumhe kahin bhatakne ki zarurat nahi hai, saari main files is folder ke andar hain:

```text
00_FINAL_DASHBOARDS_READY_TO_SUBMIT/
│
├── 📊 1_EXCEL_DASHBOARD/
│   └── ITC_Executive_Live_Dashboard.xlsx     <-- Excel ka live dashboard (5 bottom tabs)
│
├── 📓 2_JUPYTER_DASHBOARD/
│   ├── interactive_jupyter_dashboard.ipynb   <-- Plotly interactive dashboard
│   └── data_cleaning_eda.ipynb              <-- Data cleaning + Matplotlib charts
│
├── 📈 3_POWER_BI_DASHBOARD/
│   ├── POWER_BI_SQL_INTEGRATION_GUIDE.md     <-- Power BI me kya-kya karna hai step-by-step
│   ├── itc_luxury_theme.json                 <-- Dark luxury theme (1-click)
│   ├── itc_master_hospitality_data.csv       <-- Power BI me load karne wali data file
│   └── itc_hotels_mysql_dump.sql             <-- Agar SQL database se connect karna ho
│
└── 📄 4_COMPLETE_REPORT_PDF/
    └── ITC_Hotels_Project_Complete_Documentation.pdf  <-- 18-page ki complete project report
```

---

## 🧩 3. Wo 4 Modules Kya Hain Jo Professor Ne Bole The?

Professor ne bola tha ki project ko 4 parts me divide karo aur har module ka alag folder aur GitHub branch banao:

1. **Module 1 (`ITC-Room-Analytics`):** Room Revenue, Occupancy Rate, ADR (Average Daily Rate = ₹8,941).
2. **Module 2 (`ITC-FnB-Analytics`):** Food & Beverage (Bukhara, Dum Pukht) + Banquets (Weddings & Conferences) = ₹104.84 Cr.
3. **Module 3 (`ITC-Guest-Demographics`):** Guests kahan se aate hain (India vs Foreign), Direct Booking vs OTA (MakeMyTrip), Club ITC Loyalty tiers.
4. **Module 4 (`ITC-Profitability-Costs`):** Hotel ke kharche (Staff, Electricity, Food cost) aur Net Profit (GOP = ₹143.68 Cr, 48.15% margin).

---

## 🚀 4. Professor Ko Kya Dikhana Hai? (Step-by-Step Viva Demo)

### A. Excel Dashboard Dikhana Ho Toh:
1. `1_EXCEL_DASHBOARD/ITC_Executive_Live_Dashboard.xlsx` open karo.
2. Niche 5 tabs hain: `Room Analytics`, `FnB Analytics`, `Demographics`, `Profitability`, aur `Final`.
3. `Final` tab par top par 4 square cards hain (Total Revenue ₹298.4 Cr, Profit ₹143.7 Cr, Occupancy 62.9%, F&B ₹104.8 Cr) aur native charts hain.

### B. Jupyter / Python Plotting Dikhana Ho Toh:
1. Terminal me run karo:
   ```bash
   cd /home/goku/ITC_Hotels_Project
   ./run_dashboard.sh
   ```
2. Option 1 dabao -> `data_cleaning_eda.ipynb` khulega jisme Matplotlib ke 8 charts aur data cleaning dikhegi.
3. Option 2 dabao -> `interactive_jupyter_dashboard.ipynb` khulega jo interactive dark theme dashboard hai.

### C. Power BI Dikhana Ho Toh:
1. Windows boot karo.
2. `3_POWER_BI_DASHBOARD/` folder kholo.
3. `POWER_BI_SQL_INTEGRATION_GUIDE.md` ke simple steps padh kar Power BI Desktop me `itc_master_hospitality_data.csv` load karo, `itc_luxury_theme.json` apply karo, aur DAX measures copy-paste karo.

### D. Report ya PDF Maange Toh:
- `4_COMPLETE_REPORT_PDF/ITC_Hotels_Project_Complete_Documentation.pdf` ka print-out ya PDF seedha de do!
