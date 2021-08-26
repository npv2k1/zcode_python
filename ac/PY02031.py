def arr_input():
    return list(map(int,input().split()))
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
n,m = arr_input()
arr=[]
for i in range(n):
    tmp = arr_input()
    for i in range(0,len(tmp)):
        if(is_prime(tmp[i])):
            tmp[i]=1
        else:
            tmp[i]=0
    arr.append(tmp)
for i in arr:
    for j in i:
        print(j,end=' ')
    print()
#chua submit