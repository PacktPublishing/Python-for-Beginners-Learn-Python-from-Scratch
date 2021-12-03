"""
Write a program that will allow the user to:
1) Add new definitions
2) Search existing definitions
3) Delete the definition that he has chosen
TAB
"""

dictionary = {}

while(True): 
    print("1: Add definition")
    print("2: Search for definition")
    print("3: Remove definition")
    print("4: End")

    choice = input("What do you want to do? ")

    if (choice == "1"):
        key = input("Enter the word (key) to define: ")
        definition = input("Enter definition: ")
        dictionary[key] = definition
        print("Definition added successfully")
    elif (choice == "2"):
        key = input("What are you searching for? ")
        if key in dictionary:
            print(dictionary[key])
        else:
            print("Definition has not been found: ", key)
    elif (choice == "3"):
        key = input("What definition do you want to remove? ")
        if key in dictionary:
            del dictionary[key]
            print("Definition", key," removed successfully")
        else:
            print("Definition has not been found: ", key)        
    elif (choice == "4"):
        print("Bye then!")
        break
