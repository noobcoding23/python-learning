class Person: # Defining a class called Person # Classes should be started with caps
    name = "Jugal"
    occupation = "Game Developer"
    networth = "1B"
    def info(self): # Here self is the keyword to represent the object which the method is being called 
        print(f"{self.name} is a {self.occupation} who's worth is {self.networth}")

# Usses of the class
a = Person() # Here a is the object
b = Person() # Here b is the object
c = Person() # Here c is the object

a.name = "Himangku" # Changing the default value to Himangku
a.occupation = "Clerk"
a.networth = "10L"

b.name = "Pritam"
b.occupation = "Teacher"
b.networth = "7.5L"

a.info()
b.info()
c.info() # c is going with the default values of the class