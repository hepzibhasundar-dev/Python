from Inheritance1 import dad


class son(dad):
    def factory(self):
        print("White")

    #override the dad's house method - method override
    def house(self):
        print("Yellow")

s=son()
s.factory()
s.house()