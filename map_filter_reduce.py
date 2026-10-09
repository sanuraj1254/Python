from functools import reduce
# Map example
l = [1,2,3,4,5,6,7]

square = lambda x: x*x 

sqlist = map(square , l)
print(list(sqlist))

# Filter example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyeven = filter(even , l)
print(list(onlyeven))

# Reduce example
def sum(a,b):
    return a+b

mul  = lambda x,y:x*y
print(reduce(mul,l))

print(reduce(sum,l))