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
    len_n = len(n)
    if(len(n) % 2 == 0 or n[0] == n[1]):
        print('NO')
        return
    for i in range(0, len_n, 2):
        if(n[i] != n[0]):
            print('NO')
            return
    print('YES')


solve_problem()
