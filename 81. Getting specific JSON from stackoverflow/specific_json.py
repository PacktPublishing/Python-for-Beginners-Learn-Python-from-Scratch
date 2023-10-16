import requests
import json
import pprint
import webbrowser

"""

API - Application Programming Interface

Questions should follow below rules:
1) minimum 15 points (score)
2) sorted in descending order
3) from last week
4) from the Python category

"""
params = {
      "site": "stackoverflow",
      "sort": "votes",
      "min" : 15,
      "order" : "desc",
      "fromdate" : "2019-08-03",
      "tagged": "python"
      
      
    }

response = requests.get("https://api.stackexchange.com/2.2/questions", params)

try:
    questions = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
    

