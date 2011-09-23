import math

def archimedes(sides):

    innerangleB = 360.0/sides
    halfangleA = innerangleB/2

    onehalfsideS = math.sin(math.radians(halfangleA))

    sideS = onehalfsideS * 2

    polygonCircumference = sides * sideS
    pi = polygonCircumference / 2

    return pi

#Repeat the loop in session 2.4
for sides in range(8,100,8):
    print(sides, archimedes(sides))
    

a = archimedes(20) #Call archimedes function
b = math.pi #assign pi to a variable
c = a - b #subtract the value of the archimedes function from the math.pi


#Fibonacci sequence
def fib(x):
    a = 0
    b = 1
    for num in range(x-1):
       c = a + b 
       a = b
       b = c

    return b
