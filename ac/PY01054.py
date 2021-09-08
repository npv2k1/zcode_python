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
    s = 1
    for i in n:
        s *= int(i) if i != '0' else 1
    print(s)

solve_problem()
