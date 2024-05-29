import requests

# URL of the microservice
url = 'http://127.0.0.1:5000'

# Test data
email_data = {
    'Inactive': {'event': 'Inactive', 'email': 'user1@example.com'},
    'MissedTranscription': {'event': 'MissedTranscription', 'email': 'user2@example.com'},
    'Unsubscribe': {'email': 'user1@example.com'}
}

# Function to send a POST request and handle response
def send_post_request(endpoint, data):
    response = requests.post(f"{url}/{endpoint}", json=data)
    try:
        response_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Failed to decode JSON. Status code: {response.status_code}, 
              Response text: {response.text}")
        response_data = None
    return response_data

def sendEventEmail(eventName, email_data):
    response = send_post_request("send_email", email_data)
    print(f"{eventName} response: {response}")

def main():
    print("Sending Missed Transcription event email...")
    sendEventEmail("Missed Transcription", email_data['MissedTranscription'])

    print("Unsubscribing user1@example.com...")
    unsubscribe_response = send_post_request("unsubscribe", email_data['Unsubscribe'])
    print(f"Unsubscribe response: {unsubscribe_response}")

    print("Sending Inactive event email to unsubscribed user...")
    sendEventEmail("Inactive", email_data['Inactive'])

if __name__ == "__main__":
    main()
