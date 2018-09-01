from Game import Game
from Card import Card


class Minion(Card):
    def __init__(self, mana, attack, defense):
        super(Minion, self).__init__(mana)

        self.attack = attack
        self.defense = defense

        Game.player_battlefield.append(self)

    def __del__(self):
        Game.player_battlefield.remove(self)
