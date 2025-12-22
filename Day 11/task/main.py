import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
pc_cards = []

def deal_hand(my_cards, pc_cards):
    print(f"Your cards: {my_cards}. current score: {sum(my_cards)}")
    print(f"Computer's first card: {pc_cards}")

play_blackjack = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if play_blackjack == "y":
    my_cards.append(random.choice(cards))
    my_cards.append(random.choice(cards))
    pc_cards.append(random.choice(cards))
    print("\n" * 20)
    print(logo)
    deal_hand(my_cards, pc_cards)
else:
    exit()

want_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

while want_another_card == "y":
    print("\n" * 20)
    print(logo)
    my_cards.append(random.choice(cards))
    deal_hand(my_cards, pc_cards)
    if sum(my_cards) < 22:
        want_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if sum(my_cards) >= 22:
        print("You went over 21, you lose foo")
        exit()

if want_another_card == "n":
    print(f"Your final hand: {my_cards}, total {sum(my_cards)}")
    while sum(pc_cards) < 17 :
        pc_cards.append(random.choice(cards))
    if sum(pc_cards) >= 22:
        print(f"Computer's final hand: {pc_cards}, Total: {sum(pc_cards)}")
        print("Opponent went over. You win")
        exit()
    print(f"Computer's final hand: {pc_cards}, Total: {sum(pc_cards)}")
    if sum(pc_cards) == sum(my_cards):
        print("It's a draw")
    elif sum(pc_cards) > sum(my_cards):
        print("Opponent wins")
    else:
        print("You Win")