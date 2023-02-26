# Zad1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy


def potęgowanie(numbers, potęga=2):
    for num in numbers:
        num **= potęga
    return numbers

numbers = [2, 3, 4]

print(potęgowanie(numbers))
# print(potęgowanie(numbers,2))
