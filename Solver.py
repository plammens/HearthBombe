from Game import GameStatus
from Spell import Spell


def solve(objective: str):
    """Algorithm for solving puzzles"""
    global main_game

    stati = [GameStatus()]

    while True:
        status = stati[-1]

        if status.inspected:
            break

        if main_game.minion_count == 0:
            break

        # expand possibilities
        for card in main_game.player.hand:
            if issubclass(type(card), Spell):
                for target in [character for character in main_game.characters if card.is_valid_target(character)]:
                    pass
            new_status = GameStatus()
        pass

    return steps
