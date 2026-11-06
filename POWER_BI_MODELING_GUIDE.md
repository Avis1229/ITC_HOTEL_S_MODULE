# ITC Hotels — Power BI Modeling & Implementation Guide
### Master Hospitality Executive Dashboard
**Author:** Goku | **Target Platform:** Microsoft Power BI Desktop (Windows Dual-Boot)

---

## 1. Quick Setup in Windows
1. Boot into Windows on your HP Victus laptop.
2. Open **Power BI Desktop**.
3. Click **Get Data** ➔ **Text/CSV**.
4. Navigate to your project folder (or USB/shared drive where you copied `itc_master_hospitality_data.csv`).
5. Click **Load** (or *Transform Data* if you wish to inspect column types).

---

## 2. Recommended Star Schema Data Model
If building separate dimensional tables inside Power Query:
- **Fact Table:** `Fact_HospitalityBookings` (`itc_master_hospitality_data.csv`)
- **Dim_Date:** `arrival_date`, `arrival_date_year`, `arrival_date_month`
- **Dim_Hotel:** `hotel_name` (Resort vs City Executive)
- **Dim_Room:** `reserved_room_category`, `assigned_room_category`, `is_upgraded`
- **Dim_Guest:** `guest_origin_country`, `geographic_region`, `guest_profile`, `loyalty_program_tier`
- **Dim_Channel:** `channel_clean`, `customer_type`

---

## 3. Essential Ready-to-Use DAX Measures
Create a dedicated table named `_Measures` and add these DAX formulas:

### 1. Total Gross Realized Revenue
```dax
Total Gross Revenue (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(Fact_HospitalityBookings[gross_total_revenue_inr]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    10000000,
    0
)
```

### 2. Room Revenue & ADR
```dax
Total Room Revenue (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(Fact_HospitalityBookings[room_revenue_inr]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    10000000,
    0
)

Average Daily Rate (ADR) = 
CALCULATE(
    AVERAGE(Fact_HospitalityBookings[adr_inr]),
    Fact_HospitalityBookings[is_canceled] = 0
)
```

### 3. F&B & Banquet Revenue
```dax
Total F&B and Banquet Revenue (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(Fact_HospitalityBookings[combined_fnb_banquet_rev_inr]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    10000000,
    0
)
```

### 4. Cancellation Rate (%)
```dax
Cancellation Rate % = 
DIVIDE(
    CALCULATE(COUNTROWS(Fact_HospitalityBookings), Fact_HospitalityBookings[is_canceled] = 1),
    COUNTROWS(Fact_HospitalityBookings),
    0
) * 100
```

### 5. USALI Gross Operating Profit (GOP) & Margin
```dax
Gross Operating Profit (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(Fact_HospitalityBookings[gross_operating_profit_inr]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    10000000,
    0
)

GOP Margin % = 
DIVIDE(
    [Gross Operating Profit (₹ Cr)],
    [Total Gross Revenue (₹ Cr)],
    0
) * 100
```

### 6. GOPPAR (GOP per Billed Room Night)
```dax
GOPPAR (₹) = 
DIVIDE(
    CALCULATE(
        SUM(Fact_HospitalityBookings[gross_operating_profit_inr]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    CALCULATE(
        SUM(Fact_HospitalityBookings[billed_nights]),
        Fact_HospitalityBookings[is_canceled] = 0
    ),
    0
)
```

---

## 4. Visual Dashboard Layout (Canvas Recommendations)
- **Top Row (KPI Cards):**
  - Gross Revenue (`₹ 298.42 Cr`)
  - Gross Operating Profit (`₹ 143.68 Cr`)
  - GOP Margin (`48.15%`)
  - Average ADR (`₹ 8,941`)
  - Cancellation Rate (`37.0%`)
- **Row 2:**
  - *Left (Clustered Column Chart):* Monthly Revenue vs GOP (`arrival_date_month`).
  - *Right (Donut Chart):* Revenue by Stream (Room Rev vs F&B/Banquet vs Minor Depts).
- **Row 3:**
  - *Left (Bar Chart):* Top Restaurant Outlets by Revenue (`primary_restaurant_outlet`).
  - *Middle (Treemap):* Distribution Channel Mix (`channel_clean`).
  - *Right (Line Chart):* Lead Time vs Cancellation Probability.
- **Slicers (Filters on Left or Top):**
  - `hotel_name` (Resort vs City Luxury)
  - `arrival_date_year` (2015, 2016, 2017)
  - `loyalty_program_tier` (Club ITC Tiers)
