import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# URL der Testumgebung
url = "https://maschinenraum.atlassian.net/wiki/api/v2/pages"
# E-Mail eines Atlassian Users, der für die Testumgebung registriert ist
user_email = "fabiokeller@bluewin.ch"
# API Key des Users als "Passwortersatz"
api_key = os.getenv("API_KEY")

auth = HTTPBasicAuth(user_email, api_key)
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Replace these values with your own
page_id = 426182
space_key = 425986  # Replace with your space key

# Load the confluence.html file
with open("confluence.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Edit the HTML content as needed
edited_html_content = html_content.replace("pencil", "pen")

payload = json.dumps( {
  "spaceId": space_key,
  "status": "current",
  "title": "Test page",
  "body": {
    "representation": "storage",
    "value": edited_html_content
  }
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))