"""
  yield - means - supply, provide, generate

  iterator

  iterate on

  GO THROUGH it

  GENERATOR FUNCTION is a function that has a YIELD keyword
"""

def generate_even_numbers():
    print("start")
    for element in range(400):
        print("before yield")
        if (element % 2 == 0):
            yield element
            print("after yield")


evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0))


numberGenerator = generate_even_numbers()

def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1

generate_10_numbers_expression = (x for x in range(10))

print(list(generate_10_numbers()))
print(list(generate_10_numbers()))
print(list(generate_10_numbers()))

print(list(generate_10_numbers_expression))
print(list(generate_10_numbers_expression))
print(list(generate_10_numbers_expression))
