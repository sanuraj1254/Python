try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as a:
    print(a)

else:
    print("I am in else")

finally:
    print("Finally i am in finally")