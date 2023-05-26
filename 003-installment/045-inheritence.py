class Employee:

    def __init__(self, name, id):
        self.id = id
        self.name = name
    # @property
    def showEmplyeeDetails(self):
        print(f"The Employee number {self.id} is {self.name}")

# Here creating a new Class which will inherit the Employee Class
class Programmer(Employee):
    def showLanguagesKnown(self):
        print("The default language is python")

e1 = Employee("Nayan Jyoti Nath", 420)
e1.showEmplyeeDetails()

e2 = Programmer("JK", 1000)
e2.showEmplyeeDetails()

e2.showLanguagesKnown()