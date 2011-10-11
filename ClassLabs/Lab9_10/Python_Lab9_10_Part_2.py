# 4A: DIY Python list count method
def counter(value):
   listly = [1,1,2,3,4,4,4,5,5]
   count = 0
   for item in listly:
       if item == value:
           count = count + 1
   return count

# 4B: DIY In function - return True if item is in list

def inside(value, list):
   answer = ""
   for item in list:
       if value == item:
           answer = "True"
       break
   if answer == "":
       answer = "False"
   return answer
   
   
# 4C: DIY list reverse function

def reverseList(list):
    rev = []
    count = -1
    for num in list:
        ch = list[count]
        rev.append(ch)
        count = count - 1
    return rev

# 4D: DIY Index function

def getindex(item,list):
   count = 0
   for element in list:
       if element == item:
           print count
       else:
           count = count + 1
   if item not in list:
        print 1
        
# 4E: DIY Insert function     

def inserter(index, item, list):
    newlist = []
    count = 0
    for element in list:
        if count == index:
            newlist = list[:count]
            newlist.append(item)
            for thing in list[count:]:
                newlist.append(thing)
                #newlist.append(list[count:])
        else:
            count = count + 1
    return newlist

# 5: Create a function called shuffle that takes a list and returns a new
# list with the elements shuffled into a random order

def shuffle(list):
   import random
   mylist = []
   for item in list:
       mylist.insert(random.randint(0,len(list)-1),item)
   return mylist
   
# 6: Implement the getMin function using iteration by item

def getMin(list):
   min = list[0]
   for num in range(1,len(list)):
       if list[num] < min:
           min = list[num]
   return min   
















   
