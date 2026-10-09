class Employee:
    def __init__(self):
        print("constructor of employee")
    a=1

class programmer(Employee):
    def __init__(self):
        print("constructor of programmer")
    b=2
 
class Manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3
o = Manager()
print(o.a, o.b, o.c)

