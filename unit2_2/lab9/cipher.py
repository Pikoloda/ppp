# Xq|`gf(bm{|(nibfq)
# znamy sposób zakodowania
# dla każdego znaku zmieniono 4 bit na przeciwny
# bity liczymy od najmniej znaczącego, 4 bit -> indeks 3
# zbior znaków aski !!! poczytać ord()

# print(ord("c"))
# print(bin(ord("c")))
# print(char(99)) - zamiana na stringa

# print("{:08b}".format(ord("c"))) #01100011

# 01100011 - nasza liczba
# 00001000 - maska
# 01100011 - używamy XORa (alternatywa rozłączna)

# print("{:08b}".format(1 << 3))  # maska, przesuniecie o indeks 3
#
# print("{:08b}".format(ord("c") ^ (1) << 3))
#
# print(chr(ord("c") ^ (1) << 3))



msg = "Xq|`gf(bm{|(nibfq)"
for c in msg: # do "c" wstawiane pokolei ciag znaków
    print(chr(ord(c) ^ (1 << 3)), end="")
    
