class Stack: # definiujemy klasę stosu
    def __init__(self): # definiujemt konstruktor
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def show_all_element(self):
        print(self.__stack_list)


class StackSum(Stack): # dziedziczenie w nawiasach po tej klasie wszystkich właśiwości
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


# --------------------------------------------------



obj = StackSum()
obj2 = StackSum()
obj3 = StackSum()

print("Umieszczamy elementy na stosach!")

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())
print()

print("Ściągamy elemnty ze stosu!")

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())

print()


#
# print()
#
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# # obj.__stack_list = [4,4,4]
# print()
#
# print("stos 1", obj.get_sum())
# print("stos 2", obj2.get_sum())