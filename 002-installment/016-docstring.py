def squareOf(n):
    '''Accepts a number 'n' and returns square of the number''' # <-- This line which is before the definition of the function is doc string which is kind of like a string. So it is not ignored by python and can be accessed or print by using __doc__ attribute
    print(n**2)

squareOf(5)
print(squareOf.__doc__) # Prints the commented line inside the function