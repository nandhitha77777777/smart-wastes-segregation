import streamlit as st

st.title("Smart Waste Management System")
st.write("Welcome to our municipal waste dashboard!")

st.subheader("Waste Segregation Data")
st.bar_chart({
    "Organic": [50],
    "Recyclable": [30],
    "Hazardous": [20]
})

st.subheader("Collection Updates")
st.write("Collection is on schedule for Sector 5 and Sector 8 today.")
