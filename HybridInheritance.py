#Within the file using different inheritance
'''
single level
multi level
multiple
hierarchy
'''
#Hybrind inheritance combines two or more types of inheritance
#eg. multiple + multilevel

#Base class
class Animal:
    def breathe(self):
        print("Breathing...")

#Single inheritance from Animal
class Mammal(Animal):
    def feed_milk(self):
        print("Feeding milk...")

#Single inheritance from Animal
class Bird(Animal):
    def lay_eggs(self):
        print("Laying eggs...")

#Multiple inheritance from Mammal and Bird (this creates Hybrid)
class Platypus(Mammal, Bird):
    def special(self):
        print("I am unique - I'm a mammal that lays eggs!")

#usage
p = Platypus()
p.breathe() #from Animal
p.feed_milk() #from Mammal
p.lay_eggs() #from Bird
p.special() #own method
'''
Animal          ← Base (Level 1)
       /      \
   Mammal    Bird       ← Single inheritance (Level 2)
       \      /
       Platypus         ← Multiple inheritance (Level 3)
'''
'''
It's a mix of:

Multilevel — Animal → Mammal → Platypus
Multiple — Platypus inherits from both Mammal and Bird
'''

'''
Hybrid inheritance is powerful but should be used carefully — deep or complex hierarchies can make code hard to maintain.
'''
'''
Key Takeaway:
Inheritance type        What it means
Single                  One Parent
Multiple                Two + parents
Multilevel              Chain(grandparent->parent->child)
Hybrid                  combination of the above
'''