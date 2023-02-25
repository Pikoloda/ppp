# # 1. Napisz skrypt symulujący grę losową:
# # • użytkownik obstawia 6 liczb z 49,
# # • program losuje 6 liczb z 49,
# # • użytkownik dostaje informacje o ilości trafień.
# import random
#
# # user = int(input("Podaj liczbę z zakresu od 1 do 49: "))
# user_numbers = []
# for i in range(6):
#     user = int(input("Podaj liczbę z zakresu od 1 do 49: "))
#     user_numbers.append(user)
# print(user_numbers)
#
# program_numbers = []
# numbers = [i for i in range(1, 50)]
# program_numbers.append(random.sample(numbers, 6))
# print(program_numbers)
#
# sum = 0
# for i in range(len(user_numbers)):
#     if user_numbers[i] in program_numbers:
#         sum += 1
# print(sum)

# ____
# rozwiązanie

import random

user_numbers = []
random_numbers = []
hit_total = 0

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę od 1 do 49: ")))

    random_numbers = random.sample(range(1, 50), 6)

for number in user_numbers:
    if number in random_numbers:
        hit_total += 1

user_numbers.sort()
random_numbers.sort()


print("Wylosowane liczby :",random_numbers)
print("Obstawione liczby:",user_numbers)

print("Trafiono: ", hit_total, "liczb.")


