# Zad3.
# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

def calculate_bmi(weght_in_kg, height_in_cm):
    return weght_in_kg / height_in_cm ** 2


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


print("Obliczanie wskaźnika BMI!")
weght_in_kg = float(input("Podaj swoją wagę w kg:"))

height_in_cm = float(input("Podaj swój wzrost (cm):"))


bmi = round(calculate_bmi(weght_in_kg, height_in_cm*0.01 ),2)
category = determine_bmi_category(bmi)

print("Wskaźnik bmi wynosi: ",bmi)
print("Kategoria: ",category)


# print(weght_in_kg, height_in_cm)
# print(calculate_bmi(weght_in_kg, height_in_cm * 0.01))