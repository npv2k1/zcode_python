import math


def solve(n, p):
    cout = 0
    for i in range(1, n+1):
        if(math.trunc(n/p**i) < 1):
            break
        cout += math.trunc(n/p**i)
    print(cout)


t = int(input())
for i in range(t):
    n, p = list(map(int, input().strip().split()))
    solve(n, p)
