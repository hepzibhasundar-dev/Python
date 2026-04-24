#Tuple - allow different data types, duplicate values.  But it is immutable
#Difference between list and tuple is list is mutable, tuple is immutable
#both maintain order, 
#only read purpose tuple is the best option
#list use for dynamic values
#log, audit log, it is very fast - it can use key in dictionary

#Uber use case
trip_summary = ("ubergo", "Chennai", "airport", 450.00, "completed")
print(trip_summary)

#access with index position
print(trip_summary[1])

#Looping
for item in trip_summary:
    print(item)

#length of the tuple
print(len(trip_summary))

#count and index
print(trip_summary.count("completed"))
print(trip_summary.index("completed"))




