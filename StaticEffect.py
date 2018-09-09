"""
TODO: typecheck player
"""


class StaticEffect:
    def __init__(self, **kwargs):
        self.controller = None

        mana_bias = kwargs.get('mana_bias', {})
        assert type(mana_bias) is dict

        self.mana_bias = {
            'any': mana_bias.get('any', 0),
            'spells': mana_bias.get('spells', 0),
            'minions': mana_bias.get('minions', 0)
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def activate(self):
        if self.mana_bias['any'] != 0:
            self.controller.hand.mana_bias_any += self.mana_bias['any']
        if self.mana_bias['spells'] != 0:
            self.controller.hand.mana_bias_spells += self.mana_bias['spells']
        if self.mana_bias['minions'] != 0:
            self.controller.hand.mana_bias_minions += self.mana_bias['minions']

    def deactivate(self):
        if self.mana_bias['any'] != 0:
            self.controller.hand.mana_bias_any -= self.mana_bias['any']
        if self.mana_bias['spells'] != 0:
            self.controller.hand.mana_bias_spells -= self.mana_bias['spells']
        if self.mana_bias['minions'] != 0:
            self.controller.hand.mana_bias_minions -= self.mana_bias['minions']
