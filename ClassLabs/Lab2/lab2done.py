Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cTurtle
>>> a=8
>>> a
8
>>> b=75
>>> b
75
>>> c=a*b
>>> c
600
>>> #End 1a
>>> ================================ RESTART ================================
>>> a=4
>>> b=6
>>> a
4
>>> b
6
>>> c=a*b
>>> c
24
>>> a=a*b
>>> a
24
>>> b=c+2
>>> b
26
>>> c=a*b**3/c
>>> c
17576.0
>>> #End 1b
>>> ================================ RESTART ================================
>>> a=4
>>> a
4
>>> b=9
>>> b
9
>>> c=a**b
>>> c
262144
>>> b=b**b
>>> b
387420489
>>> c=c+a**b
>>> 
>>> ================================ RESTART ================================
>>> import cTurtle
>>> myTurtle = cTurtle.Turtle()
>>> myTurtle.forward(35)
>>> myTurtle.right(90)
>>> myTurtle.forward(43)
>>> myTurtle.position()
(35.00,-43.00)
>>> Yertle = myTurtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Yertle = myTurtle.Turtle()
AttributeError: 'Turtle' object has no attribute 'Turtle'
>>> Yertle = cTurtle.Turtle()
>>> Yertle.forward(60)
>>> Yertle.right(64)
>>> Yertle.forward(28)
>>> Yertle.left(92)
>>> Yertle.back(12)
>>> Yertle.position()
(61.68,-30.80)
>>> Lumpy = cTurtle.Turtle()
>>> ================================ RESTART ================================
>>> import cTurtle
>>> Lumpy = cTurtle.Turtle()
>>> Lumpy.forward(30)
>>> Lumpy.right(90)
>>> Lumpy.forward(30)
>>> Lumpy.left(90)
>>> Lumpy.right(180)
>>> Lumpy.forward(30)
>>> Lumpy.right(90)
>>> Lumpy.forward(30)

>>> for i in range(4,35,2):
	print(i)

	
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
>>> for i in range(6,31,3):
	print(i)

	
6
9
12
15
18
21
24
27
30
>>> for i in range(-7,8,2):
	print(i)

	
-7
-5
-3
-1
1
3
5
7
>>> 