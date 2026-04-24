#for loop - if know the number of iteration, use for loop
names = ["saravanan","govinda","nandini","rahul","john","jacob"]

for test in names:
    print(test.upper())

#while loop
# if don't know the number of iteration, until the condition satisfied, use while loop
correct_pin='1234'
entered_pin=''

while entered_pin != correct_pin:
    entered_pin=input("Enter your correct pin : ")
print("Access granted")

# break and continue - to stop the loop immediately - break
# need to find 5
for i in range (10):
    if i == 5:
        break
print(i)

#using list
names = [1,2,3,4,9,6,7,8,5,10]
for i in names:
    if i == 6:
        break
    print(i)
print("Find 6 : ",i)

# continue - skip some value and continue
n=[10, -5, 7, -9, 11]

for num in n:
    print("num value : ",num)
    if num < 0:
        continue
    print(num)

#pass - place holder
n1=[10,-4,3,-9,21]

for num1 in n1:
    pass # future logic implementation

#use case count down time counter
count = 5

while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print("Time's up! ⏰ ")

# cart 
# while True:  -> infinite loop need to Ctr + C for break the loop
items = []

while True:
    item = input("Add item (type 'done' to finish) : ")
    if item.lower() == "done":
        break
    items.append(item)

print("Items in cart:", items)


