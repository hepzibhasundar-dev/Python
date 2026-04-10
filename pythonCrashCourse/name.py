#String methods
name = "hepzibha sundararaj"
print(name.title())  # Capitalizes the first letter of each word
print(name.upper())  # Converts all characters to uppercase
print(name.lower())  # Converts all characters to lowercase
print(name.strip())  # Removes leading and trailing whitespace
print(name.replace(" ", "_"))  # Replaces spaces with underscores
print(name.split())  # Splits the string into a list of words

first_name = "hepzibha"
last_name = "sundararaj"
full_name = f"{first_name} {last_name}"
print(full_name.title())  # Capitalizes the first letter of each word in full name

#newline character \n is used to create a new line in a string
print("Hello\nWorld")  # This will print "Hello" and "World" on separate lines

#tab character \t is used to create a tab space in a string
print("Hello\tWorld")  # This will print "Hello" and "World" with a tab space in between    

#backslash character \\ is used to include a backslash in a string
print("This is a backslash: \\")  # This will print "This is a backslash: \"

#raw string is used to ignore escape characters in a string
print(r"This is a raw string: \n\t\\")  # This will print "This is a raw string: \n\t\\"    

#String concatenation with variables
first_name = "hepzibha"
last_name = "sundararaj"
full_name = f"{first_name} {last_name}"
print(full_name.title())  # Capitalizes the first letter of each word in full name

#String formatting with variables
name = "hepzibha"
print(f"Hello, {name.title()}!")  # This will print "Hello, Hepzibha!"

#String formatting with variables and expressions
name = "hepzibha"
age = 25
print(f"Hello, {name.title()}! You are {age} years old.")  # This will print "Hello, Hepzibha! You are 25 years old."   

#rstrip() method is used to remove leading whitespace from a string
name = "   hepzibha   "
print(name.rstrip())  # This will print "   hepzibha" (trailing whitespace removed)

#lstrip() method is used to remove leading whitespace from a string
name = "   hepzibha   "
print(name.lstrip())  # This will print "hepzibha   " (leading whitespace removed)

#strip() method is used to remove both leading and trailing whitespace from a string
name = "   hepzibha   "
print(name.strip())  # This will print "hepzibha" (both leading and trailing whitespace removed)        

#String methods with chaining
name = "   hepzibha   "
print(name.rstrip().lstrip())  # This will print "hepzibha" (both leading and trailing whitespace removed)        

#String methods with chaining and formatting
name = "   hepzibha   "
print(f"Hello, {name.strip().title()}!")  # This will print "Hello, Hepzibha!"

#String methods with chaining and formatting and expressions
name = "   hepzibha   "
age = 25
print(f"Hello, {name.strip().title()}! You are {age} years old.")  # This will print "Hello, Hepzibha! You are 25 years old."

#String methods with chaining and formatting and expressions and escape characters
name = "   hepzibha   "
age = 25
print(f"Hello, {name.strip().title()}! You are {age} years old.")  # This will print "Hello, Hepzibha! You are 25 years old."   

#String methods with chaining and formatting and expressions and escape characters and raw string
name = "   hepzibha   "
age = 25
print(rf"Hello, {name.strip().title()}! You are {age} years old.")  # This will print "Hello, Hepzibha! You are 25 years old."      

#remove() method is used to remove a specific substring from a string
name = "hepzibha sundararaj"
print(name.removeprefix("hepzibha"))  # This will print " sundararaj" (removes "hepzibha" and leaves a space before "sundararaj")
print(name.removesuffix("sundararaj"))  # This will print "hepzibha " (removes "sundararaj" and leaves a space after "hepzibha")    
#name = "hepzibha sundararaj"
#print(name.remove("hepzibha"))  # This will print " sundararaj" (removes "hepzibha" and leaves a space before "sundararaj")

print(name.replace("hepzibha", ""))  # This will print " sundararaj" (removes "hepzibha" and leaves a space before "sundararaj" )
print(name.rfind("sundararaj"))  # This will print the index of the last occurrence of "sundararaj" in the string, which is 9
print(name.find("sundararaj"))  # This will print the index of the first occurrence of "sundararaj" in the string, which is 9
print(name.count("sundararaj"))  # This will print the number of occurrences of "sundararaj" in the string, which is 1      

#multiple assignments
first_name, last_name = "hepzibha", "sundararaj"    
print(f"First Name: {first_name}, Last Name: {last_name}")  # This will print "First Name: hepzibha, Last Name: sundararaj" 

#constant variable
PI = 3.14159  # This is a constant variable, conventionally written in uppercase letters to indicate that it should not be changed
print(f"The value of PI is {PI}")  # This will print "The value of PI is 3.14159"

