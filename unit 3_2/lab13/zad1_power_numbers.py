# Zad1.
# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

print("Pierwsza opcja")

def pow(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


print(pow([1, 2, 3], 2))

print(pow([2, 11, 5], 5))
print()

9
# druga opcja
print("Druga opcja")

def pow2(numbers, exponent):
    result = []
    for num in numbers:
        result.append(num ** exponent)
    return result


print(pow2([1, 2, 3], 2))

print(pow2([2, 11, 5], 5))
print()
# trzecia opcja

print("Trzecia opcja")

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]


print(pow3([1, 2, 3], 2))

print(pow3([2, 11, 5], 5))
