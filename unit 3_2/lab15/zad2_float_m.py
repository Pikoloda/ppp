# Zad2.
# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika.

numbers =[]


for i in range(3):
    try:
        num = float(input("Podaj liczbę zmiennoprzecinkową: "))
        numbers.append(num)
    except ValueError:
        print("To nie jest liczba zmiennoprzecinkowa!")
print(numbers)

# ValueError