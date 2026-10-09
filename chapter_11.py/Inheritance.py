class Employee():
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and The salary is {self.salary}")

class programmer(Employee):
    company = "ITC Infotech"
    def language(self):
        print(f"The language is {self.language}")

a = Employee
b = programmer  

print(a.company,b.company)
