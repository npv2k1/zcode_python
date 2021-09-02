t = int(input())
while t:
    a, b = list(map(int, input().split()))
    res = [1, 1]
    i = 2
    while i < b+1:
        res.append(res[i-1]+res[i-2])
        i += 1
    print(' '.join(map(str, res[a-1:b])))

    t -= 1
