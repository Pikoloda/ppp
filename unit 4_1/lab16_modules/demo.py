## Pierwszy sposób

# import math
# import sys

# print(math.pi)
# print(math.sin(math.pi / 2))
# print(math.factorial(15))
# print(math.floor(1.2))

## Drugi sposób

# from math import pi, sin, factorial

# print(pi)
# print(math.pi) # NameError math in not defined (math)
# print(sin(pi / 2)) # NameError math in not defined (sin)
# print(sin(pi / 2))
# print(factorial(123))

## Trzeci sposób - niezalecany

# from math import *

# print(sin(pi / 2))
# print(factorial(123))
#
# print(ceil(3.8))

## ALiasy

# import math as m

# print(m.pi)
# print(math.pi) # błąd
# print(pi) #

# from math import pi as mathpi

# print(mathpi)
# print(pi) # błąd

## Funkcja "dir"

# import math

# for e in dir(math):
#     print(e)


## Kolejny moduł random

import random

# for e in dir(random):
#     print(e)

# print(random.randint(1,3))
# print(random.random())

from random import random, seed

# seed(0) # generator ustawiony na stałą liczbę

# for i in range(5):
#     print(random())

# from random import choice, sample

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst = [ i for i in range(1,11)]

# print(choice(lst))
# print(sample(lst, 5))
# print(sample(lst, 10))
# print(sample(lst, 11)) # błąd nie można wylosowac bez powtórzeń z 10 el zbioru 11 el.

## Moduł platform

# import platform

#  help(platform)

# print(platform.machine())
# print(platform.processor())
# print(platform.system())
# print(platform.version())
# print(platform.python_implementation())
# print(platform.python_version_tuple())

# from platform import machine, version

# help(machine)
# print(machine())

# help(version())
# print(version())

# from platform import platform

# help(platform) # bez nawiasów infomacje o tym
# print(platform())

