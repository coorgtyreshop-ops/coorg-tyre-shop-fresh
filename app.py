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
    st.session_state.tyre_stock = []

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = []

if "puncture_items" not in st.session_state:
    st.session_state.puncture_items = [
        {"SERVICE": "Tubeless Puncture", "RATE": 100},
        {"SERVICE": "Tube Puncture", "RATE": 80}
    ]

if "pigmi_data" not in st.session_state:
    st.session_state.pigmi_data = []

if "sales_data" not in st.session_state:
    st.session_state.sales_data = []

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = []

if "credit_data" not in st.session_state:
    st.session_state.credit_data = []

if "market_rates" not in st.session_state:
    st.session_state.market_rates = [
        {"BRAND": "APOLLO", "SIZE": "90/100/10", "ONLINE_PRICE": 1450, "LAST_UPDATED": "24/10/2026"}
    ]

if "guarantee_claims" not in st.session_state:
    st.session_state.guarantee_claims = []

if "dealers_directory" not in st.session_state:
    st.session_state.dealers_directory = []

if "retreading_data" not in st.session_state:
    st.session_state.retreading_data = []

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
            st.success("✅ Sale recorded successfully!")
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
            st.success("✅ Tyre added successfully!")
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
            st.success("✅ Tube added successfully!")
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
        df_m = df_m[df_m['BRAND'].str.contains(search_m, case=False, na=False) | df_m['SIZE'].str.contains(search_m, case=False, na=False)]
    st.dataframe(df_m, use_container_width=True)

# 7. STATUS STUDIO
with tabs[6]:
    st.subheader("🎬 STATUS STUDIO")
    st.write("Create branded WhatsApp-status posters & videos.")

# 8. PIGMI COLLECTION
with tabs[7]:
    tot_pigmi = sum(p['BALANCE'] for p in st.session_state.pigmi_data)
    st.subheader(f"🐷 PIGMI COLLECTION • Total Balance: ₹{tot_pigmi:,.2f}")
    
    st.markdown("### ➕ Add New Pigmi Account / Person")
    with st.form("add_p_form"):
        c1, c2, c3 = st.columns(3)
        name = c1.text_input("Name (പേര്)")
        loc = c2.text_input("Location (സ്ഥലം)")
        phone = c3.text_input("Phone (ഫോൺ നമ്പർ)")
        
        c4, c5, c6 = st.columns(3)
        bank = c4.text_input("Bank / Society Name (ബാങ്ക് പേര്)")
        ac = c5.text_input("A/C Number (അക്കൗണ്ട് നമ്പർ)")
        target = c6.number_input("Daily Target Amount (₹)", min_value=10, value=500)
        
        if st.form_submit_button("Save Pigmi Account 💾"):
            st.session_state.pigmi_data.append({
                "NAME": name.upper(), "LOCATION": loc, "PHONE": phone, 
                "BANK": bank.upper(), "AC_NO": ac, "DAILY_TARGET": target, 
                "COLLECTED": 0, "WITHDRAWN": 0, "BALANCE": 0,
                "LAST_DATE": str(date.today()),
                "HISTORY": []
            })
            st.success("✅ Pigmi Account Added Successfully!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 📋 ACTIVE PIGMI ACCOUNTS")
    if not st.session_state.pigmi_data:
        st.info("No Pigmi accounts added yet.")
    else:
        for idx, p in enumerate(st.session_state.pigmi_data):
            col_main, col_del = st.columns([5, 1])
            with col_main:
                st.markdown(f"""
                <div class="card-box">
                    <h3 style="margin:0; color:#4CAF50;">{p['NAME']}</h3>
                    <p style="color:#ccc; font-size:13px; margin:2px 0;">{p['LOCATION']} • {p['PHONE']}</p>
                    <p style="color:#ff9800; font-size:13px; margin-bottom:5px;">🏛️ <b>{p['BANK']}</b> | A/C No: <b>{p['AC_NO']}</b></p>
                    <p style="font-size:13px; color:#aaa; margin-bottom:10px;">📅 Last Collection Date: <b>{p.get('LAST_DATE', 'N/A')}</b></p>
                    <p style="font-size:14px; color:#fff;">
                        Total Collected: <b style="color:#4CAF50;">₹{p['COLLECTED']:,.2f}</b> | Balance: <b style="color:#4CAF50;">₹{p['BALANCE']:,.2f}</b>
                    </p>
                </div>
                """, unsafe_allow_html=True)
            with col_del:
                if st.button("🗑️ Delete Account", key=f"del_ac_{idx}"):
                    st.session_state.pigmi_data.pop(idx)
                    st.success("Account Deleted!")
                    st.rerun()
            
            if p.get("HISTORY"):
                with st.expander(f"📜 View/Edit Collection History for {p['NAME']}"):
                    for h_idx, h in enumerate(p["HISTORY"]):
                        h_col1, h_col2 = st.columns([4, 1])
                        with h_col1:
                            st.markdown(f"- 📅 Date: **{h['DATE']}** | Collected Amount: <b style='color:#4CAF50;'>₹{h['AMOUNT']:,.2f}</b>", unsafe_allow_html=True)
                        with h_col2:
                            if st.button("🗑️ Clear Entry", key=f"del_h_{idx}_{h_idx}"):
                                st.session_state.pigmi_data[idx]['COLLECTED'] -= h['AMOUNT']
                                st.session_state.pigmi_data[idx]['BALANCE'] -= h['AMOUNT']
                                st.session_state.pigmi_data[idx]['HISTORY'].pop(h_idx)
                                st.success("Entry removed!")
                                st.rerun()
            
            with st.form(key=f"collect_form_{idx}"):
                col_b1, col_b2, col_b3 = st.columns([2, 2, 1])
                with col_b1:
                    collect_date = st.date_input("Collection Date 📅", value=date.today(), key=f"date_{idx}")
                with col_b2:
                    daily_amt = st.number_input(
                        "Amount to Add (₹)", 
                        min_value=1, 
                        value=int(p.get('DAILY_TARGET', 500)), 
                        key=f"daily_amt_{idx}"
                    )
                with col_b3:
                    st.write("")
                    st.write("")
                    submit_collect = st.form_submit_button("📥 Collect & Save")
                
                if submit_collect:
                    st.session_state.pigmi_data[idx]['COLLECTED'] += daily_amt
                    st.session_state.pigmi_data[idx]['BALANCE'] += daily_amt
                    st.session_state.pigmi_data[idx]['LAST_DATE'] = str(collect_date)
                    
                    if "HISTORY" not in st.session_state.pigmi_data[idx]:
                        st.session_state.pigmi_data[idx]["HISTORY"] = []
                    st.session_state.pigmi_data[idx]["HISTORY"].insert(0, {"DATE": str(collect_date), "AMOUNT": daily_amt})
                    
                    st.success(f"✅ Added ₹{daily_amt} on {collect_date}!")
                    st.rerun()

# 9. BILLING
with tabs[8]:
    st.subheader("🧾 BILLING & INVOICING")
    st.info("Billing feature active.")

# 10. PAYMENTS
with tabs[9]:
    st.subheader("💳 PAYMENTS")
    st.info("Payments feature active.")

# 11. CREDIT (കടം)
with tabs[10]:
    st.subheader("📒 CREDIT (കടം) MANAGEMENT")
    st.markdown("### ➕ Add New Credit Record")
    with st.form("add_credit_form"):
        col_c1, col_c2, col_c3 = st.columns(3)
        cust_name = col_c1.text_input("Customer Name")
        cust_phone = col_c2.text_input("Phone Number")
        credit_amt = col_c3.number_input("Credit Amount (₹)", min_value=1, value=500)
        credit_details = st.text_input("Details / Items Bought")
        if st.form_submit_button("Save Credit Record 💾"):
            st.session_state.credit_data.append({
                "CUSTOMER": cust_name, "PHONE": cust_phone, "DETAILS": credit_details, "AMOUNT": credit_amt, "STATUS": "Pending"
            })
            st.success("Credit added!")
            st.rerun()

# 12. EXPENSES
with tabs[11]:
    tot_exp = sum(e['AMOUNT'] for e in st.session_state.expenses_data)
    st.subheader(f"💸 EXPENSES MANAGEMENT • Total Spent: ₹{tot_exp:,.2f}")
    
    st.markdown("### ➕ Add New Expense")
    with st.form("add_exp_form"):
        c1, c2 = st.columns(2)
        cat_select = c1.selectbox(
            "Expense Category", 
            ["Room Rent (റൂം വാടക)", "Electricity Bill (കറന്റ് ബില്ല്)", "Food / Tea (ഫുഡ് / ചായ)", "Salary (ശമ്പളം)", "Transport / Freight (വണ്ടി വാടക)", "Machine Repair (മെഷീൻ റിപ്പയർ)", "Other (മറ്റുള്ളവ)"]
        )
        custom_cat = ""
        if "Other" in cat_select:
            custom_cat = c1.text_input("Enter Custom Category Name")
        
        recipient = c2.text_input("Paid To / Recipient", placeholder="e.g. Owner name, Hotel, KSEB")
        
        c3, c4, c5 = st.columns(3)
        amt = c3.number_input("Amount (തുക ₹)", min_value=1, step=50, value=100)
        urgency = c4.radio("Urgency", ["Normal", "Urgent ⚠️"], horizontal=True)
        exp_date = c5.date_input("Date", value=date.today())
        
        if st.form_submit_button("Save Expense 💾"):
            final_cat = custom_cat if ("Other" in cat_select and custom_cat) else cat_select.split(" (")[0]
            st.session_state.expenses_data.append({
                "CATEGORY": final_cat, 
                "RECIPIENT": recipient if recipient else "N/A", 
                "AMOUNT": amt, 
                "URGENCY": urgency,
                "DATE": str(exp_date)
            })
            st.success("✅ Expense Saved!")
            st.rerun()

# 13. RETREADING (FIXED DUPLICATION & CLEAN SINGLE ENTRY)
with tabs[12]:
    st.subheader("🔄 RETREADING / REBELTING MANAGEMENT")
    
    st.markdown("### ➕ Add Retreading Record")
    with st.form("add_retread_form"):
        col_r1, col_r2, col_r3 = st.columns(3)
        r_cust = col_r1.text_input("Customer Name (പേര്)")
        r_phone = col_r2.text_input("Phone Number (ഫോൺ നമ്പർ)")
        r_size = col_r3.text_input("Tyre Size (ടയർ സൈസ്)")
        
        col_r4, col_r5 = st.columns(2)
        r_qty = col_r4.number_input("Quantity / Total Tyres (ടയറുകളുടെ എണ്ണം)", min_value=1, value=1)
        r_status = col_r5.selectbox("Status (നിലവിലെ അവസ്ഥ)", ["Pending", "Sent to Factory", "Ready", "Delivered"])
        
        r_serials_input = st.text_input("Tyre Serial Numbers / SL Nos (ഒന്നിലധികം ഉണ്ടെങ്കിൽ കോമ ഇട്ട് എഴുതുക e.g. 46034733422, 46082853322)")
        
        col_r6, col_r7 = st.columns(2)
        r_tot_amt = col_r6.number_input("Total Amount (ആകെ തുക ₹)", min_value=0, value=2000)
        r_adv_amt = col_r7.number_input("Advance Paid (അഡ്വാൻസ് ₹)", min_value=0, value=500)
        
        if st.form_submit_button("Save Retreading Record 💾"):
            balance_amt = max(0, r_tot_amt - r_adv_amt)
            st.session_state.retreading_data.append({
                "CUSTOMER": r_cust,
                "PHONE": r_phone,
                "TYRE_SIZE": r_size,
                "TYRE_SERIALS": r_serials_input,
                "QTY": r_qty,
                "TOTAL": r_tot_amt,
                "ADVANCE": r_adv_amt,
                "BALANCE": balance_amt,
                "STATUS": r_status,
                "DATE": str(date.today())
            })
            st.success("✅ Retreading record saved successfully!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 📋 Retreading Records List")
    if not st.session_state.retreading_data:
        st.info("No retreading records added yet.")
    else:
        for idx, r in enumerate(st.session_state.retreading_data):
            bal = r.get('BALANCE', max(0, r.get('TOTAL', 0) - r.get('ADVANCE', 0)))
            stat = r.get('STATUS', 'Pending')
            
            status_color = "#ff9800"
            if stat == "Ready":
                status_color = "#2196F3"
            elif stat == "Delivered":
                status_color = "#4CAF50"
            elif stat == "Sent to Factory":
                status_color = "#9c27b0"

            col_rc1, col_rc2 = st.columns([5, 1])
            with col_rc1:
                st.markdown(f"""
                <div class="card-box">
                    <h3 style="margin:0; color:#4CAF50;">{r['CUSTOMER']} ({r.get('PHONE', 'N/A')})</h3>
                    <p style="color:#ccc; font-size:13px; margin:2px 0;">Tyre Size: <b>{r['TYRE_SIZE']}</b> | Qty: <b>{r['QTY']}</b></p>
                    <p style="color:#00bcd4; font-size:13px; margin:2px 0;">SL Nos: <b>{r.get('TYRE_SERIALS', 'N/A')}</b></p>
                    <p style="color:#ff9800; font-size:13px; margin:2px 0;">Total: ₹<b>{r.get('TOTAL', 0):,.2f}</b> | Advance: ₹<b>{r.get('ADVANCE', 0):,.2f}</b> | Balance Due: <b style="color:#f44336;">₹{bal:,.2f}</b></p>
                    <p style="font-size:13px; margin-top:5px;">Status: <span style="background-color:{status_color}; color:#fff; padding:2px 8px; border-radius:4px; font-weight:bold;">{stat}</span> | Date: {r.get('DATE', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)
            with col_rc2:
                st.write("")
                if st.button("🗑️ Delete", key=f"del_ret_{idx}"):
                    st.session_state.retreading_data.pop(idx)
                    st.success("Record deleted!")
                    st.rerun()

# 14. GUARANTEE / CLAIMS
with tabs[13]:
    st.subheader("🛡️ GUARANTEE & WARRANTY CLAIMS")
    st.markdown("### ➕ Add Claim Record")
    with st.form("add_claim_form"):
        col_g1, col_g2 = st.columns(2)
        g_cust = col_g1.text_input("Customer Name")
        g_item = col_g2.text_input("Item Name / Size")
        g_issue = st.text_input("Issue / Defect Description")
        if st.form_submit_button("Save Claim Record 💾"):
            st.session_state.guarantee_claims.append({
                "CUSTOMER": g_cust, "ITEM": g_issue, "ISSUE": g_issue, "STATUS": "Pending"
            })
            st.success("Claim added!")
            st.rerun()

# 15. DEALERS DIRECTORY
with tabs[14]:
    st.subheader("📖 DEALERS DIRECTORY")
    st.markdown("### ➕ Add Dealer Info")
    with st.form("add_dealer_form"):
        col_d1, col_d2, col_d3 = st.columns(3)
        d_name = col_d1.text_input("Dealer Name")
        d_loc = col_d2.text_input("Location")
        d_phone = col_d3.text_input("Phone Number")
        if st.form_submit_button("Save Dealer 💾"):
            st.session_state.dealers_directory.append({
                "DEALER": d_name, "LOCATION": d_loc, "PHONE": d_phone
            })
            st.success("Dealer added!")
            st.rerun()
