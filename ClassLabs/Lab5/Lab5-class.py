#Python Lab 5

# 1: Create a nested selection using if-else that sets the value of a variable
# named GRADEPOINT to 4, if a variable name SCORE is greater than 90, 3 if SCORE is between 80 & 89
# 2 if SCORE is between 70 and 79, 1 if SCORE is between 60 & 69, and 0 otherwise
def grade(score):
    score = int(input('Enter your score: '))
    if score >= 90:
        gradepoint = 4
    #return gradepoint
    elif score >= 80 and score <= 89:
        gradepoint = 3
    #return gradepoint
    elif score >= 70 and score <= 79:
        gradepoint = 2
    #return gradepoint
    elif score >= 60 and score <=69:
        gradepoint = 1
    #return gradepoint
    elif score > 60:
        gradepoint = 0

    return gradepoint

# 2: A year is a leap year if it's divisible by 4, unless it is a century that
# is not divisible by 400. Create a function that takes a year as a parameter
# and returns True if the year is a leap year and False otherwise

def leapYear(year):
    if year % 400 == 0:
        print("It's a leap year")
    elif year % 4 == 0 and not year % 100 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
    
        

# 3: A fruit company sells oranges for 32 cents a pound 7.50 per order for
# shipping. If an order is over 100 pounds, shipping cost is reduced by 1.50.
# Write a function that will take the number of pounds of oranges as a parameter
# and return the cost of the order

def orderCost(pounds):
    oranges = .32
    shipping = 7.50
    if pounds < 100:
        cost = (oranges * pounds) + shipping 
    elif pounds > 100:
        cost = (oranges * pounds) + (shipping - 1.50)
    return cost
        
        


