#Python Lab 3

import cTurtle
myTurtle = cTurtle.Turtle()

# 1: Write a program that prints two lines that show name and birthday
def printName():
    print ("My name is Thyrus Gorges.")
    print ("I was born in March 25, 1992.")

# 2: Write a program that asks for first name, then last name and prints them.
def getName():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    print(firstName + " " + lastName)

# 3: Write a program that ask for height in feet, then displays it in inches
def height2Inches():
    height = int(input("Enter your height in feets: "))
    feet2inches = height * 12
    print(feet2inches)

# 4: Write a function to make the turtle draw a 5-pointed star
import cTurtle
def draw5Pointstar(myTurtle,length):
    for i in range(5):
        myTurtle.forward(length)
        myTurtle.right(180-36)
    
# 5: Make function drawRectangle with the following 3 parameters(myTurlte, width, height)
def drawRectangle(myTurtle, width, height):
    for i in range(2):
        myTurtle.forward(width)
        myTurtle.right(90)
        myTurtle.forward(height)
        myTurtle.right(90)

# 6:
def sLength():
    string = "s"
    print(" " * 29 + string)
