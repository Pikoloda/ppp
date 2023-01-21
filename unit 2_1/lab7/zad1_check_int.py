# Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą.

number = int(input("Podaj liczbę całkowitą: "))

if number ** .5 % 1 == 0:  # .is int
    print("Tak, wynik z pierwiastka kwadratowego z liczby " + str(number) + " jest również liczbą całkowitą. ")
else:
    print("Nie, wynik z pierwiastka kwadratowego z liczby " + str(number) + ", nie jest liczbą całkowitą. ")

# number = int(input("Podaj liczbę całkowitą: "))
#
# if number ** .5 % 1 == 0:  # .is int
#     str1= "Tak"
#     str2= ""
# else:
#     str1 ="Nie"
#     str2="nie"
#
# print(str1+", pierwiastek kwadratowy z liczby " + str2 + "jest liczbą całkowitą.")
#
