class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary =salary

    @classmethod
    def fromString(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])

e1 = Employee('Harry', 1000)
print(e1.name)
print(e1.salary)

string = 'Jugal-12000'
e2 = Employee.fromString(string)
print(e2.name)
print(e2.salary)