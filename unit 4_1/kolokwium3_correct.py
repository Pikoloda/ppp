# Napisz funkcję, która będzię potrafiła zamienić klucze na wartości w przekazanym do nie słowniku.

# Przykład:

# print(reverse_dict({'a': 1, 'b': 2}))

# {1: 'a', 2: 'b'}


def reverse_key_and_value(dir):
    new_dict ={}
    for pl, en in dir.items():
        new_dict[en] = pl
    return new_dict




animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

print(animals_dict)
print(reverse_key_and_value(animals_dict))


