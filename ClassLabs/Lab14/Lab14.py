# 1A: Assume that the variable amount referes to 61:235. Write the output
# of the following statements. Explain the output to the lab instructor.

amount = 61.235
print("Your salary is $%0.2f" % amount)
# Returns the first two values after the .
print("The area is %0.1f" % amount)
# Returns the first value after the .
print("%7f" % amount)
# The %f string operator returns the next 6 values after the .

# 1B: Write a code segment that displays the values of the integers x,y,z
# on a single line, such that each value is left-justified in a field width
# of 6

x,y,z = 1,2,3
print "%-6d %-6d %-6d" %(x,y,z)

# 1C: Write a loop that outpit the numbers in a list named salaries. The 
# outputs should be formatted in a column that is right-justified, with a
# field width of 12 and a precision of 2

salaries = [1,2,3,4,5,6,7,8]
for item in salaries:
    print "%20.2f" % (item)

# 2: Write a program to read the 'rainfall.txt' file and then write out a new file
# called rainfallmt.txt. The new file should format each line so that the city
# is right-justified in a field that is 10 characters wide, and the rainfall
# data should be printed in a field that is 7 characters wide with 2 digits to
# the right of the decimal point. Add headers to the columns in your file.
# The output should be displayed in centimeters(in the original file it is
# displayed in inches).


def formater(file):
    f = open(file,'r')
    out = open('rainfallmt.txt','w')
    out.write("%+10s %7s \n" % ("CITY","RAINFALL")) # Create headers
    for line in f:
        splitter = line.split()
        inches = float(splitter[1])
        cent = inches * 2.54
        out.write("%10s %7.2f \n " % (splitter[0],cent))
    
    f.close()
    out.close()

# Problem: The function writes all the data to the new file, but throws an error 
# at the end. 
    


# 3: Write a program that reads in a file and then prints out the number of
# lines, words, and characters in the file.
 

def linecount(file):
    f = open(file,'r')
    linecount = 0
    for line in f:
        linecount = linecount + 1
    return linecount
    f.close()

def charactercount(file):
    f = open(file)
    count = 0
    for character in f.read():
        blah = len(character)
        count = blah + count
    return count
    f.close()


def wordcount(file):
    f=open(file,'r')
    count = 0
    for line in f:
        splitter = line.split()
        count = len(splitter) + count
    return count
    f.close()

#############################################################

def counts(file):
    f = open(file,'r')
    linecount = 0
    charactercount = 0
    wordcount = 0
    
    for line in f:
        linecount = linecount + 1
        splitter = line.split()
        wordcount = len(splitter) + wordcount
        
    f.close()    
    #print linecount, wordcount
    
    #reopen file
    f1 = open(file,'r')
    for line in f1:
        blah = len(line)
        charactercount = blah + charactercount
    f1.close()
    
    print "Line count is %s" % linecount
    print "Word count is %s" % wordcount
    print "Character count is %s" % charactercount 
