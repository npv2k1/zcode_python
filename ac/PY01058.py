import math


def is_prime(n: int):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for t in range(int(input())):
    n = input().strip()
    if(is_prime(int(n[len(n)-4:]))):
        print('YES')
    else:
        print('NO')
