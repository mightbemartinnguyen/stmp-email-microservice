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
        print(f"Failed to decode JSON. Status code: {response.status_code}, Response text: {response.text}")
        response_data = None
    return response_data

def main():
    # Send Inactive event email
    print("Sending Inactive event email...")
    inactive_response = send_post_request("send_email", email_data['Inactive'])
    print(f"Inactive event response: {inactive_response}")

    # Send Missed Transcription event email
    print("Sending Missed Transcription event email...")
    missed_transcription_response = send_post_request("send_email", email_data['MissedTranscription'])
    print(f"Missed Transcription event response: {missed_transcription_response}")

    # Unsubscribe user
    print("Unsubscribing user1@example.com...")
    unsubscribe_response = send_post_request("unsubscribe", email_data['Unsubscribe'])
    print(f"Unsubscribe response: {unsubscribe_response}")

    # Try sending Inactive event email to unsubscribed user
    print("Sending Inactive event email to unsubscribed user...")
    inactive_response_after_unsubscribe = send_post_request("send_email", email_data['Inactive'])
    print(f"Inactive event response after unsubscribe: {inactive_response_after_unsubscribe}")

if __name__ == "__main__":
    main()
