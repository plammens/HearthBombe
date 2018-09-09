"""
TODO: typecheck player
"""


class StaticEffect:
    def __init__(self, **kwargs):
        self.controller = None
        self.mana_bias = kwargs.get('mana_bias', 0)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def activate(self):
        if self.mana_bias != 0:
            self.controller.hand.mana_bias += self.mana_bias

    def deactivate(self):
        if self.mana_bias != 0:
            self.controller.hand.mana_bias -= self.mana_bias
