# This is where chapter 14 exercises go.

import urllib

# 14.2

def sed(patstr, repstr, file1, file2):
	fin1 = open(file1)
	fin2 = open(file2, 'w')
	for line in fin1:
		if line.strip() == patstr:
			fin2.write(repstr+'\n')
		else:
			fin2.write(line)
	fin1.close()
	fin2.close()

#sed('hi', 'hello', 'first_file.txt', 'second_file.txt')


# 14.6
#Build the url you will need to use to get information
def buildurl():
	zipcode = raw_input('Enter Zipcode --> ')
	compurl = 'http://www.uszip.com/zip/' + zipcode
	return compurl

def zipinfo():
	myurl = buildurl()
	conn = urllib.urlopen(myurl)
	for line in conn:
		stripline = line.strip()
		title = stripline.find('<title>')
		population = stripline.find('Total population')
		if title == 0:
			end = stripline.find(',')
			print stripline[7:end]
		if population != -1:
			popend = stripline.find('<span', population)
			print stripline[population+25:popend]
			
zipinfo()