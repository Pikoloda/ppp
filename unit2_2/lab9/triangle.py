print("Podaj długości 3 odcinków (liczby całkowite): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a + b > c and a + c > b and b + c > a):
    print("Z tych odcinków można zbudować trójkąt", end=" ")
    # sprawdzanie rodzaju trójkata ze wgledu na boku
    if a == b and a == c and b == c: # a == b == c niby okey, ale czy to dobra praktyka, mo ze powodować błedy
        print("równoboczny", end=(" "))
    elif a == b or a == c or b == c:
        print("równoramienny", end=" ")
    else:
        print("różnoramienny", end=" ")
B
    # sprawdzanie rodzaju trójkata ze wgledu na kąty

    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        print("prostokątny.")
    elif (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (a ** 2 + c ** 2 < b ** 2):
        print("rozwartokątny.")
    else:
        print("ostrokątny.")

else:
    print("Niestety z tych odcinków nie powstanie trójkąt")
