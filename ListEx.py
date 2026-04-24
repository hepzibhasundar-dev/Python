#List - create index for each element, it is mutable, we can add or delete element from that
#multiple data type we can keep in single list
#Creating lists for different apps
playList = ["Shape of you", "Naa Ready", "Believer", "Tum Hi Ho"] #spotify
favorite_foods = ["Pizza", "Burger", "Dosa", "Biriyani"]  #Zomato
recent_location = ["Home", "Airport", "Work", "Mall"]  #uber

print("Spotify Playlist : ", playList)
print("Zomato Foods : ", favorite_foods)
print("Uber Locations : ", recent_location)

#list methods
#append
playList.append("Oo antava")
print("After append : ", playList)

#insert - any place we can - position
playList.insert(1, "Song-Added")
print("After insert : ", playList)

#remove - remove the first appearance
playList.remove("Song-Added")
print("After remove : ", playList)

#pop  - it removes last element
playList.pop()
print("After pop : ", playList)

#reverse
playList.reverse()
print("After reverse : ", playList)

#count
print("Count : ",playList.count('Believer'))

#list slicing
print("Top 2 songs : ", playList[0:2]) #2 exclude, 0, 1

print("Last 2 locations : ", recent_location[-2:])

print("Display 2 and 3 songs : ", playList[2:4])

#List iteration
for food in favorite_foods:
    print("All foods : ", food)

# need to add "Hepzibha" in the song playlist for each song
for song in playList:
    print(song + " By Hepzibha")

#find the element is in the list or not,  check
if "Dosa" in favorite_foods:
    print("Yes")

# update the element - instead of Burger add Shawarma
favorite_foods[1] = "Shawarma"
print(favorite_foods)

#Mixed data types
mixed = ["Hepzibha",35,1.5, None]

for a in mixed:
    print(a)

#using enumerator - location and index
for i,location in enumerate(recent_location):
    print(f"location {i} : {location}")