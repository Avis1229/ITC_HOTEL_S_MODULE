# ITC Hotels — Power BI Final Dashboard (.pbix) Blueprint
### Matching Professor's Strict Visual Architecture & Demo Dashboard Reference
**Target Tool:** Microsoft Power BI Desktop (Windows Dual-Boot)  
**Reference Design:** 5-Tab Dark Executive Architecture with Top 4 Square KPI Cards

---

## 1. Executive Layout Architecture (Matching Demo Image)

Your demo dashboard (`media_1793968313302_8234dc6d.jpg`) has:
1. **5 Bottom Pages/Tabs**:
   - `Room Analytics` (Module 1)
   - `FnB Analytics` (Module 2)
   - `Demographics` (Module 3)
   - `Profitability` (Module 4)
   - `Final` (Master Executive Overview — Page 5 of 5)
2. **Top Header & 4 Square KPI Cards**:
   - Card 1: **Total Revenue** (`₹ 298.42 Cr`)
   - Card 2: **Total Profit (GOP)** (`₹ 143.68 Cr`)
   - Card 3: **Avg Occupancy** (`62.9%`)
   - Card 4: **F&B Sales** (`₹ 104.84 Cr`)
3. **Dark Theme Visual Canvas**:
   - Canvas Background: Dark Slate / Navy Blue (`#0F172A` or `#13182C`)
   - Visual Containers: Translucent Card Surface (`#1E293B`, Transparency 15%, Border `#334155`)
   - Accent Colors: Cyan (`#38BDF8`), Emerald (`#10B981`), Gold/Amber (`#F59E0B`), Rose (`#F43F5E`)

---

## 2. Step-by-Step Build in Windows Power BI Desktop

### Step 1: Load Master Dataset
1. Boot into Windows on your HP Victus laptop.
2. Open **Power BI Desktop**.
3. Click **Get Data** ➔ **Text/CSV**.
4. Select `itc_master_hospitality_data.csv` (from `ITC-Final-Dashboards/`).
5. Click **Load**.

### Step 2: Configure Dark Theme
1. In the top ribbon, go to **View** ➔ **Themes** dropdown.
2. Choose **Dark** (or *Innovator* / *High Contrast*), or click **Customize current theme**:
   - Background: `#0F172A`
   - Data colors: `#38BDF8`, `#10B981`, `#F59E0B`, `#A855F7`, `#F43F5E`, `#6366F1`
   - Visual background: `#1E293B`

### Step 3: Create the 5 Pages (Bottom Navigation)
At the bottom bar, click `+` to create 5 pages and rename them:
1. `Room Analytics`
2. `FnB Analytics`
3. `Demographics`
4. `Profitability`
5. `Final` *(Keep this page selected for the master presentation)*

---

## 3. Ready-to-Use DAX Measures (Copy & Paste)
Create a new measure table in Power BI by clicking **Modeling** ➔ **New Measure**:

### Measure 1: Total Revenue (₹ Crores)
```dax
Total Revenue (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(itc_master_hospitality_data[gross_total_revenue_inr]),
        itc_master_hospitality_data[is_canceled] = 0
    ),
    10000000,
    0
)
```

### Measure 2: Total Profit / GOP (₹ Crores)
```dax
Total Profit (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(itc_master_hospitality_data[gross_operating_profit_inr]),
        itc_master_hospitality_data[is_canceled] = 0
    ),
    10000000,
    0
)
```

### Measure 3: Average Occupancy Rate (%)
```dax
Avg Occupancy % = 
DIVIDE(
    CALCULATE(
        COUNTROWS(itc_master_hospitality_data),
        itc_master_hospitality_data[is_canceled] = 0
    ),
    COUNTROWS(itc_master_hospitality_data),
    0
) * 100
```

### Measure 4: F&B & Banquet Sales (₹ Crores)
```dax
F&B Sales (₹ Cr) = 
DIVIDE(
    CALCULATE(
        SUM(itc_master_hospitality_data[combined_fnb_banquet_rev_inr]),
        itc_master_hospitality_data[is_canceled] = 0
    ),
    10000000,
    0
)
```

### Measure 5: Average Daily Rate (ADR)
```dax
Avg ADR (₹) = 
CALCULATE(
    AVERAGE(itc_master_hospitality_data[adr_inr]),
    itc_master_hospitality_data[is_canceled] = 0
)
```

### Measure 6: Cancellation Rate (%)
```dax
Cancellation Rate % = 
DIVIDE(
    CALCULATE(
        COUNTROWS(itc_master_hospitality_data),
        itc_master_hospitality_data[is_canceled] = 1
    ),
    COUNTROWS(itc_master_hospitality_data),
    0
) * 100
```

---

## 4. Visual Layout on the 'Final' Page (Matching Reference Canvas)

```text
+---------------------------------------------------------------------------------------------------+
|  ITC HOTELS — EXECUTIVE BOARDROOM PERFORMANCE DASHBOARD                                           |
+---------------------+---------------------+---------------------+---------------------------------+
| [ CARD 1 ]          | [ CARD 2 ]          | [ CARD 3 ]          | [ CARD 4 ]                      |
| TOTAL REVENUE       | TOTAL PROFIT (GOP)  | AVG OCCUPANCY       | F&B SALES                       |
| ₹ 298.42 Cr         | ₹ 143.68 Cr         | 62.9%               | ₹ 104.84 Cr                     |
+---------------------+---------------------+---------------------+---------------------------------+
| [ DONUT CHART ]     | [ STACKED COLUMN ]                        | [ SLICERS (Right Strip) ]       |
| Revenue Stream Mix  | Monthly Revenue vs GOP                    | • Property (Resort / City)      |
| • Rooms (61%)       | Jan -> Dec                                | • Year (2015, 2016, 2017)       |
| • F&B/Banquet (35%) |                                           | • Loyalty Tier (Culinaire, Gold)|
+---------------------+-------------------------------------------+---------------------------------+
| [ HORIZONTAL BAR ]  | [ WATERFALL / AREA CHART ]                                                  |
| Top Source Markets  | USALI Operating Cost Walk-Down (COGS, Payroll, Utilities, GOP)              |
+---------------------+-----------------------------------------------------------------------------+
|  [ Room Analytics ] | [ FnB Analytics ] | [ Demographics ] | [ Profitability ] | [ Final (Selected) ] |
+---------------------------------------------------------------------------------------------------+
```

1. **Top Row (Visual: Card (new) / Multi-row Card):**
   - Place 4 Cards side-by-side.
   - Format: Background `#1E293B`, Data label font size 24, bold, White/Cyan.
2. **Middle Left (Visual: Donut Chart):**
   - Legend: `dining_plan` or Revenue categories.
   - Values: `gross_total_revenue_inr`.
3. **Middle Center (Visual: Clustered Column Chart):**
   - X-axis: `arrival_date_month`.
   - Y-axis: `[Total Revenue (₹ Cr)]` and `[Total Profit (₹ Cr)]`.
4. **Right Edge (Visual: Slicer with Tile style):**
   - Field 1: `hotel_name`
   - Field 2: `arrival_date_year`
   - Field 3: `loyalty_program_tier`
5. **Bottom Area (Visual: Clustered Bar Chart & Waterfall Chart):**
   - Bar chart: `guest_origin_country` on Y-axis, `total_guests` on X-axis.
   - Waterfall chart: USALI Cost Breakdown.

Once completed, click **File ➔ Save As** and save as `ITC_Hotels_Executive_Dashboard.pbix`!
