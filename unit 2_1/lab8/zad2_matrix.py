# zad2.
# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik



size = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(size):
    for j in range(size):
        print(char, end=" ")
    print()


