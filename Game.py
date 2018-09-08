"""
"""

from copy import deepcopy

from Minion import Minion
from Player import *
from utils import Callable_List


class Game:
    target_types = {Minion, Player}

    def __init__(self):
        self.player = Player()
        self.opponent = Player()

        self._play_spell_effects = Callable_List()

    @property
    def minion_count(self):
        return len(self.player.battlefield) + len(self.opponent.battlefield)

    @property
    def characters(self):
        return self.player.battlefield + self.opponent.battlefield + [self.player, self.opponent]

    @property
    def play_spell_effects(self):
        return self._play_spell_effects

    @play_spell_effects.setter
    def play_spell_effects(self, val):
        raise NotImplemented

    def run_spell_effects(self):
        for effect in self.play_spell_effects:
            effect()


main_game = Game()


class GameStatus:
    def __init__(self, game: Game = None):
        if game is None:
            game = deepcopy(main_game)
        self.game = game
        self.inspected = False
        self.steps = []
