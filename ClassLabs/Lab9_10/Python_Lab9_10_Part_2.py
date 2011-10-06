# 4A: DIY Python list count method
def counter(value):
   listly = [1,1,2,3,4,4,4,5,5]
   count = 0
   for item in listly:
       if item == value:
           count = count + 1
   return count

# 4B: DIY In function - return True if item is in list

def in(value,list):

def inside(value, list):
   answer = ""
   for item in list:
       if value == item:
           answer = "True"
       break
   return answer
   
# 4C: DIY list reverse function

def reverseList(list):
    #string = str(input('Please Enter A String: '))
    reversed = []
    for item in list:
        ch = list.index(item)
        reversed = list[ch] + reversed
    return reversed   

