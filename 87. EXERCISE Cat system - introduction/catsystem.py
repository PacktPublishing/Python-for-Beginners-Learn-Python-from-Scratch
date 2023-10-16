import requests
import json
import webbrowser
import settings

from pprint import pprint

headers = {
   "x-api-key" : settings.apiKey
         }
   

def get_json_content_from_response(response):
   try:
      content = response.json()
   except json.decoder.JSONDecodeError:
      print("Improper format", response.text)
   else:
      return content    
   
def get_favorite_cats(userId):
   params = {
        "sub_id"  : userId
      }
   r = requests.get('https://api.thecatapi.com/v1/favourites/', params,
                 headers=headers)
   
   return get_json_content_from_response(r)
    

def get_random_cat():
   
   r = requests.get('https://api.thecatapi.com/v1/images/search',
                 headers=headers)
   
   return get_json_content_from_response(r)[0]   
   

print("Hi, provide login and pw: ")
#checking whether the login and pw are correct
#assuming: loggin completed correctly
#we retrieve from database: userId and username for further reference

userId = "agh2m"
userName = "Arkadiusz"

print("Hi, " + userName)

favouriteCats = get_favorite_cats(userId)

print("Your favourite cats are: ", favouriteCats)

randomCat = get_random_cat()

print("Drawn kitten: ", randomCat["url"])













