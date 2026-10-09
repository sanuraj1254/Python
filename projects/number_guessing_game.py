import random

n = random.randint(1, 100)
a = 0
attempts = 0

print("Welcome to my Number Guessing Game!")
print("I have picked a number between 1 and 100.")
print("Let's see how many tries you need.")
print("Type 'q' if you want to quit.")

while True:
    guess = input("\nEnter your guess: ")

    if guess.lower() == "q":
        print("You left the game. The number was", n)
        break

    try:
        a = int(guess)
    except ValueError:
        print("Please enter a number, not text.")
        continue

    if a < 1 or a > 100:
        print("Please choose a number between 1 and 100.")
        continue

    attempts += 1

    if a > n:
        print("Oops! Try a smaller number.")
    elif a < n:
        print("Too low! Try a bigger number.")
    else:
        print("You got it! Congratulations!")
        print("The number was:", n)
        print("You guessed it in", attempts, "attempts.")

        if attempts <= 5:
            print("Amazing! You got it really quickly!")
        elif attempts <= 10:
            print("Good job!")
        else:
            print("Nice try! Keep practising.")

        break

print("Thanks for playing!")
