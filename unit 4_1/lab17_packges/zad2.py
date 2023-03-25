# Zad2.
# Rozbuduj program z zadania 1. zmieniając kod tak,
# aby podczas imortu wyświetlały się komunikaty o inicjalizacji
# danego pakietu lub modułu, np. "inicjalizuję pack1".


from zad1_app.pack1.mod1 import fun as f
f()

from zad1_app.pack1.subpack1.mod2 import fun as fs1
fs1()

from zad1_app.pack1.subpack2.mod3 import fun as fs2
fs2()
