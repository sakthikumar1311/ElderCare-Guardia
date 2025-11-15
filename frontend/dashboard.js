const API_BASE = 'http://localhost:5000';

async function fetchData(endpoint) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
}

async function updateDashboard() {
    // Update reminders
    const reminders = await fetchData('/reminders');
    const remindersList = document.getElementById('reminders-list');
    remindersList.innerHTML = reminders.map(r => `<li>${r.message || 'No message'}</li>`).join('');

    // Update appointments
    const appointments = await fetchData('/appointments');
    const appointmentsList = document.getElementById('appointments-list');
    appointmentsList.innerHTML = appointments.map(a => `<li>${a.title || 'No title'} - ${a.time || 'No time'}</li>`).join('');

    // Update activity status (simplified)
    const activityStatus = document.getElementById('activity-status');
    activityStatus.textContent = 'System Active';
    activityStatus.className = 'normal';

    // Update recent activities (would need to implement endpoint)
    const recentActivities = document.getElementById('recent-activities');
    recentActivities.innerHTML = '<li>Activity tracking active</li>';
}

async function sendTestAlert() {
    try {
        const response = await fetch(`${API_BASE}/alert`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: 'Test alert from dashboard'
            })
        });
        const result = await response.json();
        document.getElementById('alert-status').textContent = 'Test alert sent!';
        setTimeout(() => {
            document.getElementById('alert-status').textContent = '';
        }, 3000);
    } catch (error) {
        console.error('Error sending alert:', error);
        document.getElementById('alert-status').textContent = 'Failed to send alert';
    }
}

// Event listeners
document.getElementById('test-alert').addEventListener('click', sendTestAlert);

// Update dashboard every 30 seconds
updateDashboard();
setInterval(updateDashboard, 30000);

// Initial load
document.addEventListener('DOMContentLoaded', updateDashboard);
