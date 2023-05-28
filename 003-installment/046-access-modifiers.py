class Employee:
    def __init__(self):
        self.name = "Jugal" # Public variable
        self.__id = "1001" # Private variable

e = Employee()
print(e.name)
# print(e.__id) # Private variable cannot be accessed directly
print(e._Employee__id) # But can be accessed this way
# The above methon is called 'Name Mangling'
print(e.__dir__())