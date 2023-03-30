# Zad3.
# Rozbuduj klasę Stack o następujące metody:
# • empty() - powinna zwracać True jeżeli stos jest pusty, w przeciwnym wypadku zwracać False,
# • size() - powinna zwracać rozmiar stosu,
# • top() - powinna zwracać "górny" element stosu, czyli ten, który zostanie "ściągnięty"
# metodą pop().

class Stack:  # definiujemy klasę stosu
    def __init__(self):  # definiujemy konstruktor
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def show_all_element(self):
        print(self.__stack_list)

    def empty(self):
        return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)

    def top(self):
        if not self.empty():
            return self.__stack_list[-1]
        return None



# Test

stack = Stack()

print("Czy stos jest pusty?", stack.empty())

stack.push("Ala")
stack.push("Tomek")
stack.push("Agata")

print("\nCzy stos jest pusty?", stack.empty())
print("\nIle elementów jest na stosie?", stack.size())
print("\nNa samej górze stosu znajduje się: ",stack.top())
print("\nIle elementów jest na stosie?", stack.size())



