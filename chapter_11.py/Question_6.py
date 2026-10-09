class Vector:
    def __init__(self , x , y , k):
        self.x = x
        self.y = y
        self.k = k
    
    def __add__(self , m):
        return Vector(self.x + m.x , self.y + m.y , self.k + m.k)
    
    def __mul__(self, m):
        return self.x * m.x + self.y * m.y + self.k * m.k
        return result

    def __str__(self):
        return f"({self.x}i + {self.y}j + {self.k}k)"

x = Vector(1, 2 , 3)
y = Vector(4 , 5, 6)
k = Vector(7 , 8 , 9)

print(x + y)
print(x * y)

