top=['pepperoni', 'sausage', 'canadian bacon', 'chicken']

friend=list(top)

top.append('onions')
friend.remove('chicken')
friend.append('pineapple')

for n in top:
	print(n)
	
for f in friend:
	print(f)
