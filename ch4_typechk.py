
def displayNumType(num):
	print num, 'is',
	if isinstance(num, (int, long, float, complex)):
		print 'a number of type:', type(num).__name__
	else:
		print 'not a number at all!'

displayNumType(-69)
displayNumType(999999999999999999999999999L)
displayNumType(0.09)
displayNumType(-8.9+0.9j)
displayNumType('xxx')