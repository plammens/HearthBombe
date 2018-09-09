"""
TODO: check if needs target with class boolean
"""

from copy import deepcopy
from utils import remove_duplicates
from Game import GameStatus, main_game


def solve(objective: str = "clear battlefield"):
    """Algorithm for solving puzzles"""
    global main_game

    states = [GameStatus(main_game)]

    while True:
        # Get top status from stack
        status = states.pop()

        # Set 'active' main_game to popped state
        main_game = deepcopy(status.game)

        # Win condition
        if main_game.minion_count == 0:
            steps = status.steps
            break

        # expand possibilities
        for card in remove_duplicates(main_game.player.hand):
            # Check if there is enough mana
            if card.mana_cost <= main_game.player.mana:
                # Get list of valid targets
                if hasattr(card, 'is_valid_target'):
                    valid_targets = [ct for ct in main_game.characters if card.is_valid_target(ct)]
                    valid_targets = remove_duplicates(valid_targets)
                else:
                    valid_targets = [None]

                for target in valid_targets:
                    # Play card
                    main_game.player.play_card(card, target=target)

                    new_status = GameStatus(main_game, status.steps)
                    new_status.steps.append({'card': type(card), 'target': target})

                    states.append(new_status)

                    # Reset to previous status (to test with other targets)
                    main_game = deepcopy(status.game)

    return steps
