# Zad1.
# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.


even_sum = 0
odd_sum = 0

while True:
    number_str = input("Podaj liczbę całkowitą lub wciśnij Enter aby uzykać wynik:  ")
    if number_str == "":
        break
    number = int(number_str)
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
print()
print("-" * 50)
print()
print("Suma liczb podanych przez użytkownika wynosi: ")
print(" " * 5, "- parzystych - " + str(even_sum))
print(" " * 5, "- nieparzystych - " + str(odd_sum))
