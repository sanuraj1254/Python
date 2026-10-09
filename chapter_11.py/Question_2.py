class Animal:
    pass

class pet(Animal):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("bow bow")

D = dog()
D.bark()