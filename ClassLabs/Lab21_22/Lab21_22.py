class makeDictionary:

    def __init__(self, dictionary):
        self.dictionary = dictionary

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

    def average(dictionary):  # Untested
        listOfScores = []
        for value in self.dictionary.itervalues():
            listOfScores.append(value)
        average = sum(listOfScores) / len(listOfScores)
        return average
        #calculate the average of all the scores

    def min(dictionary):
        listOfScores = []
        for value in self.dictionary.itervalues():
            listOfScores.append(value)

    def max(dictionary):
        print(dictionary)
        #calculate the maximum score

    def printer(dictionary):
        for i in range(len(self.dictionary)):
            #a = keys, b = values
            #sort each
            print(a[i], '', b[i]])
        #print a table of all the students and their respective scores
