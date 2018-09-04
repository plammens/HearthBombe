import random

from Game import main_game
from Minion import Minion


class Shadowbeast(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)


class Possessed_Villager(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)

    def deathrattle(self):
        Shadowbeast().summon(self.controller)


class Gelbin_Coil(Minion):
    def __init__(self):
        super().__init__(1, 1, 2)

        def play_spell_effect():
            """Deal 1 damage to a random enemy minion"""
            random.choice(main_game.opponent.battlefield).damage(1)

        main_game.play_spell_effects.append(play_spell_effect)
