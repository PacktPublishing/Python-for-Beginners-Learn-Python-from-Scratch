""" Create a generator function that will generate numbers multiplied

by themselves

1

4

9

16

25

36

Generate 20 elements, stop, and then again generate 30 numbers.

Save each results in the same list and then show it.
"""

def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number


generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)


"""
MANY INSTRUCTIONS 
"""
for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)
