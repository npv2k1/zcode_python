
t = int(input())
for tt in range(t):
    n = int(input())
    i = 2
    res = {}
    while(n > 1):
        if(n % i == 0):
            n = n//i
            if(res.get(i, -1) == -1):
                res[i] = 1
            else:
                res[i] += 1
        else:
            i += 1
            c = 0
    tmp = ["1"]
    for (num, count) in res.items():
        tmp.append(f"{num}^{count}")
    print(' * '.join(tmp))
