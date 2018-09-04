from Minion import Minion
from Player import Player
from Spell import Spell


class Holy_Smite(Spell):
    def __init__(self):
        super().__init__(0, Minion, Player)

    def play(self, **kwargs):
        target = kwargs.get('target', None)

        def action():
            target.health -= 2

        super().play(action=action)
