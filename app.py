import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration
st.set_page_config(page_title="Coorg Tyre Shop", page_icon="🛞", layout="wide")

st.title("🛞 Coorg Tyre Shop - Management System")

# Clean Single Sidebar Menu
menu = st.sidebar.selectbox(
    "📌 Select Menu",
    [
        "📊 Overview & Dashboard",
        "🛞 Stock & Sales Management",
        "♻️ Re-sole (Retread) Tyres",
        "💰 Pigmi Accounts (4 ACs)",
        "🧾 Customer Bill & Print",
        "💸 Daily Expenses / Chelavukal",
        "💸 Check Kadam (Credit/Udhar)",
        "🔧 Tube, Lock & Puncture Service",
        "📓 Quick Notepad & Calculator",
        "💬 WhatsApp Integration",
        "📱 Installing App Guide"
    ]
)

# 1. Overview & Dashboard
if menu == "📊 Overview & Dashboard":
    st.header("📊 Shop Overview & Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Today's Sales", "₹ 0")
    col2.metric("Monthly Total", "₹ 0")
    col3.metric("Total Stock Items", "0")
    col4.metric("Pending Kadam", "₹ 0")
    st.success("Welcome back! Coorg Tyre Shop system is running live.")

# 2. Stock Management (Auto Selling Price & Profit Calculation)
elif menu == "🛞 Stock & Sales Management":
    st.header("🛞 Tyre, Tube & Accessories Stock")
    
    with st.form("stock_form"):
        st.subheader("➕ Add New Stock Inward")
        col_a, col_b = st.columns(2)
        with col_a:
            s_category = st.selectbox("Category", ["Tyre", "Tube", "Flap", "Neck"])
            s_company = st.text_input("Company / Brand Name (e.g. JK Tyre)")
            s_size = st.text_input("Size / Model Details")
        with col_b:
            purchase_price = st.number_input("Vanna Vila / Purchase Rate (₹)", min_value=0.0, step=10.0)
            profit_pct = st.slider("Desired Profit Percentage (%)", min_value=0, max_value=50, value=15)
            qty = st.number_input("Quantity Received", min_value=1, value=1)
        
        # Automatic Selling Price Calculation
        auto_selling_price = purchase_price + (purchase_price * profit_pct / 100)
        
        st.markdown(f"### 💡 Calculated Selling Price: **₹ {auto_selling_price:.2f}** (Includes {profit_pct}% Profit)")
        
        submitted_stock = st.form_submit_button("Save Stock Item 📦")
        if submitted_stock:
            st.success(f"✅ Added {qty} nos of {s_company} {s_size} | Purchase: ₹{purchase_price} | Sell Rate: ₹{auto_selling_price:.2f}")

# 3. Re-sole Tyres
elif menu == "♻️ Re-sole (Retread) Tyres":
    st.header("♻️ Re-sole (Retread) Tyre Tracking")
    st.info("Track customer tyres sent for retreading, vehicle numbers, and status.")

# 4. Pigmi Accounts
elif menu == "💰 Pigmi Accounts (4 ACs)":
    st.header("💰 Pigmi Monitoring (4 Accounts)")
    st.write("Track daily/monthly Pigmi collections and account balances.")

# 5. Customer Bill & Print
elif menu == "🧾 Customer Bill & Print":
    st.header("🧾 Customer Bill Generator")
    
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("Customer Name")
        cust_phone = st.text_input("Phone Number")
    with col2:
        v_no = st.text_input("Vehicle Number")
        b_date = st.date_input("Bill Date", date.today())
        
    st.subheader("Items & Service Details")
    bill_items = st.text_area("Item Description (e.g. 2x JK Tyre 145/80 R12 + Service)")
    total_bill = st.number_input("Total Bill Amount (₹)", min_value=0, step=50)
    
    st.write("---")
    
    # Printable Bill View with Full Shop Address
    st.markdown("### 🖨️ Bill Preview / Print Copy")
    st.info("👇 ഈ ബിൽ പ്രിന്റ് ചെയ്യാൻ കീബോർഡിൽ **Ctrl + P** അമർത്തുക.")
    
    bill_box = f"""
    <div style="border: 2px solid #333; padding: 20px; border-radius: 10px; background-color: #ffffff; color: #000000; font-family: Arial, sans-serif;">
        <h2 style="text-align: center; margin-bottom: 2px; color: #d32f2f;">🛞 COORG TYRE SHOP</h2>
        <p style="text-align: center; margin-top: 0px; font-size: 13px; line-height: 1.4;">
            ONTIYANGADI, ABYATH MANGALA, MAIN ROAD, SIDDAPUR<br>
            PIN: 571253 | 📱 Mobile: 9900316275
        </p>
        <hr style="border: 1px solid #333;">
        <p style="font-size: 14px;"><strong>Date:</strong> {b_date}</p>
        <p style="font-size: 14px;"><strong>Customer Name:</strong> {cust_name} &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Phone:</strong> {cust_phone}</p>
        <p style="font-size: 14px;"><strong>Vehicle Number:</strong> {v_no}</p>
        <hr style="border: 1px dashed #ccc;">
        <p style="font-size: 14px;"><strong>Description / Particulars:</strong></p>
        <p style="background: #f9f9f9; padding: 12px; border: 1px solid #ddd; font-size: 15px;">{bill_items}</p>
        <h3 style="text-align: right; color: #1b5e20; margin-top: 15px;">Total Amount Paid: ₹ {total_bill}</h3>
        <hr style="border: 1px solid #333;">
        <p style="text-align: center; font-size: 12px; margin-bottom: 0;">Thank you for visiting Coorg Tyre Shop!</p>
    </div>
    """
    st.markdown(bill_box, unsafe_allow_html=True)

# 6. Daily Expenses
elif menu == "💸 Daily Expenses / Chelavukal":
    st.header("💸 Daily Shop Expenses / ചെലവുകൾ")
    st.write("Record daily shop operational expenses, electricity bills, rent, etc.")

# 7. Check Kadam
elif menu == "💸 Check Kadam (Credit/Udhar)":
    st.header("💸 Customer Credit / Udhar Tracking (ചെക്ക് കടം)")
    st.write("Track customer dues, pending balance, and payments.")

# 8. Tube, Lock & Puncture Service
elif menu == "🔧 Tube, Lock & Puncture Service":
    st.header("🔧 Puncture & Repair Service Logging")
    st.write("Log puncture works, tube replacements, and service charges.")

# 9. Quick Notepad & Calculator
elif menu == "📓 Quick Notepad & Calculator":
    st.header("📓 Quick Notes & Calculator")
    st.text_area("Write quick shop reminders:")
    val1 = st.number_input("Amount 1", value=0.0)
    val2 = st.number_input("Amount 2", value=0.0)
    st.write(f"**Total Addition:** ₹ {val1 + val2}")

# 10. WhatsApp Integration
elif menu == "💬 WhatsApp Integration":
    st.header("💬 WhatsApp Marketing & Offers")
    st.write("Send quick messages or offers to customers.")

# 11. App Installation Guide
elif menu == "📱 Installing App Guide":
    st.header("📱 How to Install as Mobile App")
    st.markdown("""
    * **Android:** Open Chrome -> Click 3 dots -> **Add to Home screen**.
    * **Chromebook / PC:** Click menu -> **Cast, save and share** -> **Create shortcut**.
    """)
# Page Configuration
st.set_page_config(page_title="Coorg Tyre Shop", page_icon="🛞", layout="wide")

st.title("🛞 Coorg Tyre Shop - Management System")
st.set_page_config(page_title="നിങ്ങളുടെ പുതിയ പേര്", page_icon="https://example.com/your-logo.png", layout="wide")
import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration
st.set_page_config(page_title="COORG TYRE SHOP", page_icon="🛞", layout="wide")

# Session State for Live Data Tracking (Stock & Sales)
if "stock_data" not in st.session_state:
    st.session_state.stock_data = []

if "sales_data" not in st.session_state:
    st.session_state.sales_data = []

st.title("🛞 COORG TYRE SHOP - Management System")

# Clean Single Sidebar Menu
menu = st.sidebar.selectbox(
    "📌 Select Menu",
    [
        "📊 Overview & Dashboard",
        "🛞 Stock & Sales Management",
        "🧾 Customer Bill & Print",
        "♻️ Re-sole (Retread) Tyres",
        "💰 Pigmi Accounts (4 ACs)",
        "💸 Daily Expenses / Chelavukal",
        "💸 Check Kadam (Credit/Udhar)",
        "🔧 Tube, Lock & Puncture Service",
        "📓 Quick Notepad & Calculator",
        "📱 Installing App Guide"
    ]
)

# 1. Overview & Dashboard
if menu == "📊 Overview & Dashboard":
    st.header("📊 Live Dashboard & Summary")
    
    # Calculate Live Metrics
    total_stock_qty = sum(item["Quantity"] for item in st.session_state.stock_data)
    total_sold_qty = sum(item["Quantity Sold"] for item in st.session_state.sales_data)
    total_sales_amount = sum(item["Total Price"] for item in st.session_state.sales_data)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales Amount", f"₹ {total_sales_amount:,.2f}")
    col2.metric("Total Tyres Sold", f"{total_sold_qty} nos")
    col3.metric("Current Available Stock", f"{total_stock_qty} nos")
    col4.metric("Pending Kadam", "₹ 0")

    st.write("---")
    st.subheader("📦 Current Available Stock List")
    if st.session_state.stock_data:
        df_stock = pd.DataFrame(st.session_state.stock_data)
        st.dataframe(df_stock, use_container_width=True)
    else:
        st.info("No stock items added yet.")

    st.subheader("🛍️ Recent Sales History")
    if st.session_state.sales_data:
        df_sales = pd.DataFrame(st.session_state.sales_data)
        st.dataframe(df_sales, use_container_width=True)
    else:
        st.info("No sales recorded yet.")

# 2. Stock & Sales Management
elif menu == "🛞 Stock & Sales Management":
    st.header("🛞 Stock & Sales Entry")
    
    tab1, tab2 = st.tabs(["➕ Add Stock (ചേർക്കുക)", "🛒 Record Sale (വിൽപന)"])
    
    with tab1:
        with st.form("stock_form"):
            st.subheader("Add New Tyre / Item")
            col_a, col_b = st.columns(2)
            with col_a:
                s_category = st.selectbox("Category", ["Tyre", "Tube", "Flap", "Neck"])
                s_company = st.text_input("Brand / Company Name (e.g. JK Tyre)")
                s_size = st.text_input("Size / Model Details (e.g. 145/80 R12)")
            with col_b:
                purchase_price = st.number_input("Purchase Price (₹)", min_value=0.0, step=10.0)
                profit_pct = st.slider("Desired Profit Percentage (%)", min_value=0, max_value=50, value=15)
                qty = st.number_input("Quantity Received", min_value=1, value=1)
            
            auto_selling_price = purchase_price + (purchase_price * profit_pct / 100)
            st.markdown(f"### 💡 Selling Price per piece: **₹ {auto_selling_price:.2f}**")
            
            submitted_stock = st.form_submit_button("Save to Stock 📦")
            if submitted_stock:
                new_item = {
                    "Category": s_category,
                    "Company": s_company,
                    "Size": s_size,
                    "Purchase Price": purchase_price,
                    "Selling Price": auto_selling_price,
                    "Quantity": qty
                }
                st.session_state.stock_data.append(new_item)
                st.success(f"✅ Added {qty} nos of {s_company} {s_size} to Stock!")

    with tab2:
        st.subheader("Sell Item from Stock")
        if st.session_state.stock_data:
            stock_options = [f"{item['Company']} {item['Size']} (Available: {item['Quantity']})" for item in st.session_state.stock_data if item['Quantity'] > 0]
            
            if stock_options:
                selected_stock = st.selectbox("Select Tyre / Item to Sell", stock_options)
                sell_qty = st.number_input("Selling Quantity", min_value=1, value=1)
                
                # Extract Index
                selected_index = stock_options.index(selected_stock)
                item_to_sell = st.session_state.stock_data[selected_index]
                
                if sell_qty > item_to_sell["Quantity"]:
                    st.error("❌ Not enough stock available!")
                else:
                    total_sell_price = item_to_sell["Selling Price"] * sell_qty
                    st.write(f"**Total Selling Amount:** ₹ {total_sell_price:.2f}")
                    
                    if st.button("Complete Sale 🛒"):
                        # Reduce Stock
                        item_to_sell["Quantity"] -= sell_qty
                        
                        # Add to Sales
                        sale_record = {
                            "Date": str(date.today()),
                            "Item": f"{item_to_sell['Company']} {item_to_sell['Size']}",
                            "Quantity Sold": sell_qty,
                            "Total Price": total_sell_price
                        }
                        st.session_state.sales_data.append(sale_record)
                        st.success("✅ Sale Recorded Successfully! Dashboard updated.")
            else:
                st.warning("No available items in stock to sell.")
        else:
            st.warning("Please add stock items first.")

# 3. Customer Bill & Print
elif menu == "🧾 Customer Bill & Print":
    st.header("🧾 Customer Bill Generator")
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("Customer Name")
        cust_phone = st.text_input("Phone Number")
    with col2:
        v_no = st.text_input("Vehicle Number")
        b_date = st.date_input("Bill Date", date.today())
        
    bill_items = st.text_area("Item Description (e.g. 2x JK Tyre 145/80 R12)")
    total_bill = st.number_input("Total Amount (₹)", min_value=0, step=50)
    
    st.markdown("### 🖨️ Bill Preview")
    bill_box = f"""
    <div style="border: 2px solid #333; padding: 20px; border-radius: 10px; background-color: #ffffff; color: #000000; font-family: Arial, sans-serif;">
        <h2 style="text-align: center; color: #d32f2f;">🛞 COORG TYRE SHOP</h2>
        <p style="text-align: center; font-size: 13px;">ONTIYANGADI, ABYATH MANGALA, SIDDAPUR | 📱 9900316275</p>
        <hr>
        <p><strong>Date:</strong> {b_date} | <strong>Customer:</strong> {cust_name} ({cust_phone})</p>
        <p><strong>Vehicle No:</strong> {v_no}</p>
        <p><strong>Particulars:</strong> {bill_items}</p>
        <h3 style="text-align: right; color: #1b5e20;">Total: ₹ {total_bill}</h3>
    </div>
    """
    st.markdown(bill_box, unsafe_allow_html=True)

# Other Menus Placeholder
elif menu == "♻️ Re-sole (Retread) Tyres":
    st.header("♻️ Re-sole (Retread) Tyre Tracking")
elif menu == "💰 Pigmi Accounts (4 ACs)":
    st.header("💰 Pigmi Monitoring")
elif menu == "💸 Daily Expenses / Chelavukal":
    st.header("💸 Daily Shop Expenses")
elif menu == "💸 Check Kadam (Credit/Udhar)":
    st.header("💸 Customer Credit / Udhar Tracking")
elif menu == "🔧 Tube, Lock & Puncture Service":
    st.header("🔧 Service Logging")
elif menu == "📓 Quick Notepad & Calculator":
    st.header("📓 Quick Notes")
elif menu == "📱 Installing App Guide":
    st.header("📱 App Installation Guide")
