import math
import random


class Gen:
    @staticmethod
    def deck(decks):
        base_deck = ([2,3,4,5,6,7,8,9]*4+[10]*16+["A"]*4)*4
        random.shuffle(base_deck)
        return base_deck

    @staticmethod
    def player(player, game_state):
        game_state[player] = []
        card = game_state["deck"].pop()
        game_state[player].append(card)
        card = game_state["deck"].pop()
        game_state[player].append(card)
        print(f"    ╰╴{player} has {game_state[player]}")

player_count = int(input("How many players: "))

decks = math.ceil((player_count+1)*1.25)
base_deck = Gen.deck(decks)

game_state = {
    "deck": base_deck
}
print("A game has been created with:")
print(f" ╰╴{decks} decks")
print(f" ╰╴{player_count} players")

for player in range(0, 1+player_count):
    Gen.player(player, game_state)








