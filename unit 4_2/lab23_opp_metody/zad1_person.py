class Person():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Cześć, jestem", self.__name, "i mam", self.__age,"lat/a.")


persons = []
persons.append(Person("Jan",20))
persons.append(Person("Agata",14))
persons.append(Person("Piotr",35))
persons.append(Person("Marcin",41))
persons.append(Person("Zygfryd",80))

Person.introduce()

#dokończyć
