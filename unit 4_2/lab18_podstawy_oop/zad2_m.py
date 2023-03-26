# Zad2.
# Korzystając z napisanej wcześniej klasy Stack:
# • utwórz 3 stosy (3 obiekty klasy Stack),
# • połóż na pierwszym stosie kolejno liczby od 1 do 100,
# • ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
# • ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
# • ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.

class Stack: # definiujemy klasę stosu
    def __init__(self): # definiujemt konstruktor
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val



obj1 = Stack()
obj2 = Stack()
obj3 = Stack()

obj = [i for i  in range(1,101)]




# class StackSum(Stack): # dziedziczenie w nawiasach po tej klasie wszystkich właśiwości
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self,val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

