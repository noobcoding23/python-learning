class Employee:

    company = 'Apple'
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod # Using class method we can change the class
    def changeCompany(cls, newCompany): # Here cls represents class
        cls.company = newCompany
    

e1 = Employee()
e1.name = 'Jugal'
e1.show()

e1.changeCompany('Tesla') # Changing company name with changeCompany method
print(e1.company)
e1.show()