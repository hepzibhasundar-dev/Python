#multiple inheritance
# daughter can access both of the parents 
class dad:
    def house(self):
        print("Red house")

class mom:
    def shop(self):
        print("Blue Shop")

class daughter(dad, mom):
    def factory(self):
        print("Factory")

#daughter inherits dad and mom's object
v1=daughter()
v1.factory()
v1.house()
v1.shop()

#Multi level inheritance
'''
a
b(a)
c(b)
'''
#Multiple inheritance
'''
A
B
C(A, B)
'''