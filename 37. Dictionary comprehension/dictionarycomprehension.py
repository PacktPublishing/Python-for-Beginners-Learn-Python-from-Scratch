"""
    dictionary comprehensions(expressions/formula)
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celsius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

multipliedNumbers = {
    number: number*number
    for number in range(1,500)
}

fahrenheit = {
    key: celsius * 1.8 + 32
    for key, celsius in celsius.items()
    if celsius > -10
    if celsius < 20
}




