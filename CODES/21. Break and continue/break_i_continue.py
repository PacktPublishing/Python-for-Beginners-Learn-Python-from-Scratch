"""
break (leaves loop entirely)

continue (leaves current iteration (repetition of loop) and CONTINUE)
"""

result = 0

i = 0

while i < 3:
    x = int(input("Enter a positive number: "))
    if (x > 0):
        result += x
    else:
        print("I expected positive number, you gave me a negative number, you are a bad boy!")
        continue
    print("Current addition result =", result)
    i += 1
