# Zad1.
# Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.

alphabet = ""

for i in range(ord("a"),ord("z")+1):
    alphabet += chr(i)
    # print(chr(i),"->",ord(chr(i)))

# print(alphabet)
znaki_diaktryczne = "ąćęłńóśźż"
alphabet += znaki_diaktryczne

for el in alphabet:
    print(el,"->",ord(el))
print(alphabet)
