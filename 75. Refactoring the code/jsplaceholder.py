"""
Refactoring code - changing your code so it doesn't change its behaviour
(the things that it does).

Why do it then?

Do it so it's easier to maintain


"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(response.text)

def count_completed_task_frequency(tasks):
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1
    return completedTasksFrequencyByUser

def get_users_with_top_completed_tasks(completedTasksFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTasks = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUser.items():   
       if (numberOfCompletedTasks == maxAmountOfCompletedTasks):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
            
    return usersIdWithMaxCompletedAmountOfTasks

def get_keys_with_top_values(my_dict):
    return [key
    for key, value in my_dict.items()
    if (value == max(my_dict.values()))
    ]

try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    completedTasksFrequencyByUser = count_completed_task_frequency(tasks)
    usersIdWithMaxCompletedAmountOfTasks = get_users_with_top_completed_tasks(completedTasksFrequencyByUser)

    print("Cookies for:", usersIdWithMaxCompletedAmountOfTasks)


        
