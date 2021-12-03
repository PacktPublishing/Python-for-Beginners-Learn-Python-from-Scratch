"""
choice - chooses random element from the provided list,
         the probability of getting each element is equal

Python 3.6+:
choices - return list of random element/s from provided list
         allows to:
         - set probability using weighted average
         - set how many times we want to draw from provided list and
           return all results inside a single list

"""

import random

movieList = ["Title 1", "Title 2", "Title 3", "Title 4"]

randomEvent = ["death", "win", "failure", "gold lost", "hp lost", "random item gained"]

chestReward = ["green", "orange", "purple", "legendary (gold)"]

from collections import Counter

print(Counter(random.choices(chestReward, [0.80, 0.15, 0.04, 0.01], k = 100)))
