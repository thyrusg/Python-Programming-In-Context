from cImage import *

def double(oldimage):
    myWin = ImageWin('Test', 500, 500)
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw * 2, oldh * 2)
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col // 2
            originalRow = row // 2
            oldpixel = oldimage.getPixel(originalCol, originalRow)
            newim.setPixel(col, row, oldpixel)
    
    return newim

# The loop is based on the original image.
# originalCol and originalRow are calculated as integers because if they
# weren't calculated as intergers the new images dimensions would not be twice
# the original images size. Regular division would have given uneven numbers
# (Or numbers that would have distorted the dimensions of the new image)

# 2: Study the following code and add necessary code to it to draw Kochs curve
# of level 1, level 2, level 3, and level 4 in the main function. State the
# base case and recursive step. Also, explain how the recursive step brings us
# close to the base step.


def recKoch(aTurtle, distance, level):
    print("level: %3d distance: %d" % (level, distance))
    if level == 0:
        aTurtle.forward(distance)
    else:
        recKoch(aTurtle, distance / 3, level - 1)
        aTurtle.left(60)
        recKoch(aTurtle, distance / 3, level - 1)
        aTurtle.right(120)
        recKoch(aTurtle, distance / 3, level - 1)
        aTurtle.left(60)
        recKoch(aTurtle, distance / 3, level - 1)

# 3: Greatest common divisor(GCD) of two positive integers a & b is the largest
# number c that divides both a and b. We can find the GCD of two numbers using
# the following recursive formula. This function assumes that a > b.

def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b,a%b)



#4: Rewrite the following function, run it, and explain what it is doing. Can
# you figure out how this is done?


def func(aString):
    if aString == '':
        return ''
    else:
        return func(aString[1:]) + aString[0]

# The function works by removing the first letter from the string, then calling
# the function again until there are no more letters to remove. Then the function
# will word backwards and combine the letters in reverse order.
