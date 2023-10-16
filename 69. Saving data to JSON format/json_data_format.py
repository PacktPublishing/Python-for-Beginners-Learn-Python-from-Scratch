"""

json.dumps(data) - saves data in String format to JSON
json.dump(data, nameOfFileHandler, ensure_ascii=False) -
                               saves data to nameOfFileHandler in JSON format

dump means drop, throw away, ditch
"""

import json

movie = {
    "title" : "But I won't do it!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedMovie = json.dumps(movie, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(movie, file, ensure_ascii = False)
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

