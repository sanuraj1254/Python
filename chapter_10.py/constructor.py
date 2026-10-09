class Employee:
    language = "Python" #class attribute 
    salary = 1200000

    def __init__(self):#dunder methord which is automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}") 


Sanu = Employee()
Sanu.salary = "12000000"# instance attribute 
print(Sanu.language,Sanu.salary)

Sanu.getInfo()
Employee.getInfo(Sanu)#line 14 and 15 are same      
