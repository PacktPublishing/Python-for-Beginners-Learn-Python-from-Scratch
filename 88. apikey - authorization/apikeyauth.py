import requests
import json
import webbrowser
from pprint import pprint
"""
authorization
"""
params = {
    "api_key" : "yourkeygoeshere",
    "year" : 2019,
    "country" : "gb",
    "month" : 12,
    "type" : "national"
    }

response = requests.get("https://calendarific.com/api/v2/holidays/",
                        params)

try:
    content = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    pprint(content)
    

