# 2: Use the readline method to write your own myReadlines function. Your function myReadlines should take an open file as a parameter and a number n and return a 
# list of n lines that were read, where each list item is a line. 

def myReadlines(openfile, number):
    listoflines = []
    for item in range(0,number):
        listoflines.append(f.readline())
        listoflines = listoflines[:number]
    return listoflines
    
######################################33
for item in range(0,number):
...     lister.append(f.readline())

#The above statement adds all items except the first to the list

def myReadlines(openfile, number):
...     listoflines = []
...     for item in range(0,number):
...         listoflines.append(f.readline())
...         listoflines = listoflines[:number]
...     return listoflines
