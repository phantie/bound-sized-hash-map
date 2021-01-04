from collections import OrderedDict

__all__ = ('BoundSizedDict',)
__version__ = '0.3'

class BoundSizedDict(OrderedDict):
    """Dictionary restricted in growth, FIFO.
       Updating values via a key prolongs live of the key-value pair."""

    def __new__(cls, max):
        if isinstance(max, int) and max >= 1:
            return super().__new__(cls)
        else:
            raise ValueError('max must be an instance of int and >= 1')

    def __init__(self, max):        
        self.max = max

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.max:
            self.popitem(last=False)

    def __str__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self.items()) + '}'

    def __repr__(self):
        return str(self)

    def fromkeys(self, keys, value=None):
        for key in keys:
            self[key] = value

    def update(self, dict):
        raise DeprecationWarning('nondetermenistic behaviour will be achieved using this method')