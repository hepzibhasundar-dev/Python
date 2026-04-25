class grandfather:
    def car(self):
        print("red car")

class dad(grandfather):
    def house(self):
        print("house white")

class son(dad):
    def factory(self):
        print("factory")

v=son()
v.car()
v.factory()
v.house()