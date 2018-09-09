"""
TODO: Hand, Battlefield: change RuntimeError to more specific exception
"""
import Spell
import Minion


class Player:
    def __new__(cls):
        self = super().__new__(cls)

        self.health = 30
        self._mana = {'total': 0, 'available': 0}

        self.hand = Hand(self)
        self.battlefield = Battlefield(self)

        self.play_spell_effects = []

        return self

    def __getnewargs__(self):
        return tuple()


    """Properties"""

    @property
    def mana(self):
        return self._mana['available']

    @mana.setter
    def mana(self, val):
        self._mana['available'] = min(max(val, 0), self._mana['total'])

    """Methods"""

    def play_card_by_index(self, index, **kwargs):
        """Shortcut for playing nth card in hand"""
        target = kwargs.get('target', None)
        self.hand[index].play(target=target)

    def play_card(self, card_blueprint, **kwargs):
        """Play first card in hand with same attributes as card"""
        target = kwargs.get('target', None)
        self.hand.get_card(card_blueprint).play(target=target)

    def play_card_by_type(self, c_type, **kwargs):
        """Play first card in hand of given type"""
        target = kwargs.get('target', None)
        self.hand.get_card_by_type(c_type).play(target=target)

    def run_spell_effects(self):
        for effect in self.play_spell_effects:
            effect.trigger()


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

    def get_card(self, card_blueprint):
        for card in self:
            if card == card_blueprint:
                return card
        raise LookupError("Card not found")

    def get_card_by_type(self, c_type):
        for card in self:
            if isinstance(card, c_type):
                return card
        raise LookupError("Card not found")


class Hand(PlayerProperty):
    def __init__(self, holder) -> None:
        super().__init__(holder)

        self._mana_bias_any = 0
        self._mana_bias_spells = 0
        self._mana_bias_minions = 0

    @property
    def mana_bias_any(self):
        return self._mana_bias_any

    @mana_bias_any.setter
    def mana_bias_any(self, val: int):
        if type(val) is not int:
            raise TypeError

        self._mana_bias_any = val

        for card in self:
            card.mana_cost = card._mana_cost['base'] + self._mana_bias_any

    @property
    def mana_bias_spells(self):
        return self._mana_bias_spells

    @mana_bias_spells.setter
    def mana_bias_spells(self, val: int):
        if type(val) is not int:
            raise TypeError

        self._mana_bias_spells = val

        for card in self:
            if isinstance(card, Spell.Spell):
                card.mana_cost = card._mana_cost['base'] + self._mana_bias_spells

    @property
    def mana_bias_minions(self):
        return self._mana_bias_minions

    @mana_bias_minions.setter
    def mana_bias_minions(self, val: int):
        if type(val) is not int:
            raise TypeError

        self._mana_bias_minions = val

        for card in self:
            if isinstance(card, Minion.Minion):
                card.mana_cost = card._mana_cost['base'] + self._mana_bias_spells

    def append(self, card, **kwargs):
        super().append(card, max_cards=10)
        card.player = self.owner


class Battlefield(PlayerProperty):
    def __init__(self, player) -> None:
        super().__init__(player)

    def append(self, minion, **kwargs):
        super().append(minion, max_cards=7)
        minion.controller = self.owner

        if minion.static_effect is not None:
            minion.static_effect.controller = self.owner
            minion.static_effect.activate()
        if minion.triggered_effect is not None:
            minion.triggered_effect.controller = self.owner
            self.owner.play_spell_effects.append(minion.triggered_effect)

    def remove(self, minion):
        super().remove(minion)
        if minion.static_effect is not None:
            minion.static_effect.deactivate()
        if minion.triggered_effect is not None:
            self.owner.play_spell_effects.remove(minion.triggered_effect)
