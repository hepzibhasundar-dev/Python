#Creating and using a class
#Creating the Dog class
class Dog:
    """A simple to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

#The __init__() method
#Making an Instance from a class
class Dog:
    --snip--

my_dog = Dog('Willie', 6)

print(f"My dog's name is (my_dog.name)")
print(f"My dog is {my_dog.age} years old.")

