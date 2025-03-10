import random


def deal(arr):
    while True:
        color_id = random.randint(1,4)
        color = "NotSet"
        if color_id == 1:
            color = "Spade"
        elif color_id == 2:
            color = "Hearts"
        elif color_id == 3:
            color = "Diamonds"
        elif color_id == 4:
            color = "Clubs"

        card_id = random.randint(1,13)
        card_val = 0

        if card_id >= 11:
            card_val = 10
        else:
            card_val = card_id

        if (card_val, color) not in arr:
            arr.append((card_val, color))
            return (card_val, color)

def blackjack():
    cards = []
    player_1 = deal(cards)
    player_2 = deal(cards)
    player = [player_1, player_2]
    sum = 0

    dealer_1 = deal(cards)
    dealer_2 = deal(cards)
    dealer = [dealer_1, dealer_2]
    dealer_sum = 0

    print("Players cards:", player)
    print("Dealers cards:", dealer[0])

    player_turn = True
    while player_turn:
        if sum > 20:
            print(f"You lost with a sum of: {sum}, better luck next time!")
            return

        print("Your card sum:",sum )
        print("Would you like to hit or stand? [H/s]:")

        choice = input()
        if choice.lower() == "s":
            player_turn = False
        elif choice.lower() == "h":
            new_card = deal(cards)
            print("Your new card:", new_card)
            player.append(new_card)
            sum += new_card[0]

    dealer_turn = True
    while dealer_turn:
        print(dealer)

        if dealer_sum >= 17:
            dealer_turn = False
        elif dealer_sum >= 21:
            print("You win and dealer lost! Congratulations")
            return
        else:
            new_card = deal(cards)
            print(f"The dealer got: {new_card}")
            dealer.append(new_card)
            dealer_sum += new_card[0]

    if dealer_sum > sum:
        print("Dealer wins with a score of:", dealer_sum)
    elif dealer_sum < sum:
        print("Player wins with a score of:", sum)
    else:
        print("Its a tie, better luck next time!")
