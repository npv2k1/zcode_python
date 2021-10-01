# ƯU THẾ NGUYÊN TỐ
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
    n = input()
    count_prime = 0
    if(not is_prime(len(n))):
        print('NO')
        continue
    else:
        for i in n:
            if(is_prime(int(i))):
                count_prime += 1
    if(count_prime > len(n)//2):
        print('YES')
    else:
        print('NO')
#ac
