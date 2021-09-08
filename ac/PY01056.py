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
def get_int(): return int(input())


def test(solve):
    def result(*args, **kwargs):
        test_count = int(input())
        for i in range(test_count):
            solve(*args, **kwargs)
    return result


@test
def solve_problem():
    n = input()
    s=0
    for i in range(len(n)):
        if(i%2==0 and int(n[i])%2!=0):
            print('NO')
            return
        if(i%2==1 and int(n[i])%2==0):
            print('NO')
            return
        s+=int(n[i])
    if(is_prime(s)):
        print('YES')
    else:
        print('NO')
solve_problem()
