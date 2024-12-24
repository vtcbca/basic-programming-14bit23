def is_prime(n):
    if n <= 1:
        return False
    try:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                raise ValueError
        return True
    except ValueError:
        return False