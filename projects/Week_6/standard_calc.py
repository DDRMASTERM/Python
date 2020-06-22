## Matthew Conover
## Standard Calculator
## IS 3750

s=False
out=0
while s==False:
	try: 
		i1=int(input("Enter First Number: ")) ##Take first number
		i2=int(input("Enter Second Number: ")) ##Take second number
		while s==False:
			op=input("Enter a function (+-/*): ") ## Take operation
			if op == "+": ##addition
				out=i1+i2
				s=True
			elif op == "-":##subtraction
				out=i1-i2
				s=True
			elif op == "/":##division
				out=i1/i2
				s=True
			elif op == "*":##multiplication
				out=i1*i25
				s=True
			else:##invalid choice
				print("That was not an operation")
	except ValueError:##Did not enter a number
		print("That was not a number")

#Print result
print(f"{i1} {op} {i2} = {out}")
	
