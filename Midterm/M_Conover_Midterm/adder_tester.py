import word_adder

# Basic Test
print(word_adder.add("seven", "seven"))

# Test for capitalized words
print(word_adder.add("Zero", "TEN"))

# Test for Int input
print(word_adder.add(7, 8))

# Tests for one Int
print(word_adder.add("zero", 4))
print(word_adder.add(9, "four"))

# Test for invalid strings
print(word_adder.add("eleven", "fourteen"))

# Tests for one invalid string
print(word_adder.add("Fourty", "four"))
print(word_adder.add("four", "4"))
