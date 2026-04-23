#skeleton of the if statement
age=30

if age >= 18:
    print("You are eligible to vote")
else:
    print("You can vote")

#use cases mark - grade
marks=75

if marks >= 90:
    print("Grade A")
elif marks >=70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#nested if
age1 = 18
has_license = 'yes'

if age >= 18:
    if has_license == 'yes':
        print('You can drive')
    else:
        print("Go and take License first")
else:
    print('You are too young to drive')

# multiple conditions need to satisfy in one if condition
# use case attendance and exam appearing condition
mark = 80
attendance = 60

if mark >= 55 and attendance >= 70:
    print('Allowed for exam')
else:
    print('Not allowed for exam')

# And & or using use case
# mobile uploading condition
# discount bonus data - when recharge amount $350 or data balance should be 1.5GB
recharge_amount=450
data_balance=1.5

if recharge_amount >= 350 or data_balance >= 1:
    print('You are eligible for bonus data')
else:
    print('You are not eligible')
#hotel use case
# order should be more than 1000 and order on saturday or sunday 20% discount
# or if you are a gold membership
order_amount=1000
days='sat'
membership='no'

if(order_amount >= 1000 and days in['sat','sun']) or membership=='gold':
    print("20% discount")
else:
    print("No discount")

