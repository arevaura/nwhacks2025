import subprocess
import requests
import time
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Define the endpoint URL
endpoint = "http://0.0.0.0:3000/api/chatllm"  # Replace with your desired endpoint URL

while True:
    # Call the vtt.py script
    subprocess.run(["python", "vtt.py"])  # Replace "/path/to/vtt.py" with the actual path to vtt.py

    # Read the result from the output file generated by vtt.py
    with open("output.txt", "r") as file:  # Replace "/path/to/output.txt" with the actual path to the output file
        result = file.read()

    # Send the result in an API request
    payload = {
    "userId": "678c9d69e82af2068c95cac3",
    "message": result
    }
    response = requests.post(endpoint, json=payload)

    # Print the response status code
    print("API response:", response.status_code)

    # Speak the API response status code
    engine.say(f"API response: {response.status_code}")
    engine.runAndWait()

    # Wait for some time before running the script again
    time.sleep(5)  # Adjust the sleep duration as needed