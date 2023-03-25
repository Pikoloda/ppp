# Zad1.
# Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

from platform import processor
from random import sample
import math

print("Proces Komputera: ", processor())
print("Wylosowano następujące trzy liczby z przedziału (1-10): ", sample(range(1,10), 3))
print(math.degrees(math.sin(90)))


