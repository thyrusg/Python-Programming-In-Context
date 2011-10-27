# Lab15.py

# 1A: Write a code segment using a while loop that generates the same output as 
# for count in range(5,20)
#    print(count)

count = 5
while count < 20:
    print(count)
    count = count + 1

# 1B:
# for i in range(15,-1,-1):
#    print(i)

i = 15
while i > -1:
    print i
    i = i - 1


# 1C: A string can be used as the conditional in a while statement. Write 
# the following code, run it, and observe the output. Explain the result
# to your lab instructor. Make sure you can answer when a string
# evaluates to True and when it evaluates to False

# x = 'computer'
# while x:
#     print(x)
#     x = x[1:]

# The while loop will remove the first value from the string everytime it
# loops because it will start at the second value, '1', everytime it goes
# through constantly removing the first value


# 1D: 
# x = 'computer'
# while x:
#     print(x)
#     x = x[:len(x)-1]

# The while loop will start with the second value from the last and everytime
# that it loops, it will ignore the last character and start with the second 
# one everytime and continue to do this until it's only one character less.



# 2: The following program converts temperature from Celsius to Fahrenheit or
# Fahrenheit to Celsius, depending on user input. Understand what the program
# is doing and then convert the program so that it repeat the calculation as
# long as the user wants. When the user runs the program, it will ask for the 
# input and calculate accordingly. After that, it will ask the user whether
# they want to repeat. If the user's response is 'yes', the program will take 
# the input again and perform the calculation. It will continue like this as
# long as the user respondes 'yes' for repeating the calculation. You need
# a while loop to solve the problem. 

import math
done = True
while done:
     op = int(input('Please enter 1: for converting Fahrenheit -> Celsius, \n 2: for converting Celsius -> Fahrenheit'))
     num = int(input('Please enter the temperature: '))
     if op == 1:
         convert1 = (num - 32) * 5/9
         print('The temperature in Celsius is: ', convert1)
     elif op == 2:
         convert = 9/5 * (num + 32)
         print('The temperature in Fahrenheit: ', convert)
     else:
         print('Invalid operation: enter 1 or 2')
     answer = str(input('Repeat ? Enter yes or no'))
     if answer == 'yes':
         done = True
     elif answer == 'no':
         done = False

# 3: Take the earthquake statistics program 'extractMag.py' and change it so that 
# instead of writing to a screen, you write to an output file, formatted as a csv file.
# Download both 'extractMag.py' and 'Earthquake.txt' from blackboard

# Currently fixing number 3

def makeMagnitudeList():
    quakefile = open("Earthquake.txt","r")
    outfile = open("format.csv","w")
    outfile.write(quakefile.readline())
    maglist = [] #outfile.write(maglist = [ ])
    for aline in quakefile:
        vlist = aline.split()
        maglist.append(float(vlist[1])) #outfile.write(maglist.append(float(vlist[1])))
    outfile.write(maglist)
    return maglist

#magList = makeMagnitudeList()
#print(magList)
