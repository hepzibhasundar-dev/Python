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
