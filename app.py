import streamlit as st
import pandas as pd
import os

# Title
st.title("♻️ Smart Waste Segregation & Recycling System")

# Check if the CSV file exists in the same folder
CSV_FILE = "sample_data.csv"

# --- Function to Load Data ---
def load_data():
    if os.path.exists(CSV_FILE):
        try:
            data = pd.read_csv(CSV_FILE)
            return data
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return None
    else:
        st.warning("No data found. Please upload a CSV file below.")
        return None

# --- Sidebar Menu ---
menu = ["Home", "Upload CSV", "Download Example", "Municipal Dashboard", "Help"]
choice = st.sidebar.selectbox("Select an option", menu)

# --- Home Page ---
if choice == "Home":
    st.header("🏠 Waste Data Overview")

    data = load_data()
    if data is not None:
        st.subheader("Current Waste Data")
        st.write(data)

        st.subheader("Waste Segregation Chart")
        st.bar_chart(data.set_index("Category"))
    else:
        st.info("Upload a CSV file to view waste data.")

# --- Upload CSV Page ---
elif choice == "Upload CSV":
    st.header("📤 Upload Your Waste Data CSV")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file:
        try:
            data = pd.read_csv(uploaded_file)
            data.to_csv(CSV_FILE, index=False)  # Save file to project folder
            st.success("File uploaded successfully! Go back to 'Home' to view data.")
            st.write(data)
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")

# --- Download Example CSV ---
elif choice == "Download Example":
    st.header("📥 Download Sample CSV")

    example_data = pd.DataFrame({
        "Category": ["Organic", "Recyclable", "Hazardous"],
        "Amount": [50, 30, 20]
    })

    st.write("Here is an example of what your CSV should look like:")
    st.write(example_data)

    csv = example_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Sample CSV",
        data=csv,
        file_name="sample_data.csv",
        mime="text/csv",
    )

# --- Municipal Dashboard ---
elif choice == "Municipal Dashboard":
    st.header("🏙 Municipal Waste Dashboard")
    st.write("This dashboard helps track collection across the city.")

    st.map(pd.DataFrame({
        'lat': [12.9716, 12.9720, 12.9750],
        'lon': [77.5946, 77.6000, 77.5980],
    }))

    st.write("Green dots represent waste collection points.")

# --- Help Page ---
elif choice == "Help":
    st.header("ℹ️ Help & Instructions")
    st.markdown("""
    ### How to Use This App:
    1. **Upload CSV** with waste data (Category and Amount).
    2. Go to **Home** to see data and charts.
    3. Download a sample CSV under **Download Example**.
    4. Use **Municipal Dashboard** to track collection points.
    5. Make sure your CSV file has exactly these columns:
       - `Category` (Organic, Recyclable, Hazardous)
       - `Amount` (numbers)
    """)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Smart Waste System Prototype | Built with Streamlit")
