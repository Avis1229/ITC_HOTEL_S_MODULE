# 📊 ITC Hotels Analytics — Power BI with SQL Database Integration Guide
**Invertis University, Bareilly | BCA Final Year Capstone Project**  
**Project:** *ITC Hotels: Revenue & Business Performance Analysis*  
**Database:** MySQL 8.0 / SQLite 3NF Schema (`itc_hotel_analytics.db` & `itc_hotels_mysql_dump.sql`)

---

## 📌 1. Overview & Architecture

According to the BCA Final Year Project Report (**Appendix B: Figure B.1 & Appendix D: Figures D1, D2**), the reporting model is powered by a relational SQL database. 

Power BI connects directly to the SQL database using a **Star Schema** architecture:

```
                  ┌────────────────────┐
                  │   dim_calendar     │
                  │   (Date Dimension) │
                  └─────────┬──────────┘
                            │ 1
                            │
                            │ *
┌─────────────────┐ 1     * ┌────────────────────┐ *     1 ┌─────────────────┐
│  dim_properties ├─────────┤   fact_bookings    ├─────────┤    dim_rooms    │
│  (Hotels Info)  │         │   (Reservations)   │         │  (Categories)   │
└────────┬────────┘         └────────────────────┘         └─────────────────┘
         │ 1                         *
         │                           │
         │ *                         │
┌────────┴──────────────┐            │
│  fact_room_inventory  ├────────────┘
│  (Daily Occupancy)    │
└───────────────────────┘
```

---

## 🔌 2. How to Connect Power BI to the SQL Database

You have two simple options when running Windows:

### Option A: Connect to MySQL (Recommended if XAMPP is installed)
1. Open **XAMPP Control Panel** on Windows and click **Start** next to MySQL.
2. Open phpMyAdmin (`http://localhost/phpmyadmin`) or MySQL Command Line.
3. Import the provided SQL script:
   ```bash
   mysql -u root itc_hotels_db < itc_hotels_mysql_dump.sql
   ```
4. Open **Power BI Desktop** on Windows.
5. Click **Get Data** → **MySQL Database**.
6. Server: `localhost` | Database: `itc_hotels_db`.
7. Data Connectivity mode: Select **Import**.
8. Select the tables: `properties`, `rooms`, `calendar`, `bookings`, `room_inventory`, `kpi_monthly`.
9. Click **Load**.

### Option B: Connect to SQLite directly via ODBC
1. Install the free **SQLite ODBC Driver** on Windows (download from `http://www.ch-werner.de/sqliteodbc/` - `sqliteodbc_w64.exe`).
2. Open **ODBC Data Source Administrator (64-bit)** in Windows.
3. In **System DSN**, click **Add** → select **SQLite3 ODBC Driver**.
4. Data Source Name: `ITC_Hotels_DB` | Database Name: Browse to `itc_hotel_analytics.db`.
5. Open **Power BI Desktop** → **Get Data** → **ODBC** → select `ITC_Hotels_DB`.
6. Click **Connect** and select the tables!

### Option C: Direct SQL Query Import (Instant & Zero Configuration)
In Power BI Desktop, click **Get Data** → **Blank Query** or use Python Script connector:
```python
import sqlite3
import pandas as pd
conn = sqlite3.connect(r'C:\path\to\itc_hotel_analytics.db')
bookings = pd.read_sql_query('SELECT * FROM bookings', conn)
properties = pd.read_sql_query('SELECT * FROM properties', conn)
room_inventory = pd.read_sql_query('SELECT * FROM room_inventory', conn)
calendar = pd.read_sql_query('SELECT * FROM calendar', conn)
rooms = pd.read_sql_query('SELECT * FROM rooms', conn)
```

---

## 📐 3. Data Model Relationships (Model View in Power BI)

Switch to **Model View** (left sidebar icon) and configure these 1-to-Many (`1:*`) relationships:

| From Table (Dimension) | From Column | To Table (Fact) | To Column | Cardinality | Cross Filter |
|------------------------|-------------|-----------------|-----------|-------------|--------------|
| `properties` | `property_id` | `bookings` | `property_id` | 1 to Many (`1:*`) | Single |
| `properties` | `property_id` | `room_inventory` | `property_id` | 1 to Many (`1:*`) | Single |
| `calendar` | `date_val` | `bookings` | `check_in_date` | 1 to Many (`1:*`) | Single |
| `calendar` | `date_val` | `room_inventory` | `check_in_date` | 1 to Many (`1:*`) | Single |

---

## 🧮 4. Key DAX Measures (Table: `Financial_Measures`)

Create a dedicated blank table named `Financial_Measures` (Modeling → New Table → `Financial_Measures = ROW("Name", "KPIs")`).  
Then right-click and add these official measures from the report:

### 4.1 Revenue & Booking Measures
```dax
-- Total Bookings
Total Bookings = COUNTROWS(bookings)

-- Total Successful Bookings (Checked Out)
Total Successful Bookings = 
CALCULATE(
    COUNTROWS(bookings),
    bookings[booking_status] = "Checked Out"
)

-- Total Cancelled Bookings
Total Cancellations = 
CALCULATE(
    COUNTROWS(bookings),
    bookings[booking_status] = "Cancelled"
)

-- Cancellation Rate %
Cancellation Rate % = 
DIVIDE([Total Cancellations], [Total Bookings], 0)

-- Total Revenue Generated (Gross Billed)
Total Revenue Generated = SUM(bookings[revenue_generated])

-- Total Revenue Realized (Actual Collected)
Total Revenue Realized = SUM(bookings[revenue_realized])

-- Total Revenue Lost to Cancellations
Total Revenue Lost = 
CALCULATE(
    SUM(bookings[revenue_generated]),
    bookings[booking_status] = "Cancelled"
)

-- Realisation Rate %
Realisation % = 
DIVIDE([Total Revenue Realized], [Total Revenue Generated], 0)
```

### 4.2 Capacity & Occupancy Measures
```dax
-- Total Room Capacity
Total Capacity = SUM(room_inventory[capacity])

-- Daily Sellable Room Nights (DSRN)
DSRN = SUM(room_inventory[capacity])

-- Daily Utilized Room Nights (DURN)
DURN = SUM(room_inventory[successful_bookings])

-- Occupancy Rate %
Occupancy % = 
DIVIDE([DURN], [DSRN], 0)

-- Rolling 7-Day Occupancy %
Rolling 7D Occupancy % = 
VAR CurrentDate = MAX(calendar[date_val])
RETURN
CALCULATE(
    [Occupancy %],
    DATESINPERIOD(calendar[date_val], CurrentDate, -7, DAY)
)
```

### 4.3 Key Hospitality Performance Indicators (ADR & RevPAR)
```dax
-- Average Daily Rate (ADR)
ADR = 
DIVIDE([Total Revenue Realized], [Total Successful Bookings], 0)

-- Revenue Per Available Room (RevPAR)
RevPAR = 
DIVIDE([Total Revenue Realized], [Total Capacity], 0)

-- Average Length of Stay (ALOS)
ALOS = 
AVERAGEX(
    FILTER(bookings, bookings[booking_status] = "Checked Out"),
    DATEDIFF(bookings[check_in_date], bookings[checkout_date], DAY)
)

-- Average Lead Time
Avg Lead Time = AVERAGE(bookings[lead_time])
```

### 4.4 Growth & Trend Measures
```dax
-- Month-over-Month Revenue Growth %
MoM Revenue Growth % = 
VAR PreviousMonthRev = 
    CALCULATE([Total Revenue Realized], DATEADD(calendar[date_val], -1, MONTH))
RETURN
    DIVIDE([Total Revenue Realized] - PreviousMonthRev, PreviousMonthRev, 0)

-- Week-over-Week Revenue Growth %
WoW Revenue Growth % = 
VAR PreviousWeekRev = 
    CALCULATE([Total Revenue Realized], DATEADD(calendar[date_val], -7, DAY))
RETURN
    DIVIDE([Total Revenue Realized] - PreviousWeekRev, PreviousWeekRev, 0)
```

---

## 🎨 5. Building the 5 Report Pages (Matching PDF Appendices)

Apply the luxury dark palette using **`itc_luxury_theme.json`** (**View → Themes → Browse for themes**).

### Page 1: Room Category Performance & Category Insights (Figure A.1)
- **Top Slicers:** `city`, `Property Name`, `lead_time (days)`, `check_in_date range`, `room_category`
- **Left Bar Chart:** `Total Revenue Generated by room_category`
- **Center Bar Chart:** `Total Revenue Generated by lead_time`
- **Right Line Chart:** `ALOS by Room Class`
- **Bottom Left KPI Cards:** 
  - Total Revenue Generated (`₹70.24M`)
  - Avg Lead Time (`4.58`)
  - Avg ALOS (`2.76`)
- **Bottom Right Tables:** 
  - `Month_Name`, `Total_Revenue_Generated`, `MoM_Growth%`
  - `Week_of_Year`, `Total_Revenue_Generated`, `WoW_Growth%`

### Page 2: Occupancy & Capacity Analysis (Figure A.2)
- **Top Summary Table:** Date, Occupancy Rate %, Rolling 7D Occupancy %
- **Property Comparison Table:** `property_id`, `property_name`, `Occupancy Rate`
- **Left KPI Cards:**
  - `Occupancy Rate %` (Gauge / Card)
  - `Rooms Available`
  - `Avg Rooms Sold / Day`
  - `WoW % Occupancy`
  - `Monthly Occupancy %`
- **Donut Visual:** `Occupancy Rate by room_category`
- **Line Charts:**
  - `Monthly Occupancy Rate`
  - `Occupancy Rate by Week of Year`
  - `Occupancy Rate, RevPAR and Avg Rooms Sold / Day by property`

### Page 3: Cancellations & Lost Revenue Analysis (Figure A.3)
- **Top Line Trend:** `Cancellation Rate by booking_date`
- **KPI Cards:**
  - `Total Cancellations` (Card: e.g. 619)
  - `Revenue Lost` (Card: e.g. ₹7.6M)
  - `Cancellation Rate %` (Card: 25.72%)
  - `WoW Cancellation Rate %`
- **Center Bar Visual:** `Total Cancellations & Revenue Lost by property and room_category`
- **Bottom Detailed Matrix Tables:**
  - `Week of Year`, `WoW Cancellations`, `Cumulative Cancellations`
  - `Date`, `Cancellations`, `Cumulative Cancellations`
  - `Week of Year`, `Revenue Lost`, `Cumulative Revenue Lost`

### Page 4: Financial Overview & Performance (Figure A.4)
- **Top Metric Cards:**
  - `Cumulative Running Total Revenue`
  - `MoM Growth %`
  - `WoW Growth %`
  - `ADR`
  - `RevPAR`
- **Charts:**
  - `Total Revenue Realized & Generated by Date` (Dual Line/Bar)
  - `MoM & WoW Growth Trend` (Line chart)
  - `Total Revenue Generated by room_category` (Donut chart)
  - `Total Revenue Generated by category and property_name` (Horizontal bar)

### Page 5: Master Executive KPI Dashboard (Dark Mode Overview)
- **Top 4 Square KPI Cards:**
  1. `Gross Revenue (₹298.4 Cr)`
  2. `Gross Operating Profit (₹143.7 Cr)`
  3. `Average Occupancy (62.9%)`
  4. `F&B + Banquet Sales (₹104.8 Cr)`
- **Visuals:**
  - Monthly Occupancy vs Cancellations (Multi-Bar)
  - USALI Waterfall Profit Analysis
  - Channel Revenue Share (Donut Chart)
  - City/Property Performance Matrix

---

## 💡 6. Viva Defense Points (Professor Questions)

1. **"How does your Power BI dashboard connect to SQL?"**
   > *"We structured our schema into Third Normal Form (3NF) in MySQL/SQLite with 12 entities. For Power BI, we exposed star-schema fact and dimension tables (`fact_bookings`, `dim_properties`, `dim_rooms`, `dim_calendar`). Power BI queries this SQL database directly via ODBC/MySQL connector, calculating industry-standard DAX metrics like RevPAR, ADR, and DURN in real-time."*

2. **"Why use a Star Schema instead of one big flat CSV?"**
   > *"A flat file creates massive data duplication and slow refresh times. Our star schema separates dimensions (`properties`, `rooms`, `calendar`) from transactional facts (`bookings`, `room_inventory`), enabling 1-to-many relationships, faster DAX calculation, and seamless slicer filtering across multiple properties without memory bottlenecks."*
