from itertools import combinations_with_replacement
def triangle(n):
    for i in range(1, n+1):
        print(*combinations_with_replacement(range(1, i+1), i))