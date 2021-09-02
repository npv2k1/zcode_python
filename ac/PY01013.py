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
    a, b = list(map(int, input().split()))
    ucln = math.gcd(a, b)
    s = 0
    for i in str(ucln):
        s += int(i)
    if(is_prime(s)):
        print('YES')
    else:
        print("NO")

    t -= 1
