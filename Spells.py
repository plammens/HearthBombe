from Minion import Minion
from Player import Player
from Spell import Spell


class HolySmite(Spell):
    def __init__(self):
        super().__init__(1, target_types={Minion, Player})

    def play(self, **kwargs):
        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified for spell %s" % self)

        def action():
            target.health -= 2

        super().play(action=action, target=target)


class VividNightmare(Spell):
    def __init__(self):
        super().__init__(3, target_types={Minion})

    def play(self, **kwargs):
        try:
            minion = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified for spell %s" % self)

        def action():
            copy_ = minion.copy()
            copy_.health = 1
            copy_.summon(self.player)

        super().play(action=action, target=minion)

    def is_valid_target(self, target):
        return super().is_valid_target(target) and target.controller is self.player


class ShadowWordPain(Spell):
    def __init__(self):
        super().__init__(2, target_types={Minion})

    def is_valid_target(self, target):
        return super().is_valid_target(target) and target.attack <= 3

    def play(self, **kwargs):
        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified for spell %s" % self)

        def action():
            target.destroy()

        super().play(action=action, target=target)
