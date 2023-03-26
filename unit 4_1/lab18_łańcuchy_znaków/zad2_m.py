# Zad2.
# Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1 }.

def str(char):
    dirt ={}
    for el in char:
        dirt[el] = char.count(el)
    return dirt

print(str("asdadaasasfasfawfa"))
print(str("Ala ma kota i kot ma Ale."))
# Lista l = [1, 2, 3] l[0] - list
# krotka t = (1, 2, 3) t[1] - tuple
# słownika d = {"a" : 1, "b" : 2} - dict
# ciąg znaków s = "abcde" - string

