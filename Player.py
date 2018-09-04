from utils import Hand, Battlefield


class Player:
    def __init__(self):
        self.hand = Hand(self)
        self.battlefield = Battlefield(self)
        self.health = 30

    def play_card(self, index):
        """Shortcut for playing nth card in hand"""
        self.hand.pop(index).play()
