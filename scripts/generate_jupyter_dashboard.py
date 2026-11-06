"""
Generates the Interactive Jupyter Notebook Final Dashboard using Plotly.
Matches the professor's strict UI/UX:
- Dark theme background (Plotly Dark with Luxury Slate & Gold accents)
- Top 4 Square KPI Cards (Total Revenue, Total Profit, Avg Occupancy, F&B Sales)
- Interactive visuals: Donut chart, Waterfall chart, Multi-line seasonality, Bar charts
- Interactive module tabs & views
"""

import os
import nbformat as nbf

BASE_DIR = "/home/goku/ITC_Hotels_Project"
OUTPUT_NB_PATH = os.path.join(BASE_DIR, "ITC-Final-Dashboards", "interactive_jupyter_dashboard.ipynb")

def create_notebook():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell("""# 🏨 ITC HOTELS — EXECUTIVE BOARDROOM LIVE DASHBOARD
### University Capstone Analytics Project | Executive Multi-Module Presentation
**Author:** Avi Singh &bull; **Environment:** Python / Pandas / Plotly (Jupyter Interactive)

---
> **UI/UX Architecture:**
> - **Top Row:** 4 Square KPI Scorecards (Total Revenue, Total Profit / GOP, Avg Occupancy Rate, F&B & Banquet Sales)
> - **Visuals:** Interactive Donut Chart, USALI Waterfall P&L Chart, Seasonality Multi-Bar/Line Chart, and Channel Risk Chart.
> - **Dark Luxury Theme:** Optimized for executive board presentations.
"""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# 1. Load Master Dataset
df = pd.read_csv('itc_master_hospitality_data.csv')
active = df[df['is_canceled'] == 0]
print(f"Loaded {len(df):,} total bookings ({len(active):,} confirmed stays)")"""),

        nbf.v4.new_markdown_cell("""---
## 1. Top 4 Square KPI Summary Cards
*Total Revenue, Total Profit (GOP), Avg Occupancy, and Food & Beverage Sales*"""),

        nbf.v4.new_code_cell("""# Calculate Key Metrics
gross_rev_cr = active['gross_total_revenue_inr'].sum() / 1e7
gop_cr = active['gross_operating_profit_inr'].sum() / 1e7
gop_margin = (gop_cr / gross_rev_cr) * 100
occupancy_rate = (len(active) / len(df)) * 100
fnb_sales_cr = active['combined_fnb_banquet_rev_inr'].sum() / 1e7

# Build 4 Square KPI Cards in a single row using Plotly Indicator
fig_kpis = make_subplots(
    rows=1, cols=4,
    specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]]
)

fig_kpis.add_trace(go.Indicator(
    mode="number+delta",
    value=gross_rev_cr,
    number={'prefix': "₹ ", 'suffix': " Cr", 'valueformat': ".2f", 'font': {'color': '#38bdf8', 'size': 32}},
    title={'text': "<b>TOTAL REVENUE</b><br><span style='font-size:11px;color:#94a3b8'>Gross Realized</span>"},
    delta={'reference': 265.0, 'relative': True, 'position': "bottom", 'valueformat': ".1%"},
), row=1, col=1)

fig_kpis.add_trace(go.Indicator(
    mode="number+delta",
    value=gop_cr,
    number={'prefix': "₹ ", 'suffix': " Cr", 'valueformat': ".2f", 'font': {'color': '#10b981', 'size': 32}},
    title={'text': "<b>TOTAL PROFIT (GOP)</b><br><span style='font-size:11px;color:#94a3b8'>EBITDA (48.15% Margin)</span>"},
    delta={'reference': 125.0, 'relative': True, 'position': "bottom", 'valueformat': ".1%"},
), row=1, col=2)

fig_kpis.add_trace(go.Indicator(
    mode="number",
    value=occupancy_rate,
    number={'suffix': "%", 'valueformat': ".1f", 'font': {'color': '#f59e0b', 'size': 32}},
    title={'text': "<b>AVG OCCUPANCY</b><br><span style='font-size:11px;color:#94a3b8'>75,166 Confirmed Stays</span>"},
), row=1, col=3)

fig_kpis.add_trace(go.Indicator(
    mode="number+delta",
    value=fnb_sales_cr,
    number={'prefix': "₹ ", 'suffix': " Cr", 'valueformat': ".2f", 'font': {'color': '#e879f9', 'size': 32}},
    title={'text': "<b>F&B & BANQUET SALES</b><br><span style='font-size:11px;color:#94a3b8'>Bukhara, Events & Dining</span>"},
    delta={'reference': 90.0, 'relative': True, 'position': "bottom", 'valueformat': ".1%"},
), row=1, col=4)

fig_kpis.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    height=200,
    margin=dict(l=20, r=20, t=50, b=20)
)
fig_kpis.show()"""),

        nbf.v4.new_markdown_cell("""---
## 2. Interactive Donut Chart: Revenue Stream Contribution
*Visualizing the share of Room Revenue, Food & Beverage Dining, Banquet Events, and Minor Departments.*"""),

        nbf.v4.new_code_cell("""# Revenue breakdown
room_rev = active['room_revenue_inr'].sum() / 1e7
dining_rev = active['total_fnb_revenue_inr'].sum() / 1e7
banquet_rev = active['banquet_revenue_inr'].sum() / 1e7
minor_rev = active['minor_dept_revenue_inr'].sum() / 1e7

rev_df = pd.DataFrame({
    'Revenue_Stream': ['Room Inventory Revenue', 'F&B Restaurant Dining', 'Banquet & MICE Events', 'Minor Depts (Spa, Laundry)'],
    'Revenue_Cr': [room_rev, dining_rev, banquet_rev, minor_rev]
})

fig_donut = px.pie(
    rev_df,
    names='Revenue_Stream',
    values='Revenue_Cr',
    hole=0.6,
    color_discrete_sequence=['#38bdf8', '#f59e0b', '#a855f7', '#10b981'],
    title="<b>ITC Luxury Revenue Mix (Total: ₹ 298.42 Cr)</b>"
)

fig_donut.update_traces(
    textinfo='percent+label',
    textfont=dict(color='white', size=12),
    marker=dict(line=dict(color='#0f172a', width=3))
)

fig_donut.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    height=450,
    margin=dict(l=40, r=40, t=60, b=30),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)
fig_donut.show()"""),

        nbf.v4.new_markdown_cell("""---
## 3. USALI Waterfall Chart: From Gross Revenue to Operating Profit
*Step-by-step financial walk-down showing direct departmental costs, staff payroll, LEED Platinum green utilities, and net GOP.*"""),

        nbf.v4.new_code_cell("""# USALI Cost items
fnb_cogs = -(active['fnb_cogs_operating_cost_inr'].sum() / 1e7)
staff_payroll = -(active['staff_payroll_allocated_inr'].sum() / 1e7)
rooms_cost = -(active['rooms_operating_cost_inr'].sum() / 1e7)
energy_cost = -(active['energy_utility_cost_inr'].sum() / 1e7)
ota_comm = -(active['booking_distribution_commission_inr'].sum() / 1e7)
maintenance = -(active['property_maintenance_inr'].sum() / 1e7)
marketing = -(active['marketing_brand_cost_inr'].sum() / 1e7)

fig_waterfall = go.Figure(go.Waterfall(
    name="USALI P&L",
    orientation="v",
    measure=["relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "total"],
    x=[
        "Gross Revenue", "F&B COGS", "Staff Payroll", "Rooms Cost",
        "LEED Utilities", "OTA Commission", "Maintenance", "Brand Marketing", "Gross Operating Profit"
    ],
    textposition="outside",
    text=[
        f"₹ {gross_rev_cr:.1f} Cr", f"₹ {fnb_cogs:.1f} Cr", f"₹ {staff_payroll:.1f} Cr", f"₹ {rooms_cost:.1f} Cr",
        f"₹ {energy_cost:.1f} Cr", f"₹ {ota_comm:.1f} Cr", f"₹ {maintenance:.1f} Cr", f"₹ {marketing:.1f} Cr",
        f"₹ {gop_cr:.1f} Cr"
    ],
    y=[gross_rev_cr, fnb_cogs, staff_payroll, rooms_cost, energy_cost, ota_comm, maintenance, marketing, 0],
    connector={"line": {"color": "#64748b"}},
    decreasing={"marker": {"color": "#f43f5e"}},
    increasing={"marker": {"color": "#38bdf8"}},
    totals={"marker": {"color": "#10b981"}}
))

fig_waterfall.update_layout(
    title="<b>USALI Hospitality P&L Waterfall Walk-Down (₹ Crores)</b>",
    template="plotly_dark",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    height=480,
    margin=dict(l=40, r=40, t=60, b=40),
    yaxis=dict(title="₹ Crores")
)
fig_waterfall.show()"""),

        nbf.v4.new_markdown_cell("""---
## 4. Multi-Series Seasonality Chart: Monthly Revenue vs Profitability Trajectory"""),

        nbf.v4.new_code_cell("""month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_perf = active.groupby('arrival_date_month').agg(
    revenue=('gross_total_revenue_inr', lambda x: x.sum() / 1e7),
    gop=('gross_operating_profit_inr', lambda x: x.sum() / 1e7)
).reindex(month_order).reset_index()

monthly_perf['margin_pct'] = (monthly_perf['gop'] / monthly_perf['revenue']) * 100

fig_monthly = make_subplots(specs=[[{"secondary_y": True}]])

fig_monthly.add_trace(
    go.Bar(
        x=monthly_perf['arrival_date_month'],
        y=monthly_perf['revenue'],
        name="Gross Revenue (₹ Cr)",
        marker_color="#38bdf8"
    ),
    secondary_y=False
)

fig_monthly.add_trace(
    go.Bar(
        x=monthly_perf['arrival_date_month'],
        y=monthly_perf['gop'],
        name="GOP Profit (₹ Cr)",
        marker_color="#10b981"
    ),
    secondary_y=False
)

fig_monthly.add_trace(
    go.Scatter(
        x=monthly_perf['arrival_date_month'],
        y=monthly_perf['margin_pct'],
        name="GOP Margin %",
        mode="lines+markers",
        line=dict(color="#f59e0b", width=3),
        marker=dict(size=8)
    ),
    secondary_y=True
)

fig_monthly.update_layout(
    title="<b>Monthly Revenue, GOP Profit & Margin Trajectory</b>",
    template="plotly_dark",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    barmode="group",
    height=450,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig_monthly.update_yaxes(title_text="Amount (₹ Crores)", secondary_y=False)
fig_monthly.update_yaxes(title_text="GOP Margin (%)", secondary_y=True, range=[35, 60])
fig_monthly.show()"""),

        nbf.v4.new_markdown_cell("""---
## 5. Booking Channels & Intermediary Acquisition Risk"""),

        nbf.v4.new_code_cell("""channel_analysis = df.groupby('channel_clean').agg(
    total_bookings=('booking_id', 'count'),
    cancellations=('is_canceled', 'sum'),
    cancel_rate=('is_canceled', lambda x: x.mean() * 100),
    confirmed_stays=('is_canceled', lambda x: (x == 0).sum())
).sort_values('total_bookings', ascending=False).reset_index()

fig_channel = px.bar(
    channel_analysis,
    x='channel_clean',
    y='total_bookings',
    color='cancel_rate',
    color_continuous_scale='Reds',
    title="<b>Distribution Channels: Booking Volume vs Cancellation Risk (%)</b>",
    labels={'total_bookings': 'Total Bookings', 'cancel_rate': 'Cancellation %', 'channel_clean': 'Distribution Channel'},
    text='total_bookings'
)

fig_channel.update_traces(texttemplate='%{text:,}', textposition='outside')
fig_channel.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    height=450
)
fig_channel.show()"""),

        nbf.v4.new_markdown_cell("""---
## 6. Executive Strategic Recommendations Summary
1. **Early-Bird Price Fences:** Implement strict deposits on bookings placed >90 days in advance to mitigate 52% cancellation loss.
2. **Channel Migration to Club ITC:** Shift 5% of third-party OTA bookings to direct ITC App reservations to save ₹2.2 Crores in pure commission.
3. **Curated F&B Upselling:** Introduce wine-pairing packages at Bukhara and Dum Pukht to lift beverage sales contribution from 24% to 35%.""")
    ]

    with open(OUTPUT_NB_PATH, 'w') as f:
        nbf.write(nb, f)
    print(f"Jupyter Interactive Dashboard notebook written -> {OUTPUT_NB_PATH}")

if __name__ == '__main__':
    create_notebook()
