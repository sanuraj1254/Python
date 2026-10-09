class TwoDVector:
    def __init__(self , i , j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")    

class ThreeDVector(TwoDVector):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.k= k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j +{self.k}k")

a = TwoDVector(37 , 63)
a.show()

b = ThreeDVector(57,64,63)
b.show()