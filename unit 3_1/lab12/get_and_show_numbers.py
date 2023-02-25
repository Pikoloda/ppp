# def show_message(number_no):
#     print("Proszę podaj " + str(number_no) + " liczbę:", end=" ")
#
#
# show_message(1)
# a = int(input())
# show_message(2)
# b = int(input())
# show_message(3)
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

# przekształcamy do jeszcze krótszej wersji

def get_number(number_no):
    return int(input("Proszę podaj " + str(number_no) + " liczbę: "))

print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))
