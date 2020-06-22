spam = True
while spam:
	ans=input("Do you like green eggs and spam? ")
	if (ans.lower() == 'yes') or (ans.lower() == 'y'):
		print("Spam!")
		spam = False
	else:
		print("I do not like green eggs and spam, I do not like them Sam I am!")
