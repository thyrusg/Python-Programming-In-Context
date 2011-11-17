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

    def update(self, name, score):

    def sort(self, dictionary):
        print(self.dictionary)
        #return a sorted list of all the scores

    def average(dictionary):
        print(dictionary)
        #calculate the average of all the scores

    def min(dictionary):
        print(dictionary)
        #calculate the minimum score

    def max(dictionary):
        print(dictionary)
        #calculate the maximum score

    def printer(dictionary):
        print(dictionary)
        #print a table of all the students and their respective scores
