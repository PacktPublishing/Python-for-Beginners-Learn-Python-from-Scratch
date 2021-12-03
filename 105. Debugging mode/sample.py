
from collections import Counter
import random

x = 0

weaponChanceToHitPercentage = (input("Weapon percentage: "))


def will_weapon_hit(weaponChanceToHitPercentage):
    chanceToHit = random.uniform(0, 100)
    if (weaponChanceToHitPercentage > chanceToHit):
        return "hit"
    else:
        return "not hit"


hitList = []

while x < 5:
    x = x + 1
    hitList.append(will_weapon_hit(weaponChanceToHitPercentage))

print(Counter(hitList))
