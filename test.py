j, k = 1, 2


def proc1():
	j, k = 3, 4
	print j, k
	k = 5


def proc2():
	j = 6
	proc1()
	print j, k

k = 7
proc1()
print j, k

j = 8
proc2()
print j, k
