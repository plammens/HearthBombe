"""
TODO: Hand, Battlefield: change RuntimeError to more specific exception
TODO: make Player_Property metaclass for Hand and Battlefield
TODO: separate from utils?
"""


class Callable_List(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def append(self, val):
        if callable(val):
            list.append(self, val)
        else:
            raise TypeError


class Hand(list):
    def __init__(self, holder) -> None:
        list.__init__(self)
        self.holder = holder
        self._mana_bias = 0

    @property
    def mana_bias(self):
        return self._mana_bias

    @mana_bias.setter
    def mana_bias(self, val):
        if type(val) is not int:
            raise TypeError

        self._mana_bias = val

        for card in self:
            card.mana = card._mana['base'] + val

    def initialize(self, *cards):
        self.clear()
        for card in cards:
            self.append(card)
            card.owner = self.holder

    def append(self, card):
        if len(self) == 7:
            raise RuntimeError("Max minions on battlefield reached")
        list.append(self, card)
        card.player = self.holder

    def extend(self, iterable):
        for card in iterable:
            self.append(card)

    def remove(self, card):
        try:
            list.remove(self, card)
        except ValueError:
            raise RuntimeError("Removing missing card from hand!")


class Battlefield(list):
    def __init__(self, player) -> None:
        list.__init__(self)
        self.controller = player

    def initialize(self, *minions):
        self.clear()
        for minion in minions:
            minion.summon(self.controller)
            minion.owner = self.controller

    def append(self, minion):
        list.append(self, minion)
        minion.controller = self.controller

    """def extend(self, iterable):
        for minion in iterable:
            self.append(minion)"""

    def remove(self, minion):
        try:
            list.remove(self, minion)
        except ValueError:
            raise ValueError("Removing missing minion from battlefield!")
