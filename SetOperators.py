# set un ordered 
# set no index
# duplicate eliminated
# we can change list to set
a = set([1,2,3])
print(a)

# a = {1,2,3} - set  but dictionary key, value pair
uber_cities = ["Chennai","Bangalore","Delhi","Chennai","Bangalore"]
unique_cities=set(uber_cities) # it removes the duplicates
print(unique_cities)

#set operations
#create two sets and apply the set operations
uber_cities1 = {"Chennai","Mumbai","Bangalore"}
uber_cities2 = {"Bangalore","Delhi","Hyd"}

print(uber_cities1.union(uber_cities2))  #combine or join the sets
print(uber_cities1.intersection(uber_cities2)) # common values from both of the sets
print(uber_cities1.difference(uber_cities2)) # difference in first set
print(uber_cities2.difference(uber_cities1)) # difference in second set

#add value in set - it add in anywhere, no index
uber_cities1.add("Karur")
print(uber_cities1)

#remove value in set
uber_cities1.remove("Chennai")
print(uber_cities1)

#if give the value to remove not from the set will throw error
#use discard for the safer side
my_set = {1,2,3}
print(my_set)
my_set.discard(8) #not in the set
print(my_set)


