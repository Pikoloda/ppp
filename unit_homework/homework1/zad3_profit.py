#   Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
#   następujących założeniach:
# • własne środki 30 tys. zł,
# • roczna lokata kapitału,
# • kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
# • oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
# • pokazać salda po każdym kwartale,
# • wyliczyć roczny zysk.

deposite = 30_000
invest = deposite

factor1 = 0.075
factor2 = 0.08
factor3 = 0.0825

# dla oprocentowania 7.5%

deposite = 30_000
invest = deposite
print("Oprocentowanie 7.5%\n")

invest *= (1 + factor1 / 4)
print("Saldo po pierwszym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor1 / 4)
print("Saldo po drugim kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor1 / 4)
print("Saldo po trzecim kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor1 / 4)
print("Saldo po czwartym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

print("Roczny zysk na lokacie bankowej z oprocentowaniem 7.5%, przy kapitalizacji kwartalnej wynosi", round(invest - deposite,2),
      "zł.\n\n")

# dla oprocentowania 8%

deposite = 30_000
invest = deposite
print("Oprocentowanie 8%\n")

invest *= (1 + factor2 / 4)
print("Saldo po pierwszym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor2 / 4)
print("Saldo po drugim kwartale kapitalizacji odsetek wynosi", round(invest,2), "zł\n ")

invest *= (1 + factor2 / 4)
print("Saldo po trzecim kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor2 / 4)
print("Saldo po czwartym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

print("Roczny zysk na lokacie bankowej z oprocentowaniem 8%, przy kapitalizacji kwartalnej wynosi", round(invest - deposite,2),
      "zł.\n\n")

# dla oprocentowania 8.25%

deposite = 30_000
invest = deposite
print("Oprocentowanie 8.25%\n")

invest *= (1 + factor3 / 4)
print("Saldo po pierwszym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor3 / 4)
print("Saldo po drugim kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor3 / 4)
print("Saldo po trzecim kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

invest *= (1 + factor3 / 4)
print("Saldo po czwartym kwartale kapitalizacji odsetek wynosi",round(invest,2), "zł\n ")

print("Roczny zysk na lokacie bankowej z oprocentowaniem 8.25%, przy kapitalizacji kwartalnej wynosi", round(invest - deposite,2),
      "zł.\n")