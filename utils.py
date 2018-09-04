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

    def initialize(self, *cards):
        self.clear()
        for card in cards:
            list.append(self, card)
            card.player = self.holder
            card.owner = self.holder

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
            self.add(minion)

    def add(self, minion):
        list.append(self, minion)
        minion.controller = self.controller

    def remove(self, minion):
        try:
            list.remove(self, minion)
        except ValueError:
            raise ValueError("Removing missing minion from battlefield!")
