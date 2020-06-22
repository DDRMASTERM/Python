# Return a string that is full name
def full_name(first, last, middle=''):
	'''Take two required as strings, optional third argument as string.
	returns combined string'''
	if middle:
		name = f"{first.title()} {middle.title()} {last.title()}"
	else:
		name = f"{first.title()} {last.title()}"
	return name
	
print(f"Hello, {full_name('jonas', 'mike', 'johnson')}!")
print(f"Hello, {full_name('jane', 'smith')}!")

n = full_name('jay', 'bob')
print("Hello, "+n+"!")
print("Hello, %s!" %n)
