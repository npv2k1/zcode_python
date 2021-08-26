p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = input().split()

    if(len(inp) == 1):
        break
    k, s = inp
    k = int(k)
    s = s.strip()

    res = []
    for i in s:
        res.append(p[(p.index(i)+k) % 28])
    print(''.join(reversed(res)))
