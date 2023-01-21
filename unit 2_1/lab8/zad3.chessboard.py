# szachownica ma 64 pola

# 0 1 2 3
# 1 2 4 8 ... 2 ** i
sum = 0
for i in range(64):
    sum += 2 ** i
print("Suma wszystkich ziaren zboża na szachownicy: " + str(sum))

# 1 ziarno to - 0,4 mg
# 1 ziarno to - 0,0004 g
# 1 ziarno to - 0,0000004 kg
# 1 tona = 1000 kg

tons = int(sum * 0.0004 / 1000 / 1000)
print(tons)

# produkcja przeniscy na świecie to około 782 mln ton

years = round((tons / 782_000_000), 2)  # 782_000_000 =782e6 = 782 * 1000 * 1000
print(years)

# 1 pociag może przetransportować 2200 ton
trains = int(tons / 2200) # i jeden wiecej na końcówke
print(trains)
