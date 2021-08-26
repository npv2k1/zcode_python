# CHIA HẾT CHO K
# a+b<=n
# a+b%k==0
a, K, N = list(map(int, input().strip().split()))
ok = False
for i in range(1, N//K+1):
    if(K*i > a):
        print(K*i-a, end=' ')
        ok = True
if(not ok):
    print(-1, end='')
