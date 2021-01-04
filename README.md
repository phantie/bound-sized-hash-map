# bound-sized-hash-map
Dictionary restricted in growth, FIFO

```python
    (take(BoundSizedDict(2))(print)
        .__setitem__('a', 20)(print)
        .__setitem__('b', 30)(print)
        .__setitem__('c', 30)(print)
        .__setitem__('d', 40)(print))
```

    {}
    {'a': 20}
    {'a': 20, 'b': 30}
    {'b': 30, 'c': 30}
    {'c': 30, 'd': 40}

Import:

    from bmap import BoundSizedDict

Install:

    pip install git+https://github.com/phantie/bound-sized-hash-map -U