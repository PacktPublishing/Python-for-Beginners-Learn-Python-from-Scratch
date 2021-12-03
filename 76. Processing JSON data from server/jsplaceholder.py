"""
Our JSON data looks like that:
idTask
idUser
taskContent
completed


idUser when
completed == "true"

and save each occurence/appearance/manifestation in format:

{
   1 : 11
   2 : 8
   3 : 5

   #and so on   
}

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
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1

    usersIdWithMaxCompletedAmountOfTasks = []
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUser.items():        
        maxAmountOfCompletedTasks = max(completedTasksFrequencyByUser.values())
        if (numberOfCompletedTasks == maxAmountOfCompletedTasks):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    print("Cookies for: ", usersIdWithMaxCompletedAmountOfTasks)
        
