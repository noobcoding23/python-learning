class Person:
    name = "Jugal"
    i = 0
    for c in name:
        i += 1
    
class PersonD: # This is class with dunder method
    name = "Jugal"
    def __len__(self): # This is a dunder method
        i = 0
        for c in self.name:
            i += 1
        return i

    
p1 = Person()
print(p1.name)
print(p1.i)

p2 = PersonD()
print(p2.name)
print(len(p2))

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    def __str__(self):
        return f"The name of the Employee is {self.name} str"
    
    def __repr__(self):
        return f"Employee('Harry')"
    
    def __call__(self): # Can make an object behave like a function or method
        print("Hey there this is an object")

e = Employee("Harry")
print(e.name)
print(e) # Prints repr part when ther is no str
print(str(e))
print(repr(e)) # Prints repr part
e() # By using call method the object 'e' turns into a callable function or method

class Programmer:
    def __init__(self, name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

    def __call__(self):
        print(f"The name of the employee is {self.name} id {self.id} and knows {self.lang}")

pr = Programmer("Jugal", "40", "Python")
pr()
