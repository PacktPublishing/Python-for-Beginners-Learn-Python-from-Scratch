"""
JSONplaceholder

idTask
idUser
taskContent
completed

"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(response.text)
try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    print("THIS IS A PLACE WHERE YOU SHOULD PUT A CODE if everything went fine")
    print(tasks[0])
