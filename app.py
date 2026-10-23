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
        {"BRAND": "APOLLO", "SIZE": "90/90/12", "CONDITION": "New", "PATTERN": "ZIP54 J", "STOCK": 0, "PURCHASE RATE": 950, "SELLING RATE": 1350}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = [
        {"BRAND": "MRF", "SIZE": "3.00-10", "STOCK": 5, "PURCHASE RATE": 180, "SELLING RATE": 250},
        {"BRAND": "BRAZA", "SIZE": "3.00/18", "STOCK": 4, "PURCHASE RATE": 200, "SELLING RATE": 245}
    ]

if "pigmi_data" not in st.session_state:
    st.session_state.pigmi_data = [
        {
            "NAME": "SHAHAJAHAN E", 
            "LOCATION": "ONTIYANGADI", 
            "PHONE": "9900316275", 
            "BANK": "Janaasha South Nidhi Ltd", 
            "AC_NO": "035601167", 
            "OLD_BAL": 1000, 
            "COLLECTED": 6000, 
            "WITHDRAWN": 0, 
            "BALANCE": 7000
        },
        {
            "NAME": "SHAHAJAHAN", 
            "LOCATION": "ONTIYANGADI", 
            "PHONE": "9900316275", 
            "BANK": "Nelliyanipuri Society Bank", 
            "AC_NO": "11298", 
            "OLD_BAL": 0, 
            "COLLECTED": 5500, 
            "WITHDRAWN": 0, 
            "BALANCE": 5500
        }
    ]

if "retread_data" not in st.session_state:
    st.session_state.retread_data = [
        {
            "CUSTOMER": "PRAVEEN", "MOBILE": "", "VEHICLE": "LORY", "VEH_NO": "JK - 10.20", 
            "PROCESS": "Cold", "BRAND": "JK", "SIZE": "10.20", "TYRE_NO": "#V003519", 
            "MFG": "0325", "QTY": 1, "DATE": "2026-10-05", "TOTAL": 6880, "PAID": 6880, "STATUS": "Delivered"
        }
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

if "shop_settings" not in st.session_state:
    st.session_state.shop_settings = {
        "name_en": "COORG TYRE SHOP",
        "name_ml": "കൂർഗ് ടയർ ഷോപ്പ്",
        "address": "Abyayath Mangala, Ontiyangadi, Main Road, Siddapura - 571253",
        "phone": "9900316275",
        "upi": "coorgtyreshop-1@okhdfcbank",
        "account_holder": "SHAHAJAHAN IBRAHIM"
    }

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
st.markdown(f"""
<div class="main-header" style="display:flex; justify-content:space-between; align-items:center;">
    <div>
        <div class="shop-title">🛞 {st.session_state.shop_settings['name_en']}</div>
        <div class="shop-sub">{st.session_state.shop_settings['address']}</div>
    </div>
    <div>
        <span style="background-color: #d9534f; color: white; padding: 6px 12px; border-radius: 4px; font-weight: bold; font-size: 12px;">🔴 CCTV Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ALL NAVIGATION TABS
# ---------------------------------------------------------
tabs = st.tabs([
    "📈 Overview", 
    "🛞 Tyre Stock", 
    "🔘 Tube Stock",
    "📋 Reorder / Low Stock",
    "📊 Market Rates",
    "🔧 Puncture Items",
    "🎬 Status Studio", 
    "🚚 Suppliers / Inward", 
    "🔄 Retreading / Rebelting",
    "📖 Dealers Directory",
    "💳 Credit (Kadam)",
    "🐷 Pigmi Collection", 
    "🧾 Billing", 
    "🛡️ Guarantee / Claims",
    "💳 Payments", 
    "💸 Expenses",
    "⚙️ Shop Settings"
])

# 1. OVERVIEW
with tabs[0]:
    st.subheader("OVERVIEW • DASHBOARD")
    
    # Report Filter Header
    col_r1, col_r2, col_r3, col_r4 = st.columns([1, 1, 1, 1])
    report_type = col_r1.radio("Report Filter", ["Daily", "Monthly", "Annual"], horizontal=True, label_visibility="collapsed")
    selected_date = col_r3.date_input("Date", date.today(), label_visibility="collapsed")
    if col_r4.button("Generate 🚀"):
        st.success("Report generated!")

    st.markdown("---")
    
    # Metrics Grid (As shown in video)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("TODAY'S SALES", "₹ 100")
    c2.metric("CASH", "₹ 0")
    c3.metric("PAYTM / UPI", "₹ 0")
    c4.metric("CREDIT GIVEN TODAY", "₹ 0")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("PIGMI COLLECTED TODAY", "₹ 22,500")
    c6.metric("PIGMI WITHDRAWN", "₹ 0")
    c7.metric("PAID TO AGENTS", "₹ 0")
    c8.metric("EXPENSES TODAY", "₹ 0")

    c9, c10 = st.columns(2)
    c9.metric("NET CASH IN HAND", "₹ 0")
    c10.metric("TOTAL OUTSTANDING", "₹ 4,000")

    st.markdown("---")
    st.subheader("🛒 TODAY'S WORK BREAKDOWN")
    
    with st.form("work_breakdown_form"):
        col_w1, col_w2, col_w3, col_w4 = st.columns([2, 1, 1, 1])
        item_type = col_w1.selectbox("ITEM", [
            "Tubeless Puncture", "Tube Puncture", "Inside Puncture", 
            "Neck / Valve Change", "Tyre Setting", "Tyre Sale", 
            "Tube Sale", "Fitting Charge", "Wheel Balancing", "Flap Change"
        ])
        qty = col_w2.number_input("QTY", min_value=1, value=1)
        amount = col_w3.number_input("AMOUNT (₹)", min_value=0, value=100)
        pay_mode = col_w4.selectbox("PAYMENT MODE", ["Cash", "UPI", "Credit"])
        
        if st.form_submit_button("💾 Save Work"):
            st.success("Work entry saved successfully!")

    st.markdown("---")
    st.subheader("📅 THIS MONTH")
    m1, m2 = st.columns(2)
    m1.metric("TODAY'S SALES", "₹ 1,18,888")
    m2.metric("CASH", "₹ 51,449")
    
    m3, m4 = st.columns(2)
    m3.metric("PAYTM / UPI", "₹ 66,139")
    m4.metric("EXPENSES", "₹ 93,120")

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")
    search_t = st.text_input("🔍 Search size / brand (e.g. 165/80 or MRF)...")
    df_t = pd.DataFrame(st.session_state.tyre_stock)
    if not df_t.empty and search_t:
        df_t = df_t[df_t['BRAND'].str.contains(search_t, case=False, na=False) | df_t['SIZE'].str.contains(search_t, case=False, na=False)]
    st.dataframe(df_t, use_container_width=True)

# 3. TUBE STOCK
with tabs[2]:
    st.subheader(f"TUBE STOCK ({len(st.session_state.tube_stock)})")
    df_tu = pd.DataFrame(st.session_state.tube_stock)
    st.dataframe(df_tu, use_container_width=True)

# 4. REORDER / LOW STOCK
with tabs[3]:
    st.subheader("REORDER / LOW STOCK")
    low_limit = st.slider("Low if <=", 1, 5, 3)
    out_of_stock = [item for item in st.session_state.tyre_stock if item['STOCK'] <= low_limit]
    for item in out_of_stock:
        st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #f44336;">
            <b>{item['BRAND']} {item['SIZE']}</b> — Stock Qty: <span style="color:#f44336;">{item['STOCK']}</span>
        </div>
        """, unsafe_allow_html=True)

# 5. MARKET RATES
with tabs[4]:
    st.subheader("LIVE MARKET RATE LOOKUP")
    st.write("Enter vehicle type, brand & tyre size — get today's online market prices.")
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.selectbox("VEHICLE", ["Car", "Bike", "Scooter", "Auto", "Truck"])
    col_m2.selectbox("BRAND", ["Apollo", "MRF", "CEAT", "JK Tyre"])
    col_m3.text_input("SIZE", placeholder="e.g. 165/80 R14")

# 6. PUNCTURE ITEMS
with tabs[5]:
    st.subheader("PUNCTURE ITEMS (5)")
    st.markdown("""
    <div class="card-box">
        <b>Flap</b><br>Stock: 3 pcs<br><span style="color:#f44336;">LOW STOCK</span>
        <h3 style="color:#4CAF50;">₹320</h3>
    </div>
    """, unsafe_allow_html=True)

# 7. STATUS STUDIO
with tabs[6]:
    st.subheader("STATUS STUDIO")
    st.write("Create branded WhatsApp-status posters & videos.")
    st.radio("Format", ["Poster", "Status Video"], horizontal=True)
    st.radio("Source", ["AI-made", "My photo"], horizontal=True)
    st.file_uploader("Choose File", type=["jpg", "png", "mp4"])

# 8. SUPPLIERS / INWARD
with tabs[7]:
    st.subheader("SUPPLIERS / INWARD")
    st.info("Manage suppliers and incoming stock invoices.")

# 9. RETREADING / REBELTING
with tabs[8]:
    st.subheader("RETREADING / REBELTING (2)")
    with st.expander("➕ Add Retread Job"):
        with st.form("retread_form"):
            c1, c2 = st.columns(2)
            cust = c1.text_input("Customer Name")
            mob = c2.text_input("Mobile")
            c3, c4 = st.columns(2)
            veh = c3.text_input("Vehicle")
            veh_no = c4.text_input("Vehicle Number")
            proc = st.selectbox("Process", ["Cold", "Hot / Normal"])
            brand = st.text_input("Brand")
            size = st.text_input("Size")
            tyre_no = st.text_input("Tyre Number")
            qty = st.number_input("Qty", min_value=1, value=1)
            if st.form_submit_button("Save Job"):
                st.success("Retread job added!")

    for r in st.session_state.retread_data:
        st.markdown(f"""
        <div class="card-box">
            <h3 style="color:#ff9800; margin:0;">{r['CUSTOMER']}</h3>
            <p style="color:#aaa; font-size:13px;">{r['VEHICLE']} • {r['VEH_NO']} | {r['PROCESS']}</p>
            <p><b>{r['TYRE_NO']}</b> | Qty: {r['QTY']} | Total: ₹{r['TOTAL']} | Paid: ₹{r['PAID']}</p>
            <span style="background-color:#4CAF50; color:white; padding:2px 8px; border-radius:4px; font-size:12px;">{r['STATUS']}</span>
        </div>
        """, unsafe_allow_html=True)

# 10. DEALERS DIRECTORY
with tabs[9]:
    st.subheader("DEALERS DIRECTORY")
    st.info("Direct supplier contact details.")

# 11. CREDIT (KADAM)
with tabs[10]:
    st.subheader("CREDIT (KADAM) MANAGEMENT")
    st.info("Track customer credit and dues.")

# 12. PIGMI COLLECTION
with tabs[11]:
    tot_pigmi = sum(p['BALANCE'] for p in st.session_state.pigmi_data)
    st.subheader(f"🐷 PIGMI COLLECTION • Total balance: ₹{tot_pigmi:,.2f}")
    
    with st.expander("➕ Add Pigmi Account"):
        with st.form("add_pigmi_form"):
            c1, c2, c3 = st.columns(3)
            p_name = c1.text_input("Customer Name")
            p_place = c2.text_input("Place")
            p_mob = c3.text_input("Mobile")
            c4, c5 = st.columns(2)
            p_bank = c4.text_input("Bank name")
            p_ac = c5.text_input("Pigmy Account No / A/C")
            p_old = st.number_input("Old Balance (₹)", min_value=0.0)
            
            if st.form_submit_button("Save Account 💾"):
                if p_name and p_ac:
                    st.session_state.pigmi_data.append({
                        "NAME": p_name.upper(), "LOCATION": p_place.upper(), "PHONE": p_mob,
                        "BANK": p_bank, "AC_NO": p_ac, "OLD_BAL": p_old, 
                        "COLLECTED": 0.0, "WITHDRAWN": 0.0, "BALANCE": p_old
                    })
                    st.success("Pigmi account added!")
                    st.rerun()

    for idx, p in enumerate(st.session_state.pigmi_data):
        st.markdown(f"""
        <div class="card-box">
            <h3 style="margin:0; color:#4CAF50;">{p['NAME']}</h3>
            <p style="color:#aaa; font-size:13px; margin:2px 0;">{p['LOCATION']} • {p['PHONE']}</p>
            <p style="color:#ff9800; font-size:13px; margin-bottom:10px;">🏛️ <b>{p['BANK']}</b> | A/C: {p['AC_NO']}</p>
            <p style="font-size:14px;">
                Old Balance: <b>₹{p['OLD_BAL']:,.2f}</b> | Collected: <b style="color:#4CAF50;">₹{p['COLLECTED']:,.2f}</b> | Withdrawn: <b style="color:#f44336;">₹{p['WITHDRAWN']:,.2f}</b> | <b style="color:#4CAF50;">Balance: ₹{p['BALANCE']:,.2f}</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        c_btn1, c_btn2 = st.columns(2)
        if c_btn1.button(f"📥 Collect ({p['AC_NO']})", key=f"col_{idx}"):
            st.session_state.pigmi_data[idx]['COLLECTED'] += 500
            st.session_state.pigmi_data[idx]['BALANCE'] += 500
            st.rerun()
        if c_btn2.button(f"📤 Withdraw ({p['AC_NO']})", key=f"wit_{idx}"):
            st.session_state.pigmi_data[idx]['WITHDRAWN'] += 500
            st.session_state.pigmi_data[idx]['BALANCE'] -= 500
            st.rerun()

# 13. BILLING
with tabs[12]:
    st.subheader("BILLING")
    for b in st.session_state.billing_data:
        st.markdown(f"""
        <div class="card-box">
            <b style="color:#ff9800; font-size:16px;">{b['BILL_NO']}</b> - {b['TYPE']} ({b['SERVICE']})
            <h3 style="color:#4CAF50; margin:5px 0 0 0;">₹ {b['AMOUNT']}</h3>
        </div>
        """, unsafe_allow_html=True)

# 14. GUARANTEE / CLAIMS
with tabs[13]:
    st.subheader("GUARANTEE / CLAIMS")
    st.info("Warranty claims management.")

# 15. PAYMENTS
with tabs[14]:
    st.subheader("PAYMENTS")
    c1, c2 = st.columns(2)
    c1.metric("CASH TODAY", "₹ 0")
    c2.metric("DIGITAL TODAY", "₹ 0")

# 16. EXPENSES
with tabs[15]:
    tot_exp = sum(e['AMOUNT'] for e in st.session_state.expenses_data)
    st.subheader(f"EXPENSES • Total: ₹{tot_exp:,.2f}")
    df_exp = pd.DataFrame(st.session_state.expenses_data)
    st.dataframe(df_exp, use_container_width=True)

# 17. SHOP SETTINGS
with tabs[16]:
    st.subheader("SHOP SETTINGS")
    st.write("Add your bank & UPI details — these power the Scan & Pay QR and bill header.")
    with st.form("settings_form"):
        s_name_en = st.text_input("SHOP NAME (ENGLISH)", value=st.session_state.shop_settings['name_en'])
        s_name_ml = st.text_input("SHOP NAME (MALAYALAM)", value=st.session_state.shop_settings['name_ml'])
        s_addr = st.text_input("ADDRESS", value=st.session_state.shop_settings['address'])
        s_ph = st.text_input("PHONE", value=st.session_state.shop_settings['phone'])
        s_upi = st.text_input("UPI ID (FOR QR)", value=st.session_state.shop_settings['upi'])
        s_acc = st.text_input("ACCOUNT HOLDER", value=st.session_state.shop_settings['account_holder'])
        
        if st.form_submit_button("Save Settings 💾"):
            st.session_state.shop_settings['name_en'] = s_name_en
            st.session_state.shop_settings['name_ml'] = s_name_ml
            st.session_state.shop_settings['address'] = s_addr
            st.session_state.shop_settings['phone'] = s_ph
            st.session_state.shop_settings['upi'] = s_upi
            st.session_state.shop_settings['account_holder'] = s_acc
            st.success("Settings updated successfully!")
            st.rerun()
