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


n = int(input())
arr = list(map(int, input().split()))
arr_nt = []
index_nt = []
for i in range(n):
    if(is_prime(arr[i])):
        arr_nt.append(arr[i])
        index_nt.append(i)
arr_nt.sort()
for i in range(len(index_nt)):
    arr[index_nt[i]] = arr_nt[i]
print(' '.join(map(str, arr)))
