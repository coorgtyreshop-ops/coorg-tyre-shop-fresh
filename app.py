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
    st.session_state.pigmi_data = [
        {
            "NAME": "KADEEJA P R", 
            "LOCATION": "ONTIYANGADI", 
            "PHONE": "7204814476", 
            "BANK": "JANAASHA SOUTH NIDHI LTD", 
            "AC_NO": "035601113", 
            "DAILY_TARGET": 500, 
            "COLLECTED": 20600, 
            "WITHDRAWN": 0, 
            "BALANCE": 20600, 
            "LAST_DATE": "2026-10-24",
            "HISTORY": [
                {"DATE": "2026-10-24", "AMOUNT": 5300},
                {"DATE": "2026-10-23", "AMOUNT": 5000},
                {"DATE": "2026-10-22", "AMOUNT": 5000},
                {"DATE": "2026-10-21", "AMOUNT": 5300}
            ]
        }
    ]

if "sales_data" not in st.session_state:
    st.session_state.sales_data = []

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = []

if "credit_data" not in st.session_state:
    st.session_state.credit_data = []

if "market_rates" not in st.session_state:
    st.session_state.market_rates = []

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

# 8. PIGMI COLLECTION (WITH DETAILED HISTORY LOG)
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
                    "BANK": bank.upper(), "AC_NO": ac, "DAILY_TARGET": target, 
                    "COLLECTED": 0, "WITHDRAWN": 0, "BALANCE": 0,
                    "LAST_DATE": str(date.today()),
                    "HISTORY": []
                })
                st.success("✅ Pigmi Account Added Successfully!")
                st.rerun()

    st.markdown("### 📋 ACTIVE PIGMI ACCOUNTS")
    for idx, p in enumerate(st.session_state.pigmi_data):
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
        
        # Display History of Collections
        if p.get("HISTORY"):
            with st.expander(f"📜 View Collection History for {p['NAME']}"):
                for h in p["HISTORY"]:
                    st.markdown(f"- 📅 Date: **{h['DATE']}** | Collected Amount: <b style='color:#4CAF50;'>₹{h['AMOUNT']:,.2f}</b>", unsafe_allow_html=True)
        
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
            st.write("") 
            st.write("")
            if st.button(f"📥 Collect ₹{daily_amt}", key=f"col_btn_{idx}"):
                st.session_state.pigmi_data[idx]['COLLECTED'] += daily_amt
                st.session_state.pigmi_data[idx]['BALANCE'] += daily_amt
                st.session_state.pigmi_data[idx]['LAST_DATE'] = str(collect_date)
                
                # Append to history
                if "HISTORY" not in st.session_state.pigmi_data[idx]:
                    st.session_state.pigmi_data[idx]["HISTORY"] = []
                st.session_state.pigmi_data[idx]["HISTORY"].insert(0, {"DATE": str(collect_date), "AMOUNT": daily_amt})
                
                st.success(f"Collected ₹{daily_amt} on {collect_date}!")
                st.rerun()

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")

# 3. TUBE STOCK
with tabs[2]:
    st.subheader(f"TUBE STOCK ({len(st.session_state.tube_stock)})")

# 4. PUNCTURE ITEMS
with tabs[3]:
    st.subheader("🛠️ PUNCTURE & SERVICE ITEMS")

# 5. REORDER / LOW STOCK
with tabs[4]:
    st.subheader("REORDER / LOW STOCK")

# 6. MARKET RATES
with tabs[5]:
    st.subheader("📈 MARKET RATES & ONLINE PRICES")

# 7. STATUS STUDIO
with tabs[6]:
    st.subheader("🎬 STATUS STUDIO")

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

# 13. RETREADING
with tabs[12]:
    st.subheader("🔄 RETREADING / REBELTING")

# 14. GUARANTEE / CLAIMS
with tabs[13]:
    st.subheader("🛡️ GUARANTEE & WARRANTY CLAIMS")

# 15. DEALERS DIRECTORY
with tabs[14]:
    st.subheader("📖 DEALERS DIRECTORY")
