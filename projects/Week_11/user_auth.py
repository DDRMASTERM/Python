import login

# Take username
username = input("Enter a username: ")

# Take password
password = input("Enter a password: ")
logAtt = login.auth(username, password)

# Match was found
if logAtt == 'success':
	print("Login Successful")

# Name was found but password was invalid
elif logAtt == 'bad pass':
	
	# 3 additional tries allowed
	for i in range(0, 3):
		print(f"Incorrect: {3-i} tries remaining")
		password = input("Enter a password: ")
		
		# Password is correct
		if login.auth(username, password) == 'success':
			print("Login Successful")
			break
			
		# Password was incorrect
		else:
			
			# Attempts ran out
			if i == 2:
				print("Your account has been locked")

# No user was found	
elif logAtt == 'no user':
	print("That name does not exist")
	
	# Does user want to create a new account?
	new = input("Create a new account (yes/y or no/n): ")
	
	# User chose yes
	if new == 'yes' or new == 'y':
		login.add_user(username, password)
		print("Your account was created")
	
	# User did not choose yes
	else:
		print("Goodbye")


