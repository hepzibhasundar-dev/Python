#Access specifier - public, private, protected
# or Access modifier - abstract, static
#This program for variables
class Parent:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def access_from_same_class(self):
        print("Inside parent class : ")
        print("Public : ", self.public_var)
        print("Protected : ", self._protected_var)
        print("Private : ", self.__private_var)

class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child class(SubClass) : ")
        print("Public : ", self.public_var)
        print("Protected : ", self._protected_var)
        #we can access the parent private class in the following method
        print("Private : ", self._Parent__private_var)  #it is name mangling
        try:
            print("Private : ", self.__private_var)
        except AttributeError:
            print("Private : ❌ Cannot access (AttributeError)")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger class (Unrelated) : ")    
        print("Public : ", obj.public_var)
        print("Protected : ", obj._protected_var) #Not Recommented
        try:
            print("Private : ", obj.__private_var)
        except AttributeError:
            print("Private : ❌ Cannot access (AttributeError)")
#Demo
p = Parent()
c = Child()
s = Stranger()

print("\n ➡️ Access from SAME class : ")
p.access_from_same_class()

print("\n ➡️ Access from SUB class : ")
c.access_from_subclass()

print("\n ➡️ Access fro OTHER class : ")
s.access_from_other_class(p)