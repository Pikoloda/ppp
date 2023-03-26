# Zad1.
# Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.

alphabet = "abcdefghijklmnopqrstuvwxyząćęłńóśźż" # po kolei wkleić !!

for c in alphabet:
    print(c,"->", ord(c))
