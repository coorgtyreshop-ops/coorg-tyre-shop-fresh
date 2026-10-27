import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Coorg Tyre Shop Management",
    page_icon="🛞",
    layout="wide"
)

DATA_FILE = "coorg_tyre_data.json"

# Load Data
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {
        "tyre_stock": [],
        "tube_stock": [],
        "sales": [],
        "expenses": [],
        "credit": [],
        "pigmi": [],
        "retreading": []
    }

# Save Data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

if "data" not in st.session_state:
    st.session_state.data = load_data()

# App Title & Backup / Download Section
st.title("🛞 COORG TYRE SHOP MANAGEMENT")
st.markdown("---")

# Sidebar for Backup / Download / Upload
st.sidebar.header("📁 Data Backup & Restore")

# Download JSON Backup
data_str = json.dumps(st.session_state.data, indent=4)
st.sidebar.download_button(
    label="📥 Download Data Backup",
    data=data_str,
    file_name=f"coorg_tyre_backup_{datetime.now().strftime('%Y-%m-%d')}.json",
    mime="application/json"
)

# Upload JSON Restore
uploaded_file = st.sidebar.file_uploader("📤 Restore Data from Backup", type=["json"])
if uploaded_file is not None:
    try:
        restored_data = json.load(uploaded_file)
        st.session_state.data = restored_data
        save_data(restored_data)
        st.sidebar.success("Data restored successfully! Please refresh.")
    except Exception as e:
        st.sidebar.error(f"Error restoring file: {e}")

# Main Tabs
tabs = st.tabs([
    "📈 Overview", 
    "🛞 Tyre Stock", 
    "🔘 Tube Stock", 
    "🧾 Billing", 
    "🐷 Pigmi", 
    "📒 Credit", 
    "💸 Expenses", 
    "🔄 Retreading"
])

# 1. Overview Tab
with tabs[0]:
    st.header("இന്നത്തെ സംഗ്രഹം (Overview)")
    data = st.session_state.data
    
    total_sales = sum(item.get("total", 0) for item in data["sales"])
    total_expenses = sum(item.get("amount", 0) for item in data["expenses"])
    total_credit = sum(item.get("amount", 0) for item in data["credit"])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"₹ {total_sales}")
    col2.metric("Total Expenses", f"₹ {total_expenses}")
    col3.metric("Total Credit", f"₹ {total_credit}")

# 2. Tyre Stock Tab
with tabs[1]:
    st.header("Tyre Stock Management")
    with st.form("tyre_form"):
        brand = st.text_input("Tyre Brand")
        size = st.text_input("Tyre Size")
        price = st.number_input("Selling Price (₹)", min_value=0.0)
        qty = st.number_input("Quantity", min_value=1, step=1)
        submitted = st.form_submit_button("Add Tyre Stock")
        
        if submitted and brand and size:
            st.session_state.data["tyre_stock"].append({
                "brand": brand, "size": size, "price": price, "qty": qty
            })
            save_data(st.session_state.data)
            st.success("Tyre added successfully!")
            st.rerun()
            
    if st.session_state.data["tyre_stock"]:
        st.dataframe(pd.DataFrame(st.session_state.data["tyre_stock"]))

# 3. Tube Stock Tab
with tabs[2]:
    st.header("Tube Stock Management")
    with st.form("tube_form"):
        t_brand = st.text_input("Tube Brand/Size")
        t_price = st.number_input("Price (₹)", min_value=0.0, key="t_price")
        t_qty = st.number_input("Quantity", min_value=1, step=1, key="t_qty")
        t_submitted = st.form_submit_button("Add Tube Stock")
        
        if t_submitted and t_brand:
            st.session_state.data["tube_stock"].append({
                "brand": t_brand, "price": t_price, "qty": t_qty
            })
            save_data(st.session_state.data)
            st.success("Tube added successfully!")
            st.rerun()
            
    if st.session_state.data["tube_stock"]:
        st.dataframe(pd.DataFrame(st.session_state.data["tube_stock"]))

# 4. Billing Tab
with tabs[3]:
    st.header("Billing & Invoice")
    cust_name = st.text_input("Customer Name")
    veh_no = st.text_input("Vehicle Number")
    bill_amount = st.number_input("Bill Amount (₹)", min_value=0.0)
    
    if st.button("Save & Generate Bill"):
        if cust_name and bill_amount > 0:
            sale_record = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "customer": cust_name,
                "vehicle": veh_no,
                "total": bill_amount
            }
            st.session_state.data["sales"].append(sale_record)
            save_data(st.session_state.data)
            st.success("Bill saved successfully!")
        else:
            st.error("Please enter customer name and valid amount.")

# 5. Pigmi Tab
with tabs[4]:
    st.header("Pigmi Collection")
    p_name = st.text_input("Customer Name (Pigmi)")
    p_amt = st.number_input("Collection Amount (₹)", min_value=0.0)
    if st.button("Add Pigmi Collection"):
        if p_name:
            st.session_state.data["pigmi"].append({"name": p_name, "amount": p_amt, "date": datetime.now().strftime("%Y-%m-%d")})
            save_data(st.session_state.data)
            st.success("Pigmi saved!")

# 6. Credit Tab
with tabs[5]:
    st.header("Credit (കടം) Management")
    c_name = st.text_input("Customer Name (Credit)")
    c_amt = st.number_input("Credit Amount (₹)", min_value=0.0, key="c_amt")
    if st.button("Save Credit"):
        if c_name:
            st.session_state.data["credit"].append({"name": c_name, "amount": c_amt, "date": datetime.now().strftime("%Y-%m-%d")})
            save_data(st.session_state.data)
            st.success("Credit saved!")

# 7. Expenses Tab
with tabs[6]:
    st.header("Expenses Management")
    e_desc = st.text_input("Expense Description (Eg: Rent, Tea)")
    e_amt = st.number_input("Amount (₹)", min_value=0.0, key="e_amt")
    if st.button("Add Expense"):
        if e_desc:
            st.session_state.data["expenses"].append({"desc": e_desc, "amount": e_amt, "date": datetime.now().strftime("%Y-%m-%d")})
            save_data(st.session_state.data)
            st.success("Expense added!")

# 8. Retreading Tab
with tabs[7]:
    st.header("Retreading Management")
    r_name = st.text_input("Customer Name (Retreading)")
    r_details = st.text_input("Tyre Details")
    if st.button("Add Retreading"):
        if r_name:
            st.session_state.data["retreading"].append({"name": r_name, "details": r_details, "status": "Pending"})
            save_data(st.session_state.data)
            st.success("Retreading record saved!")
