import os
import json
import requests

# URL to retrieve data from

url = "http://192.168.180.53:3000/js/send.json"

# Retrieve data from the URL
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON data
    new_data = json.loads(response.content)
    # Create the directory if it doesn't exist
    directory = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Create the file if it doesn't exist
    file_path = os.path.join(directory, 'newdata.json')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('[]')
    # Load the existing data
    with open(file_path, 'r') as f:
        existing_data = json.load(f)
    # Update the count in the new data
    if len(existing_data) > 0:
        last_item = existing_data[-1]
        new_data[0]['count'] += last_item['count']
    # Append the new data to the existing data
    existing_data.extend(new_data)
    # Write the combined data back to the file
    with open(file_path, 'w') as f:
        json.dump(existing_data, f)
else:
    print(f"Error: Could not retrieve data from {url}. Status code: {response.status_code}")

