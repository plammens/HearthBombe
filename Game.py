class Player:
    def __init__(self):
        self.hand = []
        self.battlefield = []
        self.health = 30


class Game:
    target_types = ("Minion", "Hero")

    player1 = Player()
    player2 = Player()

    @staticmethod
    def minion_count():
        return len(Game.player_battlefield) + len(Game.opponent_battlefield)
