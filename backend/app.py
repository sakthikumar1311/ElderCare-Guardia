from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Simple data storage (in production, use a database)
DATA_FILE = 'data/activities.json'
REMINDERS_FILE = 'data/reminders.json'
APPOINTMENTS_FILE = 'data/appointments.json'

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def save_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/activity', methods=['POST'])
def log_activity():
    data = request.json
    activities = load_data(DATA_FILE)
    activity = {
        'timestamp': datetime.now().isoformat(),
        'type': data.get('type'),
        'value': data.get('value')
    }
    activities.append(activity)
    save_data(DATA_FILE, activities)
    return jsonify({'status': 'Activity logged'}), 200

@app.route('/alert', methods=['POST'])
def send_alert():
    data = request.json
    # In production, send SMS/email alert
    print(f"ALERT: {data.get('message')}")
    return jsonify({'status': 'Alert sent'}), 200

@app.route('/reminders', methods=['GET'])
def get_reminders():
    reminders = load_data(REMINDERS_FILE)
    return jsonify(reminders), 200

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = load_data(APPOINTMENTS_FILE)
    return jsonify(appointments), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
