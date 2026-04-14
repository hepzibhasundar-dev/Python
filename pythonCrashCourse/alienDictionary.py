#simple dictionary to store alien words and their translations
alien_dictionary = {
    "greeting": "hello",
    "goodbye": "goodbye",
    "please": "please"
}
#function to translate an alien word
def translate_alien_word(word):
    return alien_dictionary.get(word, "Translation not found.") 
#test the function
print(translate_alien_word("greeting"))  # Output: hello
print(translate_alien_word("goodbye"))  # Output: goodbye
print(translate_alien_word("please"))   # Output: please
print(translate_alien_word("thank you")) # Output: Translation not found.

alien_0 = {
    'color': 'green',
    'points': 5
}
print(alien_0['color'])  # Output: green
print(alien_0['points']) # Output: 5

#working with dictionaries
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # Output: {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}    

#Accessing values in a dictionary
print(alien_0['color'])  # Output: green
print(alien_0['points']) # Output: 5
print(alien_0['x_position']) # Output: 0
print(alien_0['y_position']) # Output: 25

#Adding new key-value pairs to a dictionary
alien_0['speed'] = 'slow'
print(alien_0)  # Output: {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'slow'}   
#Modifying values in a dictionary
alien_0['color'] = 'yellow'
print(alien_0)  # Output: {'color': 'yellow', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'slow'}      
#Removing key-value pairs from a dictionary
del alien_0['points']
print(alien_0)  # Output: {'color': 'yellow', 'x_position': 0, 'y_position': 25, 'speed': 'slow'}       
#starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)  # Output: {'color': 'red', 'points': 10}
#A dictionary of similar objects
alien_2 = {
    'color': 'blue',
    'points': 15
}
print(alien_2)  # Output: {'color': 'blue', 'points': 15}
#using get() to access values in a dictionary
print(alien_0.get('color'))  # Output: yellow
print(alien_2.get('color'))  # Output: blue
print(alien_0.get('speed'))  # Output: slow
print(alien_2.get('speed', 'Speed not found.'))  # Output: Speed not found.

#6-1 Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.  

person_0 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}
print(person_0)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}    
#6-2 Favorite Numbers: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Then think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number.        
favorite_numbers = {
    'Alice': 7,
    'Bob': 13,
    'Charlie': 25,
    'David': 42,
    'Eve': 69
}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
#6-3 Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary. Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values. Print each word and its meaning as neatly formatted output.
glossary = {
    'variable': 'A named storage location in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.'
}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")
#Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
#looping through all keys in a dictionary
for key in user_0.keys():
    print(f"Key: {key}")
#looping through all values in a dictionary
for value in user_0.values():
    print(f"Value: {value}")
#looping through a dictionary's keys in a particular order
for key in sorted(user_0.keys()):
    print(f"Key: {key}")
#looping through all key-value pairs in a dictionary
for key, value in sorted(user_0.items()):
    print(f"Key: {key}")
    print(f"Value: {value}\n")
#use set() to find unique values in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"- {language}")
#6-4: Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary.
glossary = {
    'variable': 'A named storage location in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.'
}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")
#6-5 Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. Use a loop to print a sentence about each river, such as The Nile runs through Egypt. Use a loop to print the name of each river included in the dictionary. Use a loop to print the name of each country included in the dictionary.
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")
print("\nRivers:")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\nCountries:")
for country in rivers.values():
    print(f"- {country}")
#6-6 Polling: Use the code in favorite_languages.py (page 104). Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not. Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take the poll!")
#nesting dictionaries
alien_0 = {
    'color': 'green',
    'points': 5
}
alien_1 = {
    'color': 'yellow',
    'points': 10
}
alien_2 = {
    'color': 'red',
    'points': 15
}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
#makeing a fleet of aliens
aliens = []
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)
print(f"Total number of aliens: {len(aliens)}")
#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
#change the first 3 aliens to yellow and medium speed
for alien in aliens[:3]:
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10 
    print(alien)   
#make an empty list for storing pets
pets = []
#make individual dictionaries for each pet, and add each to the list
pet_0 = {
    'type': 'dog',
    'owner': 'alice'
}
pets.append(pet_0)
pet_1 = {
    'type': 'cat',
    'owner': 'bob'
}
pets.append(pet_1)
pet_2 = {
    'type': 'bird',
    'owner': 'charlie'
}
pets.append(pet_2)
#show all pets
for pet in pets:
    print(pet)
#store information about a pizza being ordered
pizza_order = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'extra cheese']
}
print(pizza_order)
#value associated with each person is a list of their favorite languages
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
print(favorite_languages)
#loop through the dictionary and print each person's favorite languages
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"- {language.title()}")
#A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")
#6-7 People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
person_0 = {
    'first': 'alice',
    'last': 'smith',
    'age': 30,
    'city': 'new york'
}
person_1 = {
    'first': 'bob',
    'last': 'johnson',
    'age': 25,
    'city': 'los angeles'
}
person_2 = {
    'first': 'charlie',
    'last': 'brown',
    'age': 35,
    'city': 'chicago'
}
people = [person_0, person_1, person_2]
for person in people:
    print(f"\nName: {person['first']} {person['last']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
#6-8 Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pet_0 = {
    'type': 'dog',
    'owner': 'alice'
}
pet_1 = {
    'type': 'cat',
    'owner': 'bob'
}
pet_2 = {
    'type': 'bird',
    'owner': 'charlie'
}
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(f"\nPet: {pet['type']}")
    print(f"Owner: {pet['owner']}")
#6-9 Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {
    'alice': ['paris', 'tokyo'],
    'bob': ['new york', 'london'],
    'charlie': ['sydney']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
#6-10 Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.
favorite_numbers = {
    'alice': [7, 14],
    'bob': [3, 9],
    'charlie': [5]
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
#6-11 Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Loop through your cities dictionary, and print the name of each city and all of the information you have stored about it.
cities = {
    'new york': {
        'country': 'United States',
        'population': 8336697,
        'fact': 'Known as the Big Apple.'
    },
    'london': {
        'country': 'United Kingdom',
        'population': 9642652,
        'fact': 'Home to the Tower of London.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'The largest metropolitan area in the world.'
    }
}
for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
#6-12 Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use your imagination to extend one (or more) of the example programs from this chapter. Here are a few ideas to get you started:
#- In favorite_languages.py, add more people and languages, and make sure to print the list of favorite languages for each person in a neatly formatted way.
favorite_languages = {
    'alice': ['python', 'javascript'],
    'bob': ['java', 'c++'],
    'charlie': ['python', 'ruby']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"- {language}")
#- In the example about aliens, make a fleet of 1,000 aliens. Make the first 10 aliens green, the next 10 yellow, and the next 10 red. Have each alien print out its color and point value.
aliens = []
for alien_number in range(1000):
    if alien_number < 10:
        color = 'green'
        points = 5
    elif alien_number < 20:
        color = 'yellow'
        points = 10
    elif alien_number < 30:
        color = 'red'
        points = 15
    else:
        color = 'green'
        points = 5
    new_alien = {
        'color': color,
        'points': points
    }
    aliens.append(new_alien)
for alien in aliens[:30]:  # Print the first 30 aliens
    print(f"Alien color: {alien['color']}, Points: {alien['points']}")
    