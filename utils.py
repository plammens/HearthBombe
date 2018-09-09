class Callable_List(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def append(self, val):
        if callable(val):
            list.append(self, val)
        else:
            raise TypeError


def remove_duplicates(entities: list):
    result = []
    for entity in entities:
        if not any([entity == oth_entity for oth_entity in result]):
            result.append(entity)

    return result
