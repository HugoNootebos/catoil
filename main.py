
import matplotlib.pyplot as plt

class Player:
    def __init__(self, name, wood=0, stone=0, wheat=0, wool=0, ore=0, rent=0, tax=0):
        self.name = name
        self.prices = {
            'wood': wood,
            'stone': stone,
            'wheat': wheat,
            'wool': wool,
            'ore': ore,
            'rent': rent,
            'tax': tax
        }
        self.cash = None

turn = ()

def start():
    while True:
        try:
            player_num = int(input("How many players? "))
            break
        except TypeError:
            pass
    players = [Player(input(" Player " + str(i+1) + "'s name: ")) for i in range(player_num)]
    for player in players:
        player.cash = {other.name + "Coin": 0 for other in players if other.name != player.name}
    seven(players)


def seven(players):
    turn += 1
    for player in players:
        print(player.name + ": ")
        for tag in player.prices:
            player.prices[tag] = input('How much does {} cost? '.format(tag))

def show():
    for player in players:
        plt.plot(turn)

if __name__ == 'main':
    start()
