class Student:
    # Class Attribute (common for all objects)
    college_name = "ABC College"

    def __init__(self, name, roll):
        # Object Attributes (unique for each object)
        self.name = name
        self.roll = roll

# Create objects
s1 = Student("Sanu", 101)
s2 = Student("Aman", 102)

# Accessing class and object attributes
print("S1 ->", s1.name, s1.roll, s1.college_name)
print("S2 ->", s2.name, s2.roll, s2.college_name)

# Changing class attribute
Student.college_name = "XYZ University"

print("\nAfter changing class attribute:")
print("S1 ->", s1.name, s1.roll, s1.college_name)
print("S2 ->", s2.name, s2.roll, s2.college_name)

# Changing object attribute
s1.name = "Rohit"

print("\nAfter changing object attribute:")
print("S1 ->", s1.name, s1.roll, s1.college_name)
print("S2 ->", s2.name, s2.roll, s2.college_name)
