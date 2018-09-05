"""
TODO: typecheck player
"""


class StaticEffect:
    def __init__(self, **kwargs):
        self.player = None
        self.mana_bias = kwargs.get('mana_bias', 0)

    def activate(self):
        if self.mana_bias != 0:
            self.player.hand.mana_bias += self.mana_bias

    def deactivate(self):
        if self.mana_bias != 0:
            self.player.hand.mana_bias -= self.mana_bias
