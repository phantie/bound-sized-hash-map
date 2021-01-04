# bound-sized-hash-map
Dictionary restricted in growth, FIFO

```python
(take(BoundSizedDict(2))(print)
    .__setitem__('a', 20)(print)
    .__setitem__('b', 30)(print)
    .__setitem__('c', 40)(print)
    .__setitem__('d', 50)(print))
```

Output:

    {}
    {'a': 20}
    {'a': 20, 'b': 30}
    {'b': 30, 'c': 40}
    {'c': 40, 'd': 50}

Import:

    from bmap import BoundSizedDict

Install:

    pip install git+https://github.com/phantie/bound-sized-hash-map -U
