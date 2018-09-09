"""
"""

from copy import deepcopy

from Player import *


class Game:
    def __init__(self):
        self.player = Player()
        self.opponent = Player()

    @property
    def minion_count(self):
        return len(self.player.battlefield) + len(self.opponent.battlefield)

    @property
    def characters(self):
        return self.player.battlefield + self.opponent.battlefield + [self.player, self.opponent]


main_game = Game()


class GameStatus:
    count = 0

    def __init__(self, game: Game, steps: list = None):
        if game is None:
            game = main_game
        self.game = deepcopy(game)

        if steps is None:
            steps = []
        self.steps = steps.copy()

        GameStatus.count += 1
