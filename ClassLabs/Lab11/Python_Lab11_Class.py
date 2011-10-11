# Python Lab 11

# 1: Replace the call to the sum function with an iteration that 
# computes the total of the values in a list.

def sumthem(list):
    sum = 0
    for number in list:
        sum = number + sum
    return sum
    
# 2: Find the mean age of ten people within your friends groups. The ages # are: Ages = [21,30,27,34,22,26,29,19,31,30]

def mean(list):
    avg = sum(list) / len(list)
    return avg
    
# 3: Find the median age of ten people within your friend groups. The ages
# are: Ages = [21,30,27,34,22,26,29,19,31,30]

def median(list):
   copylist = alist[:]
   copylist.sort()
   pos = len(copylist) // 2
   print(len(copylist)," ",pos)
   if len(copylist) %2 != 0:
       median = copylist[pos]
   else:
       median = (copylist[pos] + copylist[pos-1] / 2.0
        
   return median
   
# 4: Create a list of the number of students in each of your classes.
# Use the mean function on that list
    
# 5: Write a function, makeDictionary, that takes the two lists and #returns a dictionary with the names as the key and the scores as the #values. Assign the result of makeDictionary to scoreDict, which will be #used in the excercises that follow.     

Name = ['joe','tom','barb','sue','sally']
Scores = [10,23,13,18,12]

def makeDirectory(name,scores):
    scoreDict = {}
    count = 0
    for person in name:
        scoreDict[person] = scores[count]
        count = count + 1
    return scoreDict
     
        


