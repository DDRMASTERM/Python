my_order = ['spam', 'eggs', 'sausage', 'spam', 'bacon', 'spam']
while 'spam' in my_order:
    print("I don't like spam!")
    my_order.remove('spam')
print(my_order)
