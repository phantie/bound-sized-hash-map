# bound-sized-hash-map
Dictionary restricted in growth, FIFO. Updating values via a key prolongs live of the key-value pair.

```python
(take(BoundSizedDict(2))(print)
    .__setitem__('a', 20)(print)
    .__setitem__('b', 30)(print)
    .__setitem__('a', 40)(print)
    .__setitem__('c', 50)(print)
    .__setitem__('d', 60)(print))
```

Output:

    {} ←
    {'a': 20} ←
    ← {'a': 20 ← 'b': 30} ←
    ← {'b': 30 ← 'a': 40} ←
    ← {'a': 40 ← 'c': 50} ←
    ← {'c': 50 ← 'd': 60} ←
    
Import:

    from bmap import BoundSizedDict

Install:

    pip install git+https://github.com/phantie/bound-sized-hash-map -U
