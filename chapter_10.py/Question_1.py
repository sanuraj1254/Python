class programmer:
    company = "Microsoft"
    def __init__(self, name , salary , pin_code):
        self.name = name
        self.salary = salary
        self.pin_code = pin_code

s = programmer("Sanu", 1200000, 813206)
print(s.name,s.salary,s.pin_code,s.company)

p = programmer("Piyush", 1200000, 813206)
print(p.name,p.salary,p.pin_code,p.company)

sa = programmer("Satyam", 1200000, 813206)
print(sa.name,sa.salary,sa.pin_code,sa.company)