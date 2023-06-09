class ParentClass:
    def parent_method(self):
        print("This is a parent method.")
    
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")

        super().parent_method() # Using a parent class method by using super keyword
    
child_object = ChildClass()
child_object.child_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee): # inheriting Employee in Programmers class
    # def __init__(self, name, id, lang): #DRY - Making it dry
    #     self.name = name #DRY
    #     self.id = id #DRY
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

jugal = Employee("Jugal", "10")
harry = Programmer("Harry", "12", "Python")

print(jugal.name)
print(harry.name)
print(harry.id)
print(harry.lang)