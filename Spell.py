from Card import Card
from Game import Game


class Spell(Card):
    def __init__(self, mana, **kwargs):
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
