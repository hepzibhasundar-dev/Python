#user input and while loop
prompt = "Tell me something, and I will repeat it back to you: "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

#using a flag
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False  
    else:        print(message)
#using break to exit a loop
while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(message)
#using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#input() always returns a string, so if you want to work with numbers, you need to convert the string to an int or a float.
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")
#ask user to enter some text, and displays the text in all uppercase letters.
message = input("Enter some text: ")
print(message.upper())
#using int() to get numerical input from a user, and then doing something with that input.
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:    print("\nYou'll be able to ride when you're a little older.")
#the modulo operator can be used to determine if a number is even or odd.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")
#7-1: rental car: write a program that asks the user what kind of rental car they would like. Print a message about that car, such as "Let me see if I can find you a Subaru."
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")
#7-2: restaurant seating: write a program that asks the user how many people are in their dinner group. If the answer is more than 8, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.
people = input("How many people are in your dinner group? ")
people = int(people)
if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
#7-3: multiples of ten: ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")
#7-4: pizza toppings: write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.
prompt = "Enter a pizza topping (or 'quit' to finish): "    
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Adding {topping} to your pizza.")
#while loop in action: write a program that asks the user how many people they need to invite to a party. If the number is more than 10, print a message saying they'll have to find a bigger place. Otherwise, print a message saying the number of people they can invite.
people = input("How many people do you need to invite to your party? ")
people = int(people)
if people > 10:
    print("You'll have to find a bigger place.")
else:
    print("You can invite that many people.")   
#while loop in action: counting to 20: write a program that uses a while loop to print the numbers from 1 to 20, inclusive.
current_number = 1
while current_number <= 20:
    print(current_number)
    current_number += 1
#avoiding infinite loops: write a program that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza. Make sure to use a break statement to exit the loop when the user enters 'quit'.
prompt = "Enter a pizza topping (or 'quit' to finish): "
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Adding {topping} to your pizza.")
#7-4: pizza toppings: write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.
prompt = "Enter a pizza topping (or 'quit' to finish): "
topping = ""
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
#7-5: movie tickets: write a program that asks users how old they are, and then tells them the cost of their movie ticket based on their age. If they are under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over the age of 12, the ticket is $15.
age = input("How old are you? ")
age = int(age)
if age < 3:
    print("Your ticket is free.")
elif age >= 3 and age <= 12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")
#7-6: three exits: write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once: use a conditional test in the while statement to stop the loop, use an active variable to control how long the loop runs, and use a break statement to exit the loop when the user enters a 'quit' value.
#version 1: using a conditional test in the while statement to stop the loop
prompt = "Enter a pizza topping (or 'quit' to finish): "
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Adding {topping} to your pizza.")
#version 2: using an active variable to control how long the loop runs
prompt = "Enter a pizza topping (or 'quit' to finish): "
active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
#version 3: using a break statement to exit the loop when the user enters a 'quit' value
prompt = "Enter a pizza topping (or 'quit' to finish): "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
#7-7: infinity: write a loop that never ends, and run it. (To end the loop, press Ctrl-C or close the window displaying the output.)
while True:    print("This loop will never end!")
#using while loops with lists and dictionaries: moving items from one list to another
#start with users that need to be verified, and an empty list to hold confirmed users.  
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#verify each user until there are no more unconfirmed users. Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#start with a list of pets that need to be adopted, and an empty list to hold adopted pets.
pets = ['dog', 'cat', 'rabbit', 'hamster']
adopted_pets = []
#simulate adopting each pet until there are no more pets to adopt. Move each adopted pet into the list of adopted pets.
while pets:
    current_pet = pets.pop()
    print(f"The {current_pet} has been adopted.")
    adopted_pets.append(current_pet)
#display all adopted pets.
print("\nThe following pets have been adopted:")
for adopted_pet in adopted_pets:
    print(adopted_pet.title())
#removing all instances of specific values from a list
#start with a list of pets that includes multiple instances of 'cat'
pets = ['dog', 'cat', 'rabbit', 'cat', 'hamster']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#Filling a dictionary with user input
responses = {}
#Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store the response in the dictionary.
    responses[name] = response
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Display the results of the poll.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
#7-8: Deli: make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich". As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['tuna', 'ham', 'veggie', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)    
#7-9: no pastrami: make a list called sandwich_orders and fill it with the names of various sandwiches, including 'pastrami' at least three times. Then make an empty list called finished_sandwiches. Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders, and print a message saying "Sorry, we're out of pastrami." Then use another while loop to make the sandwiches, and move them to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'veggie', 'pastrami', 'chicken']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry, we're out of pastrami.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)    
#7-10: dream vacation: write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Display the results of the poll.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
