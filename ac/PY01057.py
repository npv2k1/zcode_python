
def get_int(): return int(input())


def test(solve):
    def result(*args, **kwargs):
        test_count = int(input())
        for i in range(test_count):
            solve(*args, **kwargs)
    return result


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


@test
def solve_problem():
    # code here
    n = input()
    for i in range(len(n)):

        if(is_prime(i) and not is_prime(int(n[i]))):
            print('NO')
            return
        if(not is_prime(i) and is_prime(int(n[i]))):
            print('NO')
            return
    print('YES')


solve_problem()
