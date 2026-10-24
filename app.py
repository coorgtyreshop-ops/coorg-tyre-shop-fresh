import streamlit as st
import pandas as pd
from datetime import date
import os

# Page Configuration with Dark Theme
st.set_page_config(
    page_title="COORG TYRE SHOP",
    page_icon="🛞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

DATA_FILE = "coorg_tyre_data.pkl"

# ---------------------------------------------------------
# PERSISTENT LOCAL STORAGE LOGIC
# ---------------------------------------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            return pd.read_pickle(DATA_FILE)
        except Exception:
            pass
    return {
        "tyre_stock": [],
        "tube_stock": [],
        "puncture_items": [
            {"SERVICE": "Tubeless Puncture", "RATE": 100},
            {"SERVICE": "Tube Puncture", "RATE": 80}
        ],
        "pigmi_data": [],
        "sales_data": [],
        "expenses_data": [],
        "credit_data": [],
        "market_rates": [
            {"BRAND": "APOLLO", "SIZE": "90/100/10", "ONLINE_PRICE": 1450, "LAST_UPDATED": "24/10/2026"}
        ],
        "guarantee_claims": [],
        "dealers_directory": [],
        "retreading_data": []
    }

def save_data():
    store = {
        "tyre_stock": st.session_state.tyre_stock,
        "tube_stock": st.session_state.tube_stock,
        "puncture_items": st.session_state.puncture_items,
        "pigmi_data": st.session_state.pigmi_data,
        "sales_data": st.session_state.sales_data,
        "expenses_data": st.session_state.expenses_data,
        "credit_data": st.session_state.credit_data,
        "market_rates": st.session_state.market_rates,
        "guarantee_claims": st.session_state.guarantee_claims,
        "dealers_directory": st.session_state.dealers_directory,
        "retreading_data": st.session_state.retreading_data
    }
    pd.to_pickle(store, DATA_FILE)

# Initialize session state from file
saved_store = load_data()
for key, val in saved_store.items():
    if key not in st.session_state:
        st.session_state[key] = val

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
    today_sales_list = [s for s in st.session_state.sales_data if s.get('DATE') == today_str]
    
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
    
    item_type = st.selectbox(
        "Select Item / Service Type",
        ["Tubeless Puncture", "Tube Puncture", "Inside Puncture", "Neck / Valve Change", "Tyre Setting", "Tyre Sale", "Tube Sale", "Fitting Charge", "Wheel Balancing", "Flap Change"]
    )
    
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
            save_data()
            st.success("✅ Sale recorded and saved permanently!")
            st.rerun()

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"🛞 TYRE STOCK MANAGEMENT ({len(st.session_state.tyre_stock)})")
    
    st.markdown("### ➕ Add New Tyre Stock")
    with st.form("add_tyre_form"):
        col1, col2, col3, col4 = st.columns(4)
        brand = col1.selectbox("Company / Brand", ["APOLLO", "MRF", "CEAT", "TVS", "JK TYRE", "OTHER"])
        vehicle = col2.selectbox("Vehicle Type", ["Scooter", "Bike", "Auto", "Car", "Jeep", "Truck / Bus", "Tractor", "Other"])
        size = col3.text_input("Size (e.g. 90/100/10)")
        condition = col4.selectbox("Condition", ["New", "Used", "Retread"])
        
        col5, col6, col7, col8 = st.columns(4)
        pattern = col5.text_input("Pattern (e.g. 53J GRIP)")
        p_rate = col6.number_input("Purchase Rate (₹)", min_value=0, value=1000)
        s_rate = col7.number_input("Selling Rate (₹)", min_value=0.0, value=1500.0)
        qty = col8.number_input("Stock Qty", min_value=0, value=1)
        
        if st.form_submit_button("Save Tyre Stock 📦"):
            st.session_state.tyre_stock.append({
                "BRAND": brand, "VEHICLE": vehicle, "SIZE": size, 
                "CONDITION": condition, "PATTERN": pattern, "STOCK": qty, 
                "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
            })
            save_data()
            st.success("✅ Tyre added & saved permanently!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 📋 Existing Tyre Stock List")
    if not st.session_state.tyre_stock:
        st.info("No tyre stock added yet.")
    else:
        for idx, t in enumerate(st.session_state.tyre_stock):
            v_type = t.get('VEHICLE', 'General')
            col_t1, col_t2 = st.columns([5, 1])
            with col_t1:
                st.markdown(f"""
                <div class="card-box" style="padding:10px; margin-bottom:5px;">
                    <b style="color:#ffffff;">{t['BRAND']}</b> <span style="color:#cccccc;">({v_type})</span> - <span style="color:#ffffff;">{t['SIZE']}</span> | Cond: <span style="color:#cccccc;">{t.get('CONDITION', 'New')}</span> | Stock: <b style="color:#4CAF50;">{t['STOCK']}</b> | Sell: <b style="color:#ff9800;">₹{t['SELLING RATE']}</b>
                </div>
                """, unsafe_allow_html=True)
            with col_t2:
                if st.button("🗑️ Delete", key=f"del_t_{idx}"):
                    st.session_state.tyre_stock.pop(idx)
                    save_data()
                    st.rerun()

# 3. TUBE STOCK
with tabs[2]:
    st.subheader(f"🔘 TUBE STOCK MANAGEMENT ({len(st.session_state.tube_stock)})")
    
    st.markdown("### ➕ Add New Tube Stock")
    with st.form("add_tube_form"):
        c1, c2, c3, c4 = st.columns(4)
        brand = c1.selectbox("Company / Brand", ["BRAZA", "TVS", "MRF", "APOLLO", "JK TYRE", "OTHER"])
        vehicle = c2.selectbox("Vehicle Type", ["Scooter", "Bike", "Auto", "Car", "Jeep", "Truck / Bus", "Other"])
        size = c3.text_input("Size (e.g. 3.00-10)")
        cond = c4.selectbox("Condition", ["New", "Used"])
        
        c5, c6, c7 = st.columns(3)
        qty = c5.number_input("Qty", min_value=1, value=1)
        p_rate = c6.number_input("Purchase Rate (₹)", min_value=0, value=150)
        s_rate = c7.number_input("Selling Rate (₹)", min_value=0, value=220)
        
        if st.form_submit_button("Save Tube Stock 💾"):
            st.session_state.tube_stock.append({
                "BRAND": brand, "VEHICLE": vehicle, "SIZE": size, 
                "CONDITION": cond, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
            })
            save_data()
            st.success("✅ Tube added and saved permanently!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 📋 Existing Tube Stock List")
    if not st.session_state.tube_stock:
        st.info("No tube stock added yet.")
    else:
        for idx, tu in enumerate(st.session_state.tube_stock):
            tu_veh = tu.get('VEHICLE', 'General')
            col_tu1, col_tu2 = st.columns([5, 1])
            with col_tu1:
                st.markdown(f"""
                <div class="card-box" style="padding:10px; margin-bottom:5px;">
                    <b style="color:#ffffff;">{tu['BRAND']}</b> <span style="color:#cccccc;">({tu_veh})</span> - <span style="color:#ffffff;">{tu['SIZE']}</span> | Stock: <b style="color:#4CAF50;">{tu['STOCK']}</b> | Sell: <b style="color:#ff9800;">₹{tu['SELLING RATE']}</b>
                </div>
                """, unsafe_allow_html=True)
            with col_tu2:
                if st.button("🗑️ Delete", key=f"del_tu_{idx}"):
                    st.session_state.tube_stock.pop(idx)
                    save_data()
                    st.rerun()

# 4. PUNCTURE ITEMS
with tabs[3]:
    st.subheader("🛠️ PUNCTURE & SERVICE ITEMS")
    st.markdown("### ➕ Add New Service Item")
    with st.form("add_punc_form"):
        service_name = st.text_input("Service Name (e.g. Tubeless Puncture)")
        service_rate = st.number_input("Standard Rate (₹)", min_value=0, value=100)
        if st.form_submit_button("Save Service Item"):
            st.session_state.puncture_items.append({"SERVICE": service_name, "RATE": service_rate})
            save_data()
            st.success("Service item added!")
            st.rerun()

    st.markdown("---")
    for idx, pi in enumerate(st.session_state.puncture_items):
        col_pi1, col_pi2 = st.columns([5, 1])
        with col_pi1:
            st.markdown(f"""<div class="card-box" style="padding:10px; margin-bottom:5px;"><b style="color:#ffffff;">{pi['SERVICE']}</b> — Rate: <b style="color:#4CAF50;">₹{pi['RATE']}</b></div>""", unsafe_allow_html=True)
        with col_pi2:
            if st.button("🗑️ Delete", key=f"del_pi_{idx}"):
                st.session_state.puncture_items.pop(idx)
                save_data()
                st.rerun()

# 5. REORDER / LOW STOCK
with tabs[4]:
    st.subheader("📋 REORDER / LOW STOCK")
    low_limit = st.slider("Low stock limit <=", 1, 5, 3)
    out_of_stock = [item for item in st.session_state.tyre_stock if item['STOCK'] <= low_limit]
    if out_of_stock:
        for item in out_of_stock:
            v_t = item.get('VEHICLE', '')
            st.markdown(f"""<div class="card-box" style="border-left: 4px solid #f44336;"><b style="color:#ffffff;">{item['BRAND']} ({v_t}) {item['SIZE']}</b> — Stock Qty: <span style="color:#f44336; font-weight:bold;">{item['STOCK']}</span></div>""", unsafe_allow_html=True)
    else:
        st.success("All items have sufficient stock!")

# 6. MARKET RATES
with tabs[5]:
    st.subheader("📈 MARKET RATES & ONLINE PRICES")
    search_m = st.text_input("🔍 Search brand or size in market rates...")
    df_m = pd.DataFrame(st.session_state.market_rates)
    if not df_m.empty and search_m:
        df_m = df_m[df_m['BRAND'].str.contains(search_m, case=False, na=False) | df_m['SIZE'].str.contains(search_m, case=False,
