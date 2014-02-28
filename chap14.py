# This is where chapter 14 exercises go.

def sed(patstr, repstr, file1, file2):
	fin1 = open(file1)
	fin2 = open(file2, 'w')
	for line in fin1:
		if line.strip() == patstr:
			fin2.write(repstr+'\n')
		else:
			fin2.write(line)

sed('hi', 'hello', 'first_file.txt', 'second_file.txt')
