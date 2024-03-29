# Zad1.
# Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
# • dodaj metodę risesalary(),
# • metoda powinna zwiększać zarobki o podaną wartość procentową,
# • domyślnie metoda powinną zwiększać zarobkio 10%

class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_fullname(self):
        return self.__firstname + " " + self.__lastname

    def get_age(self):
        return self.__age

    def risesalary(self, percenrt=10):
        self.__salary *= percenrt / 100 + 1


def payroll(employees):
    print("Lista płac")
    print("-" * 50)
    for e in employees:
        print(e.get_fullname(), " wiek:", e.get_age(), "lat, pensja:", e.get_salary(), "zł")
    print()


employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("Natalia", "Nowak", 60, 15200))

print()

payroll((employees))
employees[0].risesalary()
employees[2].risesalary(30)
payroll(employees)
