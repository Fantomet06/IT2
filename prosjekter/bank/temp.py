# Creating a Base class
class Base:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")

# Creating a derived class


class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)

	def call_public(self):

		# Calling public method of base class
		print("\nInside derived class")
		self.fun()

	def call_private(self):

		# Calling private method of base class
		self.__fun()


# Driver code
obj1 = Base()

# Calling public method
obj1.__fun()
