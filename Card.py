class Card:
    def __init__(self, mana: int):
        self.mana = mana
        self.player = None
        self.owner = None

    @property
    def mana(self):
        mana = self._mana['current']
        return mana if mana > 0 else 0

    @mana.setter
    def mana(self, val: int):
        if type(val) is not int:
            raise TypeError

        if not hasattr(self, '_mana'):
            self._mana = {'base': val, 'current': val}

        self._mana['current'] = val

    def play(self, **kwargs):
        pass


if __name__ == '__main__':
    pass
