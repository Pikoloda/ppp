# Zad3.
# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter



import random


# print(ord("A"))
# print(chr(65))
FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 8

# losowanie jednej litery

def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))

# losowanie ciągu 3 liter

def draw_row():
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]


# sprawdzanie czy są takie same elementy

def check(row):
    first_element = row[0]
    for element in row:
        if element != first_element:
            return False
    return True

# zaczynamy losowanie , w pętli while

counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1


 # przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.
#   zmiany w każdej def