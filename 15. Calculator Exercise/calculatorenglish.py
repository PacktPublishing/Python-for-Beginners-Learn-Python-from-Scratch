'''
ADD SUBTRACT MULTIPLY DIVIDE

CALCULATOR
'''

menuOption = input("+ - ADD 2 - SUBTRACT * - MULTIPLY / - DIVIDE: ")

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))

if (menuOption == '+'):
    print(firstNumber + secondNumber)
elif (menuOption == '-'):
    print(firstNumber - secondNumber)
elif (menuOption == '*'):
    print(firstNumber * secondNumber)
elif (menuOption == '/'):
    if (secondNumber == 0):
        print('Division by zero - you cannot do it!')
    else:
        print(firstNumber / secondNumber)
else:
    print("You have typed something unexpected")
