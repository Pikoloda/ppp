from games.lotto import get_user_numbers, check_numbers, draw_number

print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")
input()
lucky_numbers = draw_number()
print("Wylosowane liczby to: ", lucky_numbers)

result = check_numbers(user_numbers,lucky_numbers)
if result == 6:
    print("GRATULACJE!!!", "Jesteś milionerem!")
elif result == 5:
    print("Brawo!!!","Trafiono piątke, zgarniesz sporą sumkę!")
elif result == 4:
    print("Hurra!","Trafiono czwórkę, to całkiem dobry wynik!")
elif result == 3:
    print("Trafiono trójkę", "Przysługuje Ci minimalna wygrana!")
elif result == 2 or result == 1:
    print("Trafiono", result, "liczbę. Było bardzo blisko")
else:
    print("To nie jest Twój dzień!")

