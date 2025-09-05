import streamlit as st
import os
from datetime import datetime
import random

# ==========================
# Define bins and user points
# ==========================
bins = {
    "hazardous": {"fill": 0, "capacity": 100, "points": 10},
    "recyclable": {"fill": 0, "capacity": 100, "points": 5},
    "organic": {"fill": 0, "capacity": 100, "points": 3}
}

user_points = {}
NOTIFY_THRESHOLD = 90  # percent

# ==========================
# Mock classifier
# ==========================
def classify_waste(image_path):
    """Randomly assign a category (replace with AI model later)."""
    return random.choice(list(bins.keys()))

# ==========================
# Notification
# ==========================
def notify_municipal(bin_type):
    st.warning(f"{bin_type.capitalize()} bin is 90% full! Municipal team notified!")

# ==========================
# Add waste to bin
# ==========================
def add_waste(user_id, category, amount=10):
    bin_info = bins[category]
    bin_info['fill'] += amount
    user_points[user_id] = user_points.get(user_id, 0) + bin_info['points']

    fill_percent = (bin_info['fill'] / bin_info['capacity']) * 100
    if fill_percent >= NOTIFY_THRESHOLD:
        notify_municipal(category)
    return fill_percent, user_points[user_id]

# ==========================
# Streamlit App
# ==========================
st.title("Smart Waste Segregation System")
st.write("Categories: Hazardous, Recyclable, Organic")

# User ID input
user_id = st.text_input("Enter your User ID:")

# File uploader
uploaded_file = st.file_uploader("Upload an image of the waste:", type=["jpg", "png", "jpeg"])

if uploaded_file and user_id:
    # Save the uploaded image temporarily
    os.makedirs("uploads", exist_ok=True)
    filename = f"uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}_{uploaded_file.name}"
    with open(filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Classify waste
    category = classify_waste(filename)
    fill_percent, points = add_waste(user_id, category)

    st.success(f"Waste classified as: **{category.capitalize()}**")
    st.info(f"Bin fill: {fill_percent:.1f}%")
    st.info(f"{user_id}'s points: {points}")

# Display all bins with progress bars
st.subheader("Bin Status")
for name, info in bins.items():
    st.write(f"{name.capitalize()} ({info['fill']}/{info['capacity']})")
    st.progress(min(info['fill']/info['capacity'],1.0))


