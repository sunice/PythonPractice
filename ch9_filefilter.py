"""
Show each line of a file, ignore the lines started with #
"""

filename = raw_input("Enter file name: ")
fp = open(filename, 'r')

for eachline in fp:
	if eachline[0] != "#":
		print eachline,

fp.close()
