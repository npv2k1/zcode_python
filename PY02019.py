import math
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if(math.gcd(arr[i], arr[j]) == 1):
            res.append([arr[i], arr[j]])
for i in res:
    print(i[0], i[1])
