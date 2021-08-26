t = int(input())
for tt in range(t):
    s = list(input())
    s.sort()
    num_sum = 0
    while(s[0] >= '0' and s[0] <= '9'):
        num_sum += int(s.pop(0))
    print(''.join(s)+str(num_sum))
