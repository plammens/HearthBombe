"""
"""

import random

from Game import main_game
from Minion import Minion
from StaticEffect import StaticEffect
from TriggeredEffect import TriggeredEffect


class Shadowbeast(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)


class PossessedVillager(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)

    def deathrattle(self):
        Shadowbeast().summon(self.controller)


class GelbinCoil(Minion):
    def __init__(self):
        super().__init__(1, 1, 2)

        def triggered_effect():
            """Deal 1 damage to a random enemy minion"""
            opponent = main_game.opponent if self.controller is main_game.player else main_game.player
            if len(opponent.battlefield) > 0:
                random.choice(opponent.battlefield).damage(1)

        self.triggered_effect = TriggeredEffect(triggered_effect)


class TestSubject(Minion):
    def __init__(self):
        super(TestSubject, self).__init__(1, 0, 2)

    def deathrattle(self):
        super().deathrattle()
        self.controller.hand.extend(self.spells_cast_upon)


class RadiantElemental(Minion):
    def __init__(self):
        super().__init__(2, 2, 3)
        self.static_effect = StaticEffect(mana_bias={'spells': -1})
