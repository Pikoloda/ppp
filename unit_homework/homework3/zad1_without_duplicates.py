# Zad1.
# Napisz funckję, która pozbędzie się z listy powtarzających się elementów.

def without_duplicates(list):
    list_without_duplicate = []
    for el in list:
        if el not in list_without_duplicate:
            list_without_duplicate.append(el)
    list_without_duplicate.sort()
    print(list_without_duplicate)


# Przykład
number_1 = [2, 34, 5, 56, 6, 345, 4, 4, 4, 4, 4]
number_2 = [2.3, 2.3, 3.2, 33., 1, 2.3]
number_3 = ["a","A","maks","paasda","aks","ca","ca" ]

# Sprawdzenie
without_duplicates(number_1)
without_duplicates(number_2)
without_duplicates(number_3)
