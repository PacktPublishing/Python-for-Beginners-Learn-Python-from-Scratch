import requests
import json
import webbrowser
from datetime import datetime, timedelta


"""
time stamp

1st 1970 - stamp time

"""
timeBefore = timedelta(days = 7)

searchDate = datetime.today() - timeBefore


params = {
      "site": "stackoverflow",
      "sort": "votes",
      "min" : 15,
      "order" : "desc",
      "fromdate" : int(searchDate.timestamp()),
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
    

