from Card import Card
from Game import main_game, Game


class Spell(Card):
    def __init__(self, mana: int, *targets):
        super(Spell, self).__init__(mana)
        self.target_types = set(targets)

    @property
    def target_types(self):
        return self._target_types

    @target_types.setter
    def target_types(self, val: set):
        if val.issubset(Game.target_types):
            self._target_types = val
        else:
            raise ValueError("Invalid target types")

    def target_check(self, target):
        if not (target is None or
                any([issubclass(type(target), t_type) for t_type in self.target_types])):
            raise ValueError("Invalid target")

    def play(self, **kwargs):
        target = kwargs.get('target', None)
        action = kwargs.get('action', None)

        self.target_check(target)

        if (action is not None) and (not callable(action)):
            raise ValueError("Non-callable action")

        super().play()

        if action is not None:
            action()

        main_game.run_spell_effects()
