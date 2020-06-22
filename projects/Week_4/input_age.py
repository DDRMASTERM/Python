b = True

while b:
	
    try:
		
		
        age = int(input("How old are you? "))
        b = False
         
    except ValueError:
        print("Use integers please.")


if age < 4:
		price = 0
elif age < 18:
		price = 5
elif age < 65:
		price = 10
elif age >= 65:
		price = 5
print("Your admission cost is $%s." % price)
