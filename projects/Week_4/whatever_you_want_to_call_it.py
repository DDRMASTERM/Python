nums = {1: 'one',
		2: 'two',
		3: 'three',
		'four': 4,
		'five': 5,
		'six': 6
		}
		
print(nums[2]+ nums[3])
print(nums['four'] + nums['five'])

##for n in nums.items():
##	print(n)
	
for k, v in nums.items():
	print(f'Name: {k} \n\tValue:{v}')

for k in nums.keys():
	print(k)
	
for v in nums.values():
	print(v)
