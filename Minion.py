from Game import main_game
from Card import Card


class Minion(Card):
    def __init__(self, mana, attack, health):
        super(Minion, self).__init__(mana)

        self.attack = attack
        self.health = health

    def destroy(self):
        self.deathrattle()
        if self in main_game.player.battlefield:
            main_game.player.battlefield.remove(self)

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
            self.destroy()

    def summon(self):
        main_game.player.battlefield.append(self)

    def play(self):
        super().play()
        self.battlecry()
        self.summon()

    def damage(self, dmg: int):
        self.health -= dmg

    """Special abilities: """

    def battlecry(self):
        pass

    def deathrattle(self):
        pass
