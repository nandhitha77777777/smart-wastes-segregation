from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime
import random  # For mock classification

app = Flask(__name__)

# Define all bins with capacity, fill, and points per deposit
bins = {
    "hazardous": {"fill": 0, "capacity": 100, "points": 10},
    "recyclable": {"fill": 0, "capacity": 100, "points": 5},
    "organic": {"fill": 0, "capacity": 100, "points": 3},
    "ewaste": {"fill": 0, "capacity": 50, "points": 15},
    "compostable": {"fill": 0, "capacity": 120, "points": 2},
    "glass": {"fill": 0, "capacity": 100, "points": 5},
    "plastic": {"fill": 0, "capacity": 100, "points": 5},
    "metal": {"fill": 0, "capacity": 100, "points": 7},
    "paper": {"fill": 0, "capacity": 100, "points": 4},
    "textile": {"fill": 0, "capacity": 100, "points": 6}
}

user_points = {}
NOTIFY_THRESHOLD = 90  # percent

# Mock classifier
def classify_waste(image_path):
    return random.choice(list(bins.keys()))

# Notification
def notify_municipal(bin_type):
    print(f"[{datetime.now()}] {bin_type.capitalize()} bin is 90% full. Municipal team notified!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_waste():
    if 'waste_image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['waste_image']
    user_id = request.form.get('user_id', 'anonymous')
    
    # Save image
    os.makedirs("uploads", exist_ok=True)
    filename = f"uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    file.save(filename)
    
    # Classify
    category = classify_waste(filename)
    
    # Update bin and user points
    bin_info = bins[category]
    bin_info['fill'] += 10  # amount per waste
    user_points[user_id] = user_points.get(user_id, 0) + bin_info['points']
    
    fill_percent = (bin_info['fill'] / bin_info['capacity']) * 100
    if fill_percent >= NOTIFY_THRESHOLD:
        notify_municipal(category)
    
    return jsonify({
        "category": category,
        "bin_fill_percent": fill_percent,
        "user_points": user_points[user_id]
    })

if __name__ == '__main__':
    app.run(debug=True)

