import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# URL der Testumgebung
url = "https://maschinenraum.atlassian.net/wiki/api/v2/pages/426182"
# E-Mail eines Atlassian Users, der für die Testumgebung registriert ist
user_email = "fabiokeller@bluewin.ch"
# API Key des Users als "Passwortersatz"
api_key = os.getenv("API_KEY")

auth = HTTPBasicAuth(user_email, api_key)

headers = {"Accept": "application/json"}

# Add "expand" parameter to expand "body.storage" property
params = {"expand": "body.storage"}

response = requests.get(url, headers=headers, auth=auth, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Get the HTML content from the response
html_content = data["body"]["storage"]["value"]

# Save the HTML content to a file
with open("confluence.html", "w", encoding='utf-8') as file:
    file.write(html_content)
