class FooClass(object):
	"""docstring for FooClass"""
	version = 0.1
	def __init__(self, arg='John Doe'):
		self.name = arg
		print "Created a class instance for", arg
	def showname(self):
		print "Your name is", self.name
		print "My name is", self.__class__.__name__
	def showver(self):
		print self.version
	def addMe2Me(self, x):
		return x + x

fool = FooClass()
fool.showname()
fool.showver()
print fool.addMe2Me(5)
print fool.addMe2Me("xyz")

foo2 = FooClass('Jane Smith')
foo2.showname()