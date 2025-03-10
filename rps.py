import random

def play():
    print("Lets play Scissors, Paper, Stone!")
    comp_guess_id = random.randint(1,3)
    comp_guess = ""
    if comp_guess_id == 1:
        comp_guess = "Rock"
    elif comp_guess_id == 2:
        comp_guess = "Paper"
    elif comp_guess_id == 3:
        comp_guess = "Scissors"

    player_choice_char = input("What do you guess? [r,p,s]\n").lower()

    p_choice = ("",0)

    if player_choice_char == "r":
        p_choice = ("Rock", 1)
    elif player_choice_char == "p":
        p_choice = ("Paper", 2)
    elif player_choice_char == "s":
        p_choice = ("Stone", 3)

    if p_choice[1] == comp_guess_id:
        print("It's a tie!")
        return


    elif p_choice[1] == 3 or comp_guess_id == 3:

        if comp_guess_id > p_choice[1] :
            print("You win and the computer loses!")
            print(f"{p_choice[0]} defeats {comp_guess}")
            return

        else:
            print("Aww, you lost, try again next time!")
            return

    elif p_choice[1] > comp_guess_id:
        print("Player wins!")
        print(f"{p_choice[0]} defeats {comp_guess}")
        return

    elif p_choice[1] < comp_guess_id:
        print("Aww, you lost, try again next time!")
        return
