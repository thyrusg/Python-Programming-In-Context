
def makeMagnitudeList():
        quakefile = open("earthquakes.txt","r")
        headers = quakefile.readline()
        
        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            maglist.append(float(vlist[1]))
        return maglist

magList = makeMagnitudeList()
print(magList)


-----------------------------------------------------------------

def makeMagnitudeList():
    quakefile = open("Earthquake.txt","r")
    f = open("output.csv","w")
    
