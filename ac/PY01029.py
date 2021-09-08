from math import gcd

def get_int(): return int(input())


def test(solve):
    def result(*args, **kwargs):
        test_count = int(input())
        for i in range(test_count):
            solve(*args, **kwargs)
    return result


@test
def solve_problem():
    # code here
    n = input()
    if(gcd(int(n),int(n[::-1]))==1):
        print("YES")
    else:
        print('NO')

solve_problem()
