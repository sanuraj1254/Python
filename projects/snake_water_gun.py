'''
1 = snake
-1 = water
0 = gun
'''
import random

print("Welcome to Snake, Water, Gun Game!")

choices = ["snake", "water", "gun"]

user_score = 0
computer_score = 0

while True:
    user = input("\nChoose snake, water or gun (q to quit): ").lower().strip()

    if user == "q":
        break

    if user not in choices:
        print("Please choose snake, water or gun.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        print("You won this round!")
        user_score += 1

    else:
        print("Computer won this round!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

    again = input("\nWant to play again? (yes/no): ").lower().strip()

    if again != "yes":
        break

print("\nFinal Score")
print("Your score:", user_score)
print("Computer score:", computer_score)

if user_score > computer_score:
    print("You won the game! Well played!")
elif computer_score > user_score:
    print("Computer won this time. Try again!")
else:
    print("The game ended in a tie!")

print("Thanks for playing!")
