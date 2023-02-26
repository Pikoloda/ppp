# Zad1.
# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.



phones = {
    "Adam": 123123123,
    "Karol": 111222333,
    "Mariola": 453453453,
    "Iza": 443443443
}

while True:
    name= input("Podaj imię:")
    if name == "":
        break
    if name in phones:
        print("Telefon:",phones[name])
    else:
        print("Nie znaleziono telefonu dla imienia", name)
