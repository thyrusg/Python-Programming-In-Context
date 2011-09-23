def drawSquare(myTurtle, sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
        
def drawFlower(numsquare):
    for num in range(0,numsquare):
        drawSquare(myTurtle, 90)
        if numsqaure > 4:
            myTurtle.right(45)
        else:
            myTurtle.left(60)
            