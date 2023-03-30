class MyClass:
    y = 99

    def my_method(self, x):
        self.other_method() # odwołanie do innej metody za pomocą self
        print("To jest moja metodaz parametrem:", x, "i zmienną klasy", self.y)
        print()

    def other_method(self):
        print("To jest metoda", self.y)


obj = MyClass()
obj.my_method(123)
obj.my_method("AAAA")
obj.my_method(1)

