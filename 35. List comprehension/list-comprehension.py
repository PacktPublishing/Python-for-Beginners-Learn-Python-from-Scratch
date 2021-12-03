""" LIST comprehensions (expressions/formulas)"""

numbers = [1, 2, 3, 4, 5, 6]

poweredNumbers = []
for element in numbers:
    poweredNumbers.append(element**2)

evenNumbers = []
for element in numbers:
    if (element % 2 == 0):
        evenNumbers.append(element)


poweredNumbers2 = [element**2
                   for element in range(51)
                  ]

evenNumbers2 = [element
                for element in numbers
                if (element % 2 == 0)
                ]

"""
[what_to_do_on_element | for element in old_list | condition_based_on_element]

element/item/entry
"""
