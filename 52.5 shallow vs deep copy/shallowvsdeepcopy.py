"""
    copy - shallow (of little depth)
    deepcopy - copy of each every mutable element inside of object

    mutable
    immutable
"""
import copy

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList[0]))
    toBeDestroyedList[0] = 444
    print(id(toBeDestroyedList[0]))
    print(toBeDestroyedList)
   

#myList = [[1, 4], [2, 1], [52, 3]]
myList = [1, 4, 2, 1, 52, 3]

print(id(myList[0]))
evil_function(myList.copy())
print(id(myList[0]))
print(myList)


a = 4
b = 4
