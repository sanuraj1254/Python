import random

print("Welcome to Snake, Water, Gun Game!")
print("1 = Snake | 0 = Water | 2 = Gun")
print("Type q to quit and see your final report.")

choices = {
    "1": "Snake",
    "0": "Water",
    "2": "Gun"
}

played = 0
wins = 0
losses = 0
ties = 0

while True:
    user = input("\nChoose 1, 0, 2 or q: ").strip().lower()

    if user == "q":
        break

    if user not in choices:
        print("Invalid choice! Enter 1, 0, 2 or q.")
        continue

    computer = random.choice(list(choices.keys()))

    print("You:", choices[user], "| Computer:", choices[computer])

    played += 1

    if user == computer:
        print("Round result: Tie!")
        ties += 1

    elif (
        (user == "1" and computer == "0")
        or (user == "0" and computer == "2")
        or (user == "2" and computer == "1")
    ):
        print("Round result: You won!")
        wins += 1

    else:
        print("Round result: You lost!")
        losses += 1

print("\n========== FINAL REPORT ==========")
print("Total games played:", played)
print("Games won:", wins)
print("Games lost:", losses)
print("Ties:", ties)

win_rate = played - ties
if win_rate > 0:
    win_percentage = (wins / played) * 100
    print(f"Win percentage: {win_percentage:.2f}%")
else:
    print("Win percentage: 0.00%")
print("Thanks for playing
