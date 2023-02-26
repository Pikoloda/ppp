# Zad1.
# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.

phone_numbers ={"Rafał": 123235122, "Tomek": 125556664, "Krzysztof": 550336778, "Sebastian": 880777066}

name = input("Podaj imię osoby do której potrzebujesz nr telefonu:")

if name in phone_numbers:
    print(phone_numbers.get(name))
else:
    print("Nie ma takiej osoby w książce telefonicznej.")