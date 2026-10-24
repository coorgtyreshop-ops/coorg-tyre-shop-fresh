import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration with Dark Theme
st.set_page_config(
    page_title="COORG TYRE SHOP",
    page_icon="🛞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# SESSION STATE DATA INITIALIZATION
# ---------------------------------------------------------
if "tyre_stock" not in st.session_state:
    st.session_state.tyre_stock = [
        {"BRAND": "CEAT", "VEHICLE": "Car", "SIZE": "145/70/12", "CONDITION": "New", "PATTERN": "GRIP", "STOCK": 4, "PURCHASE RATE": 2150, "SELLING RATE": 2850},
        {"BRAND": "APOLLO", "VEHICLE": "Scooter", "SIZE": "90/100/10", "CONDITION": "New", "PATTERN": "53J GRIP", "STOCK": 2, "PURCHASE RATE": 1020, "SELLING RATE": 1450}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = [
        {"BRAND": "BRAZA", "VEHICLE": "Scooter", "SIZE": "3.00-10", "CONDITION": "New", "STOCK": 5, "PURCHASE RATE": 180, "SELLING RATE": 250},
        {"BRAND": "MRF", "VEHICLE": "Bike", "SIZE": "3.00-18", "CONDITION": "New", "STOCK": 3, "PURCHASE RATE": 210, "SELLING RATE": 290}
    ]

if "puncture_items" not in st.session_state:
    st.session_state.puncture_items = [
        {"SERVICE": "Tubeless Puncture", "RATE": 100},
        {"SERVICE": "Tube Puncture", "RATE": 80}
    ]

if "pigmi_data" not in st.session_state:
    st.session_state.pigmi_data = [
        {"NAME": "SHAHAJAHAN E", "LOCATION": "ONTIYANGADI", "PHONE": "9900316275", "BANK": "Janaasha South Nidhi Ltd", "AC_NO": "035601167", "DAILY_TARGET": 500, "OLD_BAL": 1000, "COLLECTED": 6000, "WITHDRAWN": 0, "BALANCE": 7000, "LAST_DATE": str(date.today())}
    ]

if "sales_data" not in st.session_state:
    st.session_state.sales_data = [
        {"ITEM": "Tubeless Puncture", "SIZE": "N/A", "QTY": 1, "AMOUNT": 100, "MODE": "Cash", "DATE": str(date.today())}
    ]

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = [
        {"CATEGORY": "Room Rent", "RECIPIENT": "Building Owner", "AMOUNT": 15000, "URGENCY": "Normal", "DATE": "2026-10-01"}
    ]

if "credit_data" not in st.session_state:
    st.session_state.credit_data = [
        {"CUSTOMER": "Ramesh", "PHONE": "9876543210", "DETAILS": "Tyre Balance", "AMOUNT": 1500, "STATUS": "Pending"}
    ]

if "market_rates" not in st.session_state:
    st.session_state.market_rates = [
        {"BRAND": "APOLLO", "SIZE": "90/100/10", "ONLINE_PRICE": 1450, "LAST_UPDATED": "22/10/2026"}
    ]

if "guarantee_claims" not in st.session_state:
    st.session_state.guarantee_claims = [
        {"CUSTOMER": "Savad", "ITEM": "Apollo 100/90-10", "ISSUE": "Side bubble", "STATUS": "Pending"}
    ]

if "dealers_directory" not in st.session_state:
    st.session_state.dealers_directory = [
        {"DEALER": "JK Tyre Agency", "LOCATION": "Madikeri", "PHONE": "9440012345"}
    ]

if "retreading_data" not in st.session_state:
    st.session_state.retreading_data = [
        {"CUSTOMER": "Kuttappan", "TYRE_SIZE": "1000R20", "QTY": 2, "STATUS": "Sent to factory"}
    ]

# ---------------------------------------------------------
# CUSTOM CSS STYLING
# ---------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        background-color: #0e1117;
        padding: 12px 20px;
        border-radius: 8px;
        color: white;
        margin-bottom: 15px;
        border: 1px solid #262730;
    }
    .shop-title {
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 1px;
    }
    .shop-sub {
        font-size: 12px;
        color: #888;
    }
    .card-box {
        background-color: #1e222b;
        color: #ffffff !important;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #3a3f4b;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Top Banner
st.markdown("""
<div class="main-header">
    <div class="shop-title">🛞 COORG TYRE SHOP</div>
    <div class="shop-sub">Abyayath Mangala, Ontiyangadi, Main Road, Siddapura - 571253</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVIGATION TABS
# ---------------------------------------------------------
tabs = st.tabs([
    "📈 Overview", 
    "🛞 Tyre Stock", 
    "🔘 Tube Stock",
    "🛠️ Puncture Items",
    "📋 Reorder / Low Stock",
    "📈 Market Rates",
    "🎬 Status Studio", 
    "🐷 Pigmi Collection", 
    "🧾 Billing", 
    "💳 Payments", 
    "📒 Credit (കടം)",
    "💸 Expenses",
    "🔄 Retreading",
    "🛡️ Guarantee / Claims",
    "📖 Dealers Directory"
])

# 1. OVERVIEW
with tabs[0]:
    st.subheader("OVERVIEW • TODAY's SUMMARY")
    
    today_str = str(date.today())
    today_sales_list = [s for s in st.session_state.sales_data if s['DATE'] == today_str]
    
    tot_sales = sum(s['AMOUNT'] for s in today_sales_list)
    cash_today = sum(s['AMOUNT'] for s in today_sales_list if s['MODE'] == 'Cash')
    upi_today = sum(s['AMOUNT'] for s in today_sales_list if s['MODE'] == 'UPI')
    credit_given_today = sum(c['AMOUNT'] for c in st.session_state.credit_data)
    
    tot_pigmi_col = sum(p['COLLECTED'] for p in st.session_state.pigmi_data)
    tot_pigmi_wit = sum(p['WITHDRAWN'] for p in st.session_state.pigmi_data)
    tot_expenses = sum(e['AMOUNT'] for e in st.session_state.expenses_data)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("TODAY'S SALES", f"₹ {tot_sales:,.2f}")
    c2.metric("CASH", f"₹ {cash_today:,.2f}")
    c3.metric("PAYTM / UPI", f"₹ {upi_today:,.2f}")
    c4.metric("CREDIT GIVEN", f"₹ {credit_given_today:,.2f}")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("PIGMI COLLECTED", f"₹ {tot_pigmi_col:,.2f}")
    c6.metric("PIGMI WITHDRAWN", f"₹ {tot_pigmi_wit:,.2f}")
    c7.metric("PAID TO AGENTS", "₹ 0.00")
    c8.metric("TOTAL EXPENSES", f"₹ {tot_expenses:,.2f}")

    st.markdown("---")
    st.subheader("➕ ADD TODAY'S WORK / SALE")
    
    # Selection for item type
    item_type = st.selectbox(
        "Select Item / Service Type",
        ["Tubeless Puncture", "Tube Puncture", "Inside Puncture", "Neck / Valve Change", "Tyre Setting", "Tyre Sale", "Tube Sale", "Fitting Charge", "Wheel Balancing", "Flap Change"]
    )
    
    # Conditional logic for Tyre Sale & Tube Sale sizes
    selected_size = "N/A"
    default_rate = 100

    if item_type == "Tyre Sale":
        tyre_options = [f"{t['BRAND']} {t['SIZE']} ({t.get('VEHICLE', '')}) - Stock: {t['STOCK']} (₹{t['SELLING RATE']})" for t in st.session_state.tyre_stock]
        if tyre_options:
            selected_tyre_str = st.selectbox("Select Tyre Size / Stock", tyre_options)
            for t in st.session_state.tyre_stock:
                if f"{t['BRAND']} {t['SIZE']}" in selected_tyre_str:
                    selected_size = f"{t['BRAND']} {t['SIZE']}"
                    default_rate = int(t['SELLING RATE'])
        else:
            st.warning("No Tyre stock available!")

    elif item_type == "Tube Sale":
        tube_options = [f"{tu['BRAND']} {tu['SIZE']} ({tu.get('VEHICLE', '')}) - Stock: {tu['STOCK']} (₹{tu['SELLING RATE']})" for tu in st.session_state.tube_stock]
        if tube_options:
            selected_tube_str = st.selectbox("Select Tube Size / Stock", tube_options)
            for tu in st.session_state.tube_stock:
                if f"{tu['BRAND']} {tu['SIZE']}" in selected_tube_str:
                    selected_size = f"{tu['BRAND']} {tu['SIZE']}"
                    default_rate = int(tu['SELLING RATE'])
        else:
            st.warning("No Tube stock available!")

    with st.form("quick_sale_form"):
        col_w1, col_w2, col_w3 = st.columns(3)
        qty = col_w1.number_input("Qty", min_value=1, value=1)
        amount = col_w2.number_input("Amount (₹)", min_value=0, value=default_rate)
        mode = col_w3.selectbox("Payment Mode", ["Cash", "UPI", "Credit"])
        
        if st.form_submit_button("Save Sale 💾"):
            st.session_state.sales_data.append({
                "ITEM": item_type, "SIZE": selected_size, "QTY": qty, "AMOUNT": amount, "MODE": mode, "DATE": str(date.today())
            })
            if mode == "Credit":
                st.session_state.credit_data.append({
                    "CUSTOMER": "Counter Customer", "PHONE": "N/A", "DETAILS": f"{item_type} ({selected_size})", "AMOUNT": amount, "STATUS": "Pending"
                })
            st.success("✅ Sale recorded successfully!")
            st.rerun()

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")
    with st.expander("➕ Add New Tyre Stock"):
        with st.form("add_tyre_form"):
            col1, col2, col3, col4 = st.columns(4)
            brand = col1.selectbox("Company / Brand", ["APOLLO", "MRF", "CEAT", "TVS", "JK TYRE", "OTHER"])
            vehicle = col2.selectbox("Vehicle Type", ["Scooter", "Bike", "Auto", "Car", "Jeep", "Truck / Bus", "Tractor", "Other"])
            size = col3.text_input("Size (e.g. 90/100/10)")
            condition = col4.selectbox("Condition", ["New", "Used", "Retread"])
            
            col5, col6, col7, col8 = st.columns(4)
            pattern = col5.text_input("Pattern (e.g. 53J GRIP)")
            p_rate = col6.number_input("Purchase Rate (₹)", min_value=0)
            s_rate = col7.number_input("Selling Rate (₹)", min_value=0.0)
            qty = col8.number_input("Stock Qty", min_value=0, value=1)
            
            if st.form_submit_button("Save Tyre 📦"):
                st.session_state.tyre_stock.append({
                    "BRAND": brand, "VEHICLE": vehicle, "SIZE": size, 
                    "CONDITION": condition, "PATTERN": pattern, "STOCK": qty, 
                    "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
                })
                st.success("✅ Tyre added!")
                st.rerun()

    for idx, t in enumerate(st.session_state.tyre_stock):
        v_type = t.get('VEHICLE', 'General')
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="card-box" style="padding:10px; margin-bottom:5px;">
                <b style="color:#ffffff;">{t['BRAND']}</b> <span style="color:#cccccc;">({v_type})</span> - <span style="color:#ffffff;">{t['SIZE']}</span> | Cond: <span style="color:#cccccc;">{t.get('CONDITION', 'New')}</span> | Stock: <b style="color:#4CAF50;">{t['STOCK']}</b> | Sell: <b style="color:#ff9800;">₹{t['SELLING RATE']}</b>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_t_{idx}"):
                st.session_state.tyre_stock.pop(idx)
                st.rerun()

# 3. TUBE STOCK
with tabs[2]:
    st.subheader(f"TUBE STOCK ({len(st.session_state.tube_stock)})")
    with st.expander("➕ Add Tube Stock"):
        with st.form("add_tube"):
            c1, c2, c3, c4 = st.columns(4)
            brand = c1.selectbox("Company / Brand", ["BRAZA", "TVS", "MRF", "APOLLO", "JK TYRE", "OTHER"])
            vehicle = c2.selectbox("Vehicle Type", ["Scooter", "Bike", "Auto", "Car", "Jeep", "Truck / Bus", "Other"])
            size = c3.text_input("Size (e.g. 3.00-10)")
            cond = c4.selectbox("Condition", ["New", "Used"])
            
            c5, c6, c7 = st.columns(3)
            qty = c5.number_input("Qty", min_value=1, value=1)
            p_rate = c6.number_input("Purchase Rate (₹)", min_value=0, value=150)
            s_rate = c7.number_input("Selling Rate (₹)", min_value=0, value=220)
            
            if st.form_submit_button("Save Tube 💾"):
                st.session_state.tube_stock.append({
                    "BRAND": brand, "VEHICLE": vehicle, "SIZE": size, 
                    "CONDITION": cond, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
                })
                st.success("Tube added!")
                st.rerun()

    for idx, tu in enumerate(st.session_state.tube_stock):
        tu_veh = tu.get('VEHICLE', 'General')
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="card-box" style="padding:10px; margin-bottom:5px;">
                <b style="color:#ffffff;">{tu['BRAND']}</b> <span style="color:#cccccc;">({tu_veh})</span> - <span style="color:#ffffff;">{tu['SIZE']}</span> | Stock: <b style="color:#4CAF50;">{tu['STOCK']}</b> | Sell: <b style="color:#ff9800;">₹{tu['SELLING RATE']}</b>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_tu_{idx}"):
                st.session_state.tube_stock.pop(idx
