from Card import Card
from Game import Game, main_game


class Spell(Card):
    def __init__(self, mana: int, **kwargs):
        super(Spell, self).__init__(mana)
        self.target = kwargs.get('target', None)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, val):
        if val in Game.target_types:
            self._target = val
        else:
            self._target = None

    def play(self):
        super().__init__(self)
        main_game.run_spell_effects()
