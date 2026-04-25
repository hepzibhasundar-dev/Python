# one to many - one dad has 2 sons relation
class dad:
    def house(self):
        print("house white")

class son1(dad):
    def factory(self):
        print("factory")

class son2(dad):
    def market(self):
        print("Furniture market")

# we have to create seperate object need to every child class

g=son1()
g.house()
g.factory()

h=son2()
h.house()
h.market()

#Hierarchy example
# VP -> Director -> product owner -> product manager -> project manager -> Team Lead -> team members