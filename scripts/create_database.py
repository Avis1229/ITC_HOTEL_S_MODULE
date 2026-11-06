"""
ITC Hotels Revenue & Business Performance Analysis
====================================================
Database Creation Script - SQLite (3NF Normalized Schema)
Creates 12 tables, cleans raw Kaggle data, and imports into SQL database.

Author: Avi Singh (Jatin Sagar Group)
University: Invertis University, Bareilly
"""

import sqlite3
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

# ----- Paths -----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_CSV = os.path.join(BASE_DIR, 'archive', 'hotel_bookings.csv')
DB_PATH = os.path.join(BASE_DIR, 'ITC-Final-Dashboards', 'itc_hotel_analytics.db')

# Module CSVs
ROOM_CSV = os.path.join(BASE_DIR, 'ITC-Room-Analytics', 'itc_room_revenue_occupancy.csv')
FNB_CSV  = os.path.join(BASE_DIR, 'ITC-FnB-Analytics', 'itc_fnb_banquet_performance.csv')
DEMO_CSV = os.path.join(BASE_DIR, 'ITC-Guest-Demographics', 'itc_guest_demographics_channels.csv')
COST_CSV = os.path.join(BASE_DIR, 'ITC-Profitability-Costs', 'itc_operating_costs_profitability.csv')

print("=" * 60)
print("ITC Hotels - SQL Database Builder")
print("=" * 60)

# ===== STEP 1: Load Raw Kaggle Data =====
print("\n[1/6] Loading raw Kaggle dataset...")
raw_df = pd.read_csv(RAW_CSV)
print(f"  Loaded {len(raw_df)} rows, {len(raw_df.columns)} columns")

# ===== STEP 2: Data Cleaning =====
print("\n[2/6] Cleaning raw data...")

# 2a. Check for nulls
null_counts = raw_df.isnull().sum()
null_cols = null_counts[null_counts > 0]
print(f"  Columns with nulls: {len(null_cols)}")
for col, cnt in null_cols.items():
    print(f"    - {col}: {cnt} nulls ({cnt/len(raw_df)*100:.1f}%)")

# 2b. Handle missing values
# 'children' column has 4 nulls - fill with 0 (no children)
if 'children' in raw_df.columns:
    raw_df['children'] = raw_df['children'].fillna(0).astype(int)
    
# 'agent' and 'company' have NULL string values from Kaggle
raw_df['agent'] = raw_df['agent'].replace('NULL', np.nan)
raw_df['company'] = raw_df['company'].replace('NULL', np.nan)

# 2c. Fix negative ADR values (data anomaly in Kaggle dataset)
neg_adr = (raw_df['adr'] < 0).sum()
if neg_adr > 0:
    print(f"  Fixed {neg_adr} negative ADR values (set to median)")
    median_adr = raw_df.loc[raw_df['adr'] >= 0, 'adr'].median()
    raw_df.loc[raw_df['adr'] < 0, 'adr'] = median_adr

# 2d. Fix zero-night stays where guests actually checked out
zero_nights = ((raw_df['stays_in_weekend_nights'] == 0) & 
               (raw_df['stays_in_week_nights'] == 0) &
               (raw_df['reservation_status'] == 'Check-Out')).sum()
print(f"  Zero-night check-outs found: {zero_nights}")

# 2e. Remove extreme outlier ADR (>5000 EUR per night = data entry error)
outlier_adr = (raw_df['adr'] > 5000).sum()
if outlier_adr > 0:
    print(f"  Capped {outlier_adr} extreme ADR outliers to 5000")
    raw_df.loc[raw_df['adr'] > 5000, 'adr'] = 5000

# 2f. Create proper date column
raw_df['arrival_date'] = pd.to_datetime(
    raw_df['arrival_date_year'].astype(str) + '-' +
    raw_df['arrival_date_month'] + '-' +
    raw_df['arrival_date_day_of_month'].astype(str),
    format='%Y-%B-%d'
)

# 2g. Total nights
raw_df['total_nights'] = raw_df['stays_in_weekend_nights'] + raw_df['stays_in_week_nights']

# 2h. Remove duplicate bookings (if any)
dupes = raw_df.duplicated().sum()
if dupes > 0:
    print(f"  Removed {dupes} duplicate rows")
    raw_df = raw_df.drop_duplicates().reset_index(drop=True)
else:
    print(f"  No duplicate rows found")

# 2i. Data type fixes
raw_df['is_canceled'] = raw_df['is_canceled'].astype(int)
raw_df['is_repeated_guest'] = raw_df['is_repeated_guest'].astype(int)
raw_df['reservation_status_date'] = pd.to_datetime(raw_df['reservation_status_date'])

print(f"  Cleaning complete. Final shape: {raw_df.shape}")

# ===== STEP 3: ITC Hotels Domain Transformation =====
print("\n[3/6] Applying ITC Hotels domain transformation...")

EUR_TO_INR = 85  # conversion factor

# Hotel name mapping (Resort/City → ITC property)
hotel_map = {
    'Resort Hotel': 'ITC Grand Bharat (Luxury Resort)',
    'City Hotel': 'ITC Maurya (City Hotel)'
}
raw_df['hotel_name'] = raw_df['hotel'].map(hotel_map)

# Room category mapping
room_map = {
    'A': 'ITC One Luxury Room', 'B': 'Towers Club Room',
    'C': 'Executive Suite', 'D': 'Premium Room',
    'E': 'Deluxe Room', 'F': 'Superior Room',
    'G': 'Standard Room', 'H': 'Studio Room',
    'I': 'Heritage Room', 'L': 'Presidential Suite',
    'K': 'Presidential Suite', 'P': 'Penthouse Suite'
}
raw_df['reserved_room_category'] = raw_df['reserved_room_type'].map(room_map).fillna('Standard Room')
raw_df['assigned_room_category'] = raw_df['assigned_room_type'].map(room_map).fillna('Standard Room')

# Convert ADR to INR
raw_df['adr_inr'] = round(raw_df['adr'] * EUR_TO_INR, 2)
raw_df['room_revenue_inr'] = round(raw_df['adr_inr'] * raw_df['total_nights'], 2)

# Generate booking IDs
raw_df['booking_id'] = [f'ITC-{yr}-{str(i).zfill(6)}' 
                         for i, yr in enumerate(raw_df['arrival_date_year'], 1)]

# Guest origin country cleanup
raw_df['country'] = raw_df['country'].fillna('Unknown')

# Geographic region mapping
region_map = {
    'PRT': 'Europe', 'GBR': 'Europe', 'FRA': 'Europe', 'ESP': 'Europe',
    'DEU': 'Europe', 'ITA': 'Europe', 'IRL': 'Europe', 'NLD': 'Europe',
    'BEL': 'Europe', 'CHE': 'Europe', 'AUT': 'Europe', 'NOR': 'Europe',
    'SWE': 'Europe', 'POL': 'Europe', 'ROU': 'Europe', 'RUS': 'Europe',
    'USA': 'North America', 'CAN': 'North America',
    'BRA': 'South America', 'ARG': 'South America', 'COL': 'South America',
    'CHN': 'Asia Pacific', 'JPN': 'Asia Pacific', 'KOR': 'Asia Pacific',
    'IND': 'South Asia', 'LKA': 'South Asia', 'BGD': 'South Asia',
    'AUS': 'Oceania', 'NZL': 'Oceania',
    'ZAF': 'Africa', 'MAR': 'Africa', 'NGA': 'Africa',
    'ISR': 'Middle East', 'ARE': 'Middle East', 'SAU': 'Middle East',
}
raw_df['geographic_region'] = raw_df['country'].map(region_map).fillna('Other')

# Loyalty tier
conditions = [
    raw_df['is_repeated_guest'] == 1,
    raw_df['previous_bookings_not_canceled'] >= 5,
    raw_df['previous_bookings_not_canceled'] >= 2,
]
choices = ['Club ITC Platinum', 'Club ITC Gold', 'Club ITC Silver']
raw_df['loyalty_tier'] = np.select(conditions, choices, default='Standard Guest')

# F&B data generation (derived from room revenue - since Kaggle doesn't have F&B)
np.random.seed(42)
meal_map = {'BB': 'Bed & Breakfast', 'HB': 'Half Board', 'FB': 'Full Board',
            'SC': 'Self Catering', 'Undefined': 'Room Only'}
raw_df['dining_plan'] = raw_df['meal'].map(meal_map).fillna('Room Only')

restaurants = ['Bukhara', 'Dum Pukht', 'Pavilion', 'Pan Asian', 'West View', 'Peshawri']
raw_df['restaurant_outlet'] = np.random.choice(restaurants, len(raw_df))

raw_df['dining_covers'] = np.where(
    raw_df['dining_plan'] != 'Room Only',
    (raw_df['adults'] + raw_df['children'].fillna(0)).astype(int),
    0
)
raw_df['food_revenue_inr'] = np.where(
    raw_df['dining_plan'] != 'Room Only',
    np.round(raw_df['adr_inr'] * np.random.uniform(0.25, 0.45, len(raw_df)), 2),
    0
)
raw_df['beverage_revenue_inr'] = np.round(raw_df['food_revenue_inr'] * np.random.uniform(0.15, 0.35, len(raw_df)), 2)
raw_df['total_fnb_revenue_inr'] = raw_df['food_revenue_inr'] + raw_df['beverage_revenue_inr']

# Banquet data
banquet_halls = ['Mughal Hall', 'Peacock Hall', 'The Grand Ballroom', 'Rajputana Hall', None]
events = ['Corporate Conference', 'Wedding Reception', 'Board Meeting', 'Gala Dinner', 'Product Launch', None]
raw_df['banquet_hall'] = np.random.choice(banquet_halls, len(raw_df))
raw_df['banquet_event_type'] = np.where(raw_df['banquet_hall'].notna() & (raw_df['banquet_hall'] != 'None'),
                                         np.random.choice([e for e in events if e], len(raw_df)), None)
raw_df['banquet_attendees'] = np.where(raw_df['banquet_event_type'].notna(),
                                        np.random.randint(20, 300, len(raw_df)), 0)
raw_df['banquet_revenue_inr'] = np.where(raw_df['banquet_event_type'].notna(),
                                          np.round(raw_df['banquet_attendees'] * np.random.uniform(800, 2500, len(raw_df)), 2), 0)

# Operating costs (USALI framework)
billed_nights = np.maximum(raw_df['total_nights'], 1)
raw_df['rooms_cost'] = np.round(billed_nights * np.random.uniform(550, 800, len(raw_df)), 2)
raw_df['fnb_cogs'] = np.round(raw_df['total_fnb_revenue_inr'] * 0.31, 2)
raw_df['distribution_commission'] = np.round(raw_df['room_revenue_inr'] * np.random.uniform(0.08, 0.18, len(raw_df)), 2)
raw_df['energy_cost'] = np.round(billed_nights * np.random.uniform(500, 850, len(raw_df)), 2)
raw_df['staff_cost'] = np.round(billed_nights * np.random.uniform(750, 1200, len(raw_df)), 2)
raw_df['maintenance_cost'] = np.round(billed_nights * np.random.uniform(150, 400, len(raw_df)), 2)
raw_df['marketing_cost'] = np.round(raw_df['room_revenue_inr'] * np.random.uniform(0.02, 0.05, len(raw_df)), 2)

raw_df['minor_dept_revenue'] = np.round(raw_df['room_revenue_inr'] * np.random.uniform(0.04, 0.10, len(raw_df)), 2)
raw_df['gross_revenue'] = raw_df['room_revenue_inr'] + raw_df['total_fnb_revenue_inr'] + raw_df['banquet_revenue_inr'] + raw_df['minor_dept_revenue']
raw_df['total_expenses'] = (raw_df['rooms_cost'] + raw_df['fnb_cogs'] + raw_df['distribution_commission'] +
                             raw_df['energy_cost'] + raw_df['staff_cost'] + raw_df['maintenance_cost'] + raw_df['marketing_cost'])
raw_df['gross_operating_profit'] = raw_df['gross_revenue'] - raw_df['total_expenses']
raw_df['net_profit_margin_pct'] = np.where(raw_df['gross_revenue'] > 0,
                                            np.round(raw_df['gross_operating_profit'] / raw_df['gross_revenue'] * 100, 2), 0)

# Guest profile
raw_df['total_guests'] = raw_df['adults'] + raw_df['children'].fillna(0).astype(int) + raw_df['babies']
conditions_profile = [
    raw_df['total_guests'] >= 3,
    raw_df['children'] > 0,
    raw_df['customer_type'] == 'Group',
]
choices_profile = ['Family', 'Family with Kids', 'Group/MICE']
raw_df['guest_profile'] = np.select(conditions_profile, choices_profile, default='Business/Solo')

# Channel cleanup
channel_map = {
    'Direct': 'ITC Direct (Website/Walk-in)',
    'Corporate': 'Corporate Account',
    'TA/TO': 'Travel Agent / OTA',
    'GDS': 'Global Distribution System',
    'Undefined': 'Other'
}
raw_df['channel_clean'] = raw_df['distribution_channel'].map(channel_map).fillna('Other')
raw_df['market_segment_clean'] = raw_df['market_segment']

print(f"  Domain transformation complete. Total columns: {len(raw_df.columns)}")

# ===== STEP 4: Create SQLite Database =====
print("\n[4/6] Creating SQLite database...")

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"  Removed old database")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

# ----- Table 1: room_types -----
cursor.execute("""
CREATE TABLE room_types (
    room_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    base_rate_inr REAL NOT NULL,
    gst_rate_pct REAL NOT NULL,
    description TEXT
);
""")

room_type_data = [
    ('Presidential Suite', 35000, 18, 'Ultra-luxury suite with private butler'),
    ('Penthouse Suite', 28000, 18, 'Top-floor panoramic penthouse'),
    ('Executive Suite', 22000, 18, 'Business-class suite with lounge access'),
    ('ITC One Luxury Room', 18000, 18, 'Premium luxury room with ITC One privileges'),
    ('Towers Club Room', 15000, 18, 'Club floor access with exclusive lounge'),
    ('Heritage Room', 12000, 18, 'Heritage wing room with classical decor'),
    ('Premium Room', 10000, 18, 'Premium room with city/garden view'),
    ('Deluxe Room', 8500, 18, 'Spacious deluxe room'),
    ('Superior Room', 6500, 12, 'Comfortable superior room'),
    ('Standard Room', 5000, 12, 'Well-appointed standard room'),
    ('Studio Room', 7000, 12, 'Modern studio-style room'),
]
cursor.executemany("INSERT INTO room_types (category_name, base_rate_inr, gst_rate_pct, description) VALUES (?,?,?,?)", room_type_data)

# ----- Table 2: hotels -----
cursor.execute("""
CREATE TABLE hotels (
    hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_name TEXT NOT NULL UNIQUE,
    hotel_type TEXT NOT NULL,
    location TEXT,
    total_rooms INTEGER
);
""")
cursor.executemany("INSERT INTO hotels (hotel_name, hotel_type, location, total_rooms) VALUES (?,?,?,?)", [
    ('ITC Grand Bharat (Luxury Resort)', 'Resort', 'Gurugram, Haryana', 104),
    ('ITC Maurya (City Hotel)', 'City', 'New Delhi', 438),
])

# ----- Table 3: guests -----
cursor.execute("""
CREATE TABLE guests (
    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL,
    country_code TEXT,
    geographic_region TEXT,
    guest_profile TEXT,
    adults INTEGER DEFAULT 1,
    children INTEGER DEFAULT 0,
    babies INTEGER DEFAULT 0,
    total_guests INTEGER DEFAULT 1,
    customer_type TEXT,
    loyalty_tier TEXT DEFAULT 'Standard Guest',
    is_repeated_guest INTEGER DEFAULT 0,
    previous_cancellations INTEGER DEFAULT 0,
    previous_bookings_not_canceled INTEGER DEFAULT 0,
    special_requests INTEGER DEFAULT 0
);
""")

# ----- Table 4: reservations -----
cursor.execute("""
CREATE TABLE reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL UNIQUE,
    hotel_name TEXT NOT NULL,
    arrival_date TEXT NOT NULL,
    arrival_year INTEGER,
    arrival_month TEXT,
    arrival_week INTEGER,
    stays_weekend_nights INTEGER DEFAULT 0,
    stays_week_nights INTEGER DEFAULT 0,
    total_nights INTEGER DEFAULT 0,
    reserved_room TEXT,
    assigned_room TEXT,
    is_upgraded INTEGER DEFAULT 0,
    is_canceled INTEGER DEFAULT 0,
    lead_time INTEGER DEFAULT 0,
    deposit_type TEXT,
    reservation_status TEXT,
    status_date TEXT,
    booking_changes INTEGER DEFAULT 0,
    days_in_waiting_list INTEGER DEFAULT 0,
    channel TEXT,
    market_segment TEXT,
    FOREIGN KEY (hotel_name) REFERENCES hotels(hotel_name)
);
""")

# ----- Table 5: invoices -----
cursor.execute("""
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL UNIQUE,
    adr_inr REAL DEFAULT 0,
    room_revenue_inr REAL DEFAULT 0,
    fnb_revenue_inr REAL DEFAULT 0,
    banquet_revenue_inr REAL DEFAULT 0,
    minor_dept_revenue_inr REAL DEFAULT 0,
    gross_total_revenue_inr REAL DEFAULT 0,
    gst_rate_pct REAL DEFAULT 18,
    FOREIGN KEY (booking_id) REFERENCES reservations(booking_id)
);
""")

# ----- Table 6: fnb_orders -----
cursor.execute("""
CREATE TABLE fnb_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL,
    dining_plan TEXT,
    restaurant_outlet TEXT,
    dining_covers INTEGER DEFAULT 0,
    food_revenue_inr REAL DEFAULT 0,
    beverage_revenue_inr REAL DEFAULT 0,
    total_fnb_revenue_inr REAL DEFAULT 0,
    FOREIGN KEY (booking_id) REFERENCES reservations(booking_id)
);
""")

# ----- Table 7: banquet_events -----
cursor.execute("""
CREATE TABLE banquet_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL,
    banquet_hall TEXT,
    event_type TEXT,
    attendees INTEGER DEFAULT 0,
    banquet_revenue_inr REAL DEFAULT 0,
    FOREIGN KEY (booking_id) REFERENCES reservations(booking_id)
);
""")

# ----- Table 8: operating_costs -----
cursor.execute("""
CREATE TABLE operating_costs (
    cost_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL,
    billed_nights INTEGER DEFAULT 0,
    rooms_operating_cost REAL DEFAULT 0,
    fnb_cogs_cost REAL DEFAULT 0,
    distribution_commission REAL DEFAULT 0,
    energy_utility_cost REAL DEFAULT 0,
    staff_payroll_cost REAL DEFAULT 0,
    maintenance_cost REAL DEFAULT 0,
    marketing_cost REAL DEFAULT 0,
    total_operating_expenses REAL DEFAULT 0,
    gross_operating_profit REAL DEFAULT 0,
    net_profit_margin_pct REAL DEFAULT 0,
    FOREIGN KEY (booking_id) REFERENCES reservations(booking_id)
);
""")

# ----- Table 9: staff (simulated) -----
cursor.execute("""
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    department TEXT,
    hotel_name TEXT,
    hire_date TEXT,
    salary_inr REAL,
    FOREIGN KEY (hotel_name) REFERENCES hotels(hotel_name)
);
""")
staff_data = [
    ('Rajesh Kumar', 'General Manager', 'Administration', 'ITC Maurya (City Hotel)', '2018-03-15', 250000),
    ('Priya Sharma', 'Front Office Manager', 'Front Office', 'ITC Maurya (City Hotel)', '2019-07-01', 85000),
    ('Amit Singh', 'Revenue Manager', 'Revenue', 'ITC Maurya (City Hotel)', '2020-01-10', 95000),
    ('Neha Gupta', 'F&B Director', 'Food & Beverage', 'ITC Maurya (City Hotel)', '2017-11-20', 120000),
    ('Suresh Patel', 'Executive Chef', 'Kitchen', 'ITC Grand Bharat (Luxury Resort)', '2016-05-01', 150000),
    ('Kavita Reddy', 'Housekeeping Manager', 'Housekeeping', 'ITC Grand Bharat (Luxury Resort)', '2021-02-14', 65000),
    ('Vikram Malhotra', 'Sales Director', 'Sales & Marketing', 'ITC Maurya (City Hotel)', '2019-09-30', 110000),
    ('Anita Desai', 'Night Auditor', 'Front Office', 'ITC Grand Bharat (Luxury Resort)', '2022-06-15', 45000),
    ('Deepak Joshi', 'Banquet Manager', 'Banquets', 'ITC Maurya (City Hotel)', '2020-08-01', 75000),
    ('Meera Nair', 'Spa Manager', 'Wellness', 'ITC Grand Bharat (Luxury Resort)', '2021-11-01', 60000),
]
cursor.executemany("INSERT INTO staff (name, role, department, hotel_name, hire_date, salary_inr) VALUES (?,?,?,?,?,?)", staff_data)

# ----- Table 10: users (system login - simulated) -----
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Manager', 'Receptionist', 'Analyst')),
    staff_id INTEGER,
    is_active INTEGER DEFAULT 1,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);
""")
cursor.executemany("INSERT INTO users (username, role, staff_id) VALUES (?,?,?)", [
    ('admin', 'Admin', 1),
    ('priya.fo', 'Receptionist', 2),
    ('amit.rev', 'Analyst', 3),
    ('neha.fnb', 'Manager', 4),
    ('vikram.sales', 'Manager', 7),
])

# ----- Table 11: payments -----
cursor.execute("""
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id TEXT NOT NULL,
    payment_method TEXT DEFAULT 'Card',
    amount_paid REAL DEFAULT 0,
    payment_date TEXT,
    payment_status TEXT DEFAULT 'Completed',
    FOREIGN KEY (booking_id) REFERENCES reservations(booking_id)
);
""")

# ----- Table 12: kpi_monthly (aggregated analytics) -----
cursor.execute("""
CREATE TABLE kpi_monthly (
    kpi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    month TEXT NOT NULL,
    month_num INTEGER,
    total_bookings INTEGER DEFAULT 0,
    total_cancellations INTEGER DEFAULT 0,
    occupancy_rate_pct REAL DEFAULT 0,
    avg_daily_rate_inr REAL DEFAULT 0,
    revpar_inr REAL DEFAULT 0,
    total_room_revenue REAL DEFAULT 0,
    total_fnb_revenue REAL DEFAULT 0,
    total_banquet_revenue REAL DEFAULT 0,
    gross_revenue REAL DEFAULT 0,
    total_expenses REAL DEFAULT 0,
    gross_operating_profit REAL DEFAULT 0,
    gop_margin_pct REAL DEFAULT 0,
    avg_lead_time REAL DEFAULT 0,
    repeat_guest_pct REAL DEFAULT 0
);
""")

conn.commit()
print(f"  12 tables created successfully!")

# ===== STEP 5: Import Data into Tables =====
print("\n[5/6] Importing data into SQL tables...")

# reservations table
print("  → reservations...")
reservations_data = raw_df[[
    'booking_id', 'hotel_name', 'arrival_date', 'arrival_date_year',
    'arrival_date_month', 'arrival_date_week_number',
    'stays_in_weekend_nights', 'stays_in_week_nights', 'total_nights',
    'reserved_room_category', 'assigned_room_category',
    'is_canceled', 'lead_time', 'deposit_type',
    'reservation_status', 'reservation_status_date',
    'booking_changes', 'days_in_waiting_list',
    'channel_clean', 'market_segment_clean'
]].copy()
reservations_data['is_upgraded'] = (reservations_data['reserved_room_category'] != reservations_data['assigned_room_category']).astype(int)
reservations_data['arrival_date'] = reservations_data['arrival_date'].astype(str)
reservations_data['reservation_status_date'] = reservations_data['reservation_status_date'].astype(str)

for _, row in reservations_data.iterrows():
    cursor.execute("""INSERT INTO reservations 
        (booking_id, hotel_name, arrival_date, arrival_year, arrival_month, arrival_week,
         stays_weekend_nights, stays_week_nights, total_nights, reserved_room, assigned_room,
         is_upgraded, is_canceled, lead_time, deposit_type, reservation_status, status_date,
         booking_changes, days_in_waiting_list, channel, market_segment)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (row['booking_id'], row['hotel_name'], row['arrival_date'],
         row['arrival_date_year'], row['arrival_date_month'], row['arrival_date_week_number'],
         row['stays_in_weekend_nights'], row['stays_in_week_nights'], row['total_nights'],
         row['reserved_room_category'], row['assigned_room_category'],
         row['is_upgraded'], row['is_canceled'], row['lead_time'],
         row['deposit_type'], row['reservation_status'], row['reservation_status_date'],
         row['booking_changes'], row['days_in_waiting_list'],
         row['channel_clean'], row['market_segment_clean']))

# guests table
print("  → guests...")
for _, row in raw_df.iterrows():
    cursor.execute("""INSERT INTO guests 
        (booking_id, country_code, geographic_region, guest_profile, adults, children, babies,
         total_guests, customer_type, loyalty_tier, is_repeated_guest,
         previous_cancellations, previous_bookings_not_canceled, special_requests)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (row['booking_id'], row['country'], row['geographic_region'], row['guest_profile'],
         int(row['adults']), int(row['children']), int(row['babies']),
         int(row['total_guests']), row['customer_type'], row['loyalty_tier'],
         int(row['is_repeated_guest']), int(row['previous_cancellations']),
         int(row['previous_bookings_not_canceled']), int(row['total_of_special_requests'])))

# invoices
print("  → invoices...")
for _, row in raw_df.iterrows():
    cursor.execute("""INSERT INTO invoices 
        (booking_id, adr_inr, room_revenue_inr, fnb_revenue_inr, banquet_revenue_inr,
         minor_dept_revenue_inr, gross_total_revenue_inr, gst_rate_pct)
        VALUES (?,?,?,?,?,?,?,?)""",
        (row['booking_id'], row['adr_inr'], row['room_revenue_inr'],
         row['total_fnb_revenue_inr'], row['banquet_revenue_inr'],
         row['minor_dept_revenue'], row['gross_revenue'],
         18 if row['adr_inr'] > 7500*85/100 else 12))

# fnb_orders
print("  → fnb_orders...")
for _, row in raw_df.iterrows():
    cursor.execute("""INSERT INTO fnb_orders 
        (booking_id, dining_plan, restaurant_outlet, dining_covers,
         food_revenue_inr, beverage_revenue_inr, total_fnb_revenue_inr)
        VALUES (?,?,?,?,?,?,?)""",
        (row['booking_id'], row['dining_plan'], row['restaurant_outlet'],
         int(row['dining_covers']), row['food_revenue_inr'],
         row['beverage_revenue_inr'], row['total_fnb_revenue_inr']))

# banquet_events (only rows with actual banquet)
print("  → banquet_events...")
banquet_rows = raw_df[raw_df['banquet_event_type'].notna() & (raw_df['banquet_event_type'] != 'None')]
for _, row in banquet_rows.iterrows():
    cursor.execute("""INSERT INTO banquet_events 
        (booking_id, banquet_hall, event_type, attendees, banquet_revenue_inr)
        VALUES (?,?,?,?,?)""",
        (row['booking_id'], row['banquet_hall'], row['banquet_event_type'],
         int(row['banquet_attendees']), row['banquet_revenue_inr']))

# operating_costs
print("  → operating_costs...")
for _, row in raw_df.iterrows():
    billed = max(int(row['total_nights']), 1)
    cursor.execute("""INSERT INTO operating_costs 
        (booking_id, billed_nights, rooms_operating_cost, fnb_cogs_cost,
         distribution_commission, energy_utility_cost, staff_payroll_cost,
         maintenance_cost, marketing_cost, total_operating_expenses,
         gross_operating_profit, net_profit_margin_pct)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
        (row['booking_id'], billed, row['rooms_cost'], row['fnb_cogs'],
         row['distribution_commission'], row['energy_cost'], row['staff_cost'],
         row['maintenance_cost'], row['marketing_cost'],
         row['total_expenses'], row['gross_operating_profit'], row['net_profit_margin_pct']))

# payments
print("  → payments...")
payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash', 'Corporate Account']
for _, row in raw_df.iterrows():
    if row['reservation_status'] == 'Check-Out':
        cursor.execute("""INSERT INTO payments 
            (booking_id, payment_method, amount_paid, payment_date, payment_status)
            VALUES (?,?,?,?,?)""",
            (row['booking_id'], np.random.choice(payment_methods),
             row['gross_revenue'], str(row['reservation_status_date']), 'Completed'))

conn.commit()

# ===== STEP 6: Populate kpi_monthly table using SQL =====
print("  → kpi_monthly (aggregated)...")

# Using SQL aggregation to populate monthly KPIs
month_order = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
               'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

cursor.execute("""
SELECT arrival_year, arrival_month,
       COUNT(*) as total_bookings,
       SUM(is_canceled) as cancellations,
       AVG(CASE WHEN is_canceled = 0 THEN 1.0 ELSE 0.0 END) * 100 as occ_rate,
       AVG(CASE WHEN is_canceled = 0 THEN lead_time ELSE NULL END) as avg_lead
FROM reservations
GROUP BY arrival_year, arrival_month
""")
res_agg = cursor.fetchall()

for year, month, bookings, cancels, occ, avg_lead in res_agg:
    # Get revenue aggregates
    cursor.execute("""
    SELECT AVG(i.adr_inr), SUM(i.room_revenue_inr), SUM(i.fnb_revenue_inr),
           SUM(i.banquet_revenue_inr), SUM(i.gross_total_revenue_inr)
    FROM invoices i
    JOIN reservations r ON i.booking_id = r.booking_id
    WHERE r.arrival_year = ? AND r.arrival_month = ? AND r.is_canceled = 0
    """, (year, month))
    rev = cursor.fetchone()
    
    cursor.execute("""
    SELECT SUM(oc.total_operating_expenses), SUM(oc.gross_operating_profit)
    FROM operating_costs oc
    JOIN reservations r ON oc.booking_id = r.booking_id
    WHERE r.arrival_year = ? AND r.arrival_month = ? AND r.is_canceled = 0
    """, (year, month))
    cost = cursor.fetchone()
    
    adr = rev[0] or 0
    room_rev = rev[1] or 0
    fnb_rev = rev[2] or 0
    banq_rev = rev[3] or 0
    gross = rev[4] or 0
    expenses = cost[0] or 0
    gop = cost[1] or 0
    gop_margin = (gop / gross * 100) if gross > 0 else 0
    
    # Simple RevPAR calculation
    total_available_rooms = 542  # 104 + 438
    days_in_month = 30
    revpar = room_rev / (total_available_rooms * days_in_month) if total_available_rooms > 0 else 0
    
    # Repeat guest %
    cursor.execute("""
    SELECT AVG(g.is_repeated_guest) * 100
    FROM guests g
    JOIN reservations r ON g.booking_id = r.booking_id
    WHERE r.arrival_year = ? AND r.arrival_month = ?
    """, (year, month))
    repeat_pct = cursor.fetchone()[0] or 0
    
    month_num = month_order.get(month, 0)
    
    cursor.execute("""INSERT INTO kpi_monthly 
        (year, month, month_num, total_bookings, total_cancellations,
         occupancy_rate_pct, avg_daily_rate_inr, revpar_inr,
         total_room_revenue, total_fnb_revenue, total_banquet_revenue,
         gross_revenue, total_expenses, gross_operating_profit,
         gop_margin_pct, avg_lead_time, repeat_guest_pct)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (year, month, month_num, bookings, cancels,
         round(occ, 2), round(adr, 2), round(revpar, 2),
         round(room_rev, 2), round(fnb_rev, 2), round(banq_rev, 2),
         round(gross, 2), round(expenses, 2), round(gop, 2),
         round(gop_margin, 2), round(avg_lead or 0, 1), round(repeat_pct, 2)))

conn.commit()

# ===== Verification =====
print("\n[6/6] Verification...")
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
print(f"\n  {'Table':<25} {'Rows':>10}")
print(f"  {'─'*25} {'─'*10}")
for (tname,) in tables:
    cnt = cursor.execute(f"SELECT COUNT(*) FROM {tname}").fetchone()[0]
    print(f"  {tname:<25} {cnt:>10,}")

db_size = os.path.getsize(DB_PATH)
print(f"\n  Database file: {DB_PATH}")
print(f"  Database size: {db_size / (1024*1024):.1f} MB")

conn.close()

print("\n" + "=" * 60)
print("✅ SQLite database created successfully!")
print("   12 tables in 3NF | Data cleaned & imported")
print("=" * 60)
