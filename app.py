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
        {"BRAND": "APOLLO", "SIZE": "90/100/10", "CONDITION": "New", "PATTERN": "53J GRIP", "STOCK": 1, "PURCHASE RATE": 1020, "SELLING RATE": 1450},
        {"BRAND": "MRF", "SIZE": "90/90/12", "CONDITION": "New", "PATTERN": "GRIP", "STOCK": 2, "PURCHASE RATE": 950, "SELLING RATE": 1350}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = [
        {"BRAND": "MRF", "SIZE": "3.00-10", "CONDITION": "New", "STOCK": 5, "PURCHASE RATE": 180, "SELLING RATE": 250}
    ]

if "puncture_items" not in st.session_state:
    st.session_state.puncture_items = [
        {"SERVICE": "Tubeless Puncture", "RATE": 100},
        {"SERVICE": "Tube Puncture", "RATE": 80},
        {"SERVICE": "Inside Puncture", "RATE": 150},
        {"SERVICE": "Valve Change", "RATE": 120}
    ]

if "pigmi_data" not in st.session_state:
    st.session_state.pigmi_data = [
        {"NAME": "SHAHAJAHAN E", "LOCATION": "ONTIYANGADI", "PHONE": "9900316275", "BANK": "Janaasha South Nidhi Ltd", "AC_NO": "035601167", "OLD_BAL": 1000, "COLLECTED": 6000, "WITHDRAWN": 0, "BALANCE": 7000},
        {"NAME": "SHAHAJAHAN", "LOCATION": "ONTIYANGADI", "PHONE": "9900316275", "BANK": "Nelliyanipuri Society Bank", "AC_NO": "11298", "OLD_BAL": 0, "COLLECTED": 5500, "WITHDRAWN": 0, "BALANCE": 5500}
    ]

if "billing_data" not in st.session_state:
    st.session_state.billing_data = [
        {"BILL_NO": "CTS-1176", "TYPE": "Counter Sale", "SERVICE": "Tubeless Puncture", "AMOUNT": 100, "MODE": "Cash"}
    ]

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = [
        {"CATEGORY": "Room Rent", "AMOUNT": 15000},
        {"CATEGORY": "Electricity", "AMOUNT": 2500}
    ]

if "credit_data" not in st.session_state:
    st.session_state.credit_data = [
        {"CUSTOMER": "Ramesh", "PHONE": "9876543210", "DETAILS": "Tyre Balance", "AMOUNT": 1500, "STATUS": "Pending"}
    ]

if "market_rates" not in st.session_state:
    st.session_state.market_rates = [
        {"BRAND": "APOLLO", "SIZE": "90/100/10", "ONLINE_PRICE": 1450, "LAST_UPDATED": "22/10/2026"},
        {"BRAND": "MRF", "SIZE": "3.00-10", "ONLINE_PRICE": 250, "LAST_UPDATED": "22/10/2026"}
    ]

if "guarantee_claims" not in st.session_state:
    st.session_state.guarantee_claims = [
        {"CUSTOMER": "Savad", "ITEM": "Apollo 100/90-10", "ISSUE": "Side bubble", "STATUS": "Pending"}
    ]

if "dealers_directory" not in st.session_state:
    st.session_state.dealers_directory = [
        {"DEALER": "JK Tyre Agency", "LOCATION": "Madikeri", "PHONE": "9440012345"},
        {"DEALER": "MRF Stockist", "LOCATION": "Siddapur", "PHONE": "9880098765"}
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
# NAVIGATION TABS (ALL MODULES)
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
    c8.metric("EXPENSES", f"₹ {sum(e['AMOUNT'] for e in st.session_state.expenses_data)}")

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")
    with st.expander("➕ Add New Tyre Stock"):
        with st.form("add_tyre_form"):
            col1, col2, col3, col4 = st.columns(4)
            brand = col1.text_input("Brand")
            size = col2.text_input("Size")
            condition = col3.selectbox("Condition", ["New", "Used", "Retread"])
            pattern = col4.text_input("Pattern")
            col5, col6, col7 = st.columns(3)
            p_rate = col5.number_input("Purchase Rate (₹)", min_value=0)
            s_rate = col6.number_input("Selling Rate (₹)", min_value=0.0)
            qty = col7.number_input("Stock Qty", min_value=0, value=1)
            if st.form_submit_button("Save Tyre 📦"):
                st.session_state.tyre_stock.append({"BRAND": brand.upper(), "SIZE": size, "CONDITION": condition, "PATTERN": pattern, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate})
                st.success("✅ Added!")
                st.rerun()

    for idx, t in enumerate(st.session_state.tyre_stock):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box" style="padding:10px; margin-bottom:5px;"><b>{t['BRAND']}</b> - {t['SIZE']} | Stock: <b style="color:#4CAF50;">{t['STOCK']}</b> | Sell: ₹{t['SELLING RATE']}</div>""", unsafe_allow_html=True)
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
            brand = c1.text_input("Brand")
            size = c2.text_input("Size")
            cond = c3.selectbox("Condition", ["New", "Used"])
            qty = c4.number_input("Qty", min_value=1, value=1)
            p_rate = st.number_input("Purchase Rate", min_value=0, value=150)
            s_rate = st.number_input("Selling Rate", min_value=0, value=220)
            if st.form_submit_button("Save Tube"):
                st.session_state.tube_stock.append({"BRAND": brand.upper(), "SIZE": size, "CONDITION": cond, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate})
                st.success("Tube added!")
                st.rerun()

    for idx, tu in enumerate(st.session_state.tube_stock):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box" style="padding:10px; margin-bottom:5px;"><b>{tu['BRAND']}</b> - {tu['SIZE']} | Stock: <b style="color:#4CAF50;">{tu['STOCK']}</b></div>""", unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_tu_{idx}"):
                st.session_state.tube_stock.pop(idx)
                st.rerun()

# 4. PUNCTURE ITEMS
with tabs[3]:
    st.subheader("🛠️ PUNCTURE & SERVICE ITEMS")
    with st.expander("➕ Add New Puncture/Service Item"):
        with st.form("add_punc"):
            service_name = st.text_input("Service Name (e.g. Puncher Patch)")
            service_rate = st.number_input("Standard Rate (₹)", min_value=0, value=100)
            if st.form_submit_button("Save Service"):
                st.session_state.puncture_items.append({"SERVICE": service_name, "RATE": service_rate})
                st.success("Service item added!")
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
            st.markdown(f"""<div class="card-box" style="border-left: 4px solid #f44336;"><b>{item['BRAND']} {item['SIZE']}</b> — Stock Qty: <span style="color:#f44336;">{item['STOCK']}</span></div>""", unsafe_allow_html=True)
    else:
        st.success("All items have sufficient stock!")

# 6. MARKET RATES (With Search Bar)
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
    st.radio("Format", ["Poster", "Status Video"], horizontal=True)
    st.file_uploader("Upload Shop Media", type=["jpg", "png", "mp4"])

# 8. PIGMI COLLECTION
with tabs[7]:
    tot_pigmi = sum(p['BALANCE'] for p in st.session_state.pigmi_data)
    st.subheader(f"🐷 PIGMI COLLECTION • Total: ₹{tot_pigmi:,.2f}")
    with st.expander("➕ Add Pigmi Account"):
        with st.form("add_p"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Name")
            loc = c2.text_input("Location")
            phone = c3.text_input("Phone")
            bank = st.text_input("Bank Name")
            ac = st.text_input("A/C Number")
            if st.form_submit_button("Save"):
                st.session_state.pigmi_data.append({"NAME": name.upper(), "LOCATION": loc, "PHONE": phone, "BANK": bank, "AC_NO": ac, "OLD_BAL": 0, "COLLECTED": 0, "WITHDRAWN": 0, "BALANCE": 0})
                st.success("Added!")
                st.rerun()

    for idx, p in enumerate(st.session_state.pigmi_data):
        st.markdown(f"""<div class="card-box"><h3 style="margin:0; color:#4CAF50;">{p['NAME']}</h3><p style="color:#ff9800; font-size:13px;">{p['BANK']} | A/C: {p['AC_NO']}</p><p>Balance: <b>₹{p['BALANCE']:,.2f}</b></p></div>""", unsafe_allow_html=True)

# 9. BILLING
with tabs[8]:
    st.subheader("🧾 BILLING & INVOICING")
    if st.button("➕ Create Bill"):
        new_no = f"CTS-{1177 + len(st.session_state.billing_data)}"
        st.session_state.billing_data.insert(0, {"BILL_NO": new_no, "TYPE": "Counter Sale", "SERVICE": "Tubeless Puncture", "AMOUNT": 150, "MODE": "Cash"})
        st.rerun()

    for idx, b in enumerate(st.session_state.billing_data):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box"><b>{b['BILL_NO']}</b> - {b['TYPE']} ({b['SERVICE']})<h3 style="color:#4CAF50; margin:0;">₹ {b['AMOUNT']}</h3></div>""", unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_b_{idx}"):
                st.session_state.billing_data.pop(idx)
                st.rerun()

# 10. PAYMENTS
with tabs[9]:
    st.subheader("💳 PAYMENTS")
    c1, c2 = st.columns(2)
    c1.metric("CASH TODAY", "₹ 0")
    c2.metric("DIGITAL TODAY", "₹ 0")

# 11. CREDIT (കടം)
with tabs[10]:
    st.subheader("📒 CREDIT (കടം) MANAGEMENT")
    with st.expander("➕ Add New Credit Entry"):
        with st.form("add_cred"):
            c_name = st.text_input("Customer Name")
            c_phone = st.text_input("Phone Number")
            c_det = st.text_input("Details / Items")
            c_amt = st.number_input("Amount (₹)", min_value=0, value=500)
            if st.form_submit_button("Save Credit 💾"):
                st.session_state.credit_data.append({"CUSTOMER": c_name, "PHONE": c_phone, "DETAILS": c_det, "AMOUNT": c_amt, "STATUS": "Pending"})
                st.success("Credit recorded!")
                st.rerun()

    for idx, cr in enumerate(st.session_state.credit_data):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box"><b>{cr['CUSTOMER']}</b> ({cr['PHONE']}) - {cr['DETAILS']}<h3 style="color:#f44336; margin:0;">₹ {cr['AMOUNT']}</h3></div>""", unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Clear", key=f"del_cr_{idx}"):
                st.session_state.credit_data.pop(idx)
                st.rerun()

# 12. EXPENSES (With Add & Delete categories)
with tabs[11]:
    tot_exp = sum(e['AMOUNT'] for e in st.session_state.expenses_data)
    st.subheader(f"💸 EXPENSES • Total: ₹{tot_exp:,.2f}")
    with st.expander("➕ ADD EXPENSE CATEGORY / AMOUNT"):
        with st.form("add_exp"):
            cat = st.text_input("Category (e.g. Room Rent, Tea/Food, Salary)")
            amt = st.number_input("Amount (₹)", min_value=0, step=100)
            if st.form_submit_button("Save Expense 💾"):
                st.session_state.expenses_data.append({"CATEGORY": cat, "AMOUNT": amt})
                st.success("Expense saved!")
                st.rerun()

    for idx, e in enumerate(st.session_state.expenses_data):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""<div class="card-box" style="padding:10px; margin-bottom:5px;"><b>{e['CATEGORY']}</b> — <span style="color:#f44336; font-weight:bold;">₹{e['AMOUNT']}</span></div>""", unsafe_allow_html=True)
        with col2:
            if st.button("🗑️ Delete", key=f"del_e_{idx}"):
                st.session_state.expenses_data.pop(idx)
                st.rerun()

# 13. RETREADING
with tabs[12]:
    st.subheader("🔄 RETREADING / REBELTING")
    with st.expander("➕ Add Retreading Entry"):
        with st.form("add_ret"):
            r_cust = st.text_input("Customer Name")
            r_size = st.text_input("Tyre Size")
            r_qty = st.number_input("Quantity", min_value=1, value=1)
            if st.form_submit_button("Save"):
                st.session_state.retreading_data.append({"CUSTOMER": r_cust, "TYRE_SIZE": r_size, "QTY": r_qty, "STATUS": "Processing"})
                st.success("Added!")
                st.rerun()

    for r in st.session_state.retreading_data:
        st.markdown(f"""<div class="card-box"><b>{r['CUSTOMER']}</b> - {r['TYRE_SIZE']} (Qty: {r['QTY']}) - Status: {r['STATUS']}</div>""", unsafe_allow_html=True)

# 14. GUARANTEE / CLAIMS
with tabs[13]:
    st.subheader("🛡️ GUARANTEE & WARRANTY CLAIMS")
    with st.expander("➕ Add Claim"):
        with st.form("add_claim"):
            c_cust = st.text_input("Customer Name")
            c_item = st.text_input("Tyre/Tube Details")
            c_issue = st.text_input("Issue Description")
            if st.form_submit_button("Save Claim"):
                st.session_state.guarantee_claims.append({"CUSTOMER": c_cust, "ITEM": c_item, "ISSUE": c_issue, "STATUS": "Pending"})
                st.success("Claim saved!")
                st.rerun()

    for gc in st.session_state.guarantee_claims:
        st.markdown(f"""<div class="card-box"><b>{gc['CUSTOMER']}</b> - {gc['ITEM']} | Issue: {gc['ISSUE']}</div>""", unsafe_allow_html=True)

# 15. DEALERS DIRECTORY
with tabs[14]:
    st.subheader("📖 DEALERS DIRECTORY")
    with st.expander("➕ Add Dealer"):
        with st.form("add_dealer"):
            d_name = st.text_input("Dealer Name")
            d_loc = st.text_input("Location")
            d_phone = st.text_input("Phone Number")
            if st.form_submit_button("Save Dealer"):
                st.session_state.dealers_directory.append({"DEALER": d_name, "LOCATION": d_loc, "PHONE": d_phone})
                st.success("Dealer added!")
                st.rerun()

    for d in st.session_state.dealers_directory:
        st.markdown(f"""<div class="card-box"><b>{d['DEALER']}</b> ({d['LOCATION']}) - Phone: {d['PHONE']}</div>""", unsafe_allow_html=True)
