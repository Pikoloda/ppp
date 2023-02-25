# Npisz program, który zasymuluje 10 rzutów kostką do gry a następnie wyświetli
# informacje o wynikach dla 1, 4 i 9 rzutu kostką. Przykład działania progrmau:

# Za 1 razem wypadła 1
# Za 4 razem wypadła 3
# Za 9 razem wypadła 6

#kostka oczka 1 do 6

import random
numbers =[]

for i in range(10):
    numbers.append(random.randint(1,6))

print(numbers)
print("-"*50)
print("Wyrzucono za pierwszym razem - ", numbers[1-1])
print("Wyrzucono za czwartym razem - ", numbers[4-1])
print("Wyrzucono za dziewiątym razem - ", numbers[9-1])