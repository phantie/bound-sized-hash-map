from collections import OrderedDict

__all__ = ('BoundSizedDict',)
__version__ = '0.1'

class BoundSizedDict:
    def __new__(cls, max):
        if isinstance(max, int) and max >= 1:
            return super().__new__(cls)
        else:
            raise ValueError('max must be an instance of int and >= 1')

    def __init__(self, max):        
        self._ = OrderedDict()
        self.max = max

    def __getitem__(self, item):
        return self._.__getitem__(item)

    def __setitem__(self, key, value):
        _ = self._
        _.__setitem__(key, value)
        _.move_to_end(key)
        if len(_) > self.max:
            _.popitem(last=False)

    def __delitem__(self, item):
        self._.__delitem__(item)

    def __str__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._.items()) + '}'

    def __repr__(self):
        return str(self)