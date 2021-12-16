class AlgorithmModule(object):
    """Create an Algorithm module from a dictionary.

    - Each dictionary key becomes an attribute.
    - The initializer also has a kwarg `name` that allows to modify the
    __name__ of the resulting object.
    """

    def __init__(self, _dict, name=None):
        self.__dict__ = _dict
        if name is not None:
            self.__name__ = name
