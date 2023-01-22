# 1. Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika

print("Podaj zakres liczb")
number_from = int(input("od:"))  # range_from
number_to= int(input("do:"))

print("Liczby z zakresu od", number_from, "do", number_to, "podzielne przez 3 lub 5 lub 7 to:", end=" ")

is_first = True
for i in range(number_from, number_to +1): # number nazwano i
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end="")
        is_first = False
print(".")