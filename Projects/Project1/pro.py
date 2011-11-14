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

    for line in f:
        split = line.split('\t')
        place = split[6]
        if place not in name:
            name.append(place)
        else:
            pass

    for i in name:
        greatMag.append(0)
        majorMag.append(0)
        strongMag.append(0)
        moderateMag.append(0)

    f.seek(postHeader)  # Go to the spot after reading the header

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
    outputname.write("%s\t %s\t %s\t %s\t %s\n" % ('REGION', 'MODERATE',
    'STRONG', 'MAJOR', 'GREAT'))
    #outputname.write('\n')

    for item in range(0, len(name)):
        outputname.writelines('%s\t %s\t %s\t %s\t %s\n' % (name[item],
        moderateMag[item], strongMag[item], majorMag[item], greatMag[item]))
