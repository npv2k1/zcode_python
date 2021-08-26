n = int(input())
arr = list(map(int, input().split()))
res = 0
for i in range(1, len(arr)):
    for j in range(0, i):
        if(arr[j] > arr[i]):
            res += 1
print(res)
