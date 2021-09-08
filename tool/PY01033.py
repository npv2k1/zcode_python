from math import gcd
a, b = map(int, input().split())
res = []
for x in range(a, b+1, 1):
    for y in range(x+1, b+1, 1):
        for z in range(y+1, b+1, 1):
            if(gcd(x, y) == 1 and gcd(y, z) == 1 and gcd(x, z) == 1):
                res.append((x, y, z))
for i in res:
    print(i)
