# 1: Print out a table of students and their scores with the students listed in alphabetical order.

def studentsort(dictionary):
    students = []
    for name in dictionary:
        students.append(name)
        students.sort()
    for name in students:
        if name in dictionary:
            print(name, dictionary[name])


# students = list(dictionary.keys)
# students.sort

         
# 2: Write a function called getScore that takes a name and a dictionary as a parameter and returns the score for that name if it is in the dictionary. If the name is
# not in the dictionary, print an error message and return -1.

def getScore(name, dictionary):
    if name in dictionary:
        score = dictionary[name]
    elif name not in dictionary:
        score = -1
        print("%s is not in the dictionary" % (name))
    return score

# 3: Suppose you have a list of key-score values like the following: [('john',10),('bob',8),('john',5),('bob',17]. Write a function that takes such a list as a
# parameter and prints out a table of average scores for each person. 



# 4: Another way to compute the frequency table is to obtain a list of key-value pairs using the items method. This list of tuples can be sorted and printed without
# returning to the original dictionary. Rewrite the frequency table function using this idea. 
