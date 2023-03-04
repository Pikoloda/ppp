# Zad1.
# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.


def print_char(character="*", rep=10, vert=False):
    for i in range(rep):
        if vert:
            print(character)
        else:
            print(character + " ", end="")
    if not vert:
        print()
    print()

# Sprawdzenie, 3 przykłady

print_char()
print_char("+", 5, True)
print_char("^", 7, False)
