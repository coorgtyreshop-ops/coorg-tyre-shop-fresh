import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration with Dark Theme feel
st.set_page_config(
    page_title="COORG TYRE SHOP",
    page_icon="🛞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to match your layout design
st.markdown("""
<style>
    .main-header {
        background-color: #1a1c23;
        padding: 15px;
        border-radius: 8px;
        color: white;
        margin-bottom: 20px;
    }
    .shop-title {
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 1px;
    }
    .shop-sub {
        font-size: 13px;
        color: #a0a5b5;
    }
</style>
""", unsafe_allow_html=True)

# Top Header Banner
st.markdown("""
<div class="main-header">
    <div class="shop-title">🛞 COORG TYRE SHOP</div>
    <div class="shop-sub">Abyayath Mangala, Ontiyangadi, Main Road, Siddapura - 571253</div>
</div>
""", unsafe_allow_html=True)

st.title("DASHBOARD")
st.caption("COORG TYRE SHOP")

# Navigation Tabs matching your photo
tabs = st.tabs([
    "📈 Overview", 
    "🛞 Tyre Stock", 
    "🔘 Tube Stock", 
    "📋 Reorder / Low Stock", 
    "📉 Market Rates", 
    "🎬 Status Studio", 
    "🚚 Suppliers / Inward", 
    "♻️ Retreading / Rebelting", 
    "📖 Dealers Directory", 
    "🐷 Pigmi Collection", 
    "🧾 Billing", 
    "🛡️ Guarantee / Claims", 
    "💳 Payments", 
    "💸 Expenses"
])

# 1. Overview Tab
with tabs[0]:
    st.subheader("OVERVIEW • 0 BILLS TODAY")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Today's Sales", "₹ 0")
    col2.metric("Total Tyres Sold", "0 nos")
    col3.metric("Current Available Stock", "0 nos")
    col4.metric("Pending Balance", "₹ 0")

# 2. Tyre Stock Tab
with tabs[1]:
    st.subheader("🛞 Tyre Stock Management")
    st.info("Manage all tyre items, sizes, and quantities here.")

# 3. Tube Stock Tab
with tabs[2]:
    st.subheader("🔘 Tube Stock Management")
    st.info("Manage tube inventory and stocks.")

# 4. Reorder / Low Stock Tab
with tabs[3]:
    st.subheader("📋 Reorder & Low Stock Alerts")
    st.warning("Items below reorder level will be listed here.")

# 5. Market Rates Tab
with tabs[4]:
    st.subheader("📉 Market Rates Tracking")

# 6. Status Studio Tab
with tabs[5]:
    st.subheader("🎬 Status Studio")
    st.write("Generate WhatsApp & Instagram status content.")

# 7. Suppliers / Inward Tab
with tabs[6]:
    st.subheader("🚚 Suppliers / Inward Stock Entry")

# 8. Retreading / Rebelting Tab
with tabs[7]:
    st.subheader("♻️ Retreading / Rebelting Tracking")

# 9. Dealers Directory Tab
with tabs[8]:
    st.subheader("📖 Dealers Directory")

# 10. Pigmi Collection Tab
with tabs[9]:
    st.subheader("🐷 Pigmi Collection")

# 11. Billing Tab
with tabs[10]:
    st.subheader("🧾 Billing & Invoicing")

# 12. Guarantee / Claims Tab
with tabs[11]:
    st.subheader("🛡️ Guarantee / Warranty Claims")

# 13. Payments Tab
with tabs[12]:
    st.subheader("💳 Customer Payments & Credit (Kadam)")

# 14. Expenses Tab
with tabs[13]:
    st.subheader("💸 Shop Daily Expenses")
