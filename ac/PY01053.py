# 	SỐ CHIA HẾT CHO 3
t = int(input())
for tt in range(t):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    
    if(s%3==0):
        print('YES')
    else:
        print("NO")
