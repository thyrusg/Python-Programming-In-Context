class makeDictionary:

    def __init__(self):
        self.dictionary = {}

    def add(self, name, score):  # Works
            self.dictionary[name] = score

    def delete(self, name):  # Works
        del  self.dictionary[name]

    def find(self, name):  # Works
        if name in self.dictionary:
            return self.dictionary.get(name)
        else:
            print('Name Not Found')
            return (-1)

    def update(self, name, score):  # Works
        self.dictionary[name] = score

    def sort(self):  # Works
        a = list(self.dictionary.values())
        a.sort()
        print a

    def average(self):  # Works
        listOfScores = list(self.dictionary.values())
        average = sum(listOfScores) / len(listOfScores)
        return average
        #calculate the average of all the scores

    def min(self):  # Works
        listOfScores = list(self.dictionary.values())
        minimum = min(listOfScores)
        return minimum
        # Calculate the minimum score

    def max(self):  # Works
        listOfScores = list(self.dictionary.values())
        maximum = max(listOfScores)
        return maximum
        #calculate the maximum score

    def printer(dictionary):  # Not done
        print('Hello World')
        #print a table of all the students and their respective scores

# To-Do:
# Finish the printer to function. Make sure to sort by alphabetical order
