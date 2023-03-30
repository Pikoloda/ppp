# Zad1.
# Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
# • każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
# • zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
# • ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
# • każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się

class Person():

    def __init__(self, firstname, age):
        self.__firstname = firstname
        self.__age = age

    def getname(self):
        return self.__firstname

    def age(self):
        return self.__age



# Testy

persone1 = Person("Jan",24)
persone2 = Person("Piotr",44)
persone3 = Person("Krzysztof",6)

print("Witam mam na imię",persone1.getname()+", mam",persone1.age(),"lat.")
print("Witam mam na imię",persone2.getname()+", mam",persone2.age(),"lat.")
print("Witam mam na imię",persone3.getname()+", mam",persone3.age(),"lat.")
