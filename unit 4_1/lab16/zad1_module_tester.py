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
print("Wylosowano następujące trzy liczby z przedziału (1-10): ", sample(range([i for i in range(1,11)], 3)))
print(math.sin(math.radians(90)))