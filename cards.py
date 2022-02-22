import random
suits = ["clubs", "spades", "hearts", "diamonds"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def cards():
    card_list = []
    for s in suits:
        for n in numbers:
            card_list.append(n + " of " + s)
    return card_list

my_cards = cards()
hand = []

for a in range(6):
    card = random.choice(my_cards)
    hand.append(card)

print(f"You have in your hand the: {hand}!")