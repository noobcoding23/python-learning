class MyClass:
    def __init__(self, value):
        self._value = value
        # print("This is a test")

    def show(self):
        print(f"Value is {self._value}")

    @property
    def tenX_value(self):
        return self._value*10

    @tenX_value.setter
    def tenX_value(self, new_value):
        self._value = new_value/10
    
obj = MyClass(10)
obj.tenX_value = 64
obj.show()
print(obj.tenX_value) # it returns 10x value

print()
print()

class Termpreture:
    def __init__(self, temp):
        self._temp = temp

    def showTemp(self):
        print(f"The tempretur is {self._temp}")

    @property # This here is for getter
    def celsiousToF(self):
        return self._temp*9/5 + 32
    
    @celsiousToF.setter # This here is for setter # The .setter part is important for syntax
    def celsiousToF(self, newTemp):
        self._temp = newTemp

obj1 = Termpreture(48) # this value will be replaced by the value under below
obj1._temp = 10
obj1.showTemp()
obj1.celsiousToF = 37 # This will throw an error without any setters
obj1.showTemp()
print(obj1.celsiousToF)