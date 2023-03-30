class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print("tytuł:", self.__title, "autor:",self.__author)

    def show_full_info(self):
        print("tytuł:", self.__title, "autor:", self.__author, "wydawca:", self.__publisher, "rok wydania:", self.__year)


book = []
book.append(Book("Dzieci z Bullerbyn", "Astrid Lindgren", "Nasza Księgarnia",2014))
book.append(Book("Moby Dick", "Herman Marville", "Amercon",2009))
book.append(Book("Python. Wprowadzenie", "Marek Lutz", "Hellion",2022))

for b in book:
    b.show_full_info()
