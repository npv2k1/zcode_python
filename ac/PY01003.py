t = int(input())
for tt in range(t):
    s = input()
    n = list(map(int, s))
    # print(n)
    if(len(n) <= 1):
        print(''.join(map(str, n)))
    else:
        for i in range(len(n)-1, 0, -1):
            if(n[i] < 5):
                n[i] = 0
            else:
                n[i] = 0
                n[i-1] += 1
        print(''.join(map(str, n)))
