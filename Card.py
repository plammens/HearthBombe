class Card:
    def __init__(self, mana_cost: int):
        self.mana_cost = mana_cost
        self.player = None
        self.owner = None

    eq_ignore = [
        'player', 'owner', '_controller', 'controller'
                 ]

    def __eq__(self, other):
        dict1 = self.__dict__.copy()
        dict2 = other.__dict__.copy()

        for attr in Card.eq_ignore:
            dict1.pop(attr, None)
            dict2.pop(attr, None)

        return dict1 == dict2

    @property
    def mana_cost(self):
        mana = self._mana_cost['current']
        return mana if mana > 0 else 0

    @mana_cost.setter
    def mana_cost(self, val: int):
        if type(val) is not int:
            raise TypeError

        if not hasattr(self, '_mana_cost'):
            self._mana_cost = {'base': val, 'current': val}

        self._mana_cost['current'] = val

    def play(self, **kwargs):
        assert self.mana_cost <= self.player.mana, "Not enough mana"
        self.player.mana -= self.mana_cost
        self.player.hand.remove(self)
