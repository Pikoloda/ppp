# Zad1.
# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika

# number = int(input("Podaj liczbę elementów zbioru: "))

names = []
total_elements = int(input("Podaj liczbę imion: "))

for i in range(1, total_elements + 1):
    names.append(input("Podaj "+ str(i) + " imię: "))

print("Od użytkownika pobrano następujący zbiór imion:", names)

