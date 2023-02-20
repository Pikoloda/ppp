# Zad2.
# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
# • wyświetli wylosowane serie liczb.

import random

min_value = int(input("Podaj minimalną wartość: "))
max_value = int(input("Podaj maksymalną wartość: "))

number_numbers = int(input("Podaj liczbę liczb do wylosowania: "))
number_series = int(input("Podaj liczbę serii: "))

series_list = []

for i in range(number_series):
    series = []

    for j in range(number_numbers):
        number = random.randint(min_value, max_value)
        series.append(number)

    series_list.append(series)

print()
print("-" * 50)
print()
print("Poniżej wyświetlono", number_series, "serii, które miały po", number_numbers, "wylosowanych liczb z zakresu od",
      min_value, "do", max_value,":")
print()

for i in range(number_series):
    print("Seria", i + 1, ":", series_list[i])
