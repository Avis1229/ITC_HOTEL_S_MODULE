"""
ITC Hotels Data Transformation & Engineering Pipeline
Converts raw Kaggle hotel booking demand dataset into 4 specialized ITC Hotel analytics modules:
1. Room Revenue & Occupancy Analytics
2. Food, Beverage & Banquet Performance Analytics
3. Guest Demographics & Booking Channel Analytics
4. Operating Costs & Profitability Analytics
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime

BASE_DIR = "/home/goku/ITC_Hotels_Project"
RAW_DATA_PATH = os.path.join(BASE_DIR, "archive", "hotel_bookings.csv")

def run_pipeline():
    print("Loading raw Kaggle dataset...")
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")

    # 1. Base Cleaning & Common Date Construction
    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    df['arrival_month_num'] = df['arrival_date_month'].map(month_map)
    df['arrival_date'] = pd.to_datetime(
        df['arrival_date_year'].astype(str) + '-' +
        df['arrival_month_num'].astype(str).str.zfill(2) + '-' +
        df['arrival_date_day_of_month'].astype(str).str.zfill(2),
        errors='coerce'
    )
    
    # Generate unique Booking ID
    df['booking_id'] = [f"ITC-{row['arrival_date_year']}-{i+1:06d}" for i, row in df.iterrows()]

    # Map Hotel Names to prestigious ITC Properties
    # Resort Hotel -> ITC Grand Bharat / ITC Mughal Resort & Spa
    # City Hotel -> ITC Maurya (New Delhi) / ITC Grand Chola (Chennai)
    hotel_mapping = {
        'Resort Hotel': 'ITC Grand Bharat & Mughal (Luxury Resort)',
        'City Hotel': 'ITC Maurya & Grand Chola (Executive Luxury)'
    }
    df['hotel_name'] = df['hotel'].map(hotel_mapping)

    # Room Type Mapping to ITC Room Categories
    room_mapping = {
        'A': 'Executive Club Room',
        'B': 'The Towers Room',
        'C': 'ITC One Luxury Room',
        'D': 'Deluxe Suite',
        'E': 'Grand Presidential Suite',
        'F': 'Heritage Suite',
        'G': 'Royal Luxury Suite',
        'H': 'Governor Suite',
        'L': 'Presidential Villa',
        'P': 'Club Prive Room'
    }
    df['reserved_room_category'] = df['reserved_room_type'].map(lambda x: room_mapping.get(x, f'Suite-{x}'))
    df['assigned_room_category'] = df['assigned_room_type'].map(lambda x: room_mapping.get(x, f'Suite-{x}'))
    df['is_upgraded'] = (df['reserved_room_type'] != df['assigned_room_type']).astype(int)

    # Total Nights & Guest count
    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
    # If 0 nights (day use), set to 1 for adr calculation
    df['billed_nights'] = df['total_nights'].apply(lambda x: max(x, 1))
    df['total_guests'] = df['adults'] + df['children'].fillna(0) + df['babies'].fillna(0)
    df['total_guests'] = df['total_guests'].apply(lambda x: max(int(x), 1))

    # Room Revenue calculation: ADR * billed_nights (if not canceled, or cancellation fee if guaranteed)
    # Filter or set negative adr to 0
    df['adr_clean'] = df['adr'].apply(lambda x: max(float(x), 0.0))
    # Currency standard in INR (1 EUR/USD equivalent = ~85 INR conversion factor for luxury Indian context)
    INR_FACTOR = 85.0
    df['adr_inr'] = (df['adr_clean'] * INR_FACTOR).round(2)
    
    # If canceled and deposit is Non Refund, revenue is kept, else 0 room revenue
    def calc_room_rev(row):
        if row['is_canceled'] == 0:
            return round(row['adr_inr'] * row['billed_nights'], 2)
        elif row['deposit_type'] == 'Non Refund':
            return round(row['adr_inr'] * 1.0, 2) # 1 night cancellation fee
        else:
            return 0.0
            
    df['room_revenue_inr'] = df.apply(calc_room_rev, axis=1)

    # -------------------------------------------------------------
    # MODULE 1: Room Revenue & Occupancy Analytics
    # -------------------------------------------------------------
    print("Generating Module 1: Room Revenue & Occupancy Analytics...")
    mod1_cols = [
        'booking_id', 'hotel_name', 'arrival_date', 'arrival_date_year', 'arrival_date_month',
        'arrival_date_week_number', 'stays_in_weekend_nights', 'stays_in_week_nights', 'total_nights',
        'reserved_room_category', 'assigned_room_category', 'is_upgraded', 'is_canceled',
        'lead_time', 'adr_inr', 'room_revenue_inr', 'deposit_type', 'reservation_status',
        'reservation_status_date', 'booking_changes', 'days_in_waiting_list'
    ]
    df_mod1 = df[mod1_cols].copy()
    mod1_path = os.path.join(BASE_DIR, "ITC-Room-Analytics", "itc_room_revenue_occupancy.csv")
    df_mod1.to_csv(mod1_path, index=False)
    print(f"Saved Module 1 data -> {mod1_path} ({len(df_mod1)} rows)")

    # -------------------------------------------------------------
    # MODULE 2: Food, Beverage & Banquet Performance Analytics
    # -------------------------------------------------------------
    print("Generating Module 2: Food, Beverage & Banquet Performance Analytics...")
    # Seed for deterministic simulation
    np.random.seed(42)

    # Meal Plan Mapping
    meal_map = {
        'BB': 'Bed & Breakfast (Continental Buffet)',
        'HB': 'Half Board (Breakfast + Bukhara Dinner)',
        'FB': 'Full Board (All-Inclusive Luxury Dining)',
        'SC': 'Room Only (A-La-Carte Dining)',
        'Undefined': 'Room Only (A-La-Carte Dining)'
    }
    df['dining_plan'] = df['meal'].map(lambda x: meal_map.get(x, 'Room Only'))

    # F&B Outlets at ITC: Bukhara, Peshawri, Dum Pukht, Pavilion 24/7, Dakshin, Royal Lounge Bar
    outlets = ['Bukhara Tandoor', 'Dum Pukht Awadhi', 'Peshawri Grill', 'The Pavilion (24/7)', 'Royal Afghan & Bar', 'Avartana Southern Fine Dining']
    df['primary_restaurant_outlet'] = np.random.choice(outlets, size=len(df), p=[0.25, 0.20, 0.15, 0.20, 0.10, 0.10])

    # F&B Cover count & Revenue
    # Non-canceled guests dine; average cover spend INR 1800 - 4500 per cover depending on plan
    def calc_fnb(row):
        if row['is_canceled'] == 1:
            return 0.0, 0.0, 0
        plan = row['meal']
        guests = row['total_guests']
        nights = row['billed_nights']
        
        # covers = guests * nights * meals_per_day
        if plan == 'FB':
            covers = guests * nights * 3
            food_rev = covers * np.random.uniform(1500, 2200)
            bev_rev = covers * np.random.uniform(500, 900)
        elif plan == 'HB':
            covers = guests * nights * 2
            food_rev = covers * np.random.uniform(1800, 2600)
            bev_rev = covers * np.random.uniform(600, 1100)
        elif plan == 'BB':
            covers = guests * nights * 1
            food_rev = covers * np.random.uniform(1100, 1600) + (nights * np.random.uniform(500, 1500))
            bev_rev = covers * np.random.uniform(350, 750)
        else: # Room Only / SC
            covers = max(1, int(guests * nights * np.random.uniform(0.5, 1.2)))
            food_rev = covers * np.random.uniform(1400, 2400)
            bev_rev = covers * np.random.uniform(400, 1000)
        return round(food_rev, 2), round(bev_rev, 2), covers

    fnb_results = df.apply(calc_fnb, axis=1)
    df['food_revenue_inr'] = [r[0] for r in fnb_results]
    df['beverage_revenue_inr'] = [r[1] for r in fnb_results]
    df['dining_covers'] = [r[2] for r in fnb_results]
    df['total_fnb_revenue_inr'] = df['food_revenue_inr'] + df['beverage_revenue_inr']

    # Banquet & Events (Conferences, Destination Weddings, Corporate Galas)
    # Groups & Corporates frequently book banquet facilities
    banquet_halls = ['Rajputana Grand Ballroom', 'Darbar State Hall', 'Chola Conclave Hall', 'Nalanda Executive Auditorium', 'None']
    def assign_banquet(row):
        if row['is_canceled'] == 1:
            return 'None', 'None', 0, 0.0
        # If customer is Group or Corporate or Market segment is Groups/Corporate
        if row['customer_type'] in ['Group', 'Contract'] or row['market_segment'] in ['Corporate', 'Groups']:
            hall = np.random.choice(banquet_halls[:-1], p=[0.35, 0.25, 0.25, 0.15])
            event_type = np.random.choice(['Corporate Annual Summit', 'Medical / Tech Conference', 'Luxury Royal Wedding Reception', 'Government Delegation Gala'], p=[0.4, 0.3, 0.2, 0.1])
            delegates = int(np.random.uniform(40, 250))
            # Banquet Hall rental + special banquet catering package INR 2500/head
            banquet_rev = round(delegates * np.random.uniform(2200, 4800) + np.random.uniform(50000, 150000), 2)
            return hall, event_type, delegates, banquet_rev
        elif np.random.rand() < 0.05: # 5% of regular luxury stays book mini meeting rooms
            hall = 'Nalanda Executive Auditorium'
            event_type = 'Private Boardroom Meeting'
            delegates = int(np.random.uniform(10, 25))
            banquet_rev = round(delegates * np.random.uniform(1800, 3200) + 25000, 2)
            return hall, event_type, delegates, banquet_rev
        else:
            return 'None', 'None', 0, 0.0

    banquet_results = df.apply(assign_banquet, axis=1)
    df['banquet_hall_booked'] = [b[0] for b in banquet_results]
    df['banquet_event_type'] = [b[1] for b in banquet_results]
    df['banquet_attendees'] = [b[2] for b in banquet_results]
    df['banquet_revenue_inr'] = [b[3] for b in banquet_results]
    df['combined_fnb_banquet_rev_inr'] = df['total_fnb_revenue_inr'] + df['banquet_revenue_inr']

    mod2_cols = [
        'booking_id', 'hotel_name', 'arrival_date', 'arrival_date_year', 'arrival_date_month',
        'is_canceled', 'dining_plan', 'primary_restaurant_outlet', 'dining_covers',
        'food_revenue_inr', 'beverage_revenue_inr', 'total_fnb_revenue_inr',
        'banquet_hall_booked', 'banquet_event_type', 'banquet_attendees', 'banquet_revenue_inr',
        'combined_fnb_banquet_rev_inr'
    ]
    df_mod2 = df[mod2_cols].copy()
    mod2_path = os.path.join(BASE_DIR, "ITC-FnB-Analytics", "itc_fnb_banquet_performance.csv")
    df_mod2.to_csv(mod2_path, index=False)
    print(f"Saved Module 2 data -> {mod2_path} ({len(df_mod2)} rows)")

    # -------------------------------------------------------------
    # MODULE 3: Guest Demographics & Booking Channel Analytics
    # -------------------------------------------------------------
    print("Generating Module 3: Guest Demographics & Booking Channel Analytics...")
    
    # ISO Country Mapping to Clean Full Names & Geographical Regions
    country_region_map = {
        'PRT': ('Domestic / Prime Market', 'Portugal / Europe'),
        'GBR': ('United Kingdom', 'Europe West'),
        'FRA': ('France', 'Europe West'),
        'ESP': ('Spain', 'Europe South'),
        'DEU': ('Germany', 'Europe Central'),
        'ITA': ('Italy', 'Europe South'),
        'IRL': ('Ireland', 'Europe West'),
        'BEL': ('Belgium', 'Europe West'),
        'BRA': ('Brazil', 'Americas South'),
        'USA': ('United States', 'North America'),
        'IND': ('India (Club ITC HQ)', 'South Asia / Domestic'),
        'CHN': ('China', 'East Asia'),
        'AUS': ('Australia', 'Oceania'),
        'CAN': ('Canada', 'North America'),
        'CHE': ('Switzerland', 'Europe Central'),
        'NLD': ('Netherlands', 'Europe West'),
        'RUS': ('Russian Federation', 'Eurasia'),
        'ARE': ('United Arab Emirates', 'Middle East / GCC'),
        'SAU': ('Saudi Arabia', 'Middle East / GCC'),
        'SGP': ('Singapore', 'Southeast Asia'),
        'JPN': ('Japan', 'East Asia')
    }
    def map_country(code):
        if pd.isna(code) or code == 'NULL':
            return 'Domestic Premium (India / South Asia)', 'Domestic Network'
        if code in country_region_map:
            return country_region_map[code][0], country_region_map[code][1]
        return f"International ({code})", 'Other International'

    country_res = df['country'].map(map_country)
    df['guest_origin_country'] = [c[0] for c in country_res]
    df['geographic_region'] = [c[1] for c in country_res]

    # Guest Household Profile
    def guest_profile(row):
        a, c, b = row['adults'], row['children'], row['babies']
        if a == 1 and (c + b) == 0:
            return 'Solo Business / Solo Traveler'
        elif a == 2 and (c + b) == 0:
            return 'Couple / Duo Leisure'
        elif (c + b) > 0:
            return 'Family with Children'
        elif a > 2:
            return 'Group / Corporate Delegation'
        else:
            return 'Other'
            
    df['guest_profile'] = df.apply(guest_profile, axis=1)

    # Club ITC Loyalty Tier Simulation (Green, Silver, Gold, Culinaire / Platinum)
    def loyalty_tier(row):
        rep = row['is_repeated_guest']
        prev = row['previous_bookings_not_canceled']
        if rep == 1 or prev >= 3:
            return np.random.choice(['Club ITC Gold', 'Club ITC Culinaire (Platinum)'], p=[0.6, 0.4])
        elif prev >= 1:
            return 'Club ITC Silver'
        else:
            return np.random.choice(['Non-Member Guest', 'Club ITC Green (Base)'], p=[0.75, 0.25])
            
    df['loyalty_program_tier'] = df.apply(loyalty_tier, axis=1)

    # Booking Channel Standardization
    channel_clean_map = {
        'Direct': 'Direct (ITC Hotels Website & App)',
        'Corporate': 'Corporate Contracting (ITC B2B Portal)',
        'Online TA': 'OTA (Online Travel Agent - MakeMyTrip, Agoda, Booking.com)',
        'Offline TA/TO': 'Offline Luxury Tour Operators & Travel Agents',
        'TA/TO': 'Travel Agents / Tour Operators',
        'Aviation': 'Aviation / Airline Crew Contract',
        'Complementary': 'ITC Executive Complimentary / PR'
    }
    df['channel_clean'] = df['distribution_channel'].map(lambda x: channel_clean_map.get(x, x))
    df['market_segment_clean'] = df['market_segment'].map(lambda x: channel_clean_map.get(x, x))

    mod3_cols = [
        'booking_id', 'hotel_name', 'arrival_date', 'arrival_date_year', 'arrival_date_month',
        'is_canceled', 'guest_origin_country', 'geographic_region', 'guest_profile',
        'adults', 'children', 'babies', 'total_guests', 'customer_type', 'loyalty_program_tier',
        'is_repeated_guest', 'previous_cancellations', 'previous_bookings_not_canceled',
        'channel_clean', 'market_segment_clean', 'lead_time', 'total_of_special_requests'
    ]
    df_mod3 = df[mod3_cols].copy()
    mod3_path = os.path.join(BASE_DIR, "ITC-Guest-Demographics", "itc_guest_demographics_channels.csv")
    df_mod3.to_csv(mod3_path, index=False)
    print(f"Saved Module 3 data -> {mod3_path} ({len(df_mod3)} rows)")

    # -------------------------------------------------------------
    # MODULE 4: Operating Costs & Profitability Analytics
    # -------------------------------------------------------------
    print("Generating Module 4: Operating Costs & Profitability Analytics (USALI Hospitality Standard)...")
    
    # Total Revenue per booking
    # Minor operating departments (Spa, Laundry, Valet Transport) ~ 4% of room revenue
    df['minor_dept_revenue_inr'] = np.where(df['is_canceled'] == 0, (df['room_revenue_inr'] * np.random.uniform(0.03, 0.08)).round(2), 0.0)
    df['gross_total_revenue_inr'] = df['room_revenue_inr'] + df['combined_fnb_banquet_rev_inr'] + df['minor_dept_revenue_inr']

    # Departmental Direct Expenses:
    # 1. Rooms Department Expenses (Housekeeping, linens, guest room amenities) ~ 13.5% of room rev
    df['rooms_operating_cost_inr'] = np.where(df['is_canceled'] == 0, (df['room_revenue_inr'] * np.random.uniform(0.12, 0.15)).round(2), 0.0)
    
    # 2. F&B Cost of Goods Sold (Food & Beverage supplies, kitchen team) ~ 31.0% of F&B rev
    df['fnb_cogs_operating_cost_inr'] = np.where(df['is_canceled'] == 0, (df['total_fnb_revenue_inr'] * np.random.uniform(0.28, 0.33) + df['banquet_revenue_inr'] * np.random.uniform(0.24, 0.28)).round(2), 0.0)

    # 3. Channel Commissions (OTA commission ~ 15-18%, Corporate ~ 5%, Direct ~ 1.5% payment gateway)
    def calc_commission(row):
        rev = row['room_revenue_inr']
        ch = str(row['distribution_channel'])
        if row['is_canceled'] == 1 or rev == 0:
            return 0.0
        if 'TA' in ch or 'Online' in str(row['market_segment']):
            return round(rev * np.random.uniform(0.14, 0.18), 2)
        elif 'Corporate' in ch:
            return round(rev * np.random.uniform(0.04, 0.07), 2)
        else: # Direct
            return round(rev * 0.018, 2)
            
    df['booking_distribution_commission_inr'] = df.apply(calc_commission, axis=1)

    # Undistributed Operating Expenses (Allocated per occupied night):
    # ITC Hotels LEED Platinum Sustainable Energy & Water: ~ INR 650/room night
    # Administrative & General Staff Payroll: ~ INR 950/room night
    # Property Operations & Asset Maintenance: ~ INR 450/room night
    # Sales & ITC Brand Marketing: ~ INR 350/room night
    df['energy_utility_cost_inr'] = np.where(df['is_canceled'] == 0, (df['billed_nights'] * np.random.uniform(550, 750)).round(2), 0.0)
    df['staff_payroll_allocated_inr'] = np.where(df['is_canceled'] == 0, (df['billed_nights'] * np.random.uniform(850, 1150)).round(2), 0.0)
    df['property_maintenance_inr'] = np.where(df['is_canceled'] == 0, (df['billed_nights'] * np.random.uniform(380, 520)).round(2), 0.0)
    df['marketing_brand_cost_inr'] = np.where(df['is_canceled'] == 0, (df['billed_nights'] * np.random.uniform(300, 420)).round(2), 0.0)

    # Total Operating Costs
    df['total_operating_expenses_inr'] = (
        df['rooms_operating_cost_inr'] +
        df['fnb_cogs_operating_cost_inr'] +
        df['booking_distribution_commission_inr'] +
        df['energy_utility_cost_inr'] +
        df['staff_payroll_allocated_inr'] +
        df['property_maintenance_inr'] +
        df['marketing_brand_cost_inr']
    ).round(2)

    # Gross Operating Profit (GOP) & EBITDA
    df['gross_operating_profit_inr'] = (df['gross_total_revenue_inr'] - df['total_operating_expenses_inr']).round(2)
    df['net_profit_margin_pct'] = np.where(
        df['gross_total_revenue_inr'] > 0,
        ((df['gross_operating_profit_inr'] / df['gross_total_revenue_inr']) * 100).round(2),
        0.0
    )

    mod4_cols = [
        'booking_id', 'hotel_name', 'arrival_date', 'arrival_date_year', 'arrival_date_month',
        'is_canceled', 'billed_nights', 'room_revenue_inr', 'combined_fnb_banquet_rev_inr',
        'minor_dept_revenue_inr', 'gross_total_revenue_inr', 'rooms_operating_cost_inr',
        'fnb_cogs_operating_cost_inr', 'booking_distribution_commission_inr',
        'energy_utility_cost_inr', 'staff_payroll_allocated_inr', 'property_maintenance_inr',
        'marketing_brand_cost_inr', 'total_operating_expenses_inr', 'gross_operating_profit_inr',
        'net_profit_margin_pct'
    ]
    df_mod4 = df[mod4_cols].copy()
    mod4_path = os.path.join(BASE_DIR, "ITC-Profitability-Costs", "itc_operating_costs_profitability.csv")
    df_mod4.to_csv(mod4_path, index=False)
    print(f"Saved Module 4 data -> {mod4_path} ({len(df_mod4)} rows)")

    # -------------------------------------------------------------
    # MASTER EXECUTIVE DATASET (for Live Dashboards)
    # -------------------------------------------------------------
    print("Generating Master Executive Dataset for Unified Live Dashboard...")
    master_path = os.path.join(BASE_DIR, "ITC-Final-Dashboards", "itc_master_hospitality_data.csv")
    df.to_csv(master_path, index=False)
    print(f"Saved Master Dataset -> {master_path} ({len(df)} rows, {len(df.columns)} columns)")
    print("\nSUCCESS: All 4 module datasets + Master dataset successfully generated!")

if __name__ == '__main__':
    run_pipeline()
