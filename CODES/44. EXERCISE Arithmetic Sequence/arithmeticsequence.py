"""
Write program, that will count the sum of all numbers from 1 to
number that was entered by user.

1,2,3,4,5,... 100

(1 + 100) / 2 * 100

For 5:
1+2+3+4+5
the result is gonna be:
15


(1 + 5) / 2 * 5 = 15

range(1, 6)
1,2,3,4,5
"""

def sum_up_to(end):
    sum = 0 # 15

    for number in range(1, end+1): #number = 5
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



print(sum_up_to(1255))
print(sum_up_to2(1255))
print(sum_up_to3(1255))
print(sum_up_to4(1255))
print(sum_up_to5(1255))
