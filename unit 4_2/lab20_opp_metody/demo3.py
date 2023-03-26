# importoanie z stack_oop !!!!!!

class MyClass:
    def __my_private_methode(self):
         print("To jest metoda prywatna...")

    def my_public_methode(self):
        self.__my_private_methode()
        print("To jest metoda publiczna...")


obj = MyClass()

# obj.__my_private_methode() # tak nie zadziała bo metoda prywatna
obj.my_public_methode()

print()

print(obj.__dict__)
print(MyClass.__dict__)

print()
print(MyClass.__name__)
print(type(obj).__name__)
print(type(obj))

print()

print(MyClass.__module__)