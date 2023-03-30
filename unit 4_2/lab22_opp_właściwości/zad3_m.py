# Zad3.
# Napisz klasę reprezentującą obiekty typu książka, w tym celu:
# • stwórz klasę Book z odpowiednimi właściwościami i metodami,
# • stwórz kilka przykładowych egzemplarzy tej klasy,
# • zademonstruj działanie wybranych metod na przykładowych egzemplarzach.

class Book():
    def __init__(self, tytuł, autor, tematyka):
        self.__tytuł = tytuł
        self.__autor = autor
        self.__tematyka = tematyka


libre = []
libre.append(Book("Anioły i Demony", " Dan Brown", "Kryminał"))
libre.append(Book("Inferno", " Dan Brown", "Kryminał"))
