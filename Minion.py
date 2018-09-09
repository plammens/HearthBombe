"""
"""

import copy

import Card
import Player


class Minion(Card.Card):
    def __init__(self, mana_cost: int, attack: int, health: int):
        super(Minion, self).__init__(mana_cost)

        self._attack = {'base': attack, 'current': attack}
        self._health = {'base': health, 'current': health}

        self._controller = None

        self.spells_cast_upon = []
        self.static_effect = None
        self.triggered_effect = None

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

        self._attack['current'] = max(val, 0)

    @property
    def health(self):
        return self._health['current']

    @health.setter
    def health(self, val):
        if type(val) is not int:
            raise TypeError

        self._health['current'] = min(val, self._health['base'])

        if self._health['current'] <= 0:
            self.destroy()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, val):
        if not (val is None or type(val) is Player.Player):
            raise TypeError

        self._controller = val

    """Methods"""

    def summon(self, controller):
        controller.battlefield.append(self)

    def play(self, **kwargs):
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
