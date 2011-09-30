#1 Create a function called ro13, that takes a message as a parameter and
# rotates all its characters by 13 places.

def rot13(message):
    message =  message.lower()
    newMessage = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'nopqrstuvwxyzabcdefghijklm'
    for letter in message:
       finder = alphabet.find(letter)
       blah = key[finder]
       newMessage = newMessage + blah 
    return newMessage


# 2A: Assume that the variable data refers to the string 'myprogram.exe'
# Write the values of the following expressions

data = 'myprogram.exe'
print(data[3])
print(data[-2])
print(len(data))
print(data[0:7])

# 2B: Assume that the variable data refers to the string 'myprogram.exe'
# Write the expressions that perform the following tasks and store the results
# into the variable newData

data = 'myprogram.exe'
newData = data[2:6]
print(newData)
newData = data[10:]
print(newData)
newData = data[6]

# 2C: Write a function that takes a string as an input parameter and reverses
# the string. Validate the function by taking an input from the user and invoking
# the function

def reverseString():
    string = str(input('Please Enter A String: '))
    reversed = ''
    for letter in string:
        ch = string.find(letter)
        reversed = string[ch] + reversed
    return reversed



      
