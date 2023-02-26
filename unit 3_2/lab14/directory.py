# phones = {
#     "Tomek": 345152223,
#     "Ada": 122555666,
#     "Karol": 124445588,
#     "Tomek": 1000000
# } # aktualizuje Tomka
#
# print(phones)


# animals_dict = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }

# print(animals_dict.get("kot"))
# print(animals_dict.get("krowa"))
# print(animals_dict["krowa"])
# print(animals_dict["kot"])

# print(animals_dict.get("krowa", "brak słowa"))

# words = ["kot", "lew", "chomik"]
# for word in words:
#     if word in animals_dict:
#         print(word, "->",animals_dict[word])
#     else:
#         print("Nie znaleziono słowa", word, "w słowniku.")
#
# for key in animals_dict.keys(): # for key in animals_dict(): - może byc też bez key
    # print(key,"->", animals_dict[key])
#
# for val in animals_dict.values():
#     print(val)

# for item in animals_dict.items():
#     print(item)

# for  pl,en in animals_dict.items():
#     print(pl, "->", en)

# a,b =(1,2)
# print(a)
# print(b)

animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

# animals_dict["świnka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"świnka": "piggy"})

# kopia słownika

# dict2 = animals_dict.copy()
# print(animals_dict)
# print(dict2)
# usuwanie elementów słownika

# del dict2["kot"]
# dict2.popitem() # usuwa ostatni element
#
# dict2.clear()# czyści cały słownik
# print(dict2)
