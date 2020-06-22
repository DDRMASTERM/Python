## Matthew Conover
## Logic Calculator
## IS 3750

s=False
comp=""
while s==False:
	try:##Take two inputs
		i1=int(input("Enter First Number: "))
		i2=int(input("Enter Second Number: "))
		s=True
	except ValueError:##Input was not a number
		print("That was not a number")

if i1 == i2:##If input 1 equals input 2
	comp="is equal to"
elif i1 > i2:##If input 1 is greater than input 2
	comp="is greater than"
else:##If input 1 is less than input 2 
	comp="is less than"
	
#Output the result
print(f"{i1} {comp} {i2}")
