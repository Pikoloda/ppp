# a = 1
# b = 4
#
# print("a =", a, "b =", b)
#
# # zamiana wartości zmiennych
# # tmp = a
# # a=b
# # b=tmp
#
# a, b = b, a
#
# print("a =", a, "b =", b)
#
# -------

# numbers = [1, 2, 3]

# zamiana elementów listy
# numbers[0], numbers[1] = numbers[1], numbers[0]
# print(numbers)

# ------
# różnego typu wartości w liście - sortowanie

# letters = ["A", "C", " ", "B", "a"]
# letters.sort()
# letters.sort(reverse=True)
# print(letters)

# print(ord("A"),ord("C")) podaje wartość
# print(ord("a"),ord("A")) - różne wartości -> tabeli ascii (https://www.asciitable.com/?utm_content=cmp-true)

# -------

# list_1 = [9]
# list_2 = list_1
#
# list_2[0] = 13
#
# print(list_2)
# print(list_1)

# ------
# wycinanie - slice

# list_1 =[9]
# list_2 = list_1[:] # skopiuj cała liste [:] - wycięliśmy wszystkie elementy
# list_2 = [list_1]

# list_2[0] = 13
# print(list_2)
# print(list_1)
#          -5 -4 -3 -2 -1
# numbers = [10, 8, 6, 4, 2]
# new_numbers = numbers[1:3] # oddzielne miejsce w pamieci na lista new_numbers, jakbyśmy przypisali new_numbers = numbers -> to samo miejsce wartości listy, dwie nazwy
# print(new_numbers)

# new_numbers = numbers[-4:-2]
# print(new_numbers)

# po za zakresem indeksów , wynik zbiór pusty

# new_numbers = numbers[0:len(numbers)] # kopiuje całość listy
# print(new_numbers)

# ------

# usuwanie wycinków

# numbers = [10, 8, 6, 4, 2]

# del numbers[1:3] # usuwa fragment listy
# del numbers[:] # usuwamy wszystkie elementy listy
# del numbers # usuwa obiekt numbers

# ------
# sprawdzamy czy dana wartość jest lub nie jest na liście

# numbers = [10, 8, 6, 4, 2]

# print(5 in numbers)
# print( 7 not in numbers)

# ------
# wyrażenia listowe

# numbers = [10, 8, 6, 4, 2]
# wygenerowanie listy od 1 do 1000
# numbers=[]

# for i in range(1, 1001):
#     numbers.append(i)

# print(numbers)

# zapisaliśli liste od 1 do 1000 (wygenerowaliśmy) za pomocą wyrażenie listowe

# numbers = [i for i in range(1, 1001)]
# print(numbers)

# numbers = [i ** 2 for i in range(1, 101)]

# numbers = [i for i in range(1, 101) if i % 2 == 0]

# print(numbers)

# Zadanie
# Ile liczb w  przedziale od 1 do 300, które dzielą się przez 3  i 7

# numbers = [i for i in range(1,301) if i % 3 == 0 and i % 7 == 0 ]
# print(numbers)
# print(len(numbers))

# print(len([i for i in range(1,301) if i % 3 == 0 and i % 7 == 0 ]))

