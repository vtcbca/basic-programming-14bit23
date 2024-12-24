class StarPattern:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        row = ["*" for _ in range(self.i)]
        self.i += 1
        return row

def star_pattern(n):
    for row in StarPattern(n):
        print(*row)