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
        {"BRAND": "APOLLO", "VEHICLE": "Scooter", "SIZE": "90/100/10", "CONDITION": "New", "PATTERN": "53J GRIP", "STOCK": 1, "PURCHASE RATE": 1020, "SELLING RATE": 1450}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = [
        {"BRAND": "BRAZA", "VEHICLE": "Scooter", "SIZE": "3.00-10", "CONDITION": "New", "STOCK": 5, "PURCHASE RATE": 180, "SELLING RATE": 250}
    ]

if "puncture_items" not in st.session_state:
    st.session_state.puncture_items = [
        {"SERVICE": "Tubeless Puncture", "RATE": 100},
        {"SERVICE": "Tube Puncture", "RATE": 80}
    ]

if "pigmi_data" not in st.session_state:
    st.session_state.pigmi_data = [
        {"NAME": "SHAHAJAHAN E", "LOCATION": "ONTIYANGADI", "PHONE": "9900316275", "BANK": "Janaasha South Nidhi Ltd", "AC_NO": "035601167", "DAILY_TARGET": 500, "OLD_BAL": 1000, "COLLECTED": 6000, "WITHDRAWN": 0, "BALANCE": 7000, "LAST_DATE": str(date.today())},
        {"NAME": "SHAHAJAHAN", "LOCATION": "ONTIYANGADI", "PHONE": "9900316275", "BANK": "Nelliyanipuri Society Bank", "AC_NO": "11298", "DAILY_TARGET": 100, "OLD_BAL": 0, "COLLECTED": 5500, "WITHDRAWN": 0, "BALANCE": 5500, "LAST_DATE": str(date.today())}
    ]

if "billing_data" not in st.session_state:
    st.session_state.billing_data = [
        {"BILL_NO": "CTS-1176", "TYPE": "Counter Sale", "SERVICE": "Tubeless Puncture", "AMOUNT": 100, "MODE": "Cash"}
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
        background-color: #161920;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #262730;
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
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("TODAY'S SALES", f"₹ {sum(b['AMOUNT'] for b in st.session_state.billing_data)}")
    c2.metric("CASH", "₹ 0")
    c3.metric("PAYTM / UPI", "₹ 0")
    c4.metric("CREDIT GIVEN", f"₹ {sum(c['AMOUNT'] for c in st.session_state.credit_data)}")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("PIGMI COLLECTED", f"₹ {sum(p['COLLECTED'] for p in st.session_state.pigmi_data):,.2f}")
    c6.metric("PIGMI WITHDRAWN", f"₹ {sum(p['WITHDRAWN'] for p in st.session_state.pigmi_data):,.2f}")
    c7.metric("PAID TO AGENTS", "₹ 0")
    c8.metric("TOTAL EXPENSES", f"₹ {sum(e['AMOUNT'] for e in st.session_state.expenses_data):,.2f}")

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
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="card-box" style="padding:10px; margin-bottom:5px;">
                <b>{t['BRAND']}</b> ({t['VEHICLE']}) - {t['SIZE']} | Cond: {t['CONDITION']} | Stock: <b style="color:#4CAF50;">{t['STOCK']}</b> | Sell: ₹{t['SELLING RATE']}
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
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="card-box" style="padding:10px; margin-bottom:5px;">
                <b>{tu['BRAND']}</b> ({tu['VEHICLE']}) - {tu['SIZE']} | Stock: <b style="color:#4CAF50;">{tu['STOCK']}</b> | Sell: ₹{tu['SELLING RATE']}
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_tu_{idx}"):
                st.session_state.tube_stock.pop(idx)
                st.rerun()

# 4. PUNCTURE ITEMS
with tabs[3]:
    st.subheader("🛠️ PUNCTURE & SERVICE ITEMS")
    with st.expander("➕ Add New Service Item"):
        with st.form("add_punc"):
            service_name = st.text_input("Service Name")
            service_rate = st.number_input("Standard Rate (₹)", min_value=0, value=100)
            if st.form_submit_button("Save Service"):
                st.session_state.puncture_items.append({"SERVICE": service_name, "RATE": service_rate})
                st.success("Service added!")
                st.rerun()

    for idx, pi in enumerate(st.session_state.puncture_items):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box" style="padding:10px; margin-bottom:5px;"><b>{pi['SERVICE']}</b> — Rate: <b style="color:#4CAF50;">₹{pi['RATE']}</b></div>""", unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_pi_{idx}"):
                st.session_state.puncture_items.pop(idx)
                st.rerun()

# 5. REORDER / LOW STOCK
with tabs[4]:
    st.subheader("REORDER / LOW STOCK")
    low_limit = st.slider("Low stock limit <=", 1, 5, 3)
    out_of_stock = [item for item in st.session_state.tyre_stock if item['STOCK'] <= low_limit]
    if out_of_stock:
        for item in out_of_stock:
            st.markdown(f"""<div class="card-box" style="border-left: 4px solid #f44336;"><b>{item['BRAND']} ({item['VEHICLE']}) {item['SIZE']}</b> — Stock Qty: <span style="color:#f44336;">{item['STOCK']}</span></div>""", unsafe_allow_html=True)
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

# 8. PIGMI COLLECTION (WITH DATE CALENDAR)
with tabs[7]:
    tot_pigmi = sum(p['BALANCE'] for p in st.session_state.pigmi_data)
    st.subheader(f"🐷 PIGMI COLLECTION • Total Balance: ₹{tot_pigmi:,.2f}")
    
    with st.expander("➕ Add New Pigmi Account / Person"):
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
                    "BANK": bank, "AC_NO": ac, "DAILY_TARGET": target, 
                    "OLD_BAL": 0, "COLLECTED": 0, "WITHDRAWN": 0, "BALANCE": 0,
                    "LAST_DATE": str(date.today())
                })
                st.success("✅ Pigmi Account Added Successfully!")
                st.rerun()

    st.markdown("### 📋 ACTIVE PIGMI ACCOUNTS")
    for idx, p in enumerate(st.session_state.pigmi_data):
        st.markdown(f"""
        <div class="card-box">
            <h3 style="margin:0; color:#4CAF50;">{p['NAME']}</h3>
            <p style="color:#aaa; font-size:13px; margin:2px 0;">{p['LOCATION']} • {p['PHONE']}</p>
            <p style="color:#ff9800; font-size:13px; margin-bottom:5px;">🏛️ <b>{p['BANK']}</b> | A/C No: <b>{p['AC_NO']}</b></p>
            <p style="font-size:13px; color:#888; margin-bottom:10px;">📅 Last Collection Date: <b>{p.get('LAST_DATE', 'N/A')}</b></p>
            <p style="font-size:14px;">
                Total Collected: <b style="color:#4CAF50;">₹{p['COLLECTED']:,.2f}</b> | Balance: <b style="color:#4CAF50;">₹{p['BALANCE']:,.2f}</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Date Picker & Amount Input & Collect Button
        col_b1, col_b2, col_b3 = st.columns([2, 2, 1])
        with col_b1:
            collect_date = st.date_input("Collection Date 📅", value=date.today(), key=f"date_{idx}")
        with col_b2:
            daily_amt = st.number_input(
                f"Amount (₹)", 
                min_value=10, 
                value=int(p.get('DAILY_TARGET', 500)), 
                key=f"daily_amt_{idx}"
            )
        with col_b3:
            st.write("") # spacing
            st.write("")
            if st.button(f"📥 Collect ₹{daily_amt}", key=f"col_btn_{idx}"):
                st.session_state.pigmi_data[idx]['COLLECTED'] += daily_amt
                st.session_state.pigmi_data[idx]['BALANCE'] += daily_amt
                st.session_state.pigmi_data[idx]['LAST_DATE'] = str(collect_date)
                st.success(f"Collected ₹{daily_amt} on {collect_date}!")
                st.rerun()

# 9. BILLING
with tabs[8]:
    st.subheader("🧾 BILLING & INVOICING")

# 10. PAYMENTS
with tabs[9]:
    st.subheader("💳 PAYMENTS")

# 11. CREDIT (കടം)
with tabs[10]:
    st.subheader("📒 CREDIT (കടം) MANAGEMENT")

# 12. EXPENSES
with tabs[11]:
    tot_exp = sum(e['AMOUNT'] for e in st.session_state.expenses_data)
    st.subheader(f"💸 EXPENSES MANAGEMENT • Total Spent: ₹{tot_exp:,.2f}")
    
    with st.expander("➕ ADD NEW EXPENSE"):
        with st.form("add_exp_form"):
            c1, c2 = st.columns(2)
            cat_select = c1.selectbox(
                "Expense Category", 
                ["Room Rent (റൂം വാടക)", "Electricity Bill (കറന്റ് ബില്ല്)", "Food / Tea (ഫുഡ് / ചായ)", "Salary (ശമ്പളം)", "Transport / Freight (വണ്ടി വാടക)", "Machine Repair (മെഷീൻ റിപ്പയർ)", "Other (മറ്റുള്ളവ)"]
            )
            
            custom_cat = ""
            if "Other" in cat_select:
                custom_cat = c1.text_input("Enter Custom Category Name")
            
            recipient = c2.text_input("Paid To / Recipient (ആർക്കാണ് പണം നൽകിയത്)", placeholder="e.g. Owner name, Hotel, KSEB")
            
            c3, c4, c5 = st.columns(3)
            amt = c3.number_input("Amount (തുക ₹)", min_value=1, step=50, value=100)
            urgency = c4.radio("Urgency (മുൻഗണന)", ["Normal", "Urgent ⚠️"], horizontal=True)
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
                st.success("✅ Expense Saved Successfully!")
                st.rerun()

    st.markdown("### 📋 EXPENSE RECORDS")
    for idx, e in enumerate(st.session_state.expenses_data):
        urg_badge = "🔴 URGENT" if "Urgent" in e.get('URGENCY', '') else "🟢 NORMAL"
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="card-box" style="padding:12px; margin-bottom:8px;">
                <span style="font-size:12px; color:#ff9800; border:1px solid #ff9800; padding:2px 6px; border-radius:4px;">{e['CATEGORY']}</span>
                <span style="font-size:12px; float:right;">{urg_badge} | 📅 {e.get('DATE', '')}</span>
                <h3 style="margin:5px 0 2px 0; color:#f44336;">₹ {e['AMOUNT']:,.2f}</h3>
                <span style="font-size:13px; color:#aaa;">Paid To: <b>{e.get('RECIPIENT', 'N/A')}</b></span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_exp_{idx}"):
                st.session_state.expenses_data.pop(idx)
                st.rerun()

# 13. RETREADING
with tabs[12]:
    st.subheader("🔄 RETREADING / REBELTING")

# 14. GUARANTEE / CLAIMS
with tabs[13]:
    st.subheader("🛡️ GUARANTEE & WARRANTY CLAIMS")

# 15. DEALERS DIRECTORY
with tabs[14]:
    st.subheader("📖 DEALERS DIRECTORY")
