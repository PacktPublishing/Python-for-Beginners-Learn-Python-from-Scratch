"""
Find numbers from 2 to 470, that are:
- divisible by 7, but are not divisible by 5 

What will you use?
1) generator expression
2) list comprehension
3) set comprehension
4) dictionary comprehension

Think for a second and make notes: 
"is the answer to above question always the same?"

range(2, 471)

7
14
21
28
35
42
49
56

5
10
15
20
25
30
35
40
45
50
55

7 % 7 == 0
14 % 7 == 0
21 % 7 == 0
28 % 7 == 0
35 % 7 == 0


35 % 5 == 0
14 % 5 == 4

"""
numbers = {
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
}

print(numbers)


