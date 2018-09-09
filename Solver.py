"""
TODO: check if needs target with class boolean
"""


from copy import deepcopy

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
                # Does it need a target?
                if hasattr(card, "is_valid_target"):
                    """Runs if the card needs a target"""

                    for target in \
                            remove_duplicates([ct for ct in main_game.characters if card.is_valid_target(ct)]):
                        # Play card
                        main_game.player.play_card(card, target=target)

                        new_status = GameStatus(main_game, status.steps)
                        new_status.steps.append({'card': type(card), 'target': target})

                        states.append(new_status)

                        # Reset to previous status (to test with other targets)
                        main_game = deepcopy(status.game)
                else:
                    """Runs if card doesn't act on a specific target"""
                    main_game.player.play_card(card)

                    new_status = GameStatus(main_game, status.steps)
                    new_status.steps.append({'card': type(card), 'target': None})

    return steps


def remove_duplicates(cards: list):
    result = []
    for card in cards:
        if not any([card == card2 for card2 in result]):
            result.append(card)

    return result
