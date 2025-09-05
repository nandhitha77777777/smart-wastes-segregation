import streamlit as st
import pandas as pd

# Title
st.title("Smart Waste Management System")

# Sidebar Navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Household Dashboard", "Municipal Dashboard"])

# Home Page
if page == "Home":
    st.write("Welcome to the Smart Waste Management System!")
    st.write("Navigate using the sidebar to explore other sections.")

# Household Dashboard
elif page == "Household Dashboard":
    st.subheader("Waste Segregation Data")
    data = pd.DataFrame({
        'Category': ['Organic', 'Recyclable', 'Hazardous'],
        'Amount': [50, 30, 20]
    })
    st.bar_chart(data.set_index('Category'))
    st.write("Track your recycling habits here!")

# Municipal Dashboard
elif page == "Municipal Dashboard":
    st.subheader("Municipal Waste Tracking")
    st.write("This page is for city authorities to monitor collection.")
    st.map(pd.DataFrame({
        'lat': [12.9716, 12.9721],
        'lon': [77.5946, 77.5952]
    }))

