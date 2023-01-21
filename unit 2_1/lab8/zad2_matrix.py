
size = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(1, size + 1):
    print(char * size)


# for i in range(size):
#     for j in range(size):
#         print(char, end=" ")
#     print()