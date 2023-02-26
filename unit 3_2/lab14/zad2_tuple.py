# Zad2.
# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

wynik = ()


def create_tuple(num1, num2, num3):
    wynik = num1+num2+num3


numbers = [1, 2]
numbers1 = [4, 4, 4]
print(numbers + numbers1)