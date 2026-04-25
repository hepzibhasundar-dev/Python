class Student2:

    def __init__(self, fname, age):
        self.x = fname
        self.y = age

    def display(self):
        print(f"Name : {self.x}, Age : {self.y}")

s1 = Student2("Hepzibha", 35)
s1.display()

#Aadhaar use case
class Employee:
    
    def __init__(self, name, aadhaar):
        self.name = name      #stored once
        self.aadhaar = aadhaar #stored once

    def enter_office(self):
        print(f"{self.name} enters using Aadhaar {self.aadhaar}.")
              
    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with Aadhaar {self.aadhaar}.")

emp1 = Employee("Hepzibha", "1234-5678-9101")
emp1.enter_office()
emp1.open_bank_account()

#Without constructor
class MathTools:

    def square(self, n):
        return n*n
    
    def cube(self, n):
        return n*n*n
    
tool = MathTools()
print(tool.square(4))  #16
print(tool.cube(2)) #8
