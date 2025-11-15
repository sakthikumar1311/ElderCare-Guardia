import json
import os

class AnomalyDetector:
    def __init__(self):
        self.is_trained = False
        self.normal_patterns = {}

    def train(self, data):
        """Train the anomaly detection model with normal activity data"""
        if len(data) > 10:  # Need minimum data for training
            self.normal_patterns = self.extract_patterns(data)
            self.is_trained = True

    def detect_anomaly(self, activity_data):
        """Detect if the current activity is anomalous using simple rule-based detection"""
        if not self.is_trained:
            return False

        activity_type = activity_data.get('type', '')
        value = activity_data.get('value', 0)

        # Simple anomaly detection rules
        if activity_type in self.normal_patterns:
            avg_value = self.normal_patterns[activity_type]['avg']
            std_value = self.normal_patterns[activity_type]['std']
            # Flag as anomaly if value deviates by more than 2 standard deviations
            if abs(value - avg_value) > 2 * std_value:
                return True

        # Flag unknown activity types as anomalies
        if activity_type not in self.normal_patterns:
            return True

        return False

    def extract_patterns(self, activities):
        """Extract statistical patterns from activity data"""
        patterns = {}
        for activity in activities:
            activity_type = activity.get('type', '')
            value = activity.get('value', 0)

            if activity_type not in patterns:
                patterns[activity_type] = {'values': []}

            patterns[activity_type]['values'].append(value)

        # Calculate statistics
        for activity_type, data in patterns.items():
            values = data['values']
            if values:
                data['avg'] = sum(values) / len(values)
                data['std'] = (sum((x - data['avg']) ** 2 for x in values) / len(values)) ** 0.5
            else:
                data['avg'] = 0
                data['std'] = 0

        return patterns

def load_activities():
    """Load activities from data file"""
    file_path = 'data/activities.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

# Initialize detector
detector = AnomalyDetector()

def check_for_anomalies():
    """Check recent activities for anomalies"""
    activities = load_activities()
    if not activities:
        return []

    # Train on historical data
    detector.train(activities[:-1])  # Train on all but latest

    # Check latest activity
    latest = activities[-1]
    if detector.detect_anomaly(latest):
        return [latest]
    return []
