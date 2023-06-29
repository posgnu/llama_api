import requests

# Define the URL of the API server
url = 'http://localhost:8000/'  # Replace with the actual server URL

# Define the JSON payload
payload = {
    'prompt': 'Hello'
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was unsuccessful
    print(f"Request failed with status code {response.status_code}")