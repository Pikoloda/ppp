# ValueError

counter = 0
numbers = []

while True:
    if counter > 4:
        break
    try:
        n = int(input("Podaj liczbę całkowitą: "))
        numbers.append(n)
        counter += 1
    except:
        print("To nie jest liczba całkowita! Spróbuj ponownie")

print(numbers)


