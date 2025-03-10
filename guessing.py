import random

def guessing():
    guessed = False
    target_num = random.randint(1,100)
    attempts = 0

    while not guessed and attempts < 5:
        x = input("Guess a number\n")
        if int(x) == target_num:
            print("You guessed it!")
            guessed = True
        elif int(x) < target_num:
            print("Too small")
            attempts +=1
        elif int(x) > target_num:
            print("Too big")
            attempts +=1

        if not attempts < 5:
            print(f"You lost, the number was: {target_num}")
