#Access specifier Methods

class Parent:

    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

    def access_from_same_class(self):
        print("Inside Parent class : ")
        self.public_method()
        self._protected_method()
        self.__private_method()

class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child class (Subclass) : ")
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except:
            print("Private method : ❌ cannot access (AttributeError)")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger class (Unrelated) : ")
        obj.public_method()
        obj._protected_method() # ⚠️ Not recommended
        try:
            obj.__private_method()
        except AttributeError:
            print("Private method : ❌ cannot access (AttributeError)")

#Demo
p =  Parent()
c = Child()
s = Stranger()

print("\n ➡️ Access from SAME class : ")
p.access_from_same_class()


print("\n ➡️ Access from Sub Class : ")
c.access_from_subclass()

print("\n ➡️ Access from OTHER class : ")
s.access_from_other_class(p)