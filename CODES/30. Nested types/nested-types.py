# NESTED TYPES UNORDERED

name = "Arkadiusz"
age = 29
sex = "man"

name2 = "Jessica"
age2 = 23
sex2 = "woman"

name3 = "John"
age3 = 32
sex3 = "man"


person1 = ['Arkadiusz', 29, 'man']
person2 = ['Jessica', 23, 'woman']
person3 = ['John', 33, 'man']
 
guestList = {
                ('Arkadiusz', 28, 'man'),
                ('Jessica', 22, 'woman'),
                ('John', 32, 'man')
            }

guestList2 = {
                ('Arkadiusz', 28, 'man'),
                ('J', 12, 'woman'),
                ('B', 42, 'man')
            }

#guestList[0][1] = 29
guestList3 = guestList & guestList2





