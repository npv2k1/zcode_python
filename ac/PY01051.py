# 	TỔNG CHỮ SỐ THUẬN NGHỊCH
t = int(input())
for tt in range(t):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    s = str(s)
    if(len(s)>1 and s == s[::-1]):
        print('YES')
    else:
        print("NO")
