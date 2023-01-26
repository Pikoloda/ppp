# Zad3.
# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp..

import random

number = random.randint(1, 10)
msg = " Zgadnij o jakiej liczbie myśle (od 1 do 10): "
guess = int(input(msg))
if guess == number:
    print("Udało Ci się ! O tej liczbie właśnie myślałem.")
else:
    msg = "Masz kolejną szanse, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess=int(input(msg))
    if guess == number:
        print("Tym razem udało Ci się! Właśnie myślałem o tej liczbie.")
    else:
        msg = "Masz ostatnią szansę, moja liczba jest "
        if number > 5:
            msg += "większa"
        else:
            msg += "mniejsza lub równa"
        guess=int(input(msg + " od 5: "))
        if guess == number:
            print("Udało Ci się ! Do trzech razy sztuka")
        else:
            print("Może następnym razem, myślałem o liczbie " + str(number) + ".")

