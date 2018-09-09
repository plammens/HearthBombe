"""
TODO: Hand, Battlefield: change RuntimeError to more specific exception
"""


class Player:
    def __init__(self):
        self.hand = Hand(self)
        self.battlefield = Battlefield(self)
        self.health = 30
        self._mana = {'total': 0, 'available': 0}

    @property
    def mana(self):
        return self._mana['available']

    @mana.setter
    def mana(self, val):
        self._mana['available'] = min(max(val, 0), self._mana['total'])

    def play_card_by_index(self, index, **kwargs):
        """Shortcut for playing nth card in hand"""
        target = kwargs.get('target', None)
        self.hand.pop(index).play(target=target)

    def play_card(self, card_blueprint, **kwargs):
        """Play first card in hand with same attributes as card"""
        target = kwargs.get('target', None)
        for card in self.hand:
            if card == card_blueprint:
                card.play(target=target)
                break
        else:
            raise LookupError("Card not found")


class PlayerProperty(list):
    def __init__(self, owner) -> None:
        list.__init__(self)
        self.owner = owner

    def initialize(self, *cards):
        self.clear()
        for card in cards:
            self.append(card)
            card.owner = self.owner

    def append(self, card, **kwargs):
        if len(self) == kwargs.get('max_cards', 7):
            raise RuntimeError("Max card number reached")

        list.append(self, card)

    def extend(self, iterable):
        for card in iterable:
            self.append(card)

    def remove(self, card):
        try:
            list.remove(self, card)
        except ValueError:
            raise ValueError("Removing missing card from %s!" % type(self))


class Hand(PlayerProperty):
    def __init__(self, holder) -> None:
        super().__init__(holder)
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
            card.mana_cost = card._mana['base'] + val

    def append(self, card, **kwargs):
        super().append(card, max_cards=10)
        card.player = self.owner


class Battlefield(PlayerProperty):
    def __init__(self, player) -> None:
        super().__init__(player)

    def append(self, minion, **kwargs):
        super().append(minion, max_cards=7)
        minion.controller = self.owner

    def remove(self, minion):
        super().remove(minion)
        if minion.static_effect is not None:
            minion.static_effect.deactivate()
