#Functions
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet('harry', 'hamster')
#8-1: Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
def display_message():
    """Display a message about what I'm learning."""
    print("I'm learning about functions in this chapter.")
display_message()
#8-2: Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(title):
    """Display a message about a favorite book."""
    print(f"One of my favorite books is {title}.")
favorite_book('Alice in Wonderland')

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#8-3: T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function.
def make_shirt(size, message):
    """Display a message about the shirt size and message."""
    print(f"The shirt size is {size} and the message is '{message}'.")
make_shirt('large', 'I love Python!')
#8-4: Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size='large', message='I love Python'):
    """Display a message about the shirt size and message."""
    print(f"The shirt size is {size} and the message is '{message}'.")
make_shirt()
make_shirt('medium')
make_shirt('small', 'Python is great!')
#positional arguments must be placed before keyword arguments in a function call. Otherwise, Python will raise a SyntaxError.
#8-5: Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country='Iceland'):
    """Display a message about the city and country."""
    print(f"{city} is in {country}.")
describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('New York', 'USA')
#multiple return values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#multiple function calls
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('john', 'hooker')
print(musician)
#order matters in functional arguments
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
#keyword arguments in a function call
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
#When you use a function, the values you pass are called arguments. The function definition has parameters that accept these arguments. In a function call, you can use positional arguments or keyword arguments. Positional arguments need to be in the same order as the parameters in the function definition, while keyword arguments can be in any order as long as they match the parameter names.   
#When you use keyword arguments in a function call, the order of the arguments does not matter. However, when you use positional arguments, the order of the arguments must match the order of the parameters in the function definition. If you mix positional and keyword arguments in a function call, make sure that all positional arguments come before any keyword arguments. Otherwise, Python will raise a SyntaxError.    
#Default values for parameters allow you to specify a default value for a parameter in the function definition. If the caller does not provide a value for that parameter, the default value will be used. This can make your functions more flexible and easier to use, as it allows you to call the function with fewer arguments when the default values are sufficient. 
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#Note:  When you use *args in a function definition, it allows the function to accept an arbitrary number of positional arguments. The *args parameter collects any additional positional arguments passed to the function into a tuple. This means that you can call the function with as many positional arguments as you like, and they will all be accessible within the function through the *args parameter.  
#When you use **kwargs in a function definition, it allows the function to accept an arbitrary number of keyword arguments. The **kwargs parameter collects any additional keyword arguments passed to the function into a dictionary. This means that you can call the function with as many keyword arguments as you like, and they will all be accessible within the function through the **kwargs parameter.    
#when you define a function, you can specify default values for parameters. This means that if the caller does not provide a value for that parameter, the default value will be used. This can make your functions more flexible and easier to use, as it allows you to call the function with fewer arguments when the default values are sufficient. 
#When you call a function, you can use positional arguments or keyword arguments. Positional arguments need to be in the same order as the parameters in the function definition, while keyword arguments can be in any order as long as they match the parameter names. If you mix positional and keyword arguments in a function call, make sure that all positional arguments come before any keyword arguments. Otherwise, Python will raise a SyntaxError. 
#When you define a function, you can specify default values for parameters. This means that if the caller does not provide a value for that parameter, the default value will be used. This can make your functions more flexible and easier to use, as it allows you to call the function with fewer arguments when the default values are sufficient. 
#When you use default values for parameters, you can call the function with fewer arguments than the number of parameters. The parameters that have default values will use those values if the caller does not provide a value for them. This can make your functions more flexible and easier to use, as it allows you to call the function with fewer arguments when the default values are sufficient.  
#This allows you to create functions that can be called with a varying number of arguments, making your code more flexible and adaptable to different situations.   
#This allows Python to continue interpreting positional arguments correctly.
#Equivalent function calls with positional and keyword arguments:
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
#Avoiding Argument Errors: If you call a function without the required arguments, Python will raise a TypeError. To avoid this, make sure to provide all the required arguments when calling a function. If a parameter has a default value, you can omit that argument when calling the function, and the default value will be used. However, if you omit an argument for a parameter that does not have a default value, Python will raise a TypeError. Always check the function definition to see which parameters are required and which have default values before calling the function. 
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('bulldog')
describe_pet('bulldog', 'dog')
describe_pet('harry', 'hamster')

#8-3: T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function.
def make_shirt(size, message):
    """Display a message about the shirt size and message."""
    print(f"The shirt size is {size} and the message is '{message}'.")

make_shirt('medium', 'Hello, World!')

#8-4: Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size='large', message='I love Python'):
    """Display a message about the shirt size and message."""
    print(f"The shirt size is {size} and the message is '{message}'.")
make_shirt()
make_shirt('medium')
make_shirt('small', 'Python is great!')
#8-5: Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country='Iceland'):
    """Display a message about the city and country."""
    print(f"{city} is in {country}.")
describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('New York', 'USA')
#Return values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#Making an Argument Optional: Sometimes you may want to make an argument optional. To do this, you can give the parameter a default value. If the caller doesn't provide a value for that parameter, the default value will be used. This allows you to call the function with fewer arguments when the default values are sufficient.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()    
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('john', 'hooker')
print(musician)
#Returning a Dictionary: A function can return any kind of value you need it to, including more complex data structures like lists and dictionaries. For example, you can write a function that builds a dictionary representing a person, and then returns that dictionary.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
#using functions with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")   
    f_name = input("First name: ")
    if f_name == 'q':
        break 
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
    #8-6: City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city}, {country}"

print(city_country("Santiago", "Chile"))
print(city_country("Reykjavik", "Iceland"))
print(city_country("New York", "USA"))
#8-7: Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
def make_album(artist_name, album_title):
    """Return a dictionary describing a music album."""
    return {'artist': artist_name, 'album': album_title}

album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "Wish You Were Here")
album3 = make_album("Michael Jackson", "Thriller")

print(album1)
print(album2)
print(album3)
#8-8: User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.
def make_album(artist_name, album_title):
    """Return a dictionary describing a music album."""
    return {'artist': artist_name, 'album': album_title}
while True:
    print("\nPlease enter the artist and album title:")
    print("(enter 'q' at any time to quit)")
    
    artist = input("Artist name: ")
    if artist == 'q':
        break
    
    album = input("Album title: ")
    if album == 'q':
        break
    
    album_info = make_album(artist, album)
    print(album_info)
#passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#Modifying a List in a Function: You can also pass a list to a function and have the function modify the list. For example, you can write a function that takes a list of unprinted designs and prints each design until there are none left. As each design is printed, it is moved to a separate list of completed models.
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
def show_completed_models(completed_models):
    """Show all the models that have been printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#preventing a Function from Modifying a List: If you want to keep a function from modifying a list, you can pass a copy of the list to the function. This way, the function will work with the copy and leave the original list unchanged.
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print("\nUnprinted designs:")
print(unprinted_designs)
print("\nCompleted models:")
print(completed_models)
#8-9 Messages: Make a list of three short text messages, and then use a for loop to print each message.
messages = ["Hello, World!", "Welcome to Python programming.", "Functions are fun!"]    
#8-9 Message: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)
messages = ["Hello, World!", "Welcome to Python programming.", "Functions are fun!"]
show_messages(messages)
#8-10: Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello, World!", "Welcome to Python programming.", "Functions are fun!"]
sent_messages = []

send_messages(messages, sent_messages)
print("\nUnsent messages:")
print(messages)
print("\nSent messages:")
print(sent_messages)
#8-11: Archived Messages: Start with your work from Exercise 8-10. Call the send_messages() function, and then print both of your lists to make sure the messages were moved correctly. Then, call the send_messages() function again, and make sure that nothing happens to the lists this time.
def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = ["Hello, World!", "Welcome to Python programming.", "Functions are fun!"]
sent_messages = []
send_messages(messages, sent_messages)
print("\nUnsent messages:")
print(messages)
print("\nSent messages:")
print(sent_messages)
send_messages(messages, sent_messages)
print("\nUnsent messages after second call:")
print(messages)
print("\nSent messages after second call:")
print(sent_messages)
#Passing an Arbitrary Number of Keyword Arguments: You can also write functions that accept an arbitrary number of keyword arguments. These are often called **kwargs, which stands for "keyword arguments". The double asterisk before the parameter name allows the function to accept any number of keyword arguments, which will be stored in a dictionary. This can be useful when you want to create a function that can handle a varying number of keyword arguments without having to define them all in advance.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
#Mixing Positional, Arbitrary Positional, and Arbitrary Keyword Arguments: You can mix positional arguments, arbitrary positional arguments, and arbitrary keyword arguments in a function definition. However, the order of these arguments is important. The correct order is: first any regular positional arguments, then *args for arbitrary positional arguments, and finally **kwargs for arbitrary keyword arguments. This allows Python to correctly interpret the different types of arguments when the function is called.
def example_function(positional_arg, *args, **kwargs):
    """Example function that demonstrates mixing different types of arguments."""
    print(f"Positional argument: {positional_arg}")
    
    print("Arbitrary positional arguments:")
    for arg in args:
        print(f"- {arg}")
    
    print("Arbitrary keyword arguments:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")
example_function("This is a positional argument", "arg1", "arg2", key1="value1", key2="value2") 
#Note:  You'll often see the generic parameter name "args" which collects arbitrary positional arguments, and "kwargs" which collects arbitrary keyword arguments. However, you can actually use any parameter names you like as long as you use the * and ** syntax to indicate that they are collecting arbitrary arguments. The important part is the * for arbitrary positional arguments and ** for arbitrary keyword arguments, not the specific parameter names. 
#Using arbitrary keyword arguments allows you to create functions that can accept a varying number of keyword arguments, making your code more flexible and adaptable to different situations. This is especially useful when you want to create functions that can handle a wide range of input without having to define every possible parameter in advance.  
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
#Note: You'll often see the parameter name **kwargs used to collect non specific key word arguments in a function definition. However, you can actually use any parameter name you like as long as you use the ** syntax to indicate that it is collecting arbitrary keyword arguments. The important part is the ** for arbitrary keyword arguments, not the specific parameter name.  
#When you use **kwargs in a function definition, it allows the function to accept an arbitrary number of keyword arguments. The **kwargs parameter collects any additional keyword arguments passed to the function into a dictionary. This means that you can call the function with as many keyword arguments as you like, and they will all be accessible within the function through the **kwargs parameter. This is especially useful when you want to create functions that can handle a wide range of input without having to define every possible parameter in advance.    
#8-12: Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
def make_sandwich(*ingredients):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'avocado')
make_sandwich('peanut butter', 'jelly')
#8-13: User Profile: Start with a copy of your program from Exercise 8-12. Write a function called build_profile() that accepts a first and last name, and then an arbitrary number of keyword arguments. The function should build a dictionary containing the user's profile, including their first and last name, as well as anything else you want to include. Call the function, using your own first and last name, and print the resulting dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('John', 'Doe', location='New York', field='Software Development')
print(user_profile)
#8-14: Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as color and optional features. Print the dictionary that’s returned to make sure all the information was stored correctly.
def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car
car_profile = build_car('Toyota', 'Camry', color='blue', features='sunroof')
print(car_profile)
#Storing Functions in Modules: As your functions grow in number, you can store them in a separate file called a module and then import the module into your main program. This allows you to keep your main program file clean and organized, while still being able to use the functions you've defined in the module. To create a module, simply save your functions in a file with a .py extension. Then, you can import the module into your main program using the import statement. Once imported, you can call the functions from the module using the syntax module_name.function_name(). This is a great way to organize your code and make it more reusable across different projects.    
#Importing an Entire Module: To import an entire module, you can use the import statement followed by the name of the module. For example, if you have a module named functions.py, you can import it using import functions. Once imported, you can call any function defined in that module using the syntax functions.function_name(). This allows you to access all the functions in the module without having to import them individually.
import functions
functions.greet_user()
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
functions.make_pizza('pepperoni')
functions.make_pizza('mushrooms', 'green peppers', 'extra cheese')
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
functions.make_pizza(16, 'pepperoni')
functions.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#importing specific functions: If you only want to import a specific function from a module, you can use the from keyword in your import statement. For example, if you only want to import the greet_user() function from the functions module, you can use from functions import greet_user. This allows you to call the greet_user() function directly without having to prefix it with the module name. This can be useful when you only need a few functions from a module and want to avoid cluttering your namespace with unnecessary imports.
from functions import greet_user
greet_user()
#Using as to Give a Function an Alias: If the name of a function is long or might conflict with an existing function, you can use the as keyword to give the function an alias when you import it. For example, if you want to import the make_pizza() function from the functions module but want to call it something shorter like mp(), you can use from functions import make_pizza as mp. This allows you to call the make_pizza() function using the alias mp() in your code, which can make it more concise and easier to read.
from functions import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#from module_name import function_name as alias_name
#Using as to Give a Module an Alias: You can also use the as keyword to give a module an alias when you import it. For example, if you want to import the functions module but want to call it something shorter like fn, you can use import functions as fn. This allows you to call any function from the functions module using the alias fn, such as fn.greet_user() or fn.make_pizza(). This can be useful when you want to shorten the module name for convenience or to avoid naming conflicts with other modules.
import functions as fn
fn.greet_user()
fn.make_pizza(16, 'pepperoni')
fn.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#general syntax for importing a function or a module:
#Importing an entire module:
#import module_name
#Importing a specific function from a module:
#from module_name import function_name
#Using as to give a function an alias:
#from module_name import function_name as alias_name
#Using as to give a module an alias:
#import module_name as alias_name
#importing all functions in a module:
#from module_name import *
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#Styling functions
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")   
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#If you specify a default value for a parameter in a function definition, you can call the function without providing a value for that parameter. In this case, the default value will be used. For example, if you have a function defined as def make_shirt(size='large', message='I love Python'), you can call it with make_shirt() and it will use the default values of 'large' for size and 'I love Python' for message. This allows you to call the function with fewer arguments when the default values are sufficient.   
#def function_name(parameter1=default_value1, parameter2=default_value2, ...):
#    """Function body goes here."""
#same convention should be used for keyword arguments in a function call. For example, if you have a function defined as def make_shirt(size='large', message='I love Python'), you can call it with make_shirt(size='medium') and it will use 'medium' for size and the default value of 'I love Python' for message. This allows you to override the default value for specific parameters while still using the defaults for others. 
#function_name(parameter1=value1, parameter2=value2, ...)
#def function_name(
#   parameter_0, prameter_1, parameter_2,
#   parameter_3, parameter_4, parameter_5):
#function body ....

#8-15. Printing Models: Put the functions for the example printing_modules.py in a separate file called printing_functions.py.  
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.