# 3. Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
# występuje 3 razy.

digits = [1, 3, 5, 3, 6, 6, 7, 8, 3, 3, 3, 6, 7, ]
frequancy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in digits:
    frequancy[digit] += 1

print(frequancy)

most_common = -1

for i in range(len(frequancy)):
    if frequancy[i] > most_common:
        most_common = i

print("Najczęsciej występująca cyfrą jest " + str(most_common) + ",", "występuje", frequancy[most_common], "razy")

