'''
speed: cached_fibonacci > common-loop > tail-recursive >>> linear-recursive
NOTE: cached linear-recursive method is faster than common loop impl.
'''

from functools import lru_cache


def fibonacci(n: int):
    '''linear-recursive'''
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


@lru_cache(maxsize=None)
def cached_fibonacci(n: int):
    """cached linear-recursive"""
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return cached_fibonacci(n - 2) + cached_fibonacci(n - 1)


def fibonacci2(n: int):
    '''tail-recursive'''

    def _inner(n: int, a: int, b: int):
        if (n <= 0):
            return a
        else:
            return _inner(n - 1, b, a + b)

    return _inner(n, 0, 1)


def fibonacci3(n: int):
    '''common-loop'''
    a, b, i = 0, 1, 1
    while i <= n:
        _a = a
        a = b
        b = _a + b
        i += 1
    return a


if __name__ == "__main__":
    import time

    the_range = range(0, 32)

    fibs = []
    s = time.time()
    for i in the_range:
        fibs.append(cached_fibonacci(i))
    t = time.time() - s
    print(fibs)
    print(cached_fibonacci.__doc__)
    print(t)

    fibs = []
    s = time.time()
    for i in the_range:
        fibs.append(fibonacci(i))
    t = time.time() - s
    print(fibs)
    print(fibonacci.__doc__)
    print(t)

    fibs = []
    s = time.time()
    for i in the_range:
        fibs.append(fibonacci2(i))
    t = time.time() - s
    print(fibs)
    print(fibonacci2.__doc__)
    print(t)

    fibs = []
    s = time.time()
    for i in the_range:
        fibs.append(fibonacci3(i))
    t = time.time() - s
    print(fibs)
    print(fibonacci3.__doc__)
    print(t)
