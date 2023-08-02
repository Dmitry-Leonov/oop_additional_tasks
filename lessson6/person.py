"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- __slots__ = ('name', 'age'): список атрибутов, доступных объекту.

Напишите класс Employee, наследующийся от класса Person, представляющий сотрудника, имеющий следующие атрибуты:

- __slots__ = ('salary',): список атрибутов, доступных объекту.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие атрибуты:

- __slots__ = ('bonus',): список атрибутов, доступных объекту.
"""


class Person:
    __slots__ = ('name', 'age')

    # def __init__(self):
    #     self.name = self.name
    #     self.age = self.age


class Employee(Person):
    __slots__ = ('salary',)

    # def __init__(self, name, age, salary):
    #     super().__init__(name, age)
    #     self.salary = salary


class Manager(Employee):
    __slots__ = ('bonus',)

    # def __init__(self, name, age, salary, bonus):
    #     super().__init__(name, age, salary)
    #     self.bonus = bonus


person = Person()
person.name = "John"
person.age = 30
person.salary = 5000  # raises AttributeError

employee = Employee()
employee.name = "Jane"
employee.age = 25
employee.salary = 5000

manager = Manager()
manager.name = "Bob"
manager.age = 40
manager.salary = 10000
manager.bonus = 5000
