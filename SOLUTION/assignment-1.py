from itertools import accumulate
def factorial(n):
    if n == 0:
        return 1
    return list(accumulate(range(1, n + 1), lambda x, y: x * y))[-1]