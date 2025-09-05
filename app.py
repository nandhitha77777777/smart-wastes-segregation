import streamlit as st
import pandas as pd

# Title
st.title("♻️ Smart Waste Segregation & Recycling System")

# --- Default Waste Data ---
default_data = pd.DataFrame({
    "Category": ["Organic", "Recyclable", "Hazardous"],
    "Amount": [50, 30, 20]
})

# --- Sidebar Menu ---
menu = ["Home", "Manual Data Entry", "Municipal Dashboard", "Help"]
choice = st.sidebar.selectbox("Select an option", menu)

# --- Home Page ---
if choice == "Home":
    st.header("🏠 Waste Data Overview")

    st.subheader("Current Waste Data")
    st.write(default_data)

    st.subheader("Waste Segregation Chart")
    st.bar_chart(default_data.set_index("Category"))

# --- Manual Data Entry Page ---
elif choice == "Manual Data Entry":
    st.header("✏️ Enter Waste Data Manually")

    st.write("Update the values below to simulate new waste collection data:")

    organic = st.number_input("Organic Waste", min_value=0, value=50)
    recyclable = st.number_input("Recyclable Waste", min_value=0, value=30)
    hazardous = st.number_input("Hazardous Waste", min_value=0, value=20)

    if st.button("Update Data"):
        updated_data = pd.DataFrame({
            "Category": ["Organic", "Recyclable", "Hazardous"],
            "Amount": [organic, recyclable, hazardous]
        })
        st.success("Data updated successfully!")
        st.write(updated_data)
        st.bar_chart(updated_data.set_index("Category"))

# --- Municipal Dashboard ---
elif choice == "Municipal Dashboard":
    st.header("🏙 Municipal Waste Dashboard")
    st.write("This map shows simulated waste collection points in the city.")

    st.map(pd.DataFrame({
        'lat': [12.9716, 12.9720, 12.9750],
        'lon': [77.5946, 77.6000, 77.5980],
    }))

    st.write("Green dots represent waste collection locations.")

# --- Help Page ---
elif choice == "Help":
    st.header("ℹ️ Help & Instructions")
    st.markdown("""
    ### How to Use This App:
    1. Go to **Home** to view default waste data.
    2. Use **Manual Data Entry** to input waste data without a CSV.
    3. Go to **Municipal Dashboard** to view collection points on a map.
    4. No need to upload or download files — everything works instantly!
    """)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Smart Waste System Prototype | Built with Streamlit")


