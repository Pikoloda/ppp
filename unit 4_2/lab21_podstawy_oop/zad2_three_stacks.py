from stack_oop import Stack


# class Stack:  # definiujemy klasę stosu
#     def __init__(self):  # definiujemt konstruktor
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def show_all_element(self):
#         print(self.__stack_list)


s1 = Stack()
s2 = Stack()
s3 = Stack()

print(s1, s2, s3)

for i in range(1,101):
    s1.push(i)

s1.show_all_element()

for i in range(100):
    s2.push(s1.pop())

s2.show_all_element()

for i in range(100):
    s3.push(s2.pop())

s3.show_all_element()

for i in range(100):
    print(s3.pop(), end=" ")

