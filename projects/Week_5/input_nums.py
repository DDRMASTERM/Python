try:
	num1 = int(input("First number: "))
	num2 = int(input("Second number: "))
	print(int(num1)+ int(num2))
	
except ValueError:
	print("Please use integers")
