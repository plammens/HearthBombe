"""
TODO: check if needs target with class boolean
"""

from copy import deepcopy

from Game import GameStatus, main_game
from utils import remove_duplicates

main_game = main_game


def solve(objective: str):
    """Brute-force algorithm for solving puzzles. Analogous to DFS."""
    global main_game

    states = [GameStatus(main_game)]

    print("Currently inspected:", end='\n')
    while True:
        print('\r%010d' % GameStatus.count, end='', flush=True)
        # Get top status from stack
        try:
            status = states.pop()
        except IndexError:
            return []

        # Set 'active' main_game to popped state
        main_game = deepcopy(status.game)

        # Check win condition
        if win_conditions[objective]():
            steps = status.steps
            break

        # expand possibilities
        for card in remove_duplicates(main_game.player.hand):
            # Get appropriate card (corresponding to active game object)
            try:
                card = main_game.player.hand.get_card(card)
            except LookupError:
                print(card)
                print(main_game.player.hand)
                print(status.steps)
                raise LookupError

            # Check if there is enough mana
            if card.mana_cost <= main_game.player.mana:
                # Get list of valid targets
                if hasattr(card, 'is_valid_target'):
                    valid_targets = [ct for ct in remove_duplicates(main_game.characters)
                                     if card.is_valid_target(ct)]
                else:
                    valid_targets = [None]

                for target in valid_targets:
                    # Play card
                    main_game.player.play_card(card, target=target)

                    new_status = GameStatus(main_game, status.steps)
                    new_status.steps.append({'card': type(card), 'target': type(target)})

                    states.append(new_status)

                    # Reset to previous status (to test with other targets)
                    main_game = deepcopy(status.game)

    return steps


# Win condition checkers:
def check_empty_battlefield():
    return main_game.minion_count == 0


def check_opponent_dead():
    return main_game.opponent.health == 0


def check_mirror():
    raise NotImplemented


def check_full_health():
    return main_game.player.health == main_game.player._health['base']


win_conditions = {
    "clear board": check_empty_battlefield,
    "destroy enemy": check_opponent_dead,
    "mirror": check_mirror,
    "survive": check_full_health
}
