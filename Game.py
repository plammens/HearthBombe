class Player:
    def __init__(self):
        self.hand = []
        self.battlefield = []
        self.health = 30


class Game:
    target_types = ("Minion", "Hero")

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def minion_count(self):
        return len(self.player1.battlefield) + len(self.player2.battlefield)
