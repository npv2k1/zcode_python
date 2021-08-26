def solve(s):
    s1 = list(map(ord, s))
    s2 = list(reversed(s1))
    for i in range(1, len(s1)):
        if(abs(s1[i]-s1[i-1]) != abs(s2[i]-s2[i-1])):
            print("NO")
            return
    print('YES')


t = int(input())
while(t):
    solve(input())
    t -= 1
