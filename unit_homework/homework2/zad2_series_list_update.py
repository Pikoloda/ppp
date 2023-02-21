# Zad2.
# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
# • wyświetli wylosowane serie liczb.


# Poprawiono skrypt, teraz jest losowana liczba liczb i liczba serii z przedziałów podanych przez użytkownika.


import random

min_value = int(input("Podaj minimalną wartość liczby: "))
max_value = int(input("Podaj maksymalną wartość liczby: "))

number_numbers_min = int(input("Podaj minimalną liczbę liczb do wylosowania: "))
number_numbers_max = int(input("Podaj maksymalną liczbę liczb do wylosowania: "))

number_series_min = int(input("Podaj mininalną liczbę serii: "))
number_series_max = int(input("Podaj maksymalną liczbę serii: "))

series_list = []

number_series = random.randint(number_series_min,number_series_max)
number_numbers = random.randint(number_numbers_min,number_numbers_max)

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
