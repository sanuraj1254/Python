'''
1 = snake
-1 = water
0 = gun
'''
import random
Computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1 : "snake", -1 : "water", 0 :"gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]} \n Computer Choose {reverseDict[Computer]}")

if (Computer == you):
    print("Its Draw:")

else:
    if(Computer == -1 and you == 1):
        print("You Win:")
    elif(Computer == -1 and you == 0):
        print("You Lose:")
    elif(Computer == 1 and you == -1):
        print("You Lose:")    
    elif(Computer == 1 and you == 0):
        print("You Win:")
    elif(Computer == 0 and you == -1):
        print("You Win:")        
    elif(Computer == 0 and you == 1):
        print("You Lose:")
    else:
        print("Something went wrong!")