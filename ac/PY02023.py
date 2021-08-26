def sum_e(e):
    s = 0
    for i in str(e):
        s += int(i)
    return s


t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    m = sorted(arr, key=lambda x: (sum_e(x), x))
    print(' '.join(map(str, m)))
    t -= 1
