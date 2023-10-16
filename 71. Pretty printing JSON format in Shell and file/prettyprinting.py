"""
pretty print (pprint)

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

encodedMovie = json.dumps(movie, ensure_ascii=False, indent=4, sort_keys=True)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(movie, file, ensure_ascii = False, indent=4, sort_keys=True)


with open("sample.json", encoding="UTF-8") as file:
    result = json.load(file)

print(json.dumps(result, indent=4, ensure_ascii=False, sort_keys=True))

import pprint

pprint.pprint(result)
