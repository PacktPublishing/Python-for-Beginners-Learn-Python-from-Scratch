import figures

#enum - enumeration - list of elements that are enumerated (numbered) starting from 1

from enum import IntEnum

#Menu_Figures = IntEnum('Menu_Figures', {'Square':44, 'Rectangle':12, 'Circle':42, 'Triangle':5, 'Trapeze':2})
Menu_Figures = IntEnum('Menu_Figures', ['Square', 'Rectangle', 'Circle', 'Triangle', 'Trapeze'])
print(list(Menu_Figures))

choose = int(input("""What figure area you want to measure?
1. Square
2. Rectangle
3. Circle
4. Triangle
5. Trapeze
"""))

if (choose == Menu_Figures.Square):
    a = float(input("Enter the size of square side: "))
    print("The area of square is equal to:", figures.area_of_square(a))
elif (choose == Menu_Figures.Rectangle):
    a = float(input("Enter the size of 1-st side of rectangle "))
    b = float(input("Enter the size of 2-nd side of rectangle: "))
    print("The area of rectangle is equal to:", figures.area_of_rectangle(a, b))
elif (choose == Menu_Figures.Circle):
    r = float(input("Enter the radius of circle "))
    print("The area of circle is equal to:", figures.area_of_circle(r))
elif (choose == Menu_Figures.Triangle):
    a = float(input("Enter the side of triangle: "))
    h = float(input("Enter the height of triangle: "))
    print("The area of triangle is equal to:", figures.area_of_triangle(a, h))
elif (choose == Menu_Figures.Trapeze):
    a = float(input("Enter the size of 1-st side of trapeze "))
    b = float(input("Enter the size of 2-nd side of trapeze: "))
    h = float(input("Enter the height of trapeze: "))
    print("The area of trapeze is equal to:", figuryfiguresarea_of_trapeze(a, b, h))
