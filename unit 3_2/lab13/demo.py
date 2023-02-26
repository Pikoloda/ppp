# def sum_numbers(numbers):
#     sum = 0
#     for element in numbers:
#         sum += element
#     return sum


# numbers = [1, 2, 3]
# result = sum_numbers(numbers)
# print(result)

## podstawiam wartość skalarną, błąd TypeError
## obiekt, liczba 99 nie da się iterować

# sum_numbers(99)


# -----

## Zasięg zmiennych

# def scope_test():
#     x = 123

# scope_test()
# print(x)# x NameError , nie zdefiniowana zmienna

# def scope_test():
#     print("w środku funkcji: ", x)

# x = 99
# scope_test()

## Nadpisywanie zmiennej, zmienna lokalna w ciele funkcji

# def scope_test():
#     x = 123
#     print("w środku funkcji: ", x)


# x = 99
# scope_test()
# print("na zewnątrz funkcji: ", x)

##Zmienna globalna w ciele funcji

# def scope_test():
#     global x
#     x = 123
#     print("w środku funkcji: ", x)


# x = 99
# scope_test()
# print("na zewnątrz funkcji: ", x)


## Przekazywanie wartości do funkcji
# wartość skalarna najpierw

# def change_value(n):
#     print("Przed zmianą n:", n)
#     n += 1
#     print("Po zmianie n :", n)

# val = 7
# change_value(val)
# print("val",val)

# wartość nieskalarna np lista

# def change_value(n):
#     print("Przed zmianą n:", n)
#     n =[0,0]
#     print("Po zmianie n :", n)

# val = [1,2]
# change_value(val)
# print("val",val)

# def change_value(n):
#     print("Przed zmianą n:", n)
#     n[0] = 999
#     print("Po zmianie n :", n)
#
# val = [1,2]
# change_value(val)
# print("val",val)

######## przerobić w domu !!!!!

# krotka ?
# def my_func(*args):
#     for el in args:
#         print(el)


# my_func(1, 2, 3, 4, 5, 6, 7, 8)


def my_func(**args):
    for el in args.items():
        print(el)


my_func(val1="raz", val2=999)
