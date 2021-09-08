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
    sum_n = 0
    tinh_n = 1
    check = False
    for i in range(0, len(n), 2):
        sum_n += int(n[i])
    for i in range(1, len(n), 2):
        if(n[i] != '0'):
            check = True
        tinh_n *= int(n[i]) if n[i] != '0' else 1

    if(check):
        print(sum_n, tinh_n)
    else:
        print(sum_n, 0)


solve_problem()
