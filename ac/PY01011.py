def solve(n):
    if(len(n) % 2 != 0):
        return False
    if(list(n) != list(reversed(n))):
        return False
    for i in n:
        if(int(i) % 2 != 0):
            return False
    return True


t = int(input())
for tt in range(t):
    n = int(input())
    for i in range(2, n, 2):
        if(solve(str(i))):
            print(i, end=' ')
    print()
