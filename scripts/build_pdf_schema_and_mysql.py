"""
Build PDF-Matched Tables & MySQL Dump Script (Optimized)
--------------------------------------------------------
1. Adds indexes to SQLite database for lightning-fast joins.
2. Populates `properties`, `rooms`, `calendar`, `bookings`, `room_inventory`.
3. Exports `itc_hotels_mysql_dump.sql` for MySQL / phpMyAdmin / XAMPP.
"""

import sqlite3
import pandas as pd
import numpy as np
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'ITC-Final-Dashboards', 'itc_hotel_analytics.db')
SQL_EXPORT_PATH = os.path.join(BASE_DIR, 'ITC-Final-Dashboards', 'itc_hotels_mysql_dump.sql')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

start_time = time.time()
print("Starting database optimization and schema expansion...")

# Step 0: Create indexes on existing tables for high-performance joins
print("  Creating indexes on booking_id...")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_res_booking_id ON reservations(booking_id);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_inv_booking_id ON invoices(booking_id);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_gst_booking_id ON guests(booking_id);")
conn.commit()

# 1. properties table (Fig D1)
print("  Creating properties table...")
cursor.execute("DROP TABLE IF EXISTS properties")
cursor.execute("""
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY,
    property_name TEXT NOT NULL,
    category TEXT NOT NULL,
    city TEXT NOT NULL
)
""")
properties_data = [
    (16559, 'ITC Grand Bharat (Luxury Resort)', 'Luxury Resort', 'Gurugram'),
    (16560, 'ITC Maurya (City Hotel)', 'Luxury Business', 'New Delhi'),
    (16561, 'ITC Grand Chola', 'Luxury Palace', 'Chennai'),
    (16562, 'ITC Maratha', 'Luxury Business', 'Mumbai'),
    (16563, 'ITC Windsor', 'Heritage Luxury', 'Bengaluru')
]
cursor.executemany("INSERT INTO properties VALUES (?, ?, ?, ?)", properties_data)

# 2. rooms table (Fig D2)
print("  Creating rooms table...")
cursor.execute("DROP TABLE IF EXISTS rooms")
cursor.execute("""
CREATE TABLE rooms (
    room_id TEXT PRIMARY KEY,
    room_class TEXT NOT NULL
)
""")
rooms_data = [
    ('RT1', 'Standard'),
    ('RT2', 'Elite'),
    ('RT3', 'Premium'),
    ('RT4', 'Presidential'),
    ('RT5', 'Luxury')
]
cursor.executemany("INSERT INTO rooms VALUES (?, ?)", rooms_data)

# 3. calendar / dim_date table (Fig B.1)
print("  Creating calendar dimension...")
cursor.execute("DROP TABLE IF EXISTS calendar")
cursor.execute("""
CREATE TABLE calendar (
    date_val TEXT PRIMARY KEY,
    day_name TEXT,
    day_of_week INTEGER,
    month_name TEXT,
    month_no INTEGER,
    quarter INTEGER,
    year_val INTEGER
)
""")
dates = pd.date_range(start='2015-01-01', end='2018-12-31', freq='D')
cal_data = [
    (d.strftime('%Y-%m-%d'), d.strftime('%A'), d.weekday() + 1, d.strftime('%B'), d.month, (d.month-1)//3 + 1, d.year)
    for d in dates
]
cursor.executemany("INSERT INTO calendar VALUES (?, ?, ?, ?, ?, ?, ?)", cal_data)

# 4. bookings table (Fig D1 & D2)
print("  Creating and populating bookings table...")
cursor.execute("DROP TABLE IF EXISTS bookings")
cursor.execute("""
CREATE TABLE bookings (
    booking_id TEXT PRIMARY KEY,
    property_id INTEGER,
    booking_date TEXT,
    check_in_date TEXT,
    checkout_date TEXT,
    no_guests INTEGER,
    room_category TEXT,
    booking_platform TEXT,
    ratings_given REAL,
    booking_status TEXT,
    revenue_generated REAL,
    revenue_realized REAL,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
)
""")

# Use indexed JOINs for maximum speed
cursor.execute("""
INSERT INTO bookings (
    booking_id, property_id, booking_date, check_in_date, checkout_date,
    no_guests, room_category, booking_platform, ratings_given,
    booking_status, revenue_generated, revenue_realized
)
SELECT 
    r.booking_id,
    CASE WHEN r.hotel_name LIKE '%Resort%' THEN 16559 ELSE 16560 END AS property_id,
    DATE(r.arrival_date, '-' || r.lead_time || ' days') AS booking_date,
    r.arrival_date AS check_in_date,
    DATE(r.arrival_date, '+' || r.total_nights || ' days') AS checkout_date,
    COALESCE(g.total_guests, 1) AS no_guests,
    r.assigned_room AS room_category,
    r.channel AS booking_platform,
    ROUND(3.8 + ((ABS(RANDOM()) % 12) / 10.0), 1) AS ratings_given,
    CASE 
        WHEN r.is_canceled = 1 THEN 'Cancelled'
        WHEN r.reservation_status = 'No-Show' THEN 'No-Show'
        ELSE 'Checked Out'
    END AS booking_status,
    i.gross_total_revenue_inr AS revenue_generated,
    CASE WHEN r.is_canceled = 0 THEN i.gross_total_revenue_inr ELSE 0 END AS revenue_realized
FROM reservations r
JOIN invoices i ON r.booking_id = i.booking_id
LEFT JOIN guests g ON r.booking_id = g.booking_id
""")

# 5. room_inventory table (Fig D2)
print("  Creating and populating room_inventory table...")
cursor.execute("DROP TABLE IF EXISTS room_inventory")
cursor.execute("""
CREATE TABLE room_inventory (
    property_id INTEGER,
    check_in_date TEXT,
    room_category TEXT,
    successful_bookings INTEGER,
    capacity INTEGER,
    PRIMARY KEY (property_id, check_in_date, room_category),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
)
""")

cursor.execute("""
INSERT INTO room_inventory (property_id, check_in_date, room_category, successful_bookings, capacity)
SELECT 
    property_id,
    check_in_date,
    room_category,
    COUNT(CASE WHEN booking_status = 'Checked Out' THEN 1 END) AS successful_bookings,
    COUNT(*) + (ABS(RANDOM()) % 4) + 1 AS capacity
FROM bookings
GROUP BY property_id, check_in_date, room_category
""")

# Indexes on new tables
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bkg_checkin ON bookings(check_in_date);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bkg_property ON bookings(property_id);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_inv_date ON room_inventory(check_in_date);")

conn.commit()

# Print status
print(f"\n  Populated in {time.time() - start_time:.2f} seconds!")
print("\nTable Row Counts in SQLite DB:")
for t in ['properties', 'rooms', 'calendar', 'bookings', 'room_inventory']:
    count = cursor.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t:<20}: {count:>8,}")

# Export MySQL DDL script
print(f"\nGenerating MySQL dump: {SQL_EXPORT_PATH} ...")
with open(SQL_EXPORT_PATH, 'w') as f:
    f.write("-- =============================================================================\n")
    f.write("-- ITC Hotels Revenue & Business Performance Analysis\n")
    f.write("-- MySQL 8.0 Database Dump & DDL Schema (3NF Normalized)\n")
    f.write("-- Invertis University, Bareilly (Faculty of Computer Applications)\n")
    f.write("-- Authors: Jatin Sagar, Atul Kumar, Darshika Rathore, Muskan Saxena\n")
    f.write("-- Guide: Ms. Megha Saxena, Assistant Professor\n")
    f.write("-- =============================================================================\n\n")
    f.write("CREATE DATABASE IF NOT EXISTS itc_hotels_db;\n")
    f.write("USE itc_hotels_db;\n\n")
    f.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")

    # properties
    f.write("-- 1. properties Table (Figure D1)\n")
    f.write("DROP TABLE IF EXISTS properties;\n")
    f.write("""CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    property_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")
    for row in properties_data:
        f.write(f"INSERT INTO properties VALUES ({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}');\n")
    f.write("\n")

    # rooms
    f.write("-- 2. rooms Table (Figure D2)\n")
    f.write("DROP TABLE IF EXISTS rooms;\n")
    f.write("""CREATE TABLE rooms (
    room_id VARCHAR(20) PRIMARY KEY,
    room_class VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")
    for row in rooms_data:
        f.write(f"INSERT INTO rooms VALUES ('{row[0]}', '{row[1]}');\n")
    f.write("\n")

    # calendar
    f.write("-- 3. calendar / dim_date Table (Figure B.1)\n")
    f.write("DROP TABLE IF EXISTS calendar;\n")
    f.write("""CREATE TABLE calendar (
    date_val DATE PRIMARY KEY,
    day_name VARCHAR(20),
    day_of_week INT,
    month_name VARCHAR(20),
    month_no INT,
    quarter INT,
    year_val INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # bookings table
    f.write("-- 4. bookings Table (Figure D1 & D2)\n")
    f.write("DROP TABLE IF EXISTS bookings;\n")
    f.write("""CREATE TABLE bookings (
    booking_id VARCHAR(50) PRIMARY KEY,
    property_id INT,
    booking_date DATE,
    check_in_date DATE,
    checkout_date DATE,
    no_guests INT,
    room_category VARCHAR(50),
    booking_platform VARCHAR(50),
    ratings_given DECIMAL(2,1),
    booking_status VARCHAR(20),
    revenue_generated DECIMAL(12,2),
    revenue_realized DECIMAL(12,2),
    KEY idx_checkin (check_in_date),
    KEY idx_property (property_id),
    CONSTRAINT fk_bookings_property FOREIGN KEY (property_id) REFERENCES properties(property_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # room_inventory
    f.write("-- 5. room_inventory Table (Figure D2)\n")
    f.write("DROP TABLE IF EXISTS room_inventory;\n")
    f.write("""CREATE TABLE room_inventory (
    property_id INT,
    check_in_date DATE,
    room_category VARCHAR(50),
    successful_bookings INT,
    capacity INT,
    PRIMARY KEY (property_id, check_in_date, room_category),
    CONSTRAINT fk_inventory_property FOREIGN KEY (property_id) REFERENCES properties(property_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 12 Core Tables
    f.write("""-- 6. 3NF Normalized Core Enterprise Tables (Matching Chapter 5.3)

CREATE TABLE IF NOT EXISTS room_types (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    base_rate_inr DECIMAL(10,2) NOT NULL,
    gst_rate_pct DECIMAL(4,2) NOT NULL,
    description TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS hotels (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_name VARCHAR(150) NOT NULL UNIQUE,
    hotel_type VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    total_rooms INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id VARCHAR(50) NOT NULL UNIQUE,
    hotel_name VARCHAR(150) NOT NULL,
    arrival_date DATE NOT NULL,
    arrival_year INT,
    arrival_month VARCHAR(20),
    arrival_week INT,
    stays_weekend_nights INT DEFAULT 0,
    stays_week_nights INT DEFAULT 0,
    total_nights INT DEFAULT 0,
    reserved_room VARCHAR(100),
    assigned_room VARCHAR(100),
    is_upgraded TINYINT(1) DEFAULT 0,
    is_canceled TINYINT(1) DEFAULT 0,
    lead_time INT DEFAULT 0,
    deposit_type VARCHAR(50),
    reservation_status VARCHAR(50),
    status_date DATE,
    booking_changes INT DEFAULT 0,
    days_in_waiting_list INT DEFAULT 0,
    channel VARCHAR(100),
    market_segment VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id VARCHAR(50) NOT NULL UNIQUE,
    adr_inr DECIMAL(10,2) DEFAULT 0,
    room_revenue_inr DECIMAL(12,2) DEFAULT 0,
    fnb_revenue_inr DECIMAL(12,2) DEFAULT 0,
    banquet_revenue_inr DECIMAL(12,2) DEFAULT 0,
    minor_dept_revenue_inr DECIMAL(12,2) DEFAULT 0,
    gross_total_revenue_inr DECIMAL(12,2) DEFAULT 0,
    gst_rate_pct DECIMAL(4,2) DEFAULT 18
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS fnb_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id VARCHAR(50) NOT NULL,
    dining_plan VARCHAR(50),
    restaurant_outlet VARCHAR(100),
    dining_covers INT DEFAULT 0,
    food_revenue_inr DECIMAL(10,2) DEFAULT 0,
    beverage_revenue_inr DECIMAL(10,2) DEFAULT 0,
    total_fnb_revenue_inr DECIMAL(10,2) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS operating_costs (
    cost_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id VARCHAR(50) NOT NULL,
    billed_nights INT DEFAULT 0,
    rooms_operating_cost DECIMAL(10,2) DEFAULT 0,
    fnb_cogs_cost DECIMAL(10,2) DEFAULT 0,
    distribution_commission DECIMAL(10,2) DEFAULT 0,
    energy_utility_cost DECIMAL(10,2) DEFAULT 0,
    staff_payroll_cost DECIMAL(10,2) DEFAULT 0,
    maintenance_cost DECIMAL(10,2) DEFAULT 0,
    marketing_cost DECIMAL(10,2) DEFAULT 0,
    total_operating_expenses DECIMAL(12,2) DEFAULT 0,
    gross_operating_profit DECIMAL(12,2) DEFAULT 0,
    net_profit_margin_pct DECIMAL(5,2) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS kpi_monthly (
    kpi_id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    month VARCHAR(20) NOT NULL,
    month_num INT,
    total_bookings INT DEFAULT 0,
    total_cancellations INT DEFAULT 0,
    occupancy_rate_pct DECIMAL(5,2) DEFAULT 0,
    avg_daily_rate_inr DECIMAL(10,2) DEFAULT 0,
    revpar_inr DECIMAL(10,2) DEFAULT 0,
    total_room_revenue DECIMAL(14,2) DEFAULT 0,
    total_fnb_revenue DECIMAL(14,2) DEFAULT 0,
    total_banquet_revenue DECIMAL(14,2) DEFAULT 0,
    gross_revenue DECIMAL(14,2) DEFAULT 0,
    total_expenses DECIMAL(14,2) DEFAULT 0,
    gross_operating_profit DECIMAL(14,2) DEFAULT 0,
    gop_margin_pct DECIMAL(5,2) DEFAULT 0,
    avg_lead_time DECIMAL(6,1) DEFAULT 0,
    repeat_guest_pct DECIMAL(5,2) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
\n""")

    # Sample rows
    f.write("-- Sample Bookings Data (500 rows preview for testing / XAMPP demonstration)\n")
    cursor.execute("""
    SELECT booking_id, property_id, booking_date, check_in_date, checkout_date,
           no_guests, room_category, booking_platform, ratings_given, booking_status,
           revenue_generated, revenue_realized
    FROM bookings LIMIT 500
    """)
    sample_rows = cursor.fetchall()
    f.write("INSERT INTO bookings (booking_id, property_id, booking_date, check_in_date, checkout_date, no_guests, room_category, booking_platform, ratings_given, booking_status, revenue_generated, revenue_realized) VALUES\n")
    for i, r in enumerate(sample_rows):
        term = ";" if i == len(sample_rows) - 1 else ","
        f.write(f"('{r[0]}', {r[1]}, '{r[2]}', '{r[3]}', '{r[4]}', {r[5]}, '{r[6]}', '{r[7]}', {r[8]}, '{r[9]}', {r[10]}, {r[11]}){term}\n")

    f.write("\nSET FOREIGN_KEY_CHECKS = 1;\n")

conn.close()
print("✅ Done! MySQL Dump created:", SQL_EXPORT_PATH)
