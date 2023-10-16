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
#solution 3
def change_list_into_conj_of_params(my_list, key="id"):
    conjuction_params_string = key + "="

    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conjuction_params_string += str(item)
        else:
            conjuction_params_string += str(item) + "&" + key + "="

    return conjuction_params_string

conj_params = change_list_into_conj_of_params(usersIdWithMaxCompletedAmountOfTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_params)
users = r.json()

for user in users:
    print("HEY COOKIE FOR YOU: " + user["name"])


