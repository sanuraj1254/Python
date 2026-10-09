age = int(input("Enter your age :"))

if age < 13:
    print("You are child ")
elif age > 13 and age < 19:
    print("You are teenager ")
elif age > 13 and age > 19 and age < 59:
    print("You are adult ")
else:
    print("you are senior citizen")