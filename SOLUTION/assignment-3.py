from functools import reduce
def fibonacci(n):
    return reduce(lambda x, _: x + [x[-1] + x[-2]], range(2, n), [0, 1])