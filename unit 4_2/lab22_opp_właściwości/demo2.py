class MyClass:
    counter = 0  # zmienna klasy, wspólna dla całej klasy obiektów

    def __init__(self, x=1):
        self.__x = x
        MyClass.counter += 1



obj1 = MyClass(1)
print(obj1.__dict__, obj1.counter)


obj2 = MyClass(2)
obj3 = MyClass(77)

# print(obj1.__dict__, obj1.counter)
print(obj2.__dict__, obj2.counter)
print(obj3.__dict__, obj3.counter)

print()

print("Ile obiektów?", MyClass.counter)

print(MyClass.__dict__)


# Do poprawy !! filmik