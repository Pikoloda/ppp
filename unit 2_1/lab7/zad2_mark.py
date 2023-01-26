# Zad2.
# Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość otrzymanych punków z kolokwium:
# • ocena bardzo (5,0) dobra, jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej (2.0)


points = int(input("Podaj ilość punktów z kolowium (0-100): "))

if points >= 95:
    print("Ocena - 5")
elif points > 84:
    print("Ocena - 4,5")
elif points >= 70:
    print("Ocena - 4")
elif points > 60:
    print("Ocena - 3,5")
elif points > 50:
    print("Ocena - 3")
else:
    print("Ocena - 2,0")
