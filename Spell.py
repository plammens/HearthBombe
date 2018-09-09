"""
TODO: add special Spell subclass for spells with targets?
TODO: better exception management (to asserts?)
"""

from Card import Card


class Spell(Card):
    def __init__(self, mana_cost: int, **kwargs):
        super(Spell, self).__init__(mana_cost)
        self._target_types = kwargs.get('target_types', None)

    @property
    def target_types(self):
        return self._target_types

    @target_types.setter
    def target_types(self, val: set) -> None:
        """
        if val is None or val.issubset({Player}):
            self._target_types = val
        else:
            raise ValueError("Invalid target types")
        """
        raise NotImplemented

    def is_valid_target(self, target) -> bool:
        if target is None and self.target_types is None:
            return True
        elif any([issubclass(type(target), type_) for type_ in self.target_types]):
            return True
        else:
            return False

    def play(self, **kwargs):
        super().play()

        # Get target
        try:
            target = kwargs['target']
        except KeyError:
            raise RuntimeError("No target specified by %s's play() method " % type(self))

        # Make sure it's a valid target
        assert self.is_valid_target(target), "%s is not a valid target for %s" % (target, type(self))

        # Get action
        try:
            action = kwargs['action']
        except KeyError:
            raise RuntimeError("No action passed on by %s's play() method " % type(self))

        # Make sure it's a callable action
        if not callable(action):
            raise ValueError("Invalid action for spell %s" % type(self))

        # If target keeps track of spells cast upon it, add self to list
        # Note: done before calling action to account for special abilities
        if hasattr(target, 'spells_cast_upon'):
            target.spells_cast_upon.append(self)

        # Cast spell (finally!)
        action()

        # Run any effects like "After you play a spell, [...]"
        self.player.run_spell_effects()
