from copy import deepcopy

from Game import GameStatus


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
        for card in main_game.player.hand:
            # Check if there is enough mana
            if card.mana_cost <= main_game.player.mana:
                if hasattr(card, "is_valid_target"):
                    """Runs if the card needs a target"""
                    for target in [character for character in main_game.characters if card.is_valid_target(character)]:
                        # Play card
                        card.play(target=target)

                        new_status = GameStatus(main_game, status.steps)
                        new_status.steps.append({'card': type(card), 'target': target})

                        states.append(new_status)

                        # Reset to previous status (to test with other targets)
                        main_game = deepcopy(status.game)
                else:
                    """Runs if card doesn't act on a specific target"""
                    card.play()

                    new_status = GameStatus(main_game, status.steps)
                    new_status.steps.append({'card': type(card), 'target': None})

    return steps
