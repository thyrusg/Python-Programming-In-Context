class makeDictionary:

    def __init__(self):
        self.dictionary = {}
        self.file = open('output.txt', 'a')

    def add(self, name, score):  # Works
            self.dictionary[name] = score
            self.file.write('%s\t %s\n' % ('add', str(self.dictionary)))

    def delete(self, name):  # Works
        del self.dictionary[name]
        return self.dictionary
        self.file.write('%s\t %s\n' % ('delete', str(self.dictionary)))

    def find(self, name):  # Works
        if name in self.dictionary:
            return self.dictionary.get(name)
            self.file.write('%s\t %s\n' % ('find', str(self.dictionary)))
        else:
            print('Name Not Found')
            return (-1)
            self.file.write('%s\t %\s\n' % ('find', str(self.dictionary)))

    def update(self, name, score):  # Works
        self.dictionary[name] = score
        self.file.write('%s\t %s\n' % ('update', str(self.dictionary)))

    def sort(self):  # Works
        a = list(self.dictionary.values())
        a.sort()
        print a
        self.file.write('%s\t %s\n' % ('sort', str(a)))

    def average(self):  # Works
        listOfScores = list(self.dictionary.values())
        average = sum(listOfScores) / len(listOfScores)
        return average
        self.file.write('%s\t %s\n' % ('average', str(self.dictionary)))
        #calculate the average of all the scores

    def min(self):  # Works
        listOfScores = list(self.dictionary.values())
        minimum = min(listOfScores)
        return minimum
        self.file.write('%s\t %s\n' % ('minimum', str(self.dictionary)))
        # Calculate the minimum score

    def max(self):  # Works
        listOfScores = list(self.dictionary.values())
        maximum = max(listOfScores)
        return maximum
        self.file.write('%s\t %s\n' % ('maximum', str(self.dictionary)))
        #calculate the maximum score

    def printer(self):  # Works
        names = self.dictionary.items()
        names.sort()
        for k, v in names:
            print('%s\t %s' % (k, v))
            self.file.write('%s\t %s\n' % (k, v))
        #print a table of all the students and their respective scores
