# import pygame
import guessing
import blackjack

def main():
    print("Welcome to minigame!")
    running = True
    while running:
        game = input("What game would you like to play:\n")
        if game.lower() == "guessing":
            guessing.guessing()
        elif game == "/bye":
            print("Goodbye! Hope you had fun")
            running = False
        elif game == "blackjack":
            blackjack.blackjack()




if __name__ == "__main__":
    main()
