class Employee:
    a=1

class programmer(Employee):
    b=2
 
class Manager(programmer):
    c=3
o = Employee
print(o.a)

o = programmer
print(o.a,o.b)

o = Manager
print(o.a , o.b , o.c)