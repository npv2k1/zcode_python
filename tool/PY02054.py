n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

while(m != n):
    if(n > m):
        # remove row odd
        change = n-m
        arr = arr[1:change*2+1:2]+arr[change*2:]

    if(n < m):
        # remove col even
        res = []
        change = m-n
        for i in arr:
            res.append(i[0:change*2+2:2]+i[change*2+1:])
        arr = res
    n = len(arr)
    m = len(arr[0])
for i in arr:
    print(' '.join(map(str, i)))
