
def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [6584,645,530,654,543,134,641640,65]
f = list (filter(divisible5,a))
print(f)
