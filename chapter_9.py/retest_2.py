import random

def game():
    print("You are playing the game....")
    score = random.randint(1 , 99)
    with open("highscore.txt") as f:
        highscore = f.read()
        if highscore != "":
          highscore = int(highscore)
        else:
          highscore = 0
    print(f"Your score:{score}")
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

    return score
game()                