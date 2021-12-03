import requests
import json
import webbrowser
from pprint import pprint

params = {
    "amount": 5
      
    }

response = requests.get("https://cat-fact.herokuapp.com/facts/random/",
                        params)

try:
    content = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    for cat in content:
        print(cat["text"])
    

