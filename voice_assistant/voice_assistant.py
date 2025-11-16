import pyttsx3
import requests
import json

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.api_base = 'http://localhost:5000'

    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Simulate voice input for demo purposes"""
        # For demo, we'll use text input instead of speech recognition
        text = input("Voice input (type your command): ")
        print(f"You said: {text}")
        return text.lower()

    def process_command(self, command):
        """Process voice commands"""
        if 'reminder' in command or 'medicine' in command:
            self.handle_reminders()
        elif 'appointment' in command:
            self.handle_appointments()
        elif 'help' in command or 'emergency' in command:
            self.send_alert("Emergency help requested via voice assistant")
        elif 'status' in command:
            self.speak("System is running normally")
        else:
            self.speak("I'm sorry, I didn't understand that command.")

    def handle_reminders(self):
        """Get and announce reminders"""
        try:
            response = requests.get(f"{self.api_base}/reminders")
            reminders = response.json()
            if reminders:
                self.speak(f"You have {len(reminders)} reminders.")
                for reminder in reminders:
                    self.speak(f"Reminder: {reminder.get('message', '')}")
            else:
                self.speak("You have no pending reminders.")
        except:
            self.speak("Unable to fetch reminders.")

    def handle_appointments(self):
        """Get and announce appointments"""
        try:
            response = requests.get(f"{self.api_base}/appointments")
            appointments = response.json()
            if appointments:
                self.speak(f"You have {len(appointments)} appointments.")
                for appointment in appointments:
                    self.speak(f"Appointment: {appointment.get('title', '')} at {appointment.get('time', '')}")
            else:
                self.speak("You have no upcoming appointments.")
        except:
            self.speak("Unable to fetch appointments.")

    def send_alert(self, message):
        """Send emergency alert"""
        try:
            requests.post(f"{self.api_base}/alert", json={'message': message})
            self.speak("Alert sent to caregivers.")
        except:
            self.speak("Unable to send alert.")

    def run(self):
        """Main loop for voice assistant"""
        self.speak("Voice assistant activated. Say 'help' for commands.")
        while True:
            command = self.listen()
            if command:
                if 'stop' in command or 'quit' in command:
                    self.speak("Goodbye.")
                    break
                self.process_command(command)

if __name__ == '__main__':
    assistant = VoiceAssistant()
    assistant.run()import pyttsx3
import requests
import json

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.api_base = 'http://localhost:5000'

    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Simulate voice input for demo purposes"""
        # For demo, we'll use text input instead of speech recognition
        text = input("Voice input (type your command): ")
        print(f"You said: {text}")
        return text.lower()

    def process_command(self, command):
        """Process voice commands"""
        if 'reminder' in command or 'medicine' in command:
            self.handle_reminders()
        elif 'appointment' in command:
            self.handle_appointments()
        elif 'help' in command or 'emergency' in command:
            self.send_alert("Emergency help requested via voice assistant")
        elif 'status' in command:
            self.speak("System is running normally")
        else:
            self.speak("I'm sorry, I didn't understand that command.")

    def handle_reminders(self):
        """Get and announce reminders"""
        try:
            response = requests.get(f"{self.api_base}/reminders")
            reminders = response.json()
            if reminders:
                self.speak(f"You have {len(reminders)} reminders.")
                for reminder in reminders:
                    self.speak(f"Reminder: {reminder.get('message', '')}")
            else:
                self.speak("You have no pending reminders.")
        except:
            self.speak("Unable to fetch reminders.")

    def handle_appointments(self):
        """Get and announce appointments"""
        try:
            response = requests.get(f"{self.api_base}/appointments")
            appointments = response.json()
            if appointments:
                self.speak(f"You have {len(appointments)} appointments.")
                for appointment in appointments:
                    self.speak(f"Appointment: {appointment.get('title', '')} at {appointment.get('time', '')}")
            else:
                self.speak("You have no upcoming appointments.")
        except:
            self.speak("Unable to fetch appointments.")

    def send_alert(self, message):
        """Send emergency alert"""
        try:
            requests.post(f"{self.api_base}/alert", json={'message': message})
            self.speak("Alert sent to caregivers.")
        except:
            self.speak("Unable to send alert.")

    def run(self):
        """Main loop for voice assistant"""
        self.speak("Voice assistant activated. Say 'help' for commands.")
        while True:
            command = self.listen()
            if command:
                if 'stop' in command or 'quit' in command:
                    self.speak("Goodbye.")
                    break
                self.process_command(command)

if __name__ == '__main__':
    assistant = VoiceAssistant()
    assistant.run()
