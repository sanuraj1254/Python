class Employee():
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and The company is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language {self.language}")

class programmer(Employee , coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in {self.language}")

a = Employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage() 

print(a.company,b.company)
