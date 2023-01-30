# zad3.
# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu

# 01001 - przykładowa liczba
# 00001 - maska
# &
# 00001 - wynik (1)

number = int(input("Podaj liczbę: "))
n = int(input("Podaj nr bitu: "))

mask = 1 << n
result = number & mask

bit = int(bool(result))
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit,".")