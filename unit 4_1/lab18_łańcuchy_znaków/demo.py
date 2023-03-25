# txt = "Ala ma kota."

# print(len(txt))

# print(txt[-3])

# print(len(""))

# print(len("\t\n\\"))

# txt ="To jest tekst."\
# " To dalszy ciąg"
# print(txt)


# txt ="""To jest tekst.
#      To dalszy ciąg"""

# print(len(txt))

# txt = """a
# b
# c"""

# print(len(txt))

# txt2 = "a\nb\nc"

# print(len(txt2))

# str1 = "a"
# str2 = "b"
# print(str1 + str2)
# print(str2 + str1)
# print()

# print(str1 * 3)
# print(5 * str2 )
# print()

# str1 += str2

# print(str1)

# str1 *= 10
# print(str1)

## Wartość punktu kodowego
## Funckja ord

# char1 = "a"
# char2 = " "

# print(ord(char1))
# print(ord(char2))
# print()

# print(ord("ę"))
# print(hex(ord("ę")))
# print(ord("\n"))
# print(ord("\t"))
# print("\u0119")
# c = "a"
# print(c, ord(c), hex(ord(c)), c.encode()) # punkt kodowy, unicode, ilość bajtów, które zamjmuje

# print()

# c = "\u20AC"
# print(c, ord(c), hex(ord(c)), c.encode()) # zajmuje 3 bajty


##Funkcja chr

# print(chr(97))
# print(chr(945))  # alfa

# print("a" == chr(ord("a")))


#      1234567891011
# txt = "Ala ma kota."

# print(txt[-1])

# for i in range(len(txt)):
#     print(txt[i], end="-")

# print()

# for c in txt:
#     print(c, end="-")

## Wycinki
     # 01234567891011
# txt = "Ala ma kota."

# print(txt[4:6])
# print(txt[7:])
# print(txt[-1:])
# print(txt[2::3])

# print(ord("a"))
# print(ord("z"))

alphabet = ""

for i in range(ord("a"),ord("z")+1):
    alphabet += chr(i)

# print(alphabet)
# print()

# print("abce" not in alphabet)

# del alphabet
# alphabet.append("asdafa") -> błąd AtribiutteError

# print(alphabet)

# alphabet += "AAAA"# można !!
# print(alphabet)


# print((min([1,2,3])))
# print((max([1,2,3])))
# print(min("abcABC"))
# print(max("abcABC")) # punkt kodowy c ma najwiekszy

# print(max("Ala ma kota."))

## Funkcja index

# print(alphabet.index("w"))
# print("aAbDyYzZAa".index("A")) # index zwraca index pierwszego powtórzonego argmentu "A"
# print([1,2,3].index(3))
# print(list(alphabet))
# print("Ala ma kota.".count("a"))
# print(alphabet.count("a"))
# print([1,1,1,1,1,32,3].count(1))