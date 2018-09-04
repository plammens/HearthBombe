"""
TODO: summmoning deathrattle as 'player', or 'controller'?
"""


from Card import Card
from Player import Player


class Minion(Card):
    def __init__(self, mana, attack, health):
        super(Minion, self).__init__(mana)

        self.attack = attack
        self.health = health

        self.controller = None

        self.spells_cast_upon = []

    def destroy(self):
        self.controller.battlefield.remove(self)
        self.deathrattle()

    """Properties: attack, health, controller"""

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, val):
        if type(val) is not int or val < 0:
            raise ValueError

        if not hasattr(self, '_attack'):
            self._attack = {'base': val, 'current': val}

        self._attack['current'] = val

    @property
    def health(self):
        return self._health['current']

    @health.setter
    def health(self, val):
        if type(val) is not int:
            raise TypeError

        if not hasattr(self, '_health'):
            self._health = {'base': val, 'current': val}

        self._health['current'] = val

        if self._health['current'] <= 0:
            self.destroy()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, val):
        if not (val is None or type(val) is Player):
            raise TypeError
        self._controller = val

    """Methods"""

    def summon(self, controller):
        controller.battlefield.append(self)

    def play(self):
        super().play()
        self.battlecry()
        self.summon(self.player)

    def damage(self, dmg: int):
        self.health -= dmg

    """Special abilities: """

    def battlecry(self):
        pass

    def deathrattle(self):
        pass
