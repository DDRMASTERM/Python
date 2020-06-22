food=["spam", "eggs", "bacon", "cheese"]

print(food[0],food[1],food[2],food[3]) 
print(food[-1],food[-2],food[-3],food[-4])
print(food[0].title())

message=f"My favorite food is not {food[0].upper()}!"
food[2]="sausage"
print(message) 

food.append('hash browns')
food.insert(2,'salsa')
print(food)

del food[2]
print(food)

optional=food.pop()
print(food,optional)

hate = food.pop(0)
print("I don't like "+hate+"!")

foods=["spam","eggs","spam","cheese","spam"]
foods.remove('spam')
print(foods)

foods.append("hot salsa")
foods.sort()
print(foods)

foods.sort(reverse=True)
print(foods)

foods=["spam","eggs","spam","cheese","spam"]
foods2=sorted(foods)
print(foods2)

foods3=sorted(foods,reverse=True)
print(foods3)

nums=['one',2,'three',4,'five']
print(nums)
print(nums[1]+nums[3])
print(nums[0]+nums[2])
print(len(nums))
