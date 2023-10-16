'''

You receive a list of people who will be given 'access' to secret information:
names = ['Arkadiusz', 'Chris', 'John']

If someone from the 'names' list is provided by the user in the 'name' variable
display:
"Access granted"

If not write:
"Access denied"

'''

names = ['Arkadiusz', 'Chris', 'John']

name = input()
name = name.capitalize()

if name == "Arkadiusz" or name == "Chris" or name == "John":
    print("Access granted")
else:
    print("Access denied")
