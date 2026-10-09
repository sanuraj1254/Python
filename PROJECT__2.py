import random

n = random.randint(1, 100)
a = 0
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")

while a != n:
    a = int(input("Enter your guess: "))
    attempts += 1

    if a > n:
        print("Lower number please!")
    elif a < n:
        print("Higher number please!")
    else:
        print("Congratulations! You guessed the correct number.")
        print("The correct number was:", n)
        print("Total attempts:", attempts)
