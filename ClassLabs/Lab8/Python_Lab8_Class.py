# 1: Make the word 'Python' centered and all capital letters in a string
# of length 20. 
word = 'Python'
word = word.center(20)
word = word.upper()

# 2: In Session 3.5(Page 88) of your textbook, it is shown how you can print
# all prefixes of a string 'Roy G Biv', but it does not print the entire
# string. Modify the example so that it prints all prefixes of the string
# including the entire string. You may not add additional lines of 
# Python codes.

def example():
    name = 'Roy G Biv'
    for i in range(len(name)):
        print(name[0:i+1])

# 3: What is the difference between ord('B') and ord('b')? Write a one
# sentence comment about your finding. 

#ord('B') returns 66 and ord('b') returns 98 because ASCII key considers upper case and lower case letters different. 
