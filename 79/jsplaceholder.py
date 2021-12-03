import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

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

try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
    completedTasksFrequencyByUser = count_completed_task_frequency(tasks)
    usersIdWithMaxCompletedAmountOfTasks = get_users_with_top_completed_tasks(completedTasksFrequencyByUser)




#solution 1
"""
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if (user["id"] in usersIdWithMaxCompletedAmountOfTasks):
        print("Cookie for:", user["name"])
        usersIdWithMaxCompletedAmountOfTasks.remove(user["id"])
"""
#solution 2
"""
for userId in usersIdWithMaxCompletedAmountOfTasks:    
    r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    user = r.json()
    print(user["name"])
"""
