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

t = int(input())
while t:
    n = int(input())
    k = 0
    for i in range(1, n):
        if(math.gcd(i, n) == 1):
            k += 1
    if(is_prime(k)):
        print('YES')
    else:
        print('NO')

    t -= 1
