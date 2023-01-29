# Zad3.
# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp.

# import random
#
# number = random.randint(1, 10)
# msg = "Zgadnij jaką liczbę miałem na myśli (od 1 do 10): "
# guess = int(input(msg))
# if guess == number:
#     print("Udało Ci się ! Dokładnie taką liczbę miałem na myśli!")
# else:
#     msg = "Masz kolejną szanse, moja liczba jest "
#     if number % 2 == 0:
#         msg+= "parzysta: "
#     else:
#         msg += "nieparzysta: "
#     guess = int(input(msg))
#     if guess == number:
#         print("Brawo! Udało się za drugim razem!")
#     else:
#         msg = "Masz kolejną szanse, moja liczba jest "
#         if number > 5:
#             msg += "większa "
#         else:
#             msg += "miejsza lub równa"
#         msg += " od liczby 5: "
#         guess = int(input(msg))
#     if guess == number:
#         print("Brawo! A jednak, do trzech razy sztuka!")
#     else:
#         msg = "Niestety, miałem na myśli liczbę "+ str(number)
#         print(msg)
