from utils import Hand, Battlefield


class Player:
    def __init__(self):
        self.hand = Hand(self)
        self.battlefield = Battlefield(self)
        self.health = 30

    def play_card(self, index, **kwargs):
        """Shortcut for playing nth card in hand"""
        target = kwargs.get('target', None)
        self.hand.pop(index).play(target=target)
