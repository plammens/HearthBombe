import random

from Minion import Minion
from Game import main_game


class Shadowbeast(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)


class Possessed_Villager(Minion):
    def __init__(self):
        super().__init__(1, 1, 1)

    def deathrattle(self):
        Shadowbeast().summon()


class Gelbins_Coil(Minion):
    def __init__(self):
        super().__init__(1, 1, 2)

        def play_spell_effect():
            random.choice(main_game.player2.battlefield).damage(1)

        main_game.play_spell_effects.append()
