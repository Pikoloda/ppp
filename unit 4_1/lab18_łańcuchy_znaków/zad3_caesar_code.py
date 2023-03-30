# Zad3.
# Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
# cezara z parametrem przesunięcia równym 3.

# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

delta = 3


def decode_letter(letter, delta):
    if letter < "A" or letter > "Z":
        return letter
    n = ord(letter) - delta
    if n < ord("A"):
        n += ord("Z") - ord("A") + 1
    return chr(n)


print()


# Testy
# print(decode_letter("J", delta))
# print(decode_letter("B", delta) == "Y")

def decode(string, delta):
    decoded = ""
    for char in string:
        decoded += decode_letter(char, delta)
    return decoded


# Test
print(decode("VCBIU", delta))
print(decode("VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ", delta))
