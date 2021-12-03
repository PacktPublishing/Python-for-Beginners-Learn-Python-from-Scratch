import figures

choose = input("""What figure area you want to measure?
1. Square
2. Rectangle
3. Circle
4. Triangle
5. Trapeze
""")

if (choose == '1'):
    a = float(input("Enter the size of square side: "))
    print("The area of square is equal to:", figures.area_of_square(a))
