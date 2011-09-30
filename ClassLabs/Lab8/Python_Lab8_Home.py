# 1: Write a function that takes a single character digit and returns
# its integer value. For example, if the function name is intval, intval('9')
# will return 9(the integer 9, not string '9')

def intval(i):
    i = int(i)
    return i
    
# 2: Write the letterToIndex function using ord and chr. letterToIndex is
# defined in page 93 of the textbook.     

def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ch = ord(ch)
    num = chr(ch)

return alphabet.find(num)

# 3: Write the indexToLetter function using ord & chr. indexToLetter 
# is also defined in page 93.

def index2letter(index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = ''
    num = 97
    a = index + num
    for x in alphabet:
        letters = letters + "," + str(ord(x))
    b = ''
    if str(a) in letters:
        b = chr(int(a))
        
# 4: Write a function that takes an exam score from 0-100 and returns the
# corresponding letter grade. Use the same grading scale your professor
# does for this class. 





###################################################################

def index2letter(index):
...     alphabet = "abcdefghijklmnopqrstuvwxyz"
...     letters = ''
...     num = 97
...     a = index + num
...     for x in alphabet:
...         letters = letters + "," + str(ord(x))
...     b = ''
...     if str(a) in letters:
...         b = chr(int(a))


