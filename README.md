# Email Notification Microservice
This microservice handles sending email notifications for different events and allows users to unsubscribe from receiving emails. It uses Flask and Flask-Mail for the implementation.

# Setup
For first time setup make sure to setup the Configuration for Flask Mail. Note for gmail, you will have to use an app-password instead of a regular password. After that you would run the microservice with python app.py.

# API Endpoints
# 1. Send Email
**Endpoint:** `/send_email`  
**Method:** `POST`  
**Description:** Sends an email based on the specified event.

# Request:
```
{
    "event": "Inactive",
    "email": "user1@example.com"
}
```

# Example Call:
```
import requests

url = 'http://127.0.0.1:5000/send_email'
data = {
    "event": "Inactive",
    "email": "user1@example.com"
}

response = requests.post(url, json=data)
print(response.json())
```

# Response:
```
{
    "message": "Email sent successfully"
}
```
# 2. Unsubscribe
**Endpoint:** /unsubscribe
**Method:** POST
**Description:** Unsubscribes a user from receiving further emails.

# Request:
```
{
    "email": "user1@example.com"
}
```
# Example Call:
```
import requests

url = 'http://127.0.0.1:5000/unsubscribe'
data = {
    "email": "user1@example.com"
}

response = requests.post(url, json=data)
print(response.json())
```
# Response:
```
{
    "message": "User unsubscribed successfully"
}
```
