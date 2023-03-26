class MyClass:

    def __init__(self, name):
        self.__name = name
        print("Inicjalizuje obiekt!")

    def getname(self):
        return self.__name

obj = MyClass("Piotr")

print("Mam na imię", obj.getname()+"!")


