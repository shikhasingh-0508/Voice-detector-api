import base64
import requests
import json

# --- CONFIGURATION ---
URL = "http://127.0.0.1:8000/api/voice-detection"
API_KEY = "sk_test_123456789"
FILE_NAME = "sample voice 1.mp3"  # Ensure this file is in your folder
LANGUAGE = "English"

def run_detection():
    try:
        # 1. Automatic Conversion [cite: 15, 25]
        with open(FILE_NAME, "rb") as audio_file:
            encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')

        # 2. Prepare the Payload [cite: 42-44, 48-53]
        payload = {
            "language": LANGUAGE,
            "audioFormat": "mp3",
            "audioBase64": encoded_string
        }
        headers = {
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        }

        # 3. Direct API Call [cite: 33-39]
        print(f"🚀 Sending '{FILE_NAME}' to API for analysis...")
        response = requests.post(URL, json=payload, headers=headers)

        # 4. Display the Output [cite: 56-62, 91]
        if response.status_code == 200:
            result = response.json()
            print("\n--- ANALYSIS RESULT ---")
            print(json.dumps(result, indent=4))
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)

    except FileNotFoundError:
        print(f"❌ Error: Could not find '{FILE_NAME}'.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    run_detection()