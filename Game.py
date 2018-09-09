"""
"""

from copy import deepcopy

from Player import *
from utils import Callable_List


class Game:
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
    def __init__(self, game: Game, steps: list = None):
        if game is None:
            game = main_game
        self.game = deepcopy(game)

        if steps is None:
            steps = []
        self.steps = steps
