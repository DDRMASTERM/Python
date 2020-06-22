my_tuple=('1234567890', '13/87', '123')
print(my_tuple)
print(my_tuple[1])
##my_tuple[1]='f' you cannot change a single value in a tuple
my_tuple=('1234567890', '11/22', '123')
##my_tuple.reverse() and .sort will not work
print(sorted(my_tuple))
my_cc=list(my_tuple)

for t in my_tuple:
	print(t)

print(f"Credit card num:\t\t{my_tuple[0]}\nCVV:\t\t\t{my_tuple[2]}\nExp:\t\t\t{my_tuple[1]}")

for t in my_things
