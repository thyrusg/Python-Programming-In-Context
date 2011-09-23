# 1: Write a python function stripSpaces(myString) that takes a string #representing a phrase as a parameter and returns the paragraph with the 
#order of the letters intact but the spaces between each word removed.
#For example, stripSpaces('Python Programming language') will return the #string 'Pythonprogramminglanguage' 

def stripSpaces(myString):
    a = mystring.repace(" ", "")
    return a
    
# 2: Write the substitutionDecrypt method. For hint, see #substitutionEncrypy method in page 102 of the textbook and the relevant
#discussion in Section 3.5

#Encryption function

def substitutionEncrypt(plainText, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz ' #Notice the extra space
    plainText = plainText.lower()
    cipherText = ''
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
    
#Decryption function
def substitutionDecrypt(cipherText, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cipherText = cipherText.lower()
    plainText = ''
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    return plainText
    
# 3: In Listing 3.6(Page 104) of your textbook, function removeChar is 
# implemented using a slice operator. Now, write the removeChar
# function using for loops rather than slice operators.

def removeChar(string, idx):
    kiy = string[idx]
    for ch in string:
       if kiy in string:
           string = string.replace(kiy,"")
       return string
       
    
    
    
