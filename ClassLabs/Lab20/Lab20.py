import cTurtle

# Write a recursive function to draw concentric nested boxes where each box is
# centered around the same point. It might be helpful to write a helper
# function'called drawCenteredSquare that accepts parameters for a turtle, the
# center x and y positions, and the length of the side.

def drawSquare(t,p1,p2,p3,p4):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)

def midPoint(p1,p2):
    return ((p1[0]+p2[0]) / 2.0, (p1[1]+p2[1] / 2.0))


# Write the tree function where you can add color to the tree by making the
# large branches brown, and the small branches green. Choose a threshold value
# for the length of the the trunk and set the color accordingly.

# You have learned the Sierpinski Triangle from the book. Modify the sierpinski
# and drawTriangle function to add color. [Hint: Make each recursive call draw
# a different color.]


