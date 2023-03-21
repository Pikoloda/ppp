# Zad2.
# Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy
# wyższy poziom wymaga jednej puszki mniej niż poziom na którym go
# zbudowano. Korzystając z rekurencji napisz program, który pozwoli
# wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
# poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
# dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową
# wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4
# poziomową wieżę.


def how_many_cans(level):
    if level == 1:
        return 1
    else:
        return level + how_many_cans(level - 1)


# Przykład
# print(how_many_can(15))


def how_max_level_of_tower(can_quantities):
    level = 1
    while how_many_cans(level) <= can_quantities:
        level += 1
    return level - 1, how_many_cans(level - 1)


# Przykład
# print(how_max_level_of_tower(15))

def count_the_number_of_levels_and_cans(level, quantities_can=0):
    total_can = how_many_cans(level)
    max_level = how_max_level_of_tower(quantities_can)
    return print("Ilość puszek " + str(total_can)), print("Maksymalny poziom " + str(max_level))


count_the_number_of_levels_and_cans(5, 10)
