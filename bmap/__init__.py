from collections import OrderedDict

__all__ = ('BoundSizedDict',)
__version__ = '0.4'

class BoundSizedDict(OrderedDict):
    """Dictionary restricted in growth, FIFO.
       Updating values via a key prolongs live of the key-value pair."""

    def __init__(self, max_size):
        self.max_size = max_size

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if isinstance(value, int) and value >= 1:
            if len(self) > value:
                for _ in range(len(self) - value):
                    self.popfirst()

            self._max_size = value
        else:
            raise ValueError('max_size must be an instance of int and >= 1')

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.max_size:
            self.popfirst()

    def __str__(self):
        return f"{' ← ' if len(self) == self.max_size else '   '}\x7B{' ← '.join(f'{k!r}: {v!r}' for k, v in self.items())}\x7D ← "

    def __repr__(self):
        return str(self)

    def popfirst(self):
        return self.popitem(last=False)

    def fromkeys(self, keys, value=None):
        for key in keys:
            self[key] = value

    def update(self, dict):
        raise DeprecationWarning("nondetermenistic behaviour's achieved using this method")