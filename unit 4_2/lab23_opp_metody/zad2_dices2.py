# Zad2.
# Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
# zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).

import random


class Dice:

    def __init__(self):
        self.__value = None

    def throw(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return "[{}]".format(self.__value)  # "[" + self.value +"]"

    def get_value(self):
        return self.__value


## Testy
# dice = Dice()
# print(dice)

# dice.throw()
# print(dice)


class DicePair:

    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

    def is_double(self):
        return self.__pair[0].get_value() == self.__pair[1].get_value()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])


dices = DicePair()

while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break
