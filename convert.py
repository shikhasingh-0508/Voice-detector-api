import base64
import os

# Ensure the file name matches your explorer exactly
input_file = "sample voice 1.mp3"

if os.path.exists(input_file):
    with open(input_file, "rb") as audio:
        encoded_string = base64.b64encode(audio.read()).decode('utf-8')
        with open("base64_text.txt", "w") as f:
            f.write(encoded_string)
    print("✅ Success! Open 'base64_text.txt' and copy the text.")
else:
    print(f"❌ Error: {input_file} not found. Please drag it into the folder.")