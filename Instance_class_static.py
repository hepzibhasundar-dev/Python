#Instance
#Class
#Static method
class MyClass:
    def instance_method(self):
        print("Called instance method")

    @classmethod
    def class_method(cls):
        print("Called class method")

    @staticmethod
    def static_method():
        print("Called static method")

obj = MyClass()
obj.instance_method()
MyClass.class_method()
MyClass.static_method()