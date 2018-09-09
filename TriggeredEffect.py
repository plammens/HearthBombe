"""
TODO: common class for effects
"""


class TriggeredEffect:
    def __init__(self, effect):
        self.controller = None
        assert callable(effect)
        self.effect = effect

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def trigger(self):
        self.effect()
