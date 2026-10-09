a = 426

def fun():
    global a #it change the real/global value of the a
    a = 5
    print(a)

fun()
print(a)