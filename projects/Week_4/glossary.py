# Matthew Conover
# IS 3750
# Assignment 6-3

# Defining glossary
gloss = { "String" : "A variable made of several characters",
			"list" : "A variable that stores several other variables and may be changed later",
			"Run" : "Executing a program's code",
			"If" : "A piece of code that runs only when it meets its condition(s)",
			"For" : "A loop that runs until its goes through its defined range or variables" }

# Printing the variables of the glossary
for k,v in gloss.items():
	print(f"{k}: {v}\n")
