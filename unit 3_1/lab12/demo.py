# name = input("Jak masz na imię?")
# print(("Witaj "+ name + "! ")*100)

# --------

# print("raz","dwa","trzy")

# def introduce(first_name, last_name):
#     print("Cześć, jestem", first_name,last_name)

# introduce("Jan","Kowalski")
# introduce("Kowalski","Jan")

# introduce(last_name="Kowalski", first_name="Jan")
# introduce(first_name="Jan",last_name="Kowalski")# kolejność nie ma znaczenia, można miksować te sposoby ( przekazywania argumentów)
# introduce("Jan",last_name="Kowalski")
# introduce(last_name="Kowalski","Jan")# błąd

# print("raz","dwa","trzy", sep= " - ")# tak używaliśmy już wcześniej

# def introduce(first_name = "Jan", last_name= "Kowalski"):
    # print("Cześć, jestem", first_name,last_name)

# introduce()# wartości domyślne , zdefiniowane w def , muis być podany osttani rgument np last_name = "Kowalski"

# introduce("Piotr")

# ---------

# def introduce(first_name = "Jan", last_name= "Kowalski"):
#     print("Cześć, jestem", first_name,last_name)
#     return None
#
# print(introduce())

def my_fum():
    # TODO
    return 123


if my_fum() == None:
    print("Funkcja narazie nic nie zwraca")