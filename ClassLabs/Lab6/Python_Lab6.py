# Python Lab 6
name = "Thyrus Ghanim Gorges"
name[0:6] #1B
# OUT: 'Thyrus'
#1C 
name[13:]
# OUT: ' Gorges'
# 1D
name[14:] + "," + name[0:6]
# OUT: 'Gorges,Thyrus'
# 1E
len(name[14:])
# OUT: 6
# 2A
s = 's'
p = 'p'
a = 'mi'+s*2+'i'+s*2+'i'+p*2+'i'
a
# OUT: 'mississippi'
# 2B
a.count('s')
# OUT: 4
# 2C
a.replace('iss','ox')
# OUT: 'moxoxippi'
b = 'mississippi'
b.find('p')
# OUT: 8
