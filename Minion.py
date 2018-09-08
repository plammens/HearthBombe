"""
"""

import copy

from Card import Card
from Player import Player


class Minion(Card):
    def __init__(self, mana_cost, attack, health):
        super(Minion, self).__init__(mana_cost)

        self.attack = attack
        self.health = health

        self._controller = None

        self.spells_cast_upon = []
        self.static_effect = None

    def destroy(self):
        self.controller.battlefield.remove(self)
        self.deathrattle()

    """Properties: attack, health, controller"""

    @property
    def attack(self):
        return self._attack['current']

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

        if self.static_effect is not None:
            self.static_effect.controller = self._controller

    """Methods"""

    def summon(self, controller):
        controller.battlefield.append(self)

    def play(self):
        super().play()
        self.battlecry()
        self.summon(self.player)

    to_be_referenced = {'player', 'owner', '_controller'}

    def copy(self):
        copy_ = type(self)()

        for attr in self.__dict__:
            if attr not in Minion.to_be_referenced:
                # Make an actual copy of the attribute
                copy_.__dict__[attr] = copy.copy(self.__dict__[attr])
            else:
                # Copy reference
                copy_.__dict__[attr] = self.__dict__[attr]

        return copy_

    def damage(self, dmg: int):
        self.health -= dmg

    """Special abilities: """

    def battlecry(self):
        pass

    def deathrattle(self):
        pass
