"""
EXERCISE TIME :-)

Write a function that will check if the container contains
searched value.

If the value is found return True
If the value is not found return False

CHECK PERFORMANCE of your function on set and list containing
over 1000 values.

"""

import time

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(10000)}
listContainer = [i for i in range(10000)]


def is_value_in(what_value):
    if what_value in setContainer:
        return True
    else:
        return False

print(function_performance(is_value_in, 1500, 50000))
