import streamlit as st
import pandas as pd

# Title
st.title("Smart Waste Management System")

# Load the CSV file
data = pd.read_csv("sample_data.csv")

# Display the table
st.subheader("Waste Data from CSV")
st.write(data)

# Create a bar chart
st.subheader("Waste Segregation Chart")
st.bar_chart(data.set_index("Category"))

