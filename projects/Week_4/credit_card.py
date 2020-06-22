# Matthew Conover
# IS 3750
# Assignment CC_Info

# Defining credit card dictionary
creditC = { "Edgeworth" : (1234567890123456, "01/2027", 555),
			"Peace" : (5555555555555555, "08/2025", 678),
			"Smith" : (1213141516171819, "05/2020", 735),
			"Louis" : (7777777777777777, "12/2021", 404) }

# Print elements of dictionary
for k,v in creditC.items():
	print(f"Last Name: {k}\nCredit Card Number: {v[0]}\n"
	f"Expiration month: {v[1]}\ncvv: {v[2]}\n")
	
