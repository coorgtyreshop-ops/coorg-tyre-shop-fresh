
import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration with Dark Theme feel
st.set_page_config(
    page_title="COORG TYRE SHOP",
    page_icon="🛞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session Data
if "tyre_stock" not in st.session_state:
    st.session_state.tyre_stock = [
        {"BRAND": "APOLLO", "SIZE": "90/100/10", "CONDITION": "New", "PATTERN": "53J GRIP", "STOCK": 1, "PURCHASE RATE": 1020, "SELLING RATE": 1450}
    ]

if "tube_stock" not in st.session_state:
    st.session_state.tube_stock = []

if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Styling
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
</style>
""", unsafe_allow_html=True)

# Top Banner
st.markdown("""
<div class="main-header">
    <div class="shop-title">🛞 COORG TYRE SHOP</div>
    <div class="shop-sub">Abyayath Mangala, Ontiyangadi, Main Road, Siddapura - 571253</div>
</div>
""", unsafe_allow_html=True)

# Top Navigation Tabs
tabs = st.tabs([
    "📈 Overview", 
    "🛞 Tyre Stock", 
    "🔘 Tube Stock", 
    "📋 Reorder / Low Stock", 
    "🎬 Status Studio", 
    "🚚 Suppliers / Inward", 
    "♻️ Retreading / Rebelting", 
    "📖 Dealers Directory", 
    "🐷 Pigmi Collection", 
    "🧾 Billing", 
    "🛡️ Guarantee / Claims", 
    "💳 Payments (Kadam)", 
    "💸 Expenses"
])

# 1. Overview
with tabs[0]:
    st.subheader("OVERVIEW • TODAY's SUMMARY")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Today's Sales", "₹ 0")
    col2.metric("Total Tyres Sold", "0 nos")
    col3.metric("Available Tyre Stock", f"{sum(item['STOCK'] for item in st.session_state.tyre_stock)} nos")
    col4.metric("Pending Balance", "₹ 0")

# 2. Tyre Stock Tab (Matches Photo)
with tabs[1]:
    st.subheader(f"TYRE STOCK ({len(st.session_state.tyre_stock)})")
    
    st.markdown("""
    <div class="warning-box">
        ⚠️ Innathe vila ithuvare vannittilla — Avasanam Online vila eduthathu: 22/10, 10:35 am - Ella divasavum ravile taniye puthukkum.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("➕ Add New Tyre Stock Entry"):
        with st.form("add_tyre_form"):
            c1, c2, c3, c4 = st.columns(4)
            brand = c1.text_input("Brand (e.g. APOLLO, JK TYRE)")
            size = c2.text_input("Size (e.g. 90/100/10)")
            condition = c3.selectbox("Condition", ["New", "Used", "Retread"])
            pattern = c4.text_input("Pattern (e.g. 53J GRIP)")
            
            c5, c6, c7 = st.columns(3)
            p_rate = c5.number_input("Purchase Rate (₹)", min_value=0, step=10)
            s_rate = c6.number_input("Selling Rate (₹)", min_value=0, step=10)
            qty = c7.number_input("Stock Qty", min_value=1, value=1)
            
            if st.form_submit_button("Save Tyre to Stock 📦"):
                st.session_state.tyre_stock.append({
                    "BRAND": brand.upper(), "SIZE": size, "CONDITION": condition,
                    "PATTERN": pattern, "STOCK": qty, "PURCHASE RATE": p_rate, "SELLING RATE": s_rate
                })
                st.success("✅ Tyre Stock Added!")

    search_tyre = st.text_input("🔍 Search size / brand (e.g. 165/80 or MRF)...", key="search_t")
    
    df_t = pd.DataFrame(st.session_state.tyre_stock)
    if not df_t.empty:
        if search_tyre:
            df_t = df_t[df_t['BRAND'].str.contains(search_tyre, case=False, na=False) | df_t['SIZE'].str.contains(search_tyre, case=False, na=False)]
        st.dataframe(df_t, use_container_width=True)

# 3. Tube Stock Tab
with tabs[2]:
    st.subheader(f"TUBE STOCK ({len(st.session_state.tube_stock)})")
    
    with st.expander("➕ Add New Tube Stock Entry"):
        with st.form("add_tube_form"):
            c1, c2, c3 = st.columns(3)
            t_brand = c1.text_input("Brand")
            t_size = c2.text_input("Size")
            t_qty = c3.number_input("Quantity", min_value=1, value=1)
            
            c4, c5 = st.columns(2)
            tp_rate = c4.number_input("Purchase Rate (₹)", min_value=0)
            ts_rate = c5.number_input("Selling Rate (₹)", min_value=0)
            
            if st.form_submit_button("Save Tube to Stock 🔘"):
                st.session_state.tube_stock.append({
                    "BRAND": t_brand.upper(), "SIZE": t_size, "STOCK": t_qty,
                    "PURCHASE RATE": tp_rate, "SELLING RATE": ts_rate
                })
                st.success("✅ Tube Stock Added!")

    search_tube = st.text_input("🔍 Search Tube size / brand...", key="search_tu")
    df_tu = pd.DataFrame(st.session_state.tube_stock)
    if not df_tu.empty:
        if search_tube:
            df_tu = df_tu[df_tu['BRAND'].str.contains(search_tube, case=False, na=False) | df_tu['SIZE'].str.contains(search_tube, case=False, na=False)]
        st.dataframe(df_tu, use_container_width=True)
    else:
        st.info("No tube stock records yet.")

# 4. Reorder / Low Stock Tab
with tabs[3]:
    st.subheader("📋 Reorder & Low Stock Alerts")
    st.warning("Low stock items (Qty < 2) will appear here for reordering.")

# 5. Status Studio Tab
with tabs[4]:
    st.subheader("🎬 Status Studio")
    st.write("Generate offer status images or promo text for WhatsApp & Instagram.")

# 6. Suppliers / Inward
with tabs[5]:
    st.subheader("🚚 Suppliers / Inward Bills")

# 7. Retreading / Rebelting
with tabs[6]:
    st.subheader("♻️ Retreading / Rebelting Tracking")

# 8. Dealers Directory
with tabs[7]:
    st.subheader("📖 Dealers Directory")

# 9. Pigmi Collection
with tabs[8]:
    st.subheader("🐷 Pigmi Collection Accounts")

# 10. Billing
with tabs[9]:
    st.subheader("🧾 Billing Generator")

# 11. Guarantee / Claims
with tabs[10]:
    st.subheader("🛡️ Guarantee & Claim Tracking")

# 12. Payments (Kadam)
with tabs[11]:
    st.subheader("💳 Customer Udhar / Check Kadam")

# 13. Expenses
with tabs[12]:
    st.subheader("💸 Daily Shop Expenses")
