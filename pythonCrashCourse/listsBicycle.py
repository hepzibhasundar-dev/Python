#lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements to a list
motorcycles.append('ducati')
print(motorcycles)  
motorcycles.insert(0, 'ducati')
print(motorcycles)
#removing elements from a list
del motorcycles[0]
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#insert the element into a list at a specific position
motorcycles.insert(0, 'ducati')
print(motorcycles)
#delete the element at a specific position in a list using the del statement
del motorcycles[0]
print(motorcycles)
#pop the element at a specific position in a list using the pop() method
popped_motorcycle = motorcycles.pop(0)
print(popped_motorcycle)
print(motorcycles)

#organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#temporarily sort a list using the sorted() function
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
#reverse the order of a list using the reverse() method
cars.reverse()    
print(cars)
#find the length of a list using the len() function
print(len(cars))    
#print the number of times a value appears in a list using the count() method
print(cars.count('bmw'))
#find the index of the first occurrence of a value in a list using the index() method
print(cars.index('audi'))
#check if a value is in a list using the in keyword
print('bmw' in cars)
#check if a value is not in a list using the not in keyword
print('mercedes' not in cars)
#concatenate two lists using the + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
#repeat a list using the * operator
list4 = list1 * 3
print(list4)
#create a list of lists (a list that contains other lists)
list_of_lists = [list1, list2, list3]   
print(list_of_lists)
#access elements in a list of lists using multiple indices
print(list_of_lists[0][1])  # Access the second element of the first list
#slice a list using the slice notation
print(cars[1:3])  # Access the second and third elements of the list
#use negative indices to access elements from the end of a list
print(cars[-1])  # Access the last element of the list
#Avoid IndexError by checking the length of a list before accessing an element
if len(cars) > 3:
    print(cars[3])  # Access the fourth element of the list
else:
    print("The list does not have a fourth element.")

#loop through a list using a for loop
for car in cars:
    print(car)
#use the enumerate() function to loop through a list and get the index of each element
for index, car in enumerate(cars):
    print(index, car)
#use a list comprehension to create a new list based on an existing list
squared_numbers = [x**2 for x in list1]
print(squared_numbers)
#use the zip() function to loop through two or more lists at the same time
list5 = ['a', 'b', 'c']
list6 = [1, 2, 3]
for item1, item2 in zip(list5, list6):
    print(item1, item2)
#index -1 is the last item in the list, -2 is the second to last item, and so on.
print(cars[-1])  # Access the last element of the list
print(cars[-2])  # Access the second to last element of the list
print(cars[-3])  # Access the third to last element of the list

#for loop with a list of lists
list_of_lists = [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z']]
for sublist in list_of_lists:
    for item in sublist:
        print(item)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#add a second line to the for loop to print a message for each magician
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")

#doing something after a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
print("Thank you, everyone. That was a great magic show!")


