# Earthquakes divided up into the following categories:
# Great: (8+) Major: (7-7.9) Strong: (6-6.9) Moderate: (5-5.9)
# Earthquakes below a magnitude of 5 are not classified.

# Lists should be parallel data structures.
# There should be a list of region names, where none are repeated. Just append
# all the regions to a list then turn it into a set, which will remove dups and
# turn back into  a list.

# A list for each earthquake category, where the data in these lists is to be
#parallel to the names list, namely, if regionName[0] contains
#Gulf of California, then great[0] is the number of 'great' earthquakes that
# occurred in that region.

regionNames = []
greatMag = []
majorMag = []
strongMag = []
moderateMag = []


# First tell the user to open the file they want to process.
# I.e. file = open('nameoffile', 'r') with read permissions.

def sortMag(magnitude):
    magnitude = float(magnitude)
    if magnitude >= float(8):
        greatMag.append(magnitude)
    elif magnitude >= float(7) and magnitude <= float(7.9):
        majorMag.append(magnitude)
    elif magnitude >= float(6) and magnitude <= float(6.9):
        strongMag.append(magnitude)
    elif magnitude >= float(5) and magnitude <= float(5.9):
        moderateMag.append(magnitude)


def earthquakeStats(file):
    removeHeader = file.readline()  # This removes the header of the file.
    for line in file:
        splitLine = line.split('\t')
        region = splitLine[6]
        if region not in regionNames:
            regionNames.append(region)
        else:
            pass
        magnitude = splitLine[1]
        sortMag(magnitude)
