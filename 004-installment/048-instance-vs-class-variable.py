class Employee:

    companyName = "Apple" # This is class variable
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name # This is instance variable
        self.raise_amount = 0.02 # This is instance variable
        # Here in below you have to put the class name before class variable to perfectly count the number of employees or to increament everytime when the class is used
        Employee.noOfEmployee += 1 # This will increment one everytime when the class is used

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and raise amount in {self.companyName} is {self.raise_amount}")


emp1 = Employee("Jugal")
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.companyName = "Google" # This will change the class variable # And now this is an instance variable
print(Employee.companyName) # This will simply print the class variable
print(emp2.companyName) # This will simply print instance variable value
emp2.raise_amount = 0.3
emp2.showDetails()

Employee.companyName = "SpaceX" # From this point on the class variable value is being changed
emp3 = Employee("Harry")
emp3.showDetails()

print(Employee.noOfEmployee)