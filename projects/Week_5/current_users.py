## Matthew Conover
## Assignment 5-10
## IS 3750

current_users = ['FuzzyPickle', 'TheDoc', 'GreatSaiyaM', 'FoxOnly', 'Drake']
new_users = ['SpanishInquisition', 'spamLover', 'Romans', 'draKe', 'KnightOfNi']
f = 0
current_lower = list()

for i in current_users:
	current_lower.append(i.lower())
	
for i in new_users:
	if i.lower() not in current_lower:
		print("That name is valid")
	else:
		print("That name is already taken")
