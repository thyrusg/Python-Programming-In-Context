import random

num =random.randint(0, 99)
tries = 5
isGuessed = False

while not isGuessed and tries > 0:

    tries = tries - 1

    entry = input("Enter an integer greater than or equal to 0 and less than 100: ")
    guess = int(entry)
    
    if num == guess and tries > 0:
        print("You got it!")
        isGuessed = True
	break
    elif guess <= num and tries > 0:
        print("Your guess is lower than the number.")
        print("You have %d guesses left" % tries)
    elif guess >= num and tries > 0:
        print("Your guess is higher than the number.")
        print("You have %d guesses left" % tries)

    elif tries == 0:
        print("Sorry - you lost :(")
    
    
        
