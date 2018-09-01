class Card:
    def __init__(self, mana):
        self.mana = mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, val: int):
        if type(val) is not int or val < 0:
            raise ValueError

        if not hasattr(self, '_mana'):
            self._mana = {'base': val, 'current': val}

        self._mana['current'] = val


if __name__ == '__main__':
    pass
