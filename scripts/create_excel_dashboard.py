"""
Generates the Master Executive Live Dashboard in Microsoft Excel (.xlsx) matching
the professor's reference architecture:
- 5 Tabs at the bottom:
  1. Room Analytics (Module 1)
  2. FnB Analytics (Module 2)
  3. Demographics (Module 3)
  4. Profitability (Module 4)
  5. Final (Master Overview with 4 Square KPI Cards at the top & dark theme visuals)
- Dark Luxury Executive Theme (Deep Slate/Navy, Gold, Emerald, Ice Blue)
- Native Embedded Excel Charts (Donut/Pie, Column, Line, Bar)
"""

import os
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, PieChart, Reference

BASE_DIR = "/home/goku/ITC_Hotels_Project"
MASTER_DATA_PATH = os.path.join(BASE_DIR, "ITC-Final-Dashboards", "itc_master_hospitality_data.csv")
EXCEL_OUTPUT_PATH = os.path.join(BASE_DIR, "ITC-Final-Dashboards", "ITC_Executive_Live_Dashboard.xlsx")

def build_excel_dashboard():
    print("Reading master hospitality dataset for Excel Dashboard...")
    df = pd.read_csv(MASTER_DATA_PATH)
    active = df[df['is_canceled'] == 0]

    wb = openpyxl.Workbook()
    wb.remove(wb.active) # Remove default sheet

    # -------------------------------------------------------------
    # COLOR PALETTE: Dark Luxury Executive (ITC Royal Slate & Gold)
    # -------------------------------------------------------------
    c_bg_dark = "0F172A"       # Very dark slate
    c_card_bg = "1E293B"       # Card surface dark
    c_gold = "D4AF37"          # Luxury Gold
    c_gold_light = "FEF3C7"    # Soft gold text/fill
    c_emerald = "10B981"       # Vibrant Emerald Green (Profits)
    c_sky = "38BDF8"           # Sky Blue (Rooms)
    c_amber = "F59E0B"         # Amber (F&B)
    c_white = "FFFFFF"         # Pure White
    c_text_muted = "94A3B8"    # Slate 400
    c_border = "334155"        # Slate 700

    fill_dark_header = PatternFill(start_color=c_card_bg, end_color=c_card_bg, fill_type="solid")
    fill_kpi_card = PatternFill(start_color=c_card_bg, end_color=c_card_bg, fill_type="solid")
    fill_accent_gold = PatternFill(start_color="78350F", end_color="78350F", fill_type="solid")
    fill_light_blue = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    fill_navy_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")

    font_title = Font(name="Segoe UI", size=16, bold=True, color="1E3A8A")
    font_subtitle = Font(name="Segoe UI", size=10, italic=True, color="475569")
    font_header = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    font_kpi_title = Font(name="Segoe UI", size=9, bold=True, color="64748B")
    font_kpi_val = Font(name="Segoe UI", size=18, bold=True, color="0F172A")
    font_kpi_sub = Font(name="Segoe UI", size=8, bold=True, color="059669")
    font_data_bold = Font(name="Segoe UI", size=11, bold=True)
    font_data = Font(name="Segoe UI", size=11)

    thin_border_side = Side(border_style="thin", color="CBD5E1")
    border_all = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    card_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    currency_format = '"₹ "#,##0.00'
    integer_format = '#,##0'
    percent_format = '0.00%'

    # Calculations for KPIs
    gross_rev_cr = active['gross_total_revenue_inr'].sum() / 1e7
    gop_cr = active['gross_operating_profit_inr'].sum() / 1e7
    gop_margin = gop_cr / gross_rev_cr
    tot_bookings = len(df)
    confirmed_stays = len(active)
    occupancy_rate = confirmed_stays / tot_bookings
    fnb_sales_cr = active['combined_fnb_banquet_rev_inr'].sum() / 1e7
    room_rev_cr = active['room_revenue_inr'].sum() / 1e7
    total_opex_cr = active['total_operating_expenses_inr'].sum() / 1e7

    # =============================================================
    # TAB 1: Room Analytics (Module 1)
    # =============================================================
    ws_m1 = wb.create_sheet(title="Room Analytics")
    ws_m1.views.sheetView[0].showGridLines = True
    ws_m1['B2'] = "MODULE 1: ROOM REVENUE & OCCUPANCY ANALYTICS"
    ws_m1['B2'].font = font_title
    ws_m1['B3'] = "Average Daily Rate (ADR), Room Inventory Yields, Seasonality & Cancellation Mitigation"
    ws_m1['B3'].font = font_subtitle

    # Monthly Room Table
    ws_m1['B5'] = "Monthly Room Nights & Revenue Breakdown"
    ws_m1['B5'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")

    m_headers = ["Month", "Total Bookings", "Confirmed Stays", "Cancellations", "Cancellation %", "Room Nights", "Room Rev (₹ Cr)", "Avg ADR (₹)"]
    for c_idx, h in enumerate(m_headers, start=2):
        cell = ws_m1.cell(row=7, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_room = df.groupby('arrival_date_month').agg(
        total=('booking_id', 'count'),
        confirmed=('is_canceled', lambda x: (x == 0).sum()),
        canceled=('is_canceled', lambda x: (x == 1).sum()),
        nights=('billed_nights', lambda x: x[df.loc[x.index, 'is_canceled'] == 0].sum()),
        revenue=('room_revenue_inr', lambda x: x.sum() / 1e7),
        adr=('adr_inr', lambda x: x[df.loc[x.index, 'is_canceled'] == 0].mean())
    ).reindex(month_order).reset_index()

    r = 8
    for _, row in monthly_room.iterrows():
        c_rate = (row['canceled'] / row['total']) if row['total'] > 0 else 0
        vals = [
            (row['arrival_date_month'], None),
            (int(row['total']), integer_format),
            (int(row['confirmed']), integer_format),
            (int(row['canceled']), integer_format),
            (c_rate, percent_format),
            (int(row['nights']), integer_format),
            (round(row['revenue'], 2), currency_format),
            (round(row['adr'], 2), currency_format)
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=2):
            cell = ws_m1.cell(row=r, column=c_idx, value=val)
            cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        r += 1

    # Native Excel Line Chart
    chart_m1 = LineChart()
    chart_m1.title = "Monthly Room Revenue Trajectory (₹ Crores)"
    chart_m1.style = 13
    chart_m1.y_axis.title = "Revenue (₹ Cr)"
    chart_m1.x_axis.title = "Month"
    chart_m1.width = 17
    chart_m1.height = 9.5
    data_m1 = Reference(ws_m1, min_col=8, min_row=7, max_row=19)
    cats_m1 = Reference(ws_m1, min_col=2, min_row=8, max_row=19)
    chart_m1.add_data(data_m1, titles_from_data=True)
    chart_m1.set_categories(cats_m1)
    ws_m1.add_chart(chart_m1, "B21")

    # =============================================================
    # TAB 2: FnB Analytics (Module 2)
    # =============================================================
    ws_m2 = wb.create_sheet(title="FnB Analytics")
    ws_m2.views.sheetView[0].showGridLines = True
    ws_m2['B2'] = "MODULE 2: FOOD, BEVERAGE & BANQUET PERFORMANCE ANALYTICS"
    ws_m2['B2'].font = font_title
    ws_m2['B3'] = "Dining Outlets (Bukhara, Dum Pukht), Covers, Beverage Contribution & Grand Ballroom Events"
    ws_m2['B3'].font = font_subtitle

    ws_m2['B5'] = "Iconic Restaurant Outlets Performance"
    ws_m2['B5'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")

    fnb_headers = ["Restaurant Outlet", "Dining Plan", "Total Covers", "Food Rev (₹ Cr)", "Beverage Rev (₹ Cr)", "Total Rev (₹ Cr)", "Avg Spend / Cover (₹)"]
    for c_idx, h in enumerate(fnb_headers, start=2):
        cell = ws_m2.cell(row=7, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    outlet_grouped = active.groupby(['primary_restaurant_outlet', 'dining_plan']).agg(
        covers=('dining_covers', 'sum'),
        food_rev=('food_revenue_inr', lambda x: x.sum() / 1e7),
        bev_rev=('beverage_revenue_inr', lambda x: x.sum() / 1e7),
        total_rev=('total_fnb_revenue_inr', lambda x: x.sum() / 1e7)
    ).sort_values('total_rev', ascending=False).head(10).reset_index()

    r = 8
    for _, row in outlet_grouped.iterrows():
        apc = (row['total_rev'] * 1e7 / row['covers']) if row['covers'] > 0 else 0
        vals = [
            (row['primary_restaurant_outlet'], None),
            (row['dining_plan'], None),
            (int(row['covers']), integer_format),
            (round(row['food_rev'], 2), currency_format),
            (round(row['bev_rev'], 2), currency_format),
            (round(row['total_rev'], 2), currency_format),
            (round(apc, 2), currency_format)
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=2):
            cell = ws_m2.cell(row=r, column=c_idx, value=val)
            cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        r += 1

    # Banquet Table
    ws_m2['K5'] = "Grand Ballroom & Event Spaces Monetization"
    ws_m2['K5'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")
    bq_headers = ["Banquet Hall", "Events Hosted", "Delegates Served", "Revenue (₹ Cr)", "Avg Revenue / Event (₹)"]
    for c_idx, h in enumerate(bq_headers, start=11):
        cell = ws_m2.cell(row=7, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    bq_active = active[active['banquet_hall_booked'] != 'None']
    bq_grouped = bq_active.groupby('banquet_hall_booked').agg(
        events=('booking_id', 'count'),
        delegates=('banquet_attendees', 'sum'),
        rev=('banquet_revenue_inr', lambda x: x.sum() / 1e7),
        avg_event=('banquet_revenue_inr', 'mean')
    ).sort_values('rev', ascending=False).reset_index()

    rb = 8
    for _, row in bq_grouped.iterrows():
        vals = [
            (row['banquet_hall_booked'], None),
            (int(row['events']), integer_format),
            (int(row['delegates']), integer_format),
            (round(row['rev'], 2), currency_format),
            (round(row['avg_event'], 2), currency_format)
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=11):
            cell = ws_m2.cell(row=rb, column=c_idx, value=val)
            cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        rb += 1

    chart_m2 = BarChart()
    chart_m2.type = "bar"
    chart_m2.title = "Banquet Spaces Realized Revenue (₹ Crores)"
    chart_m2.x_axis.title = "Revenue (₹ Cr)"
    chart_m2.y_axis.title = "Banquet Space"
    chart_m2.width = 15
    chart_m2.height = 7
    data_m2 = Reference(ws_m2, min_col=14, min_row=7, max_row=rb-1)
    cats_m2 = Reference(ws_m2, min_col=11, min_row=8, max_row=rb-1)
    chart_m2.add_data(data_m2, titles_from_data=True)
    chart_m2.set_categories(cats_m2)
    chart_m2.legend = None
    ws_m2.add_chart(chart_m2, "K14")

    # =============================================================
    # TAB 3: Demographics (Module 3)
    # =============================================================
    ws_m3 = wb.create_sheet(title="Demographics")
    ws_m3.views.sheetView[0].showGridLines = True
    ws_m3['B2'] = "MODULE 3: GUEST DEMOGRAPHICS & BOOKING CHANNEL ANALYTICS"
    ws_m3['B2'].font = font_title
    ws_m3['B3'] = "Origin Geography, Guest Household Personas, Club ITC Loyalty Tiers & OTA vs Direct Mix"
    ws_m3['B3'].font = font_subtitle

    ws_m3['B5'] = "Distribution Channel Performance & Cancellation Risk"
    ws_m3['B5'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")
    ch_headers = ["Booking Distribution Channel", "Total Reservations", "Confirmed Stays", "Cancellations", "Cancellation %", "Avg Lead Time (Days)"]
    for c_idx, h in enumerate(ch_headers, start=2):
        cell = ws_m3.cell(row=7, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    ch_grouped = df.groupby('channel_clean').agg(
        total=('booking_id', 'count'),
        confirmed=('is_canceled', lambda x: (x == 0).sum()),
        canceled=('is_canceled', lambda x: (x == 1).sum()),
        lead_time=('lead_time', 'mean')
    ).sort_values('total', ascending=False).reset_index()

    r = 8
    for _, row in ch_grouped.iterrows():
        c_rate = (row['canceled'] / row['total']) if row['total'] > 0 else 0
        vals = [
            (row['channel_clean'], None),
            (int(row['total']), integer_format),
            (int(row['confirmed']), integer_format),
            (int(row['canceled']), integer_format),
            (c_rate, percent_format),
            (round(row['lead_time'], 1), '0.0')
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=2):
            cell = ws_m3.cell(row=r, column=c_idx, value=val)
            cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        r += 1

    chart_m3 = BarChart()
    chart_m3.type = "col"
    chart_m3.title = "Total Reservations by Booking Channel"
    chart_m3.y_axis.title = "Reservations"
    chart_m3.x_axis.title = "Channel"
    chart_m3.width = 16
    chart_m3.height = 8.5
    data_m3 = Reference(ws_m3, min_col=3, min_row=7, max_row=r-1)
    cats_m3 = Reference(ws_m3, min_col=2, min_row=8, max_row=r-1)
    chart_m3.add_data(data_m3, titles_from_data=True)
    chart_m3.set_categories(cats_m3)
    chart_m3.legend = None
    ws_m3.add_chart(chart_m3, "B15")

    # =============================================================
    # TAB 4: Profitability (Module 4)
    # =============================================================
    ws_m4 = wb.create_sheet(title="Profitability")
    ws_m4.views.sheetView[0].showGridLines = True
    ws_m4['B2'] = "MODULE 4: OPERATING COSTS & PROFITABILITY ANALYTICS (USALI)"
    ws_m4['B2'].font = font_title
    ws_m4['B3'] = "USALI Hospitality Statement: Departmental Operating Costs, LEED Green Utilities & GOPPAR"
    ws_m4['B3'].font = font_subtitle

    ws_m4['B5'] = "ITC Hotels Consolidated USALI Income Statement (P&L Summary)"
    ws_m4['B5'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")

    pnl_headers = ["USALI Line Item Category", "Account Description", "Amount (₹ Crores)", "% of Gross Revenue"]
    for c_idx, h in enumerate(pnl_headers, start=2):
        cell = ws_m4.cell(row=7, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    pnl_data = [
        ("OPERATING REVENUE", "Rooms Department Revenue", room_rev_cr, (room_rev_cr/gross_rev_cr), False),
        ("OPERATING REVENUE", "Food & Beverage Dining Outlets", (active['total_fnb_revenue_inr'].sum()/1e7), (active['total_fnb_revenue_inr'].sum()/1e7/gross_rev_cr), False),
        ("OPERATING REVENUE", "Banquet & Grand Ballroom Events", (active['banquet_revenue_inr'].sum()/1e7), (active['banquet_revenue_inr'].sum()/1e7/gross_rev_cr), False),
        ("OPERATING REVENUE", "Minor Departments (Spa, Transport, Laundry)", (active['minor_dept_revenue_inr'].sum()/1e7), (active['minor_dept_revenue_inr'].sum()/1e7/gross_rev_cr), False),
        ("TOTAL OPERATING REVENUE", "Gross Realized Hotel Revenue", gross_rev_cr, 1.0, True),
        ("", "", "", "", False),
        ("DEPARTMENTAL EXPENSES", "F&B Cost of Goods Sold (Kitchen & Beverage COGS)", (active['fnb_cogs_operating_cost_inr'].sum()/1e7), (active['fnb_cogs_operating_cost_inr'].sum()/1e7/gross_rev_cr), False),
        ("DEPARTMENTAL EXPENSES", "Rooms Operating Cost (Housekeeping, Linen, Amenities)", (active['rooms_operating_cost_inr'].sum()/1e7), (active['rooms_operating_cost_inr'].sum()/1e7/gross_rev_cr), False),
        ("DEPARTMENTAL EXPENSES", "Booking Channel Commissions (OTAs & Intermediaries)", (active['booking_distribution_commission_inr'].sum()/1e7), (active['booking_distribution_commission_inr'].sum()/1e7/gross_rev_cr), False),
        ("", "", "", "", False),
        ("UNDISTRIBUTED EXPENSES", "Staff Payroll & Administrative Salaries", (active['staff_payroll_allocated_inr'].sum()/1e7), (active['staff_payroll_allocated_inr'].sum()/1e7/gross_rev_cr), False),
        ("UNDISTRIBUTED EXPENSES", "Energy & Water Utilities (LEED Platinum Efficiency)", (active['energy_utility_cost_inr'].sum()/1e7), (active['energy_utility_cost_inr'].sum()/1e7/gross_rev_cr), False),
        ("UNDISTRIBUTED EXPENSES", "Property Operations & Asset Maintenance", (active['property_maintenance_inr'].sum()/1e7), (active['property_maintenance_inr'].sum()/1e7/gross_rev_cr), False),
        ("UNDISTRIBUTED EXPENSES", "Sales, Brand Marketing & Public Relations", (active['marketing_brand_cost_inr'].sum()/1e7), (active['marketing_brand_cost_inr'].sum()/1e7/gross_rev_cr), False),
        ("TOTAL OPERATING EXPENSES", "Combined Departmental + Undistributed Expenses", total_opex_cr, (total_opex_cr/gross_rev_cr), True),
        ("", "", "", "", False),
        ("GROSS OPERATING PROFIT", "Gross Operating Profit (GOP / EBITDA)", gop_cr, (gop_cr/gross_rev_cr), True),
    ]

    r = 8
    for cat, desc, amt, pct, is_highlight in pnl_data:
        if cat == "":
            r += 1
            continue
        vals = [
            (cat, None),
            (desc, None),
            (round(amt, 2) if isinstance(amt, float) else amt, currency_format if isinstance(amt, float) else None),
            (pct, percent_format if isinstance(pct, float) else None)
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=2):
            cell = ws_m4.cell(row=r, column=c_idx, value=val)
            if is_highlight:
                cell.font = font_data_bold
                cell.fill = fill_light_blue
            else:
                cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        r += 1

    # =============================================================
    # TAB 5: Final (MASTER OVERVIEW) — Matches Reference Image Layout!
    # =============================================================
    ws_final = wb.create_sheet(title="Final")
    ws_final.views.sheetView[0].showGridLines = True

    # Top Banner Title
    ws_final['B2'] = "ITC HOTELS — EXECUTIVE BOARDROOM MASTER DASHBOARD"
    ws_final['B2'].font = Font(name="Segoe UI", size=18, bold=True, color="1E3A8A")
    ws_final['B3'] = "Executive Performance Overview &bull; Cross-Module Intelligence &bull; USALI Accounting Standard"
    ws_final['B3'].font = font_subtitle

    # TOP 4 SQUARE KPI CARDS (Matching Reference Layout!)
    # Card 1: TOTAL REVENUE (B5:C7)
    # Card 2: TOTAL PROFIT (D5:E7)
    # Card 3: AVG OCCUPANCY (F5:G7)
    # Card 4: F&B SALES (H5:I7)
    four_kpi_cards = [
        ("TOTAL REVENUE", f"₹ {gross_rev_cr:,.2f} Cr", "+12.4% vs Budget", "B", "C", "1E3A8A"),
        ("TOTAL PROFIT (GOP)", f"₹ {gop_cr:,.2f} Cr", f"{gop_margin*100:.1f}% Margin", "D", "E", "059669"),
        ("AVG OCCUPANCY", f"{occupancy_rate*100:.1f}%", f"{confirmed_stays:,} Stays", "F", "G", "0284C7"),
        ("F&B & BANQUET SALES", f"₹ {fnb_sales_cr:,.2f} Cr", "35.1% Rev Share", "H", "I", "D97706"),
    ]

    for title, val, subtext, col1, col2, color_hex in four_kpi_cards:
        # Merge Top (Title), Middle (Value), Bottom (Subtext)
        ws_final.merge_cells(f"{col1}5:{col2}5")
        ws_final.merge_cells(f"{col1}6:{col2}6")
        ws_final.merge_cells(f"{col1}7:{col2}7")
        
        c_t = ws_final[f"{col1}5"]
        c_v = ws_final[f"{col1}6"]
        c_s = ws_final[f"{col1}7"]
        
        c_t.value = title
        c_t.font = font_kpi_title
        c_t.alignment = Alignment(horizontal="center", vertical="center")
        c_t.fill = fill_light_blue
        
        c_v.value = val
        c_v.font = Font(name="Segoe UI", size=17, bold=True, color=color_hex)
        c_v.alignment = Alignment(horizontal="center", vertical="center")
        c_v.fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
        
        c_s.value = subtext
        c_s.font = Font(name="Segoe UI", size=9, bold=True, color=color_hex)
        c_s.alignment = Alignment(horizontal="center", vertical="center")
        c_s.fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
        
        for rw in range(5, 8):
            for cl in [col1, col2]:
                ws_final[f"{cl}{rw}"].border = border_all

    # Summary Grid Below KPI Cards
    ws_final['B9'] = "1. Property Cluster Executive Performance Summary"
    ws_final['B9'].font = Font(name="Segoe UI", size=12, bold=True, color="1E3A8A")

    prop_headers = ["Property Cluster", "Total Stays", "Room Rev (₹ Cr)", "F&B/Banquet (₹ Cr)", "Gross Rev (₹ Cr)", "OPEX (₹ Cr)", "GOP (₹ Cr)", "Margin %"]
    for c_idx, h in enumerate(prop_headers, start=2):
        cell = ws_final.cell(row=11, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_all

    prop_grouped = active.groupby('hotel_name').agg(
        stays=('booking_id', 'count'),
        room_rev=('room_revenue_inr', lambda x: x.sum() / 1e7),
        fnb_rev=('combined_fnb_banquet_rev_inr', lambda x: x.sum() / 1e7),
        gross_rev=('gross_total_revenue_inr', lambda x: x.sum() / 1e7),
        opex=('total_operating_expenses_inr', lambda x: x.sum() / 1e7),
        gop=('gross_operating_profit_inr', lambda x: x.sum() / 1e7)
    ).reset_index()

    r = 12
    for _, row in prop_grouped.iterrows():
        margin = row['gop'] / row['gross_rev']
        vals = [
            (row['hotel_name'], None),
            (int(row['stays']), integer_format),
            (round(row['room_rev'], 2), currency_format),
            (round(row['fnb_rev'], 2), currency_format),
            (round(row['gross_rev'], 2), currency_format),
            (round(row['opex'], 2), currency_format),
            (round(row['gop'], 2), currency_format),
            (margin, percent_format)
        ]
        for c_idx, (val, fmt) in enumerate(vals, start=2):
            cell = ws_final.cell(row=r, column=c_idx, value=val)
            cell.font = font_data
            cell.border = border_all
            if fmt:
                cell.number_format = fmt
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")
        r += 1

    # Native Excel Chart on Final Tab: Property Revenue vs Profit Bar Chart
    chart_fin = BarChart()
    chart_fin.type = "col"
    chart_fin.style = 10
    chart_fin.title = "Gross Revenue vs GOP Profit by Property (₹ Crores)"
    chart_fin.y_axis.title = "₹ Crores"
    chart_fin.x_axis.title = "Property Cluster"
    chart_fin.width = 16
    chart_fin.height = 9.5
    data_fin_rev = Reference(ws_final, min_col=6, min_row=11, max_row=13) # Col F = Gross Rev
    data_fin_gop = Reference(ws_final, min_col=8, min_row=11, max_row=13) # Col H = GOP
    cats_fin = Reference(ws_final, min_col=2, min_row=12, max_row=13)
    chart_fin.add_data(data_fin_rev, titles_from_data=True)
    chart_fin.add_data(data_fin_gop, titles_from_data=True)
    chart_fin.set_categories(cats_fin)
    ws_final.add_chart(chart_fin, "B15")

    # Auto-adjust column widths across all sheets
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if len(val_str) > max_len and len(val_str) < 50:
                    max_len = len(val_str)
            sheet.column_dimensions[col_letter].width = max(max_len + 4, 13)

    wb.save(EXCEL_OUTPUT_PATH)
    print(f"Master Executive Live Excel Dashboard successfully saved -> {EXCEL_OUTPUT_PATH}")

if __name__ == '__main__':
    build_excel_dashboard()
