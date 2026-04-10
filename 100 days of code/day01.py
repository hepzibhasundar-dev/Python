# Day one project
print("Hello world!"); #String of characters
# Day one project
print("Hello world!"); #String of characters
# Mix 500g of flour, 10g Yeast and 300ml of water in a bowl.
# Knead the dough for 10 minutes
# Add 3g of salt
# Leave to rise for 2hours.
#Bake at 200 degress for 30 minutes

#String manipulation
print("1. Mix 500g of flour, 10g Yeast and 300ml of water in a bowl.\n2. Knead the dough for 10 minutes\n3. Add 3g of salt\n4. Leave to rise for 2hours.\n5.Bake at 200 degress for 30 minutes")

# string concatenation with space in 3 ways
print("Hello" + " " + "world")
print("Hello", "world")
print("Hello" " " "world")
print("Hello "+ "world")
print("Hello" + " world")

# String formatting
name = "Alice"  
age = 30
print(f"My name is {name} and I am {age} years old.")
# String formatting with format method
print("My name is {} and I am {} years old.".format(name, age))
# String formatting with format method and positional arguments
print("My name is {0} and I am {1} years old.".format(name, age))
# String formatting with format method and keyword arguments
print("My name is {name} and I am {age} years old.".format(name=name, age=age))

# String formatting with format method and alignment
print("My name is {:<10} and I am {:>5} years old.".format(name, age))
# String formatting with format method and padding
print("My name is {:*^10} and I am {:0>5} years old.".format(name, age))

# String formatting with format method and precision
pi = 3.141592653589793
print("The value of pi is {:.2f}".format(pi))   

#input() function
name = input("What is your name? ")
print(f"Hello, {name}!")

#input() function with type conversion
age = int(input("What is your age? "))
print(f"Hello, {name}! You are {age} years old.")

#input() function with multiple inputs
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(f"Hello, {first_name} {last_name}!")

#variables and data types
name = "Alice"  # String    
age = 30  # Integer
height = 5.8  # Float
is_student = True  # Boolean
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

#len() function
name = "Alice"
print(f"The length of the name '{name}' is {len(name)}.")

