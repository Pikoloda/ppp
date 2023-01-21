import random

counter = 1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbe mam na myśli (1-10): "))

while number != guess:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się za " + str(counter) + " razem.")
