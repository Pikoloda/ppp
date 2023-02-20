# Zad3.
# Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
# liczbę jedynek w ciągu bitów reprezentujących tę liczbę.

number = int(input("Podaj liczbę całkowitą: "))
number_ones = 0
mask = 1
binary = bin(number)[2:]

print("-" * 50)
print("Format binarny")
# print(("{:08b}".format(number)))
print(binary)

while True:
    if number == 0:
        break
    if number & mask == 1:
        number_ones += 1
    number >>= 1

print()
print("Liczba jedynek w ciągu bitowym reprezentujących podaną przez użytkownika liczbę wynosi:", number_ones)
