#using *args - accept multiple arguments

def add(*args):
    total=0
    for num in args:
        total += num
    return total

print(add(1,2,3,4)) # any number of arguments can pass