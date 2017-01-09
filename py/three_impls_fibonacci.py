'''
speed: common-loop > tail-recursive >>> linear-recursive
'''


def fibonacci(n: int):
    '''linear-recursive'''
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def fibonacci2(n: int):
    '''tail-recursive'''

    def _inner(n: int, a: int, b: int):
        if (n <= 0):
            return a
        elif (n == 1):
            return b
        else:
            return _inner(n - 2, a + b, b + a + b)

    return _inner(n, 0, 1)


def fibonacci3(n: int):
    '''common-loop'''
    a, b, i, even = 0, 1, 1, False
    while i <= n:
        if even:
            a += b
        else:
            b += a
        even, i = not even, i + 1
    return b if even else a


if __name__ == "__main__":
    import time

    the_range = range(1, 31)
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
