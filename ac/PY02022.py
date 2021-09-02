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
arr = list(map(int,input().split()))
arr_prime={}
for i in arr:
    if(is_prime(i)):
        if(arr_prime.get(i,-1)==-1):
            arr_prime[i]=1
        else:
            arr_prime[i]+=1

for (num,count) in arr_prime.items():
    print(num,count)