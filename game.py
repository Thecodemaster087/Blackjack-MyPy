import math
import random


class Gen:
    @staticmethod
    def deck(decks):
        base_deck = ([2, 3, 4, 5, 6, 7, 8, 9] * 4 + [10] * 16 + ["A"] * 4) * decks
        random.shuffle(base_deck)
        return base_deck

    @staticmethod
    def player(player, game_state):
        game_state[player] = []
        card = game_state["deck"].pop()
        game_state[player].append(card)
        card = game_state["deck"].pop()
        game_state[player].append(card)


def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card == "A":
            aces += 1
            score += 11
        else:
            score += card
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def hit(player, game_state):
    game_state[player].append(game_state["deck"].pop())

def stand(player, game_state):
    game_state["stood"][player] = 1


player_count = int(input("How many players: "))

decks = math.ceil((player_count + 1) * 1.25)
base_deck = Gen.deck(decks)

game_state = {
    "deck": base_deck,
    "stood": []
    }

for player in range(0, 1 + player_count):
    Gen.player(player, game_state)
    game_state["stood"].append(0)

print("A game has been created with:")
print(f" ╰╴{decks} decks")
print(f" ╰╴{player_count} players")
for player in range(0, 1 + player_count):
    print(f"    ╰╴{player} has {game_state[player]} {calculate_score(game_state[player])}")




