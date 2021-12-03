"""

Drawing RANDOM numbers

random numbers

random()            0 <= x < 1 lub [0,1)

uniform(2.5, 10.0)  2.5 <= x < 10.0 lub [2.5, 10)
randrange(10)       from (0,1,2,3,4,5,6,7,8,9)
randrange(0, 15, 2) even nr from (0,2,4..14)

randint(0, 4) [0,4]

"""

import random

x = 0
"""
while x < 100:
    x = x + 1
    print(random.uniform(0, 100)) 
"""
weaponChanceToHitPercentage = 50

def will_weapon_hit(weaponChanceToHitPercentage):
    chanceToHit = random.uniform(0, 100)
    if (weaponChanceToHitPercentage > chanceToHit):
        return "hit"
    else:
        return "not hit"

hitList = []

while x < 1000:
    x = x + 1
    hitList.append(random.randint(0, 10))

from collections import Counter
print(Counter(hitList))
