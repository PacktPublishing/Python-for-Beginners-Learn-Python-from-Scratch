"""
Write a game where the player can move 5 times in
                       ONE direction 

The player has a chance to find a chest(40%) or nothing(60%)

The chests have different colours and different rewards based on colours

The chance to get
green - 75%
orange - 20%
purple - 4%
gold (legendary) - 1%

Gold is a thing that can reward a player that opens the chest:
green - 1000
orange - 4000
purple - 9000
gold (legendary) - 16000

1 1 *1                (0 +1) * (0 + 1) = 1
4 2*2 1               (1 + 1) * (1 + 1) = 4 * 1000
9 3* 3 2
16 4 * 4 3

Make sure to write:
1) clean code
2) make self-descriptive variables

"""
import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Nothing'])

eventDictionary = {
                    Event.Chest: 0.8,
                    Event.Nothing: 0.2
                  }
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Colours = Enum('Colours', {"Green": "green",
                           "Orange": "orange",
                           "Purple": "purple",
                           "Gold": "LEGENDARY"
                           })

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())

chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                        chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                        for reward in range(4)
                   }

gameLength = 5
goldAcquired = 0
while gameLength > 0:
    playerAnswer = input("Do you want to move forward?")
    if (playerAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if(drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(chestColourList, chestColourProbability)[0]
            print("The chest color is", drawnColour.value)
            playerReward = rewardsForChests[drawnColour]
            goldAcquired = goldAcquired + playerReward
        elif(drawnEvent == Event.Nothing):
            print("You've drawn nothing, you are so unlucky!")
            
    else:
        print("You can go just straight man, nothing else, this game is dumb")
        continue       
    
    gameLength = gameLength - 1

print("Congratulation, you have acquired:", goldAcquired)


