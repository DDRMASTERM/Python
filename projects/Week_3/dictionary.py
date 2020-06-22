desserts= {'france': 'crepes',
	   'netherlands': 'donuts',
	   'italy': 'gelato',
	   'germany': 'funnel cake',
	   'france': 'macaron'}
print(f'I like {desserts["italy"]}')
my_favs = {'cars' : ['VW', "BMW"],
 'colors' : ['red', 'blue', 'green'],
  'numbers' : [7, 11]
  }
  
print(my_favs['numbers'][-1])

my_favs['numbers'][-1]=42

print(my_favs['numbers'])

my_favs['desserts']=['scones', 'crepes', 'gelato']

print(my_favs)

##del my_favs['numbers']

##print(my_favs)

del my_favs['cars'][1]

print(my_favs)

for k in sorted(my_favs.keys()):
	print(k)
