class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

e1 = Employee("A")
e2 = Employee("B")
print(Employee.get_count())
