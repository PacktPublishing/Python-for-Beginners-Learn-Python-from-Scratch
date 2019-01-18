import sys
"""generator expressions"""

evenNumbers = [element
               for element in range(4401)
               if (element % 2 == 0)
               ]

evenNumbersGenerator = (element
                        for element in range(4401)
                        if (element % 2 == 0)
                        )


print(sum(evenNumbersGenerator))
"""
print(evenNumbers)
print(evenNumbersGenerator)

for number in evenNumbersGenerator:
    print(number)

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))
"""
