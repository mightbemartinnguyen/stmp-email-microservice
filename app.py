from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import logging

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'  # Replace with your app password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# In-memory store for unsubscribed users
unsubscribed_users = set()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    app.logger.debug(f"Received data: {data}")
    event = data.get('event')
    email = data.get('email')

    if email in unsubscribed_users:
        return jsonify({'message': 'User has unsubscribed from emails'}), 200

    if event == 'Inactive':
        send_inactive_email(email)
    elif event == 'MissedTranscription':
        send_missed_transcription_email(email)

    return jsonify({'message': 'Email sent successfully'}), 200

def send_inactive_email(email):
    msg = Message('We Miss You!', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = 'It seems like you haven’t used our application in a while.\
                We miss you! Click here to unsubscribe.'
    mail.send(msg)

def send_missed_transcription_email(email):
    msg = Message('You Have a Pending Transcription', 
                  sender=app.config['MAIL_USERNAME'], 
                  recipients=[email])
    msg.body = 'You have a transcription that you haven’t viewed yet. \
                Don’t miss out! Click here to unsubscribe.'
    mail.send(msg) 

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.get_json()
    app.logger.debug(f"Unsubscribe data: {data}")
    email = data.get('email')
    unsubscribed_users.add(email)
    return jsonify({'message': 'User unsubscribed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
