from flask import Flask, request, jsonify, render_template
from bins import hazardous, recyclable, organic

import os
from datetime import datetime
import random  # For mock classification

app = Flask(__name__)
user_points = {}

# Mock classifier
def classify_waste(image_path):
    return random.choice(['hazardous','recyclable','organic'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_waste():
    if 'waste_image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['waste_image']
    user_id = request.form.get('user_id', 'anonymous')
    
    os.makedirs("uploads", exist_ok=True)
    filename = f"uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    file.save(filename)
    
    category = classify_waste(filename)
    
    # Call the correct module
    if category == 'hazardous':
        fill, points = hazardous.add_waste(user_points, user_id)
    elif category == 'recyclable':
        fill, points = recyclable.add_waste(user_points, user_id)
    elif category == 'organic':
        fill, points = organic.add_waste(user_points, user_id)
   
    return jsonify({
        "category": category,
        "bin_fill_percent": fill,
        "user_points": points
    })

if __name__ == '__main__':
    app.run(debug=True)
