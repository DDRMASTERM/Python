age = input("How old are you? ")

try:
	int(age)
except ValueError:
	print("Please use integers.")
	exit(0)

   
if 	 age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print(f"Your admission cost is ${price}.")


