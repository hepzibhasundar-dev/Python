#using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)
#Using range() to make a list of even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
#Using range() to make a list of squaressquares = []
for value in range(1,11):
    square = value ** 2
    # squarevalues.append(square)
    print(square)
#Using list comprehension to make a list of squares
squares = [value ** 2 for value in range(1,11)]
print(squares)  
#slicing a list of numbers
digits = list(range(10))
print(digits)
print(digits[0:3])
print(digits[1:4])
print(digits[:4])
print(digits[4:7])
print(digits[7:10])

#statistics with a list of numbers
digits = list(range(10))
print(digits)
print(f"Minimum: {min(digits)}")
print(f"Maximum: {max(digits)}")
print(f"Sum: {sum(digits)}")

#List comprehensions
squares = [value ** 2 for value in range(1,11)]
print(squares)

#counting to 20 : use a for loop to print the numbers from 1 to 20, inclusive
for value in range(1,21):
    print(value)

#one million : make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
# numbers = list(range(1,1000001))
numbers = list(range(1,101)) # for testing purposes just to print the first 100 numbers
for number in numbers:
    print(number)

#summation : make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
numbers = list(range(1,1000001))
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

#odd numbers : use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

#threes : make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
threes = list(range(3,31,3))
for number in threes:
    print(number)

#cubes : make a list of the cubes from 1 to 10. Use a for loop to print out the value of each cube.
cubes = [value ** 3 for value in range(1,11)]
for cube in cubes:
    print(cube)

#cube comprehension : use a list comprehension to generate a list of the cubes from 1 to 10. Use a for loop to print out the value of each cube.
cubes = [value ** 3 for value in range(1,11)]
for cube in cubes:
    print(cube)

#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[4:7])
print(players[7:10])

print(players[-3:])
print(players[:4])
print(players[2:])

#looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # This creates a copy of the list
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# To prove that we have two separate lists, let's add a new food to each list.
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Pizzas:  Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ['pepperoni', 'mushroom', 'pineapple']
for pizza in pizzas:
    print(pizza)
# Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in pizzas:
    print(f'I like {pizza} pizza.')
print("I really love pizza!")

#4-10: slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#Print the message The first three items in the list are: Then use a slice to print
#the first three items from the list.
#Print the message Three items from the middle of the list are: Then use a slice to
#print three items from the middle of the list.
#Print the message The last three items in the list are: Then use a slice to print
#the last three items in the list.
print("The first three items in the list are:")
print(pizzas[:3])
print("Three items from the middle of the list are:")
print(pizzas[1:4])
print("The last three items in the list are:")
print(pizzas[-3:])

#4-11: my pizzas, your pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#Add a new pizza to the original list. Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
my_pizzas = ['pepperoni', 'mushroom', 'pineapple']
friend_pizzas = my_pizzas[:]  # Create a copy of the list

# Add a new pizza to the original list
my_pizzas.append('hawaiian')

# Add a different pizza to the list friend_pizzas
friend_pizzas.append('bbq chicken')

# Print the messages and lists
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12: more loops: All of the loops in this chapter have ended with a colon and have been followed by an indented block of code. This structure is called a loop construct. The first line of the loop construct is often called the header, and the indented block of code is called the body. The header tells Python to repeat the body once for every item in the list. The body is the code that runs once for each item in the list. Write a program that prints the header My favorite pizzas are:, and then uses a for loop to print each pizza in a list of your favorite pizzas. Make sure to include a line at the end of your program, 
# outside the for loop, that states how much you like pizza.
print("I really love pizza!")


#Tuples:  A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 # This will raise an error because tuples are immutable
# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

#4-13: buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
buffet = ('rice', 'beans', 'chicken', 'salad', 'bread')
# Use a for loop to print each food the restaurant offers.
for food in buffet:
    print(food)
# Try to modify one of the items, and make sure that Python rejects the change.
# buffet[0] = 'pasta' # This will raise an error because tuples are immutable
# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
buffet = ('pasta', 'beans', 'fish', 'salad', 'bread')
for food in buffet:
    print(food)
#4-14: ages: Store the ages of a group of people you know in a tuple. Print each person's age by looping through the tuple.
ages = (25, 30, 35, 40, 45)
for age in ages:
    print(age)

#4-15: dimensions: Store the width and height of a rectangle in a tuple, and print these values. Can you write a loop that prints each of the dimensions stored in the tuple?
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
#4-16: modified dimensions: Start with the program you wrote for Exercise 4-15. Store the same width and height in a tuple, and then modify the tuple values by writing over the existing tuple with a new tuple. Print the modified values.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
#4-14, PEP 8: style guide: Review the style guidelines for Python code in PEP 8. Write a program that has two function definitions and an import statement. The program should be well formatted according to PEP 8, and should have no more than two blank lines in a row. Run the program, and make sure it runs without error.
import math
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2
def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius
radius = 5
area = calculate_area(radius)
circumference = calculate_circumference(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}.")
print(f"The circumference of a circle with radius {radius} is {circumference:.2f}.")

#4-15, PEP 8: style guide: Choose two of the programs you wrote in this chapter, and modify each so the function name and variable names are more descriptive. Run the program to make sure it still runs correctly.
def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def calculate_circumference_of_circle(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius 
radius_of_circle = 5
area_of_circle = calculate_area_of_circle(radius_of_circle)
circumference_of_circle = calculate_circumference_of_circle(radius_of_circle)
print(f"The area of a circle with radius {radius_of_circle} is {area_of_circle:.2f}.")
print(f"The circumference of a circle with radius {radius_of_circle} is {circumference_of_circle:.2f}.")

#4-15, code review: If you have not already done so, review the style guidelines for Python code in PEP 8. Choose two of the programs you wrote in this chapter, and modify each so the function name and variable names are more descriptive. Run the program to make sure it still runs correctly.    


