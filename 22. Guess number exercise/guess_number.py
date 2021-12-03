"GUESS NUMBER"

secretNumber = 40
guessedNumber = 0

while guessedNumber != secretNumber:
    guessedNumber = int(input("Guess number: "))

    if (secretNumber > guessedNumber):
        print("It's a bit bigger ;)")
    elif (secretNumber < guessedNumber):
        print("It's a bit smaller ;(")
    else:
        print("CONGRATULATION")

