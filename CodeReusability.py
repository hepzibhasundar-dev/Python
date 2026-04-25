#Code reusability - change only the method calling
class v1: #parent
    def version1(self):
        print("I am version 1")

class v2(v1): #child access parent class
    def version2(self):
        print("I am version 2")

v=v2()
v.version2()
v.version1()  
#object call only we have to change


