from Card import Card
from Game import main_game, Game
from Minion import Minion


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
        super().play()

        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified by %s's play() method " % type(self))

        try:
            action = kwargs['action']
        except KeyError:
            raise RuntimeError("No action specified by %s's play() method " % type(self))

        self.target_check(target)
        if hasattr(target, 'spells_cast_upon'):
            target.spells_cast_upon.append(self)

        if (action is not None) and (not callable(action)):
            raise ValueError("Non-callable action")

        if action is not None:
            action()

        main_game.run_spell_effects()
