from time import ctime, sleep


def tsfunc(func):
	def wrapped_func():
		print '[%s] %s() called' % (ctime(), func.__name__)
		return func()
	return wrapped_func


@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()