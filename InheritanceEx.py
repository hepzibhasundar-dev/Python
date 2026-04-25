#Inheritance - different types
# code reusability
# parent - child relationship

class dad:  #parent class
    def house(self):
        print("I am from dad class")

#inheritance - create the relationship
class son(dad):  #child class
    def factory(self):
        print("I am from child(son)")

#single level inheritance - only one child
s5=son()
s5.house()
s5.factory()

#app use case
class app1: #parent
    def v1(self):
        print("orders")

class app1_1(app1):  

    def v2(self):
        print("refund")
    def v1(self):
        print("cart") #override the parent method

a=app1_1()
a.v1()
a.v2()


# class test:
#     def factory(self):
#         print("I am from factory class")


# without relationship, just call the methods

# d=dad()
# d.house()

# t=test()
# t.factory()

