t = int(input())
while t:
    n = input()
    a = n[:2]
    b = n[len(n)-2:]
    if(a[0] == b[0] and a[1] == b[1]):
        print('YES')
    else:
        print('NO')
    t -= 1
