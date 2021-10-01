

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


min_arr = arr[0][0]
max_arr = arr[0][0]
for i in arr:
    min_arr = min(i) if min(i) < min_arr else min_arr
    max_arr = max(i) if max(i) > max_arr else max_arr


lucky = max_arr-min_arr
check = False
index_prime = []
for i in range(n):
    for j in range(m):

        if(arr[i][j] == lucky):
            index_prime.append([i, j])
            check = True
if(not check):
    print('NOT FOUND')
else:
    print(lucky)
    for i in index_prime:
        print(f'Vi tri [{i[0]}][{i[1]}]')
