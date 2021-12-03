import requests
import json
import webbrowser
import settings

from pprint import pprint

headers = {
   "x-api-key" : settings.apiKey
         }
   

r = requests.get('https://api.thecatapi.com/v1/favourites/',
                 headers=headers)


try:
   content = r.json()
except json.decoder.JSONDecodeError:
   print("Niepoprawny format", r.text)
else:
   print(content)

