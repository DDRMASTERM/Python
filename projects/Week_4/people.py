# Matthew Conover
# IS 3750
# Assignment 6-7

# defining the dictionaries
person1 = { "first_name" : "Kayla",
			"last_name" : "Conover",
			"age" : 25,
			"city" : "Idaho Falls" }
			
person2 = { "first_name" : "Robert",
			"last_name" : "Pixton",
			"age" : 34,
			"city" : "San Jose" }
			
person3 = { "first_name" : "Ben",
			"last_name" : "Pixton",
			"age" : 30,
			"city" : "Idaho Falls" }

# Storing dictionaries in a list		
people = [person1, person2, person3]

# Go through each item of the list
for person in people:
	
	#Print elements in each dictionary
	for k,v in person.items():
		
		#if element is final in dictionary
		if k == "city":
			print(f"{k}: {v}\n")
		
		#print regularly
		else:
			print(f"{k}: {v}")

