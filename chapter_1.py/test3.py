a = int(input("enter the first num:"))
b = int(input("enter the secoend num:"))
c = int(input("enter the third num:"))

if a >= b and a >= c:
    print("A is greater ")
elif b >= a and b >= c:
    print("B is greater ")
else:
    print("C is greater ")