class Person:
	'''Description of a person'''
	def __init__(self, f_name, l_name, age):
		'''The attributes of a person'''
		self.first_name = f_name
		self.last_name = l_name
		self.age = age
		self.hair = ''
		self.height = 0
		self.weight = 0
		
	def get_full_name(self):
		"""Returns the person's full name"""
		return self.first_name.title() + " " + self.last_name.title()
		
	def get_age(self):
		"""Returns the person's age"""
		return self.age
		
	def update_age(self, yrs):
		"""Updates the person's age"""
		self.age = yrs
		print("Happy birthday!")
		
	def set_hair(self, h):
		"""Set person hair"""
		self.hair = h
	
	def get_hair(self):
		"""Get person hair"""
		return f"{self.get_full_name()}'s hair color is {self.hair}"

class Kid(Person):
	"""A model of a miniature person"""
	def __init__(self, f_name, l_name, age):
		"""Initial the parent class Person"""
		super().__init__(f_name, l_name, age)
		if age >= 18:
			print("You are not a kid.")
			
	def update_age(self, yrs):
		"""Updates a person's age"""
		if yrs <= self.age:
			print("It's not nice to lie about your age.")
		elif yrs >= 18:
			print("You are no longer a kid.")
		else:
			self.age = yrs
			print("Happy birthday %s!" % self.get_full_name())
