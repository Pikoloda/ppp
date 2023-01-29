# Zad3.
# Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
# drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
# więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
# taką sytuację i zliczy sumę wszystkich ziaren na szachownicy

# szachownica ma 64 pola

# 0 1 2 3
# 1 2 4 8 ... 2 ** i

sum = 0
for i in range(64):
    sum += 2 ** i
print("Suma wszystkich ziaren zboża na szachownicy wynosi " + str(sum))
