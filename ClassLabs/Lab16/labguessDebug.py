import random

num = random.randint(0, 99)

isGuessed = False

while not isGuessed and tries > 0:

    tries = tries - 1

    entry = input("Enter an integer greater than or equal to 0 and less than 100: ")
    guess = int(entry)
    
    if num == guess:
        print("You got it!")
    if guess <= num:
        print("Your guess is lower than a number.")
        print("You have %d guesses left" % tries)
    if guess >= num:
        print("Your guess is higher than a number.")
        print("You have %d guesses left" % tries)

if not isGuessed:
    print("Sorry - you lost :(")
    
    
        
