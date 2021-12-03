"""

Write a function that will simulate how lottery works:
return 6 UNIQUE numbers from a set of 49 numbers

SAMPLE - returns a LIST with randomly chosen elements from another list
         sample function makes SURE that it won't
         choose the same element TWICE

"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)

print(cardList)
"""
player1Cards = random.sample(cardList, 5)
player2Cards = random.sample(cardList, 5)
"""
player1Cards = []
player1Cards.append(cardList.pop())
player1Cards.append(cardList.pop())
player1Cards.append(cardList.pop())
"""
[0,1,2,3,... ,49]
def choose_random_numbers(amount, total_amount):
    return random.sample(range(total_amount + 1), amount)


print(choose_random_numbers(6, 49))
print(choose_random_numbers(2, 30))
print(choose_random_numbers(30, 50))
"""
