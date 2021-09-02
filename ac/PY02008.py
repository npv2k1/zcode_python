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


n, x = list(map(int, input().split()))
arr_prime = []
arr_prime.append(x)
i = 2
while len(arr_prime) < n+1:
    if(is_prime(i)):
        arr_prime.append(i+arr_prime[len(arr_prime)-1])
    i += 1
print(' '.join(map(str, arr_prime)))
