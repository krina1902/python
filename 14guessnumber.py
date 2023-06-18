import random

num = random.randint(1,30)

while True:
    guess = int(input("guess number between 1 to 30:"))

    if guess==num:
        print("you choose correct number")
        break
    elif guess>num:
        print("you choose greater number")
    elif guess<num:
        print("you choose smaller number")
