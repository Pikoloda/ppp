# Zad2.
# Napisz klasę zliczającą wszystkie powstałe swoje instancje.

class MyClass:
    counter = 0

    def __init__(self, x=1):
        self.__x = x
        MyClass.counter += 1


obj1 = MyClass()
obj2 = MyClass()

obj1 = MyClass(1)
print(obj1.__dict__, obj1.counter)

# print(MyClass.counter)