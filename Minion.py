from Game import Game
from Card import Card


class Minion(Card):
    def __init__(self, mana, attack, health, **kwargs):
        super(Minion, self).__init__(mana)

        self.attack = attack
        self.health = health

    def summon(self):
        Game.player_battlefield.append(self)

    def __del__(self):
        Game.player_battlefield.remove(self)

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, val):
        if type(val) is not int or val < 0:
            raise ValueError

        self._attack = val

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if type(val) is not int:
            raise TypeError

        self._health = val

        if self.health <= 0:
            del self


    """Special abilities: """

    def deathrattle(self):
        pass
