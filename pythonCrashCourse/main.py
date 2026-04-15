# 1) import module_name
import greet
greet.say_hello("Alice")

# 2) from module_name import function_name
from greet import say_hello
say_hello("Bob")

# 3) from module_name import function_name as fn
from greet import say_hello as fn
fn("Charlie")

# 4) import module_name as mn
import greet as mn
mn.say_hello("David")

# 5) from module_name import *
from greet import *
say_hello("Eve")