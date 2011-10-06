myList = [9,4,'c','elephant',True]
myList.append(3.14)
myList.append(7)
myList
# OUT: [9, 4, 'c', 'elephant', True, 3.1400000000000001, 7]
myList.insert(4,'cat')
myList
# OUT: [9, 4, 'c', 'elephant', 'cat', True, 3.1400000000000001, 7]
myList.index('elephant')
# OUT: 3
myList.count(9)
# OUT: 1
myList.remove(9)
myList
# OUT: [4, 'c', 'elephant', 'cat', True, 3.1400000000000001, 7]
myList.index('cat')
# OUT: 3
myList.pop(3)
# OUT: 'cat'
string = "the quick brown fox"
lister = string.split(" ")
lister
# OUT: ['the', 'quick', 'brown', 'fox']
newstring = "mississippi"
newstring.split("ss")
# OUT: ['mi', 'i', 'ippi']
