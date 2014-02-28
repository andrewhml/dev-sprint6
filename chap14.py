# This is where chapter 14 exercises go.

def sed(patstr, repstr, file1, file2):
	fin1 = open(file1)
	try:
		fin2 = open(file2)
	except IOError:
		print 'IOError'


sed('hi', 'hello', 'filetext.txt', 'bad_file.txt')
