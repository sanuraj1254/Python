class Employee:
    salary = 234
    increment = 20

    @property
    def Afterincrement(self):
        return (self.salary + self.salary * (self.increment /100 ))

e = Employee()
print(e.Afterincrement)