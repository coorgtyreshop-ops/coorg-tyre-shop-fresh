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
        {"BRAND": "APOLLO", "SIZE": "90/90/12", "CONDITION": "New", "PATTERN": "GRIP", "STOCK": 0, "PURCHASE RATE": 950, "SELLING RATE": 1350}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = [
        {"BRAND": "MRF", "SIZE": "3.00-10", "STOCK": 5, "PURCHASE RATE": 180, "SELLING RATE": 250}
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

if "billing_data" not in st.session_state:
    st.session_state.billing_data = [
        {"BILL_NO": "CTS-1176", "TYPE": "Counter Sale", "SERVICE": "Puncture-Service", "AMOUNT": 2350},
        {"BILL_NO": "CTS-1175", "TYPE": "Counter Sale", "SERVICE": "Puncture-Service", "AMOUNT": 350},
        {"BILL_NO": "CTS-1174", "TYPE": "Counter Sale", "SERVICE": "Puncture-Service", "AMOUNT": 100},
        {"BILL_NO": "CTS-1173", "TYPE": "Counter Sale", "SERVICE": "Puncture-Service", "AMOUNT": 500}
    ]

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = [
        {"CATEGORY": "Room Rent", "AMOUNT": 15000},
        {"CATEGORY": "Electricity", "AMOUNT": 2500},
        {"CATEGORY": "Shop Setup", "AMOUNT": 75620}
    ]

# ---------------------------------------------------------
# CUSTOM CSS STYLING (DARK THEME)
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
    .warning-box {
        background-color: #2b2308;
        border: 1px solid #f39c12;
        color: #f1c40f;
        padding: 10px;
        border-radius: 5px;
        font-size: 13px;
        margin-bottom: 15px;
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
    "📋 Reorder / Low Stock",
    "🎬 Status Studio", 
    "🐷 Pigmi Collection", 
    "🧾 Billing", 
    "💳 Payments", 
    "💸 Expenses",
    "🚚 Suppliers / Inward", 
    "🛡️ Guarantee / Claims",
    "📖 Dealers Directory"
])

# 1. OVERVIEW
with tabs[0]:
    st.subheader("OVERVIEW • TODAY's SUMMARY")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Today's Sales", "₹ 2,350")
    c2.metric("Total Tyres Sold", "1 nos")
    c3.metric("Available Stock", f"{sum(item['STOCK'] for item in st.session_state.tyre_stock)} nos")
    c4.metric("Pigmi Total Balance", f"₹ {sum(item['BALANCE'] for item in st.session_state.pigmi_data):,.2f}")

# 2. TYRE STOCK
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")
    
    st.markdown("""
    <div class="warning-box">
        ⚠️ ഇന്നത്തെ വില ഇതുവരെ വന്നിട്ടില്ല — അവസാനം Online വില എടുത്തത്: 22/10, 10:35 am - എല്ലാ ദിവസവും രാവിലെ തനിയെ പുതുക്കും.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("➕ Add New Tyre Stock"):
        with st.form("add_tyre_form"):
            col1, col2, col3, col4 = st.columns(4)
            brand = col1.text_input("Brand (e.g. APOLLO)")
            size = col2.text_input("Size (e.g. 90/100/10)")
            condition = col3.selectbox("Condition", ["New", "Used", "Retread"])
            pattern = col4.text_input("Pattern (e.g. 53J GRIP)")
            
            col5, col6, col7 = st.columns(3)
            p_rate = col5.number_input("Purchase Rate (₹)", min_value=0)
            s_rate = col6.number_input("Selling Rate (₹)", min_value=0)
            qty = col7.number_input("Stock Qty", min_value=0, value=1)
            
            if st.form_submit_button("Save Tyre 📦"):
                st.session_state.tyre_stock.append({
                    "BRAND": brand.upper(), "SIZE": size, "CONDITION": condition,
                    "PATTERN": pattern, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
                })
                st.success("✅ Tyre stock added!")
                st.rerun()

    search_tyre = st.text_input("🔍 Search size / brand (e.g. 165/80 or MRF)...", key="search_t")
    df_t = pd.DataFrame(st.session_state.tyre_stock)
    if not df_t.empty and search_tyre:
        df_t = df_t[df_t['BRAND'].str.contains(search_tyre, case=False, na=False) | df_t['SIZE'].str.contains(search_tyre, case=False, na=False)]
    st.dataframe(df_t, use_container_width=True)

# 3. TUBE STOCK
with tabs[2]:
    st.subheader(f"TUBE STOCK ({len(st.session_state.tube_stock)})")
    with st.expander("➕ Add New Tube Stock"):
        with st.form("add_tube_form"):
            c1, c2, c3 = st.columns(3)
            t_brand = c1.text_input("Brand")
            t_size = c2.text_input("Size")
            t_qty = c3.number_input("Quantity", min_value=1, value=1)
            if st.form_submit_button("Save Tube"):
                st.session_state.tube_stock.append({"BRAND": t_brand.upper(), "SIZE": t_size, "STOCK": t_qty, "PURCHASE RATE": 150, "SELLING RATE": 220})
                st.success("Tube added!")
                st.rerun()
    df_tu = pd.DataFrame(st.session_state.tube_stock)
    if not df_tu.empty:
        st.dataframe(df_tu, use_container_width=True)

# 4. REORDER / LOW STOCK
with tabs[3]:
    st.subheader("REORDER / LOW STOCK")
    low_limit = st.slider("Low if <=", 1, 5, 3)
    st.write(f"Items that are out of stock or running low (<= {low_limit}) — give this list to your agent to order.")
    
    out_of_stock = [item for item in st.session_state.tyre_stock if item['STOCK'] <= low_limit]
    if out_of_stock:
        st.markdown("### ❌ OUT OF STOCK / LOW STOCK")
        for item in out_of_stock:
            st.markdown(f"""
            <div class="card-box" style="border-left: 4px solid #f44336;">
                <b style="font-size:16px;">{item['BRAND']} {item['SIZE']}</b> — Stock Qty: <span style="color:#f44336; font-weight:bold;">{item['STOCK']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("All items have sufficient stock!")

# 5. STATUS STUDIO
with tabs[4]:
    st.subheader("STATUS STUDIO")
    st.write("Create branded WhatsApp-status posters & videos from your shop photos/clips.")
    
    st.radio("Format", ["Poster", "Status Video"], horizontal=True)
    st.radio("Source", ["AI-made", "My photo"], horizontal=True)
    
    st.file_uploader("Choose File", type=["jpg", "png", "mp4"])
    st.button("Take photo with camera 📷")
    
    st.markdown("---")
    st.write("### Design Customizations")
    st.selectbox("Text Position", ["Top", "Center", "Bottom"])
    st.text_input("Tyre Size (Optional)", placeholder="e.g. 165/80 R14")
    st.selectbox("New / Second-hand", ["New", "Second-Hand"])
    
    if st.button("✨ AI Auto-Design (from photo)"):
        st.success("Status poster generated successfully!")

# 6. PIGMI COLLECTION
with tabs[5]:
    tot_pigmi = sum(p['BALANCE'] for p in st.session_state.pigmi_data)
    st.subheader(f"🐷 PIGMI COLLECTION • Total balance: ₹{tot_pigmi:,.2f}")
    
    for idx, p in enumerate(st.session_state.pigmi_data):
        st.markdown(f"""
        <div class="card-box">
            <h3 style="margin:0; color:#4CAF50;">{p['NAME']}</h3>
            <p style="color:#aaa; font-size:13px; margin:2px 0;">{p['LOCATION']} • {p['PHONE']}</p>
            <p style="color:#ff9800; font-size:13px; margin-bottom:10px;">🏛️ <b>{p['BANK']}</b> | A/C: {p['AC_NO']}</p>
            <p style="font-size:14px;">
                Old Balance: <b>₹{p['OLD_BAL']}</b> | Collected: <b style="color:#4CAF50;">₹{p['COLLECTED']}</b> | Withdrawn: <b style="color:#f44336;">₹{p['WITHDRAWN']}</b> | <b>Balance: ₹{p['BALANCE']}</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button(f"📥 Collect (A/C: {p['AC_NO']})", key=f"col_{idx}"):
                st.session_state.pigmi_data[idx]['COLLECTED'] += 500
                st.session_state.pigmi_data[idx]['BALANCE'] += 500
                st.rerun()
        with c2:
            if st.button(f"📤 Withdraw (A/C: {p['AC_NO']})", key=f"wit_{idx}"):
                st.session_state.pigmi_data[idx]['WITHDRAWN'] += 500
                st.session_state.pigmi_data[idx]['BALANCE'] -= 500
                st.rerun()

# 7. BILLING
with tabs[6]:
    st.subheader(f"BILLING ({len(st.session_state.billing_data)})")
    
    if st.button("➕ Create Bill"):
        new_no = f"CTS-{1177 + len(st.session_state.billing_data)}"
        st.session_state.billing_data.insert(0, {"BILL_NO": new_no, "TYPE": "Counter Sale", "SERVICE": "Puncture-Service", "AMOUNT": 250})
        st.rerun()

    for b in st.session_state.billing_data:
        st.markdown(f"""
        <div class="card-box" style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <b style="color:#ff9800; font-size:16px;">{b['BILL_NO']}</b><br>
                <b style="font-size:18px;">{b['TYPE']}</b><br>
                <span style="color:#aaa; font-size:13px;">{b['SERVICE']}</span>
                <h2 style="color:#4CAF50; margin:5px 0 0 0;">₹{b['AMOUNT']}</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 8. PAYMENTS
with tabs[7]:
    st.subheader("PAYMENTS")
    st.caption("Cash and digital (UPI/GPay/PhonePe) collections, separated. Mark each digital bill paid once the money reaches your bank.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card-box">
            <span style="color:#aaa;">💵 CASH TODAY</span>
            <h2 style="color:#4CAF50; margin:5px 0;">₹ 0</h2>
            <span style="color:#888; font-size:12px;">in hand</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card-box">
            <span style="color:#aaa;">💵 CASH THIS MONTH</span>
            <h2 style="color:#fff; margin:5px 0;">₹ 51,449</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card-box">
            <span style="color:#aaa;">📱 DIGITAL TODAY</span>
            <h2 style="color:#4CAF50; margin:5px 0;">₹ 0</h2>
            <span style="color:#888; font-size:12px;">to bank account</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card-box">
            <span style="color:#aaa;">📱 DIGITAL THIS MONTH</span>
            <h2 style="color:#fff; margin:5px 0;">₹ 66,139</h2>
        </div>
        """, unsafe_allow_html=True)

# 9. EXPENSES
with tabs[8]:
    tot_exp = sum(e['AMOUNT'] for e in st.session_state.expenses_data)
    st.subheader(f"EXPENSES • Total: ₹{tot_exp:,.2f}")
    
    with st.expander("➕ ADD EXPENSE"):
        with st.form("add_exp_form"):
            cat = st.selectbox("CATEGORY", ["Room Rent", "Electricity", "Salary", "Goods Purchase", "Welding", "Machine Repair", "Shop Setup", "Tea/Food", "Transport", "Other"])
            amt = st.number_input("AMOUNT (₹)", min_value=0, step=100)
            if st.form_submit_button("Save Expense 💾"):
                st.session_state.expenses_data.append({"CATEGORY": cat, "AMOUNT": amt})
                st.success("✅ Expense saved!")
                st.rerun()

    df_exp = pd.DataFrame(st.session_state.expenses_data)
    st.dataframe(df_exp, use_container_width=True)

# 10. SUPPLIERS
with tabs[9]:
    st.subheader("🚚 SUPPLIERS / INWARD")
    st.info("Manage suppliers and inward stock entries here.")

# 11. GUARANTEE / CLAIMS
with tabs[10]:
    st.subheader("🛡️ GUARANTEE / CLAIMS")
    st.info("Track warranty and replacement claims here.")

# 12. DEALERS DIRECTORY
with tabs[11]:
    st.subheader("📖 DEALERS DIRECTORY")
    st.info("Contact info for tyre suppliers and dealers.")
