class Employee:
    language = "Python" #class attribute 
    salary = 1200000


Sanu = Employee()
Sanu.name = "Sanu Raj"# instance attribute 
print(Sanu.name,Sanu.language,Sanu.salary)

piyush = Employee()
piyush.name = "Piyush Anna"
print(piyush.name,piyush.language,piyush.salary)

satyam = Employee()
satyam.name = "Satyam"
print(satyam.name,satyam.language,satyam.salary)

'''here name is an object attribute and 
salary and language are class attribute'''