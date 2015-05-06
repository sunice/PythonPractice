'makeTestFile.py -- create text fiel'

import os
ls = os.linesep

# get filename
print "Enter the file name"
while True:
	fname = raw_input('> ')
	if os.path.exists(fname):
		print "Error: '%s' already exists" % fname
	else:
		break

# get file context (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates inputs
while True:
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!!'