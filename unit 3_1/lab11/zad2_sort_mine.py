# 2. Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.
import random

# user = int(input("Podaj liczbę: "))
num_series = random.randint(1,10)
user_numbers =[]
for i in range(num_series):
    user_numbers.append(int(input("Podaj liczbę: ")))
    user_numbers.sort(reverse=True)

print(user_numbers)
