#Polymorphism - many forms
#same method but different behavior
#method overloading, method overriding
class dad:
    def house(self):
        print("house white")

class daughter(dad):
    def factory(self):
        print("factory")

    def house(self):
        print("house yellow") #override dad's method

d=daughter()
d.house()
d.factory()

# overloading
#same method name but different parameters and different types also
# python allows only overriding no overloading
#The above example is polymorphism - method overloading