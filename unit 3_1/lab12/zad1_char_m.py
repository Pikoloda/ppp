# zad1. Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

def show_char(char, quantity, vertically=False):
    if vertically == True:
        for i in range(quantity):
            print(char, end="\n")
    else:
        print(char * quantity)


show_char("*", 5,True)

