#class
class Student1:

    def say_hello(self):
        print("Hi, I'm a student!")

s1 = Student1() #object
s1.say_hello() #s1.say_hello(s1)

#Multiple objects
class Student:
    def __init__(self, name, grade):   # __init__ is constructor
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} is in grade {self.grade}")

s2 = Student("Hepzibha", 12)
s3 = Student("Daniel", 10)
s4 = Student("Abel", 9)

s2.display()
s3.display()
s4.display()