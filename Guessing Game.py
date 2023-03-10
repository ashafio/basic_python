from random import randint

for x in range(5):
        guessNumber = int(input("Enter Your Guess between 1 to 5 : "))
        randomNumber = randint(1,5)

if guessNumber == randomNumber:
            print("You have won")
            print("Random number was : ",randomNumber)
else:
            print("You have lost")
            print("Random number was : ",randomNumber)



