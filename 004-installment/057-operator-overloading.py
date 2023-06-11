class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self): # Used to define what to print when the only the object is used as a parameter
        # When defined a function it accepts parameters
        # And when a function is called it accepts an argument
        return f'{self.i}i + {self.j}j + {self.k}k'

    def __add__(self, x): # Here x represents the other object of the class (or the other instance of class) in which we are going to perform the addition or other specific operation
        # return f'{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k' # It returns type as string
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k) # Now it returns type as a vector
    
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(8, 7, 4)
print(v2)

v3 = v1 + v2
print(v3) # Retuns error when printed without operator overloading
print(type(v3)) # it return type as string normally but after vector constructer it returns as vector

# Operation Overloading used when you have to define in python what to do when an arithmatic operation is being perfored with two instances or object of the same class