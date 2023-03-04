 # 1. Napisz skrypt symulujący grę losową:
 # • użytkownik obstawia 6 liczb z 49,
 # • program losuje 6 liczb z 49,
 # • użytkownik dostaje informacje o ilości trafień.

import random

user_numbers = []
random_numbers = []
hit_total = 0

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę (1-49): ")))

    random_numbers = random.sample(range(1, 50), 6)

for number in user_numbers:
    if number in random_numbers:
        hit_total += 1

user_numbers.sort()
random_numbers.sort()


print("Wylosowane liczby :",random_numbers)
print("Obstawione liczby:",user_numbers)

print("Trafiono: ", hit_total, "liczb.")
