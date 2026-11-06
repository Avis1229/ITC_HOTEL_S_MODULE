# ITC Hotels Analytics Project — Viva & Presentation Cheat Sheet
### Quick Revision Guide for Professor / Evaluation Panel

---

### Q1. Aapka dataset kahan se aaya aur ITC context me kaise transform kiya?
- **Source:** Kaggle ka real-world *Hotel Booking Demand Dataset* (119,390 rows, 32 columns).
- **Transformation:**
  - Standard dates, lead times, real cancellation rates, aur room types filter kiye gaye.
  - Indian context me convert karne ke liye Currency standard INR (₹) me map kiya gaya.
  - Property mapping: *Resort Hotel* ko **ITC Grand Bharat & ITC Mughal (Luxury Resort & Spa)** aur *City Hotel* ko **ITC Maurya & ITC Grand Chola (Executive Luxury)** me map kiya gaya.
  - ITC ke luxury brands add kiye gaye: Dining outlets (*Bukhara, Dum Pukht, Peshawri, Avartana*) aur Grand Ballrooms (*Rajputana Ballroom, Chola Conclave*) for MICE conferences & destination royal weddings.

---

### Q2. Charon Modules me kya-kya KPIs hain?

#### Module 1: Room Revenue & Occupancy Analytics
- **ADR (Average Daily Rate):** ₹ 8,941 per room night.
- **Confirmed Stays vs Cancellations:** 75,166 confirmed (62.9%), ~37.1% cancellations.
- **Key Finding:** 90 din se pehle book hone wale reservations ka cancellation rate >50% hota hai. Isliye non-refundable early-bird rates zaroori hain.

#### Module 2: Food, Beverage & Banquet Performance Analytics
- **Total Dining & Banquet Revenue:** ₹ 104.8 Crores across 119k bookings.
- **Top Outlets:** *Bukhara* and *Dum Pukht* lead dining sales.
- **Banquet Events:** Royal Weddings deliver highest revenue ticket (~₹10L-15L per event).
- **APC (Average Spend per Cover):** ~₹ 2,450 per dining guest.

#### Module 3: Guest Demographics & Booking Channels
- **Channels:** Direct (ITC App/Web), Corporate B2B, OTAs (MakeMyTrip, Booking.com), Offline Agents.
- **Critical Insight:** OTAs par cancellation rate 41% hai aur 15-18% commission lagta hai. Jabki Club ITC Culinaire / Gold members ka cancellation rate <12% hai aur commission 0% hai.
- **Strategy:** Guests ko direct app par book karane ke liye 15% dining credits offer karein.

#### Module 4: Operating Costs & Profitability (USALI Standard)
- **Framework:** USALI (*Uniform System of Accounts for the Lodging Industry*).
- **Gross Revenue:** ₹ 298.42 Crores.
- **Gross Operating Profit (GOP / EBITDA):** ₹ 143.68 Crores.
- **GOP Margin:** **48.15%** (Luxury industry benchmark 38-42% se kaafi behtar).
- **GOPPAR:** ₹ 5,612 per room night.
- **LEED Platinum Advantage:** ITC Hotels green wind & solar power use karte hain, isliye utility energy cost sirf 4.2% of revenue rehti hai.

---

### Q3. Dashboards kaise bane hain?
1. **Excel Dashboard (`ITC_Executive_Live_Dashboard.xlsx`):**
   - 5 tabs: Executive Scorecard, Room Revenue, F&B & Banquets, Demographics, USALI Profitability.
   - Formatted currency (`₹`), auto-fitted columns, aur **native embedded Excel charts** (Bar, Line, Column).
2. **Interactive Live Web Dashboard (`index.html`):**
   - Pure HTML5 + Tailwind CSS + Chart.js.
   - Ubuntu browser me bina Windows khole interactive charts aur live filters dikhane ke liye.
3. **Power BI Ready Model (`POWER_BI_MODELING_GUIDE.md`):**
   - Windows me Power BI Desktop me `itc_master_hospitality_data.csv` load karke ready DAX measures drag-drop karne ke liye.
