import time

def sum_up_to(end):
    sum = 0 

    for number in range(1, end+1):
        sum = sum + number

    return sum

def sum_up_to2(end):
    return sum([number for number in range(1, end+1)])
def sum_up_to3(end):
    return sum({number for number in range(1, end+1)})
def sum_up_to4(end):
    return sum((number for number in range(1, end+1)))
def sum_up_to5(end):
    return (1 + end) / 2 * end


#function_performance(sum_up_to, 325)

def show_message(message):
    print(message)

def function_performance(x, arg, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        x(arg)
        end = time.perf_counter()
        how_long = end-start
        sum  = sum + how_long
    
    return sum

print(function_performance(sum_up_to, 500000, 25))
print(function_performance(sum_up_to2, 500000))
print(function_performance(sum_up_to3, 500000))
print(function_performance(sum_up_to4, 500000))
print(function_performance(sum_up_to5, 500000))


"""
start = time.perf_counter()
print(sum_up_to(325))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sum_up_to2(325))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sum_up_to3(325))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sum_up_to4(325))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sum_up_to5(325))
end = time.perf_counter()
print(end-start)
"""
