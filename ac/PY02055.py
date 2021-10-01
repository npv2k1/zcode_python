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


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

max_prime = -1
index_prime = []
for i in range(n):
    for j in range(m):
        if(is_prime(arr[i][j]) and arr[i][j] > max_prime):
            max_prime = arr[i][j]
            index_prime = []
            index_prime.append([i, j])
        elif(arr[i][j] == max_prime):
            index_prime.append([i, j])
if(max_prime == -1):
    print('NOT FOUND')
else:
    print(max_prime)
    for i in index_prime:
        print(f'Vi tri [{i[0]}][{i[1]}]')
