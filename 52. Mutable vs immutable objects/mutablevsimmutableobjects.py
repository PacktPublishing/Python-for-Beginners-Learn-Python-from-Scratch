"""
    object is a variable with MORE features than just showing value
    You can invoke a function ON object
    object can have many different values

    immutable - unchangable (after sending as argument)
    mutable - changable 
    
     immutable object: bool, int, float, tuple, str
     
    = - means CHANGING the address. Since now the object points to DIFFENT place

    METHOD
"""

x = 4
#y = x
#y = 20
#print(id(x))

#listSample2 = listSample1

#listSample1.append(4)

def add(x, amount=1):
    print(id(x))
    x = x + amount
    print(id(x))

#add(x)

g = 20
h = 20


listSample1 = [2, 42, 125]

print(id(listSample1))

def append_element_to_list(WHATAVER, element):
    print(id(WHATAVER))
    a = [124, 124, 52, 1] # 
    WHATAVER = a
    print(id(WHATAVER))
    WHATAVER.append(4)

append_element_to_list(listSample1, 2000)

print(listSample1)
