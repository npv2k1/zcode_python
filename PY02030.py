import collections


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
set_arr = list(dict(collections.Counter(arr)).keys())
# print(set_arr)
check = False
for i in range(n):
    if(is_prime(sum(set_arr[:i+1])) and is_prime(sum(set_arr[i+1:]))):
        print(i)
        check = True
        break
if(not check):
    print("NOT FOUND")
