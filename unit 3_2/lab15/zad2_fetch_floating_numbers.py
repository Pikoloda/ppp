# Zad2.
# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika.

numbers = []
counter = 1

while True:
    if counter > 3:
        break
    try:
        number = float(input("Podaj "+ str(counter) + " liczbę zmiennoprzecinkową: "))
        numbers.append(number)
        counter += 1
    except:
        print("Podana wartość jest niepoprawna, spróbuj ponownie!")

print(numbers)
