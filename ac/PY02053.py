n = int(input())
res = []
for i in range(n):
    res.append(list(map(int, input().split())))
k = int(input())
sum_up = 0
sum_down = 0
for i in range(n):
    sum_up += sum(res[i][:n-i-1])
    sum_down += sum(res[i][n-i:])
if(abs(sum_up-sum_down) <= k):
    print('YES')
    print(abs(sum_up-sum_down))
else:
    print('NO')
    print(abs(sum_up-sum_down))
