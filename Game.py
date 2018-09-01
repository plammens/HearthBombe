class Game:
    hand = 9
    target_types = ("Minion", "Hero")

    player_battlefield = []
    opponent_battlefield = []

    player_hand = []

    @staticmethod
    def minion_count():
        return len(Game.player_battlefield) + len(Game.opponent_battlefield)
