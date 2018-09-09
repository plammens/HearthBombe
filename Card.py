from Game import main_game


class Card:
    def __init__(self, mana_cost: int):
        self.mana_cost = mana_cost
        self.player = None
        self.owner = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

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
        assert self.player == main_game.player or self.player == main_game.opponent
        assert self.mana_cost <= self.player.mana, "Not enough mana"
        self.player.mana -= self.mana_cost
