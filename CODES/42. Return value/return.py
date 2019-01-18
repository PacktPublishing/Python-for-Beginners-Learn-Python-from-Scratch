""" return as the name suggests 
    returns to the place where the function was invoked.

    None logical False
"""

def area_rectangle(side1, side2):
    return side1 * side2



areaRectangleA = area_rectangle(4, 6)
areaRectangleB = area_rectangle(2, 24)

#print("The area of rectangle is equal to: ", 5 * areaRectangleA)
#print("The area of rectangle is equal to: ", 7 * areaRectangleB)


def divide(a, b):
    if (b == 0):
        return
    
    return a / b

x = divide(20,5)
if(x):
    print("The numbers were divided properly, the result is equal to:", x)
else:
    print("Division by zero")
