from random import randint

for x in range(6):
    guessNumber = int(input("Enter Your Guess Number: "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print('You have won')
    else:
        print('You have lost')
        print("Random number was: ", randomNumber)