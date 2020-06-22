food = {'eggs', 'bacon', 'sausage'}
spam = 'spam'

if spam not in food:
	print("I don't like spam!")

else: 
	print("I love spam!")

##Python equivalent of Switch/case
if 'spam' in food:
  print("I like spam.")
elif 'ham' in food:
  print("I like ham.")
else:
  print("I don't like ham or spam.")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")       
print("\nFinished making your pizza!")
