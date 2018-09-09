class Callable_List(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def append(self, val):
        if callable(val):
            list.append(self, val)
        else:
            raise TypeError


def remove_duplicates(cards: list):
    result = []
    for card in cards:
        if not any([card == card2 for card2 in result]):
            result.append(card)

    return result
