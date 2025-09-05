from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# Mock database for bin status and user points
bin_status = {
    "hazardous": 0,
    "recyclable": 0,
    "organic": 0
}

user_points = {}

# Threshold for bin notification
BIN_CAPACITY = 100  # assume 100 units max capacity
NOTIFY_THRESHOLD = 90  # percent

# Mock AI classification function (replace with your actual ML model)
def classify_waste(image_path):
    """
    Returns one of: 'hazardous', 'recyclable', 'organic'
    For demo purposes, it randomly chooses.
    """
    import random
    return random.choice(['hazardous', 'recyclable', 'organic'])

# Mock notification function
def notify_municipal(bin_type):
    print(f"[{datetime.now()}] Notification: {bin_type} bin is 90% full. Municipal team will collect.")

@app.route('/')
def index():
    return render_template('index.html')  # a simple HTML form to upload image

@app.route('/upload', methods=['POST'])
def upload_waste():
    if 'waste_image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['waste_image']
    user_id = request.form.get('user_id', 'anonymous')
    
    # Save image
    filename = f"uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    file.save(filename)
    
    # Classify waste
    category = classify_waste(filename)
    
    # Update bin status
    bin_status[category] += 10  # assume each waste increases bin by 10 units for demo
    
    # Update user points
    user_points[user_id] = user_points.get(user_id, 0) + 10  # 10 points per deposit
    
    # Check if bin is near full
    fill_percent = (bin_status[category] / BIN_CAPACITY) * 100
    if fill_percent >= NOTIFY_THRESHOLD:
        notify_municipal(category)
    
    return jsonify({
        "category": category,
        "bin_fill_percent": fill_percent,
        "user_points": user_points[user_id]
    })

if __name__ == '__main__':
    app.run(debug=True)



