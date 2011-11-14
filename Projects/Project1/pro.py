# Name: Thyrus Gorges
# Access ID: eo8112


def earthquakeStats(file):
    f = open(file, 'r')

    removeHeader = f.readline()  # Removes the header of the file
    postHeader = f.tell()

    name = []  # List of all the region names
    greatMag = []  # Magnitudes of 8+
    majorMag = []  # Magnitudes between 7 - 7.9
    strongMag = []  # Magnitudes between 6 - 6.9
    moderateMag = []  # Magnitudes between 5 - 5.9

# Below adds all of the region names to a list
    for line in f:
        split = line.split('\t')
        place = split[6]
        if place not in name:
            name.append(place)
        else:
            pass

# The below adds zeros to each magnitude list for counting
    for i in name:
        greatMag.append(0)
        majorMag.append(0)
        strongMag.append(0)
        moderateMag.append(0)

    f.seek(postHeader)  # Go to the spot after reading the header

# This for loop keeps the lists parallel with each other and adds 1 to the
# proper index based on the current region and its magnitude

    for line in f:
        split = line.split('\t')
        mag = float(split[1])
        place = split[6]
        placeIndex = name.index(place)
        if mag >= 8:
            greatMag[placeIndex] = greatMag[placeIndex] + 1
        elif mag >= 7 and mag <= 7.9:
            majorMag[placeIndex] = majorMag[placeIndex] + 1
        elif mag >= 6 and mag <= 6.9:
            strongMag[placeIndex] = strongMag[placeIndex] + 1
        elif mag >= 5 and mag <= 5.9:
            moderateMag[placeIndex] = moderateMag[placeIndex] + 1
        else:
            pass

    print('Please enter the name of the file where the out will be stored')
    filename = input('Please include the .csv extension: ')
    outputname = open(filename, 'w')
    outputname.write("%s\t %s\t %s\t %s\t %s\t %s\n" % ('REGION', 'MODERATE',
    'STRONG', 'MAJOR', 'GREAT', 'OVERALL'))  # This makes the header of the file
    #outputname.write('\n')

# This calculates the overall amount of earthquakes when used with a for loop
    def overall(x):
        total = []
        total.append(moderateMag[x])
        total.append(strongMag[x])
        total.append(majorMag[x])
        total.append(greatMag[x])
        amount = sum(total)
        return amount

# This creates the csv file
    for item in range(0, len(name)):
        a = str(name[item])[:-1]
        a = a[:-1]
        outputname.writelines('%s\t %s\t %s\t %s\t %s\t %s\n' % (a,
        moderateMag[item], strongMag[item], majorMag[item], greatMag[item],
        overall(item)))

# To-Do: Close the files at the end
