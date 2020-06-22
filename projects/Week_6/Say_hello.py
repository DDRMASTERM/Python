# Say hello to someone formally
def say_hello(first='world', last=''):
	'''Takes two arguments as string, print to screen'''
	if last:
		print(f"Hello, {first.title()} {last.title()}!")
	else:
		print(f"Hello, {first.title()}!")
	
say_hello('john', 'doe')
say_hello(last='johnson', first='cave')
say_hello("yamcha")
say_hello()
