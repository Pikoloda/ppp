# Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
# • inwestowane środki 46 567,00 zł
# • stałe oprocentowanie roczne 7.5%
# • coroczna kapitalizacja odsetek
# • w obliczeniach zastosuj złożony operator przypisania


deposit = 46_567.
factor = 1.075
invested_funds = deposit

# invested_funds = invested_funds * factor
# invested_funds = invested_funds * factor
# invested_funds = invested_funds * factor

invested_funds *= factor
invested_funds *= factor
invested_funds *= factor

print("Zysk z trzyletniej inwestycji w lokate bankową wynosi", round(invested_funds - deposit, 2), "zł.")
