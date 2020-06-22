# Adds two numbers
def adder(num1, num2):
	'''Takes two arguments as integers. Returns sum'''
	try:
		s = int(num1) + int(num2)
		return s
	except ValueError:
		return 'NAN'
	
print(adder(20, 22))
print(adder('two', 'three'))
