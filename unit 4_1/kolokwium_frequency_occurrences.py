# Napisz funkcję zlicząjąca ilosć wystąpień poszczególnych elemenetów listy w formie słownika.

# Przykład

# print(frequency_occurrences(["Ala", "Tomek", "Ala"]))

# {'Ala':2, 'Tomek': 1)"""

def frequency_occurrences(sourde_list):
    target_list = {}
    for e in sourde_list:
        if e in target_list:
            target_list[e] += 1
        else:
            target_list[e] = 1
    return target_list


print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
print(frequency_occurrences([2, 2, 2]))
