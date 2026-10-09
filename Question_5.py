from functools import reduce
l = [65,65,69,41685,1984,9,853168,53]

def greatest(a , b):
    if (a>b):
        return a 
    return b  

print(reduce(greatest, l))