"""
Variable length argument

How to send unknown amount of arguments?

"""

import time

def function_performance(func, how_many_times = 1, **arg):
    sum = 0

   
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(100)}
listContainer = [i for i in range(100)]

def is_value_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False


print(function_performance(is_value_in, 50000, what_value=1500,
                           container=setContainer ))
print(function_performance(is_value_in, 50000, what_value=1500,
                           container=listContainer ))

"""positional arguments(unnamed) BEFORE named arguments (keyword) """

#count(2,4,1,2,4,12,5125,125,125)
