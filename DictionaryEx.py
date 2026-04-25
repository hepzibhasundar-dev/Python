#dictionary stores the data key, value pair
#lookup, one key can multiple values, dictionary not allow duplicate
trip = {
    "trip_id": "UB12345",
    "pickup": "Chennai Central",
    "drop": "Airport",
    "fare": 430.75,
    "driver": "Ravi",
    "status": "Completed"
}
print(trip["pickup"]) #lookup - key only can access

print(trip.get("pickup"))
print(trip.get("Airport")) # value given,not in key, instead of error, return none

#only keys
print(trip.keys())
print(trip.values())

#iterating
for key,value in trip.items():
    print(key," : ",value)

#update - if the key is there it update or it create and add
trip.update({"car_model":"suzuki"})
print(trip) 

trip.update({"car_model":"Honda"})
print(trip) 

trip.pop('status')
print(trip)

#duplicate allow in the assignment, but not take the duplicate
trip1 = {
    "trip_id": "UB12345",
    "pickup": "Chennai Central",
    "drop": "Airport",
    "fare": 430.75,
    "driver": "Ravi",
    "trip_id": "UB123456",
    "status": "Completed"
}

print(trip1)  # it takes the latest value, ignore the duplicate old value
for k, v in trip1.items():
    print(k," : ",v)

trip2 = {
    "trip_id": "UB12345",
    "pickup": "Chennai Central",
    "drop": ["Airport","Tambaram","Medavakkam"],
    "fare": 430.75,
    "driver": "Ravi",
    "status": "Completed"
}

for k,v in trip2.items():
    print(k," : ",v)

# only tambaram retrieve
print(trip2["drop"][1]) #it retrieve only Tambaram

# we can iterate multiple values in the key
for location in trip2["drop"]:
    print(location)

#multiple dictionary in the list
trips = [
    {"trip_id": "UB001", "pickup": "Chennai", "drop": "Airport", "fare": 430},
    {"trip_id": "UB002", "pickup": "Tambaram", "drop": "Central", "fare": 320},
    {"trip_id": "UB003", "pickup": "TNagar", "drop": "Velachery", "fare": 210},
]

for trip in trips:
    print(trip["trip_id"])

#dictionaries in dictionay
trips1 = {
    "UB001": {"trip_id": "UB001", "pickup": "Chennai", "drop": "Airport", "fare": 430},
    "UB002": {"trip_id": "UB002", "pickup": "Tambaram", "drop": "Central", "fare": 320},
    "UB003": {"trip_id": "UB003", "pickup": "TNagar", "drop": "Velachery", "fare": 210},
}
#look up
print("UB001 Fare", trips1["UB001"]) #all list value in the key UB001
print("UB001 Fare only", trips1["UB001"]["fare"]) # only face in the key UB001

#looping
for trip_id, details in trips1.items():
    print(trip_id)
    print(details["pickup"],"--> ", details["drop"])