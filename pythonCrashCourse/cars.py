# Cars list
cars = ['audi', 'bmw', 'subaru', 'toyota']
# Looping through the list
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# Checking multiple conditions
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("Both are 21 or older.")
else:
    print("At least one is not 21 or older.")
# Checking for either condition
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("At least one is 21 or older.")
else:
    print("Neither is 21 or older.")
# Checking for special items
requested_toppings = ['mushrooms', 'extra cheese']
for topping in requested_toppings:
    print(f"Adding {topping} to the pizza.")
print("\nFinished making your pizza!")
# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping} to the pizza.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
#checing for equality
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Mushrooms are requested.")
if 'pepperoni' in requested_toppings:
    print("Pepperoni is requested.")
#checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
#boolean expressions
game_active = True
can_edit = False
#Using functions to find the length of a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(len(requested_toppings))
#5-1 conditional tests. Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#look closely at your results, and make sure you understand why each line evaluates to True or False.   
#create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
#checking for equality and inequality with strings
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#5-2 more conditional tests. You don't have to limit yourself to just cars. Write a series of conditional tests and include at least one True and one False result for each of the following:
#-Tests for equality and inequality with strings
#-Tests using the lower() function
#-Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#-Tests using the and keyword and the or keyword
#-Test whether an item is in a list
#-Test whether an item is not in a list
city = 'New York'
print("Is city == 'New York'? I predict True.")
print(city == 'New York')
print("\nIs city == 'Los Angeles'? I predict False.")
print(city == 'Los Angeles')
#Tests using the lower() function
name = 'Alice'
print("Is name == 'alice'? I predict True.")
print(name.lower() == 'alice')
print("\nIs name == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')
#Numerical tests
age = 30
print("Is age == 30? I predict True.")
print(age == 30)
print("\nIs age == 25? I predict False.")
print(age == 25)
#Numerical tests involving greater than and less than
print("\nIs age > 25? I predict True.")
print(age > 25)
print("\nIs age < 25? I predict False.")
print(age < 25)
#Numerical tests involving greater than or equal to and less than or equal to
print("\nIs age >= 30? I predict True.")
print(age >= 30)
print("\nIs age <= 25? I predict False.")
print(age <= 25)
#Tests using the and keyword and the or keyword
print("\nIs age > 25 and age < 35? I predict True.")
print(age > 25 and age < 35)
print("\nIs age > 35 or age < 25? I predict False.")
print(age > 35 or age < 25)
#Test whether an item is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print('mushrooms' in requested_toppings)
print("\nIs 'pepperoni' in requested_toppings? I predict False.")
print('pepperoni' in requested_toppings)
#Test whether an item is not in a list
print("\nIs 'mushrooms' not in requested_toppings? I predict False.")
print('mushrooms' not in requested_toppings)
print("\nIs 'pepperoni' not in requested_toppings? I predict True.")
print('pepperoni' not in requested_toppings)

#if statements
#simple if statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
#many lines of code can be indented under an if statement. The block of code that is executed when the condition is true is called the if block. Python uses indentation to determine which lines of code belong to the if block. All lines of code in the if block must be indented the same amount. The standard practice is to use four spaces for each level of indentation.    
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
#if-else statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are not old enough to vote.")
#if-else multiple lines of code
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are not old enough to vote.")

#if-else multiple blocks
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#The if-elif-else chain is a way to test multiple conditions. Python executes only one block of code in an if-elif-else chain. It runs the first block of code for which the condition is true and ignores the rest of the chain. If no condition is true, Python executes the block of code in the else statement. The else block is optional; you can omit it if you only want to test for certain conditions and don't need to take any action when those conditions are not met.
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
#multiple elif blocks
age = 65
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 65:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $5.")
#omitting the else block
age = 65
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 65:
    print("Your admission cost is $10.")
#testing multiple conditions
age = 65
if age < 4:
    print("Your admission cost is $0.")
if age < 18:
    print("Your admission cost is $5.")
if age < 65:
    print("Your admission cost is $10.")

#5-3 Alien Colors #1. Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#-Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
#-Write one version of this program that passes the if test and another that fails. The version that fails will have no output.)
#version that passes the if test
alien_color = 'green'
if alien_color == 'green':
    print("Player just earned 5 points!")

#version that fails the if test
alien_color = 'red'
if alien_color == 'green':
    print("Player just earned 5 points!")
#5-4: Alien Colors #2. Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#-If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
#-If the alien's color isn't green, print a statement that the player just earned 10 points.
#-Write one version of this program that runs the if block and another that runs the else block.
#version that runs the if block
alien_color = 'green'
if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien!")
else:
    print("Player just earned 10 points!")

#version that runs the else block
alien_color = 'red'
if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien!")
else:
    print("Player just earned 10 points!")
#5-5: Alien Colors #3. Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#-If the alien's color is green, print a message that the player earned 5 points.
#-If the alien's color is yellow, print a message that the player earned 10 points.
#-If the alien's color is red, print a message that the player earned 15 points.
#-Write three versions of this program, making sure each message is printed at least once.  
#version that prints the message for green
alien_color = 'green'
if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")
#version that prints the message for yellow
alien_color = 'yellow'
if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")
#version that prints the message for red
alien_color = 'red'
if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")
#5-6: Stages of Life. Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
#-If the person is less than 2 years old, print a message that the person is a baby.
#-If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#-If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#-If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#-If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#-If the person is age 65 or older, print a message that the person is an elder.
age = 25
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
#5-7: Favorite Fruit. Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#-Make a list of your three favorite fruits and call it favorite_fruits.
favorite_fruits = ['apples', 'bananas', 'oranges']
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
#write five if statements. Each should check whether a certain kind of fruit is in your list of favorite_fruits. If the fruit is in your list, the if block should print a statement, such as You really like bananas!  
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'mangoes' in favorite_fruits:
    print("You really like mangoes!")
if 'pineapples' in favorite_fruits:
    print("You really like pineapples!")
#using if statements to check for special items
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms to your pizza.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese to your pizza.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni to your pizza.")
    #pass
#checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping} to your pizza.")
else:
    print("Are you sure you want a plain pizza?")
#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
#5-8: Hello Admin. Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
#-If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#-Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
usernames = ['admin', 'eric', 'sarah', 'michael', 'jessica']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
#5-9: No Users. Add an if test to hello_admin.py to make sure the list of usernames is not empty.
#-If the list is empty, print the message We need to find some users!
if not usernames:
    print("We need to find some users!")
#-Remove all of the usernames from your list, and make sure the correct message is printed.
usernames = []
if not usernames:
    print("We need to find some users!")
#5-10: Checking Usernames. Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#-Make a list of five or more usernames called current_users.
current_users = ['john', 'jane', 'bob', 'alice', 'charlie']
#-Make a list of five or more usernames called new_users.
new_users = ['Dave', 'JANE', 'Mike', 'Alice', 'Sarah']
#-Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
#5-11: Ordinal Numbers. Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#-Store the numbers 1 through 9 in a list.
numbers = list(range(1, 10))
#-Loop through the list.
for number in numbers:
    #-Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
#-Write a separate if test for each number to determine its ordinal suffix. You can use a series of if-elif-else tests, or you might find it easier to use a dictionary that maps numbers to their ordinal suffixes.    
ordinal_suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
for number in numbers:
    suffix = ordinal_suffixes.get(number, 'th')
    print(f"{number}{suffix}")

#styling if statements. The style of your if statements can make a big difference in how easy they are to read. Here are some tips for styling if statements:
#-Use blank lines to separate if statements from the rest of your code.
#-Use consistent indentation to clearly indicate which lines of code are part of the if block.
#-Use spaces around the operators in your if statements to make them easier to read.
#-Use descriptive variable names to make it clear what the condition is checking for.   
#By following these styling tips, you can make your if statements easier to read and understand, which will help you and others who read your code in the future.   
#5-12: Styling If Statements. Review the programs you wrote for this section, and make sure each if statement is styled according to the guidelines in this section. If you find an if statement that is not styled properly, rewrite it to make it easier to read. 
#-If you are not sure whether an if statement is styled properly, compare it to the examples in this section and see if you can improve its styling.    
#The if statements in the previous exercises are already styled according to the guidelines, so there is no need to rewrite them. However, it's always a good idea to review your code and make sure it follows best practices for readability and maintainability. 
#5-13: Your Ideas. At this point, you're a pro at writing if statements and conditional tests. Now it's time to get creative!
#-Write a series of if statements that describe what you like to do in your free time. Make sure to include at least one if statement that evaluates to True and another that evaluates to False.
free_time_activities = ['reading', 'hiking', 'cooking']
if 'reading' in free_time_activities:
    print("I like to read in my free time.")
if 'swimming' in free_time_activities:
    print("I like to swim in my free time.")
else:
    print("I don't like to swim in my free time.")
