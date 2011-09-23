import math
import cTurtle
myTurtle = cTurtle.Turtle()

def drawTriangle(sideA, sideB, angle):
    angle = angle*math.pi/180  #convert angle to radians
    sideC = math.sqrt((sideA**2) + (sideB**2) - (2*sideA*sideB*(math.cos(angle)))) #use the law of cosines  
    angle2 = (math.asin((sideA/sideC)*math.sin(angle)))
    
    #Draw the triangle
    myTurtle.forward(sideA)
    myTurtle.right(180-angle*(180/(math.pi))) #180 / pi is used to convert to radians
    myTurtle.forward(sideB)
    myTurtle.right(180-angle2*(180/(math.pi)))
    myTurtle.forward(sideC)
    
