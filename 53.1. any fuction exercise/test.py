"""
Use the any() function to
determine whether the submitted list contains even numbers

all()
"""
numbers1 = [1, 3, 5, 8]
numbers2 = [1, 3, 5, 7]

def any_even(list):
    return any([nr % 2 == 0 for nr in list])

def all_even(list):
    return all([nr % 2 == 0 for nr in list])


print(any_even(numbers1)) # True
print(any_even(numbers2)) # False

if (any_even(numbers1)):
    print("one of the number is even")
else:
    print("none is even")

if (any_even(numbers2)):
    print("one of the number is even")
else:
    print("none is even")    

# any - IF ANY value is True


john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}
