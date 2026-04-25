#single level inheritance
class dad:
    
    def house(self):
        print("House White")

class son(dad):

    def factory(self):
        print("factory")

v=son()
v.house()