from people import Person, Kid

john = Person('John', 'Doe', 103)
jane = Person('Jane', 'Doe', 104)

johnny = Kid('johnny', 'doe', 12)

john.update_age(104)
Person.update_age(johnny, 13)
johnny.set_hair("blonde")
print(johnny.get_hair())
johnny.update_age(11)
print(johnny.get_age())

