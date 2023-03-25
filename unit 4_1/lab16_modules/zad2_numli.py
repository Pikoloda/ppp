# Zad2.
# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,
# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
# • dodaj funkcję sumującą wszystkie liczby z listy,
# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.


def is_list_of_integers(list):
    for i in list:
        if not isinstance(i, int):
            return False
    return True


def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def product_list(list):
    product_list = 1
    for i in list:
        product_list *= i
    return product_list


if __name__ == "__main__":
    list = [1, 2, 3]
    print(is_list_of_integers(list) == True)
    print(is_list_of_integers(["a", "b", "c"]) == False)
    print(is_list_of_integers(["asdad", False]) == False)
    print(sum_list(list) == 6)
    print(sum_list(list) != 7)
    print(product_list(list) == 6)
    print(product_list(list) != 45)
