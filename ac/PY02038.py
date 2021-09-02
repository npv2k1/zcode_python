import math
n = int(input())
arr = []
res = 0
for i in range(n):
    arr.append(input())

for i in arr:
    tmp = i.count('C')
    if(tmp >= 2):
        res += math.comb(tmp, 2)

for i in range(n):
    tmp = 0
    for j in range(n):
        if(arr[j][i] == 'C'):
            tmp += 1
    if(tmp >= 2):
        res += math.comb(tmp, 2)
print(res)
