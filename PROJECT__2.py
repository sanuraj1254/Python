import random
n = random.randint(1 , 100)
a =-1
gusess = 0
while (a!=n):
    gusess +=1
    a = int(input("Guess the number: "))
    if (a > n):
        print("Lower no please")

    else:
        print("Higher no please")

print(f"You gussed the correct no in {gusess} gusess")