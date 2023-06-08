x = [1, 2, 3]
# print(dir(x)) # Prints all the methods that can be used in the object
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__) # This method changes the object into dictionary

print(help(str)) # This method explains everything