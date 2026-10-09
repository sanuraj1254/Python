n1 = int(input("Enter the number n1:"))
n2 = int(input("Enter the number n2:"))
n3 = int(input("Enter the number n3:"))
n4 = int(input("Enter the number n4:"))

if(n1>n2 and n1>n3 and n1>4):
    print("n1 is the greater number")
elif(n2>n1 and n2>n3 and n2>4):
    print("n2 is the greater number")
elif(n3>n1 and n3>n2 and n3>4):
    print("n3 is the greater number")
else:
    print("n4 is the greater number")
