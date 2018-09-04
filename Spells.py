from copy import deepcopy

from Minion import Minion
from Player import Player
from Spell import Spell


class Holy_Smite(Spell):
    def __init__(self):
        super().__init__(0, Minion, Player)

    def play(self, **kwargs):
        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified for spell %s" % self)

        def action():
            target.health -= 2

        super().play(action=action, target=target)


class Vivid_Nightmare(Spell):
    def __init__(self):
        super().__init__(0, Minion)

    def play(self, **kwargs):
        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified for spell %s" % self)

        def action():
            copy = deepcopy(target)
            copy.health = 1
            copy.summon(self.player)

        super().play(action=action, target=target)
