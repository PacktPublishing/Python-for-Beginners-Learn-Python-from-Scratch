"""

json.loads(jsonstring) - process jsonstring to Python type

json.load(filePointer) - loads json from a file
                        and returns as a result of method Python type

"""

import json

film = {
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

encodedRetrievedMovie = '{"title": "But I won\'t do it!!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedMovie = json.loads(encodedRetrievedMovie)

with open("sample.json", encoding="UTF-8") as file:
    result = json.load(file)

