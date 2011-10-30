# 2: Use the readline method to write your own myReadlines function. Your function myReadlines should take an open file as a parameter and a number n and return a 
# list of n lines that were read, where each list item is a line. 

def myReadlines(openfile, number):
    listoflines = []
    cc = 0
    for item in range(0,number):
       listoflines.append(openfile.readline())
    #listoflines = listoflines[:number]
    for item in listoflines:
       if item == "":
            cc = cc + 1
       elif item != "":
            pass
    lenoflist = len(listoflines)
    if cc > 1:
        listoflines = listoflines[:(lenoflist-cc)]
    else:
        pass
    return listoflines

# 3: Write a function that opens a web page & returns a dictionary of all the links
# and their text on that page. A link is defined by an HTML tag. The link is
# everything in quotes after the "<a href=" and before ">", and the text is 
# everything between the > and </a>. Use the following algorithm to process the page
# 
# Open the web page.
# While there remains some characters in line:
# 	i. if line contains <a href=
# 		a. slice line so that everyting up to <a href= is removed
#		b. find >
#		c. url = text from beginning of line to the character before >
# 		d. print url
#		e. slice line so that > is removed
# 		f. find </a>
#		g. text = text from beginning of line to the character before </a>
#		h. print text
# 		i. add {url:text}
#	ii. else truncate line
#
# The resulting dictionary is to be written to an output txt file, where each dict
# element (pair) is written on a new line. You can assume that all html tags are all
# in lower case. Download the test file 'Test.html' to test the code.


import urllib
def getUrls(webpage):
    url = webpage
    page = urllib.urlopen(url)
    url_list = {}
    for line in page:
        if '<a href=' in line:
            removeHref = line[8:]
            end = removeHref.find('>')
            url = removeHref[0:end]
            removeHref = removeHref[end+1:]
            print url 
            #print removeHref
            end2 = removeHref.find('<')
            text = removeHref[0:end2]
            print '%s \n' % text
            url_list[url] = text
    #return url_list
        else:
            pass
    f = open('output.txt','w')
    for item in url_list.iteritems():
        f.writelines(str(item)+'\n')
    f.close()

