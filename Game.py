# from Minion import Minion
from Utils import Callable_List


class Player:
    def __init__(self):
        self.hand = []
        self.battlefield = []
        self.health = 30


class Game:
    target_types = ("Minion", "Player")

    def __init__(self):
        self.player = Player()
        self.opponent = Player()

        self._play_spell_effects = Callable_List()

    def minion_count(self):
        return len(self.player.battlefield) + len(self.opponent.battlefield)

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
