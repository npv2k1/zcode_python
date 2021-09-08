t = int(input())
for tt in range(t):
    n = input()
    s = 1
    for i in n:
        s*=int(i) if i!='0' else 1
    print(s)    