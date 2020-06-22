import logging

# Set up logging and logger file
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -'
							  ' %(message)s')

fh = logging.FileHandler("equationlogfile.log")
fh.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
sh.setFormatter(formatter)

# Comment out the addHandler(sh) to turn off logging to screen
logger.addHandler(fh)
# logger.addHandler(sh)



def equation_calc():
	'''Takes an equation string'''
	finished = False
	
	# Proper equation has not been received
	while not finished:
		
		# Take an input from the user as an equation
		inp = input("Enter a full equation using only two numbers: ")
		p1 = ""
		oper = ""
		p2 = ""
		i1 = 0
		i2 = 0
		o = False
		inp = inp.strip()
		
		# Divide the equation into appropriate variables
		for n in inp:
			
			# First equation operator was found
			if (n == '*' or n == '+' or n == '-' or n == '/') and not o:
				oper = n
				o = True
				
				# Take values before the first operator
			elif not o:
				p1 += n
				
				# Take values after the first operator
			else:
				p2 += n
				
		# Equation lacked an operator
		if not o:
			print("your equation lacks an operator")
			
		# Equation had proper syntax
		else:
			
			# Try to convert the values to ints
			try:
				i1 = int(p1)
				i2 = int(p2)
				r = calc(i1, oper, i2)
				
				# calc returned a valid answer
				if r is not None:
					finished = True
					
			# Equation did not have proper ints
			except ValueError:
				logger.warning(f"This function takes an equation including two numbers and an operator")
				print(f"{p1} and/or {p2} is not a valid number.")
	
	# Returns equation and result
	return f"{i1} {oper} {i2} = {r}"


def calc(i1, o, i2):
	'''Does calculations based on the equation'''
	
	# Default value in case of errors
	res = None
	
	# Do addition
	if o == '+':
		res = i1 + i2
		
	# Do multiplication
	elif o == '*':
		res = i1 * i2
		
	# Do subtraction
	elif o == '-':
		res = i1 - i2
		
	# Do division
	elif o == '/':
		
		# Check for divide by zero
		try:
			r = i1 / i2
			
			# If division results in a whole number return an int
			if r % 1.0 == 0.0:
				res = int(r)
			
			# Else return the float
			else:
				res = r 
			
		# If they divide by zero
		except ZeroDivisionError:
			logger.warning(f"Please do not divide by zero")
			
	# Returns result
	return res

# Run equation_calc function
print(equation_calc())
