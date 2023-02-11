# Zad3.
# Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
# występuje 3 razy.

digits = [1, 3, 5, 3, 7, 8, 3, 3, 3, 7, 7, 7, 5, 5, 5, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
frequancy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in digits:
    frequancy[digit] += 1
print(frequancy)

most_common_temp = -1
most_common = 0
for i in range(len(frequancy)):
    if frequancy[i] > most_common_temp:
        most_common_temp = frequancy[i]
        most_common = i

print("Najczęsciej występującą cyfrą jest " + str(most_common) + ",", "występuje", frequancy[most_common], "razy.")
