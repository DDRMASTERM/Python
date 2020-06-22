# Matthew Conover
# IS 3750
# User_authentication module

# Store the file's elements into a dictionary
file_name = 'user_list.txt'
userDictionary = {}
with open(file_name) as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		entry = line.split(' : ')
		userDictionary[entry[0]] = entry[1]


def auth (username, password):
	'''Check if username is present and if password is valid'''
	result = ''
			
	# Username is in the dictionary
	if username in userDictionary:
		
		# Password is correct
		if userDictionary.get(username) == password:
			result = 'success'
			
		# Password is incorrect
		else:
			result = 'bad pass'
	
	# No User is in the dictionary
	else:
		result = 'no user'	
	
	# Return if any matches were found	
	print(result)
	return result
	
def add_user (username, password):	
	'''Add a new user and their password'''
	
	# Append new user to the text file as a new line
	with open(file_name, 'a') as f:
		f.write(f"\n{username} : {password}")

