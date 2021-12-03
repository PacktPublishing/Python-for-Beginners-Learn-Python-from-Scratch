import requests
import json
"""

API - Application Programming Interface

inter - between

ATM - cash machine

"""


response = requests.get("https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow")

try:
    answers = response.json()
except json.decoder.JSONDecodeError:
    print("The content is not JSON")
else:
     print(answers)
    

