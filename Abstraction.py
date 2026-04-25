#Abstraction
#hiding complex implemetation details and exposing only what's neccessary.
#abstract class can abstract method and non abstract method also.
#in abstract class we should not create the objects directly
#need to create the child class and override it and call that is the abstract class design


from abc import ABC, abstractmethod

#Architect defines the plan
#login, logout, order, checkout
class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
       pass
       
    @abstractmethod
    def logout(self):
        pass
        
#Developer implements it
class WebApp(FeaturePlan):
    def login(self):
        print("WebApp login done")

    def logout(self):
        print("WebApp logout done")

#Team Lead checks functionality
app = WebApp()
app.login()
app.logout()

'''
from abc import ABC, abstractmethod

#Architect defines the plan
#login, logout, order, checkout
class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
       pass
       
    @abstractmethod
    def logout(self):
        pass
        
#Developer implements it
class WebApp(FeaturePlan):
    def login(self):
        print("WebApp login done")

    def logout(self):
        print("WebApp logout done")

#Team Lead checks functionality
app = WebApp()
app.login()
app.logout()

'''

#Abstract class  - acts as a blueprint
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass # no implementation here - subclasses MUST define it

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self): #Regular method - shared by all shapes
        print(f"I am a {self.__class__.__name__}")

#Concrete class - must implement all abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
#Concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
    
#Usage
c=Circle(5)
c.describe()
print("Area : ", c.area())
print("Perimeter : ", c.perimeter())

r=Rectangle(4,6)
r.describe()
print("Area : ", r.area())
print("Perimeter : ",r.perimeter())
