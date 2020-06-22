## Matthew Conover
## Assignment 7-4
## IS 3750

prompt = "\nWhat toppings would you like:"
prompt += "\nEnter 'quit' to end the program. "
toppings = list()
active = True
while active: ## Take toppings until they quit
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        toppings.append(message)
        print("That topping has been added")

print("Your toppings are")#Print all the toppings
for e in toppings:
	print(e)
