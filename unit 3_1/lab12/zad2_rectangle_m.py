# 2. Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998.

def rectangle(bok_a, bok_b):
    print("Obwód prostokątką o bokach", bok_a, "i", bok_b, "wynosi : ", 2 * bok_a + 2 * bok_b)
    print("Pole prostokątką o bokach", bok_a, "i", bok_b, "wynosi : ", bok_a * bok_b)
    print("Długość przekątnej prostokątką o bokach", bok_a, "i", bok_b, "wynosi : ", (bok_a ** 2 + bok_b ** 2) ** .5)


rectangle(4, 5)
print()
rectangle(2678, 5678)
print()
rectangle(344555, 788998)
