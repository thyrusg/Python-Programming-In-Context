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
    return b
        
# 4: Write a function that takes an exam score from 0-100 and returns the
# corresponding letter grade. Use the same grading scale your professor
# does for this class. 

def grade():
    score = int(input('Enter your score: '))
    if score >= 95:
        lettergrade = "A"
    elif score >= 94 or score >= 90:
        lettergrade = "A-"
    elif score >= 89 or score >= 88:
        lettergrade = "B+"
    elif score >= 87 or score >= 83:
        lettergrade = "B"
    elif score >= 82 or score >= 80:
        lettergrade = "B-"
    elif score >= 79 or score >= 78:
        lettergrade = "C+"
    elif score >= 77 or score >= 73:
        lettergrade = "C"
    elif score >= 72 or score >= 70:
        lettergrade = "C-"
    elif score >= 69 or score >= 68:
        lettergrade = "D+"
    elif score >= 67 or score >= 63:
        lettergrade = "D"
    elif score >= 62 or score >= 60:
        lettergrade = "D-"
    elif score <= 59:
        lettergrade = "F"
    return lettergrade

    


###################################################################

"""def index2letter(index):
...     alphabet = "abcdefghijklmnopqrstuvwxyz"
...     letters = ''
...     num = 97
...     a = index + num
...     for x in alphabet:
...         letters = letters + "," + str(ord(x))
...     b = ''
...     if str(a) in letters:
...         b = chr(int(a))"""


