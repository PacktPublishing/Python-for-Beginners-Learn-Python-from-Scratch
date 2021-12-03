"""
   lambda - anonymous functions (functions without names)
   
"""
def multiply(x):
    return x * 2


def function_to_filter(x):
    if (x % 2) == 0:
        return x

print((lambda x: x * 2)(4))


my_list = [2, 24, 21, 7, 20]

print(list(filter(lambda x: x % 2 == 0, my_list)))
print(list(map(lambda x: x * 2, my_list)))

my_list_filtered = [x for x in my_list if (x % 2) == 0]
