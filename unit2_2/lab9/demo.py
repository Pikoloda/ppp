# jeżeli temperatura bedzie dodatnia i będzie słonecznie  to...
# to pójdziemy na spacer a jeżeli nie to zostaniemy w domu

temperature = 12
is_sun_shining = False

# if temperature > 0 and is_sun_shining : # True and False -> False
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu")


# if temperature > 0 or is_sun_shining : # True or False -> True
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu")


# Jeżeli temperatura będzie ujemna lub będzie pochmurno to zostaniemy w domu,
# jeżeli nie to pójdziemy na spacer

# if temperature < 0 or not is_sun_shining:
#     print("Zostajemy w domu")
# else:
#     print("Pójdziemy na spacer")


# if not (temperature < 0 or not is_sun_shining):
#     print("Pójdziemy na spacer")
# else:
#     print("Zostajemy w domu")


###  Operatory logiczne
# and - koniukcja - czytamy jako i
# or - alternatywa - czytamy jako lub
# not - negacja - czytamy jako nie

# wyświetl cyfre, chyba że...
# liczba parzysta lub liczba większa od 6 to wyświetlij *


# for i in range(10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)


### Operatory bitowe

# a = 5
# b = 3
# koniunkcja bitowa
# print(a, "&", b, "=", a & b)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a & b))

# alternatywa bitowa

# a = 5
# b = 3
# print(a, "|", b, "=", a | b)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a | b))

# alternatywa rozłączną bitowa

# a = 5
# b = 3
# print(a, "^", b, "=", a ^ b)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a ^ b))

# przesunięcie bitowe w prawo

# a = 5
# b = 2
# print(a, ">>", b, "=", a >> b)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("-" * 8)
# print("{:08b}".format(a >> b))

# przesunięcie bitowe w lewo

# a = 5
# b = 2
# print(a, "<<", b, "=", a << b)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("-" * 8)
# print("{:08b}".format(a << b))

#  negacja bitowe

# a = 5
# b = 2
# print("~", a, "=", ~a)  # !!
# print(bin(a))
# print("{:08b}".format(a))  # !!!!!
# print("-" * 8)
# print("{:08b}".format(~a))

# kod uzupełnień do dwóch !!!! wyjasnia dlaczego ~5 = - 6
# poczytać o +0 i -0 !!!

for i in range(5, -6, -1):
    print("{0:08b}=>{1:d}".format(i & 255, i))  # !!!!!

