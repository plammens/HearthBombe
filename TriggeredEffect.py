"""
TODO: common class for effects
"""


class TriggeredEffect:
    def __init__(self, effect):
        self.controller = None
        assert callable(effect)
        self.effect = effect

    def trigger(self):
        self.effect()
