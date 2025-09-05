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
# Mock classifier function
# ==========================
def classify_waste(image_path):
    """
    Mock classifier: randomly assigns category.
    Replace with ML model logic if available.
    """
    return random.choice(list(bins.keys()))

# ==========================
# Notification function
# ==========================
def notify_municipal(bin_type):
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
          f"ALERT: {bin_type.capitalize()} bin is 90% full! Municipal team notified!\n")

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
# Show current bin status
# ==========================
def show_bins():
    print("\n--- Current Bin Status ---")
    for name, info in bins.items():
        bar_length = 30  # ASCII progress bar length
        filled_length = int(bar_length * info['fill'] / info['capacity'])
                            bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"{name.capitalize():12}: |{bar}| {info['fill']}/{info['capacity']} ({(info['fill']/info['capacity']*100):.1f}%)")
    print("---------------------------\n")

# ==========================
# Main Program Loop
# ==========================
def main():
    print("Welcome to the Smart Waste Segregation System (Terminal Version)")
    print("Categories: Hazardous, Recyclable, Organic\n")
    while True:
        user_id = input("Enter your User ID (or 'exit' to quit): ")
        if user_id.lower() == "exit":
            break

        image_path = input("Enter image file path: ")
        if not os.path.exists(image_path):
            print("File not found. Please try again.\n")
            continue

        # Classify the waste
        category = classify_waste(image_path)
        fill_percent, points = add_waste(user_id, category)

        print(f"\nWaste classified as: {category.capitalize()}")
        print(f"Bin fill: {fill_percent:.1f}%")
        print(f"{user_id}'s points: {points}")
        show_bins()
if __name__ == "__main__":
    main()

