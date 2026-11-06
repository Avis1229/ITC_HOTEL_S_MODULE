"""
Generates high-quality, professional Jupyter Notebooks for all 4 ITC Hotels analytics modules.
Aligined with BCA Final Year Project Report — Invertis University, Bareilly.
Includes:
1. Relational Database SQL queries (sqlite3)
2. Data cleaning & transformation verification
3. Matplotlib & Seaborn visualizations
4. Academic and executive business interpretations
"""

import os
import nbformat as nbf

BASE_DIR = "/home/goku/ITC_Hotels_Project"

ACADEMIC_HEADER = """**Institution:** Invertis University, Bareilly (Faculty of Computer Applications)  
**Project:** ITC Hotels: Revenue & Business Performance Analysis (BCA Final Year Capstone)  
**Project Team:** Jatin Sagar (BC2023727), Atul Kumar (BC2023590), Darshika Rathore (BC2023687), Muskan Saxena (BC2023061)  
**Project Guide:** Ms. Megha Saxena, Assistant Professor  
**Database:** MySQL 8.0 / SQLite 3NF Database (`itc_hotel_analytics.db`)"""

# ==============================================================================
# MODULE 1: Room Revenue & Occupancy Analytics
# ==============================================================================
def create_module_1():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(f"""# Module 1: Room Revenue & Occupancy Analytics
{ACADEMIC_HEADER}

---
## 1. Executive Summary & Business Context
ITC Hotels is renowned for its luxury hospitality portfolio and *Responsible Luxury* philosophy. Efficient room inventory management is vital for maximizing **RevPAR (Revenue Per Available Room)** while ensuring optimal occupancy throughout seasonal cycles.

This module evaluates room booking patterns, pricing dynamics (ADR), room category upgrades, and reservation stability using both SQL queries and Pandas data structures."""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
import warnings
warnings.filterwarnings('ignore')

# Matplotlib styling - Academic publication style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Load Data via SQL Query from itc_hotel_analytics.db
db_path = '../ITC-Final-Dashboards/itc_hotel_analytics.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    sql_query = \"\"\"
    SELECT 
        r.booking_id,
        r.hotel_name,
        r.arrival_date,
        r.arrival_year,
        r.arrival_month,
        r.arrival_week,
        r.stays_weekend_nights,
        r.stays_week_nights,
        r.total_nights,
        r.reserved_room,
        r.assigned_room,
        r.is_upgraded,
        r.is_canceled,
        r.lead_time,
        i.adr_inr,
        i.room_revenue_inr,
        r.deposit_type,
        r.reservation_status,
        r.status_date,
        r.booking_changes,
        r.days_in_waiting_list
    FROM reservations r
    JOIN invoices i ON r.booking_id = i.booking_id
    \"\"\"
    df_rooms = pd.read_sql_query(sql_query, conn)
    conn.close()
    print(f"✓ Successfully loaded {len(df_rooms):,} records via SQL query from itc_hotel_analytics.db")
else:
    df_rooms = pd.read_csv('itc_room_revenue_occupancy.csv')
    print(f"✓ Loaded {len(df_rooms):,} records from CSV")

df_rooms.head()"""),

        nbf.v4.new_markdown_cell("""## 2. Dataset Hygiene & Core KPI Summary"""),

        nbf.v4.new_code_cell("""total_bookings = len(df_rooms)
confirmed_bookings = len(df_rooms[df_rooms['is_canceled'] == 0])
canceled_bookings = len(df_rooms[df_rooms['is_canceled'] == 1])
cancellation_rate = (canceled_bookings / total_bookings) * 100

total_room_rev_cr = df_rooms['room_revenue_inr'].sum() / 1e7
avg_adr = df_rooms[df_rooms['is_canceled'] == 0]['adr_inr'].mean()
avg_lead_time = df_rooms['lead_time'].mean()
upgrade_rate = df_rooms['is_upgraded'].mean() * 100

print("="*60)
print(f"ITC ROOM REVENUE & OCCUPANCY EXECUTIVE SCORECARD")
print("="*60)
print(f"Total Reservations       : {total_bookings:,}")
print(f"Confirmed Stays          : {confirmed_bookings:,} ({100 - cancellation_rate:.1f}%)")
print(f"Cancellations            : {canceled_bookings:,} ({cancellation_rate:.1f}%)")
print(f"Total Room Revenue       : ₹ {total_room_rev_cr:,.2f} Crores")
print(f"Average Daily Rate (ADR) : ₹ {avg_adr:,.2f} per room night")
print(f"Average Lead Time        : {avg_lead_time:.1f} days")
print(f"Room Upgrade Rate        : {upgrade_rate:.2f}%")
print("="*60)"""),

        nbf.v4.new_markdown_cell("""## 3. Revenue & ADR by ITC Hotel Property Type"""),

        nbf.v4.new_code_cell("""prop_perf = df_rooms[df_rooms['is_canceled'] == 0].groupby('hotel_name').agg(
    confirmed_stays=('booking_id', 'count'),
    total_nights=('total_nights', 'sum'),
    total_revenue_inr=('room_revenue_inr', 'sum'),
    mean_adr=('adr_inr', 'mean')
).reset_index()

prop_perf['revenue_crores'] = prop_perf['total_revenue_inr'] / 1e7
display(prop_perf[['hotel_name', 'confirmed_stays', 'total_nights', 'revenue_crores', 'mean_adr']])

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=prop_perf, x='hotel_name', y='revenue_crores', ax=axes[0], palette=['#1A365D', '#9B2C2C'])
axes[0].set_title('Total Room Revenue by Property Type (₹ Crores)', fontweight='bold')
axes[0].set_ylabel('Revenue (₹ Cr)')
axes[0].set_xlabel('')
axes[0].tick_params(axis='x', rotation=15)

sns.boxplot(data=df_rooms[(df_rooms['is_canceled'] == 0) & (df_rooms['adr_inr'] < 35000)], 
            x='hotel_name', y='adr_inr', ax=axes[1], palette=['#2B6CB0', '#C53030'])
axes[1].set_title('ADR Distribution by Property Type (INR)', fontweight='bold')
axes[1].set_ylabel('ADR (₹)')
axes[1].set_xlabel('')
axes[1].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 4. Room Category Performance & Luxury Upgrade Impact
Analysis of revenue generated across room categories and how upgrades impact guest yield."""),

        nbf.v4.new_code_cell("""room_col = 'assigned_room' if 'assigned_room' in df_rooms.columns else 'assigned_room_category'
room_cat_summary = df_rooms[df_rooms['is_canceled'] == 0].groupby(room_col).agg(
    bookings=('booking_id', 'count'),
    total_revenue_cr=('room_revenue_inr', lambda x: x.sum() / 1e7),
    avg_adr=('adr_inr', 'mean'),
    avg_stay_nights=('total_nights', 'mean')
).sort_values(by='total_revenue_cr', ascending=False).reset_index()

display(room_cat_summary)

plt.figure(figsize=(12, 5))
bars = plt.barh(room_cat_summary[room_col], room_cat_summary['total_revenue_cr'], color='#2D3748', edgecolor='#D69E2E', linewidth=1.2)
plt.title('Room Revenue Contribution by Assigned Category (₹ Crores)', fontweight='bold', fontsize=13)
plt.xlabel('Revenue (₹ Crores)')
plt.ylabel('Room Category')
plt.gca().invert_yaxis()

for bar in bars:
    w = bar.get_width()
    plt.text(w + 0.5, bar.get_y() + bar.get_height()/2, f'₹{w:,.2f} Cr', va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 5. Monthly Seasonality & Occupancy Demand Curve"""),

        nbf.v4.new_code_cell("""month_col = 'arrival_month' if 'arrival_month' in df_rooms.columns else 'arrival_date_month'
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_trend = df_rooms.groupby([month_col, 'is_canceled']).size().unstack(fill_value=0).reindex(month_order)
monthly_trend.columns = ['Confirmed Stays', 'Cancellations']
monthly_trend['Total Demand'] = monthly_trend['Confirmed Stays'] + monthly_trend['Cancellations']
monthly_trend['Cancellation Rate %'] = (monthly_trend['Cancellations'] / monthly_trend['Total Demand']) * 100

fig, ax1 = plt.subplots(figsize=(14, 6))

x = np.arange(len(month_order))
width = 0.35

ax1.bar(x - width/2, monthly_trend['Confirmed Stays'], width, label='Confirmed Stays', color='#2B6CB0')
ax1.bar(x + width/2, monthly_trend['Cancellations'], width, label='Cancellations', color='#E53E3E')
ax1.set_ylabel('Number of Bookings', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels([m[:3] for m in month_order], rotation=0)
ax1.set_title('Monthly Demand & Reservation Cancellation Patterns', fontweight='bold', fontsize=14)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(x, monthly_trend['Cancellation Rate %'], color='#D69E2E', marker='o', linewidth=2.5, label='Cancellation %')
ax2.set_ylabel('Cancellation Rate (%)', color='#D69E2E', fontweight='bold')
ax2.grid(False)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 6. Strategic Takeaways & Academic Recommendations
1. **Dynamic Pricing During Peak Season:** High booking concentration in Oct-Dec warrants a dynamic pricing algorithm.
2. **Cancellation Hedging:** Stricter non-refundable deposit terms during high-demand months can safeguard ₹ Crores in potential lost room yield.
3. **Upsell Optimization:** Premium suites exhibit higher average length of stay (ALOS), providing clear ROI for targeted upgrade promotions at check-in.""")
    ]
    return nb

# ==============================================================================
# MODULE 2: Food, Beverage & Banquet Performance Analytics
# ==============================================================================
def create_module_2():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(f"""# Module 2: Food, Beverage & Banquet Performance Analytics
{ACADEMIC_HEADER}

---
## 1. Executive Summary & Business Context
Culinary excellence is a cornerstone of ITC Hotels' identity, home to award-winning brands like **Bukhara, Dum Pukht, and Peshawri**. MICE (Meetings, Incentives, Conferences, and Exhibitions) and grand weddings held in halls like *The Grand Ballroom* and *Peacock Hall* generate crucial non-room revenue streams.

This notebook evaluates restaurant covers, dining plan profitability, beverage margins, and banquet event yield."""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.figsize'] = (12, 6)

# Load via SQL from itc_hotel_analytics.db
db_path = '../ITC-Final-Dashboards/itc_hotel_analytics.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    sql_query = \"\"\"
    SELECT 
        f.booking_id,
        r.hotel_name,
        r.arrival_date,
        r.arrival_year,
        r.arrival_month,
        r.is_canceled,
        f.dining_plan,
        f.restaurant_outlet,
        f.dining_covers,
        f.food_revenue_inr,
        f.beverage_revenue_inr,
        f.total_fnb_revenue_inr,
        b.banquet_hall,
        b.event_type AS banquet_event_type,
        b.attendees AS banquet_attendees,
        b.banquet_revenue_inr,
        (f.total_fnb_revenue_inr + COALESCE(b.banquet_revenue_inr, 0)) AS combined_fnb_banquet_rev_inr
    FROM fnb_orders f
    JOIN reservations r ON f.booking_id = r.booking_id
    LEFT JOIN banquet_events b ON f.booking_id = b.booking_id
    \"\"\"
    df_fnb = pd.read_sql_query(sql_query, conn)
    conn.close()
    print(f"✓ Successfully loaded {len(df_fnb):,} records via SQL query")
else:
    df_fnb = pd.read_csv('itc_fnb_banquet_performance.csv')
    print(f"✓ Loaded {len(df_fnb):,} records from CSV")

df_fnb.head()"""),

        nbf.v4.new_markdown_cell("""## 2. F&B Executive Scorecard"""),

        nbf.v4.new_code_cell("""valid_fnb = df_fnb[df_fnb['is_canceled'] == 0]
tot_fnb_cr = valid_fnb['total_fnb_revenue_inr'].sum() / 1e7
tot_food_cr = valid_fnb['food_revenue_inr'].sum() / 1e7
tot_bev_cr = valid_fnb['beverage_revenue_inr'].sum() / 1e7
tot_banq_cr = valid_fnb['banquet_revenue_inr'].sum() / 1e7
tot_combined_cr = valid_fnb['combined_fnb_banquet_rev_inr'].sum() / 1e7
total_covers = valid_fnb['dining_covers'].sum()

print("="*60)
print(f"ITC F&B AND BANQUET PERFORMANCE SCORECARD")
print("="*60)
print(f"Total Dining Covers Served: {total_covers:,}")
print(f"Food Revenue              : ₹ {tot_food_cr:,.2f} Crores")
print(f"Beverage Revenue          : ₹ {tot_bev_cr:,.2f} Crores")
print(f"Total Restaurant F&B Rev  : ₹ {tot_fnb_cr:,.2f} Crores")
print(f"Total Banquet Event Rev   : ₹ {tot_banq_cr:,.2f} Crores")
print(f"Combined F&B Portfolio Rev: ₹ {tot_combined_cr:,.2f} Crores")
print("="*60)"""),

        nbf.v4.new_markdown_cell("""## 3. Signature Restaurant Outlet Revenue Contribution"""),

        nbf.v4.new_code_cell("""rest_perf = valid_fnb[valid_fnb['dining_covers'] > 0].groupby('restaurant_outlet').agg(
    total_covers=('dining_covers', 'sum'),
    food_rev_cr=('food_revenue_inr', lambda x: x.sum() / 1e7),
    bev_rev_cr=('beverage_revenue_inr', lambda x: x.sum() / 1e7),
    total_rev_cr=('total_fnb_revenue_inr', lambda x: x.sum() / 1e7)
).sort_values(by='total_rev_cr', ascending=False).reset_index()

display(rest_perf)

fig, ax = plt.subplots(figsize=(12, 5))
x = np.arange(len(rest_perf))
width = 0.35

ax.bar(x - width/2, rest_perf['food_rev_cr'], width, label='Food Revenue (₹ Cr)', color='#2B6CB0')
ax.bar(x + width/2, rest_perf['bev_rev_cr'], width, label='Beverage Revenue (₹ Cr)', color='#D69E2E')
ax.set_xticks(x)
ax.set_xticklabels(rest_perf['restaurant_outlet'], rotation=15, fontweight='bold')
ax.set_ylabel('Revenue (₹ Crores)', fontweight='bold')
ax.set_title('Revenue Breakdown by Signature Restaurant Brand', fontweight='bold', fontsize=14)
ax.legend()
plt.tight_layout()
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 4. Banquet Event Analysis & MICE Contribution"""),

        nbf.v4.new_code_cell("""banq_data = valid_fnb[valid_fnb['banquet_event_type'].notna() & (valid_fnb['banquet_event_type'] != 'None')]
event_summary = banq_data.groupby('banquet_event_type').agg(
    events_hosted=('booking_id', 'count'),
    total_attendees=('banquet_attendees', 'sum'),
    revenue_cr=('banquet_revenue_inr', lambda x: x.sum() / 1e7)
).sort_values(by='revenue_cr', ascending=False).reset_index()

display(event_summary)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=event_summary, x='banquet_event_type', y='revenue_cr', ax=axes[0], palette='Blues_r')
axes[0].set_title('Banquet Revenue by Event Type (₹ Cr)', fontweight='bold')
axes[0].set_ylabel('Revenue (₹ Cr)')
axes[0].set_xlabel('')
axes[0].tick_params(axis='x', rotation=25)

n_events = len(event_summary)
explode = [0.03] * n_events
axes[1].pie(event_summary['revenue_cr'], labels=event_summary['banquet_event_type'], 
            autopct='%1.1f%%', startangle=140, colors=sns.color_palette('tab10', n_events),
            explode=explode)
axes[1].set_title('Banquet Revenue Share', fontweight='bold')

plt.tight_layout()
plt.show()""")
    ]
    return nb

# ==============================================================================
# MODULE 3: Guest Demographics & Booking Channel Analytics
# ==============================================================================
def create_module_3():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(f"""# Module 3: Guest Demographics & Booking Channel Analytics
{ACADEMIC_HEADER}

---
## 1. Executive Summary & Business Context
Understanding guest personas and booking origin channels is vital for customer acquisition cost (CAC) reduction and Club ITC loyalty retention.

This notebook assesses customer origin geographies, channel dependencies (Direct vs OTA vs Corporate), and loyalty tier engagement."""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.figsize'] = (12, 6)

# Load via SQL from itc_hotel_analytics.db
db_path = '../ITC-Final-Dashboards/itc_hotel_analytics.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    sql_query = \"\"\"
    SELECT 
        g.booking_id,
        r.hotel_name,
        r.arrival_date,
        r.arrival_year,
        r.arrival_month,
        r.is_canceled,
        g.country_code AS guest_origin_country,
        g.geographic_region,
        g.guest_profile,
        g.adults,
        g.children,
        g.babies,
        g.total_guests,
        g.customer_type,
        g.loyalty_tier AS loyalty_program_tier,
        g.is_repeated_guest,
        g.previous_cancellations,
        g.previous_bookings_not_canceled,
        r.channel AS channel_clean,
        r.market_segment AS market_segment_clean,
        r.lead_time,
        g.special_requests AS total_of_special_requests
    FROM guests g
    JOIN reservations r ON g.booking_id = r.booking_id
    \"\"\"
    df_demo = pd.read_sql_query(sql_query, conn)
    conn.close()
    print(f"✓ Successfully loaded {len(df_demo):,} records via SQL query")
else:
    df_demo = pd.read_csv('itc_guest_demographics_channels.csv')
    print(f"✓ Loaded {len(df_demo):,} records from CSV")

df_demo.head()"""),

        nbf.v4.new_markdown_cell("""## 2. Guest Profile & Persona Segmentation"""),

        nbf.v4.new_code_cell("""persona_summary = df_demo[df_demo['is_canceled'] == 0].groupby('guest_profile').agg(
    stays=('booking_id', 'count'),
    repeat_guests=('is_repeated_guest', 'sum'),
    avg_lead_time=('lead_time', 'mean'),
    special_reqs=('total_of_special_requests', 'sum')
).sort_values(by='stays', ascending=False).reset_index()

display(persona_summary)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=persona_summary, x='guest_profile', y='stays', ax=axes[0], palette='crest')
axes[0].set_title('Guest Distribution by Profile Segment', fontweight='bold')
axes[0].set_ylabel('Total Stays')
axes[0].set_xlabel('')
axes[0].tick_params(axis='x', rotation=15)

axes[1].pie(persona_summary['stays'], labels=persona_summary['guest_profile'], 
            autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(persona_summary)),
            explode=[0.02]*len(persona_summary))
axes[1].set_title('Guest Segment Proportions', fontweight='bold')

plt.tight_layout()
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 3. Booking Channel Dependency & OTA Commission Risk"""),

        nbf.v4.new_code_cell("""channel_summary = df_demo.groupby('channel_clean').agg(
    total_bookings=('booking_id', 'count'),
    confirmed_stays=('is_canceled', lambda x: (x == 0).sum()),
    cancellations=('is_canceled', lambda x: (x == 1).sum()),
    cancellation_rate=('is_canceled', lambda x: x.mean() * 100),
    avg_lead_time=('lead_time', 'mean')
).sort_values(by='total_bookings', ascending=False).reset_index()

display(channel_summary)

plt.figure(figsize=(12, 5))
sns.barplot(data=channel_summary, x='channel_clean', y='cancellation_rate', palette='Reds_r')
plt.title('Cancellation Rate (%) Across Booking Channels', fontweight='bold', fontsize=13)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Distribution Channel')
plt.axhline(df_demo['is_canceled'].mean()*100, color='navy', linestyle='--', label=f'Avg Cancellation ({df_demo["is_canceled"].mean()*100:.1f}%)')
plt.legend()
plt.tight_layout()
plt.show()""")
    ]
    return nb

# ==============================================================================
# MODULE 4: Operating Costs & Profitability Analytics
# ==============================================================================
def create_module_4():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(f"""# Module 4: Operating Costs & Profitability Analytics
{ACADEMIC_HEADER}

---
## 1. Executive Summary & Business Context
Hospitality profitability requires adhering to the **USALI (Uniform System of Accounts for the Lodging Industry)** framework. Net yield depends on managing room operating expenses, F&B COGS, energy/utility expenses, and booking commissions.

This notebook models Gross Operating Profit (GOP), expense variance, and Net Profit Margin % across properties."""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.figsize'] = (12, 6)

# Load via SQL from itc_hotel_analytics.db
db_path = '../ITC-Final-Dashboards/itc_hotel_analytics.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    sql_query = \"\"\"
    SELECT 
        oc.booking_id,
        r.hotel_name,
        r.arrival_date,
        r.arrival_year,
        r.arrival_month,
        r.is_canceled,
        oc.billed_nights,
        i.room_revenue_inr,
        (i.fnb_revenue_inr + i.banquet_revenue_inr) AS combined_fnb_banquet_rev_inr,
        i.minor_dept_revenue_inr,
        i.gross_total_revenue_inr AS gross_total_revenue_inr,
        oc.rooms_operating_cost AS rooms_operating_cost_inr,
        oc.fnb_cogs_cost AS fnb_cogs_operating_cost_inr,
        oc.distribution_commission AS booking_distribution_commission_inr,
        oc.energy_utility_cost AS energy_utility_cost_inr,
        oc.staff_payroll_cost AS staff_payroll_allocated_inr,
        oc.maintenance_cost AS property_maintenance_inr,
        oc.marketing_cost AS marketing_brand_cost_inr,
        oc.total_operating_expenses AS total_operating_expenses_inr,
        oc.gross_operating_profit AS gross_operating_profit_inr,
        oc.net_profit_margin_pct
    FROM operating_costs oc
    JOIN reservations r ON oc.booking_id = r.booking_id
    JOIN invoices i ON oc.booking_id = i.booking_id
    \"\"\"
    df_cost = pd.read_sql_query(sql_query, conn)
    conn.close()
    print(f"✓ Successfully loaded {len(df_cost):,} records via SQL query")
else:
    df_cost = pd.read_csv('itc_operating_costs_profitability.csv')
    print(f"✓ Loaded {len(df_cost):,} records from CSV")

df_cost.head()"""),

        nbf.v4.new_markdown_cell("""## 2. Financial Performance & GOP Executive Scorecard"""),

        nbf.v4.new_code_cell("""valid_cost = df_cost[df_cost['is_canceled'] == 0]

gross_rev_cr = valid_cost['gross_total_revenue_inr'].sum() / 1e7
total_exp_cr = valid_cost['total_operating_expenses_inr'].sum() / 1e7
gop_cr = valid_cost['gross_operating_profit_inr'].sum() / 1e7
avg_gop_margin = (gop_cr / gross_rev_cr) * 100

print("="*60)
print(f"ITC HOTELS USALI PROFITABILITY SCORECARD")
print("="*60)
print(f"Gross Portfolio Revenue    : ₹ {gross_rev_cr:,.2f} Crores")
print(f"Total Operating Expenses   : ₹ {total_exp_cr:,.2f} Crores")
print(f"Gross Operating Profit (GOP): ₹ {gop_cr:,.2f} Crores")
print(f"GOP Margin                 : {avg_gop_margin:.2f}%")
print("="*60)"""),

        nbf.v4.new_markdown_cell("""## 3. USALI Operating Expense Breakdown"""),

        nbf.v4.new_code_cell("""expense_cols = {
    'Rooms Operations': valid_cost['rooms_operating_cost_inr'].sum() / 1e7,
    'F&B COGS': valid_cost['fnb_cogs_operating_cost_inr'].sum() / 1e7,
    'OTA Commission': valid_cost['booking_distribution_commission_inr'].sum() / 1e7,
    'Energy & Utilities': valid_cost['energy_utility_cost_inr'].sum() / 1e7,
    'Staff Payroll': valid_cost['staff_payroll_allocated_inr'].sum() / 1e7,
    'Property Maintenance': valid_cost['property_maintenance_inr'].sum() / 1e7,
    'Brand & Marketing': valid_cost['marketing_brand_cost_inr'].sum() / 1e7,
}

df_exp = pd.DataFrame(list(expense_cols.items()), columns=['Expense Category', 'Amount_Cr']).sort_values(by='Amount_Cr', ascending=False)
display(df_exp)

plt.figure(figsize=(12, 5))
bars = plt.barh(df_exp['Expense Category'], df_exp['Amount_Cr'], color='#C53030', edgecolor='#742A2A')
plt.title('Operating Expense Distribution by USALI Cost Center (₹ Crores)', fontweight='bold', fontsize=13)
plt.xlabel('Expense (₹ Crores)')
plt.gca().invert_yaxis()

for bar in bars:
    w = bar.get_width()
    plt.text(w + 0.2, bar.get_y() + bar.get_height()/2, f'₹{w:,.2f} Cr', va='center', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.show()""")
    ]
    return nb

# ==============================================================================
# MAIN GENERATOR
# ==============================================================================
if __name__ == "__main__":
    targets = [
        ("ITC-Room-Analytics/module1_room_revenue_occupancy.ipynb", create_module_1()),
        ("ITC-FnB-Analytics/module2_fnb_banquet_performance.ipynb", create_module_2()),
        ("ITC-Guest-Demographics/module3_guest_demographics_channels.ipynb", create_module_3()),
        ("ITC-Profitability-Costs/module4_operating_costs_profitability.ipynb", create_module_4()),
    ]
    
    for path, nb in targets:
        full_path = os.path.join(BASE_DIR, path)
        with open(full_path, "w") as f:
            nbf.write(nb, f)
        print(f"✅ Generated: {path}")
