x = 30
y = 10
print (x + y)
#concatination
a = '1'
b = '2'
print(a + b)
# Data type - float, string, int, boolean, none
is_active = True
print(type(is_active))
# dynamic
# scope, life time
# L -> E -> G -> B
# L - Local
# E - Enclosing
# G - Global
# B - Built-in
#Local variable - within function declared
def order():
    food='Curd Rice'
    print('Your order is : ', food)
order()
#E - nested function
def cart():
    discount=10
    
    def checkout():
        print("applying discount : ", discount)

    checkout()

cart()

# G - Global
user_id="name12"

def homepage():
    print("Welcome : ", user_id)

def profile():
    print("Welcome to the profile page : ", user_id)

homepage()
profile()

# built-in variables
# B - built-in variables
print(__file__) # path of the file
print(__name__) # name of current file
print(__builtins__)  # all builtin functions

# use case
delivery_partner='swiggy'
def hotel():
    item="pizza"

    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order_now()

hotel()

#type casting and type checking
# one data type to another data type
x="10"
print(type(x))
print(type(int(x)))
#print(type(x))
# where we can't use type cast - string change int have some issues
# float change to int has issues

# operators & Expressions
c=10
d=3
print(c+d)
print(c-d)
print(c/d)
print(c%d)
print(c**d)
print(c // d)
# Arithmetic operations, logical, bitwise, comparision operators
#comparison
x=5
y=10
print(x==y)
print(x!=y)
print(x<y)
print(x>y)

#Logical
g=True
v=False
print(g and v)
print(g or v)
print(not g)

#use case
#Billing calculation
# GST and discount
amount = 1200
tax=amount + 0.18
total = amount + tax
print(total)

if total > 1000 :
    discount = total * 0.10
    total -= discount
print(total)

# logical and comparison
# movie ticket discount for aged and students

age = 65
student = 'yes'

if age >= 60 or student == 'yes':
    print('Yes discount applicable')
else:
    print('No discount')

# command - multiline command
# single line command
""" multiline command
everything command with more details"""
'''This is also multiline command
notes and multiline command'''

#input
# more types are there in input
x1=10
y1=20
print(x1+y1) #hard coding

#change management process
x2=input('Enter the first number : ') # 5
y2=input('Enter the second number : ') #6

print(a+b) # 56   it converts the input value to string

#type cast
x3=int(input('Enter the first value : ')) #2
y3=int(input('Enter the second value : ')) #3

print(x3+y3) #5


