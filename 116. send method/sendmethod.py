def number_multiplied_by_itself_generator():
    number = 0
    while True:
        print("before yield number:", number)
        #number = number + 1
        number = yield number * number
        print("after yield number:", number)


      


generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()

numberGenerator.send(None)
#next(numberGenerator)

for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)



for i in range(30, 50):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)

