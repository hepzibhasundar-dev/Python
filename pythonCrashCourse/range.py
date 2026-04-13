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
numbers = list(range(1,101))
for number in numbers:
    print(number)


