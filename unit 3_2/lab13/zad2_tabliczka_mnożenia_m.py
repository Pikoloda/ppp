# Zad2. Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

def multiplication_table(number=100, sum = 0 ):
    for i in range(1, number + 1):
        sum = i ** i
    return
    i += 1
    recursion(multiplication_table())


print(multiplication_table())
