import logging

# Set up logging and logger file
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -'
							  ' %(message)s')

fh = logging.FileHandler("adderlogfile.log")
fh.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
sh.setFormatter(formatter)

# Comment out the addHandler(sh) to turn off logging to screen
logger.addHandler(fh)
# logger.addHandler(sh)


def add(inp1, inp2):
	'''Take two words as inputs'''
	
	out = "Invalid Input"
	
	# Try .lower on the input
	try:
		s1 = inp1.lower()
		s2 = inp2.lower()
		i1 = 0
		i2 = 0
		
		# Convert the inputs into ints
		i1 = sConv(s1)
		i2 = sConv(s2)
		
		# Alternate responses for inputs not 0-10
		if i1 == -1 and i2 == -1:
			out = f"{s1} and {s2} are outside the range."
		elif i1 == -1:
			out = f"{s1} is outside the range"
		elif i2 == -1:
			out = f"{s2} is outside the range"
			
		# Both inputs are valid
		else:
			i3 = i1 + i2
			out = iConv(i3)
			
	# Inputs were not strings
	except AttributeError:
		logger.warning(f"AttributeError: Function input is two strings")
		
	# Return final result
	return out


def sConv(s):
	'''Convert input into an int between 0-10'''
	
	# Dictionary for converting strings to ints
	d = {
		"zero": 0,
		"one": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7,
		"eight": 8,
		"nine": 9,
		"ten": 10
			}
			
	# Return -1 if no match is found
	return d.get(s, -1)
	
	
def iConv(i):
	'''Convert input to a string between 0-20'''
	
	# Dictionary converting ints to strings
	d = {
		0: "zero",
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
		20: "twenty"
			}
			
	# Return empty string if no match is found
	return d.get(i, "")
