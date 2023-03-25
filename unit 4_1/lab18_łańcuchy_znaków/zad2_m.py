# Zad2.
# Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1 }.

def str(char):
    dirt ={}
    for el in char:
        print(el, end=" ")
        dirt[el] = char.count(el)
    return dirt

print(str("asdadaasasfasfawfa"))




