class Person:

    # def __init__(self): # This is a default constructer which is accepting only a self argument
    #     print("Hello World!")

    # This is parameterized constructer which is accecpting multiple arguments other than 'self'
    def __init__(self, n, o): # self is for the object
        print("Hey three!")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

# a = Person() # This will also print the line in the function
# This line will now thro error cause the now there are arguments in the __init__ function
a = Person("Jugal", "Game Developer") # This will always show the print line and will change the values in info() function
a.info()

# a = Person(1, 2, 3) This will throw error cause there is one more additional argument wchich isn't needed