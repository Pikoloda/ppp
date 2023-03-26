# Zad1.
# Stwórz klasę o nazwie Student i utwórz 3 instancje nowo utworzonej klasy.

class Student():
    def __init__(self):
        self.__firstName__ =[]

    def get_name(self, name):
        self.__firstName__.append(name)
        return name




student1 = Student()
student2 = Student()
student3 = Student()

print(student1.get_name("Piotr"))
print(student2.get_name("Rafał"))
print(student3.get_name("Krzysztof"))




