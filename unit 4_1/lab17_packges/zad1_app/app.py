# Zad1.
# Stwórz pakiet wraz z subpakietami i modułami wg schematu jak na rysunku i dodatkowo:
# • w każdym module umieść definicję funkcji fun(),
# • wspomniana funkcja powinna wyświetlać informacje
# • funkcji, module oraz pakiecie z jakiego została wywołana,
# • skrypt app.py powinien wywoływać wszystkie funkcje.

from pack1.mod1 import fun as f
f()

from pack1.subpack1.mod2 import fun as fs1
fs1()

from pack1.subpack2.mod3 import fun as fs2
fs2()
