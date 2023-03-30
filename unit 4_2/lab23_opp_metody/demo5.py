class MyClass:
    x = 5

    def __init__(self):
        self.y = 9


obj = MyClass()
print(obj.x , obj.y)

print(MyClass.__dict__)
print(obj.__dict__)

setattr(obj, "z", 1 ) # refleksja
print(getattr(obj,"x")) # introspekcja ( na działającym "ciele" - potężne narzędzie)

print("z:", obj.z)
