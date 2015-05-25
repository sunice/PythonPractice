def display_num_type(num):
	print num, 'is',
	if isinstance(num, (int, long, float, complex)):
		print 'a number of type:', type(num).__name__
	else:
		print 'not a number at all!'

display_num_type(-69)
display_num_type(999999999999999999999999999L)
display_num_type(0.09)
display_num_type(-8.9+0.9j)
display_num_type('xxx')