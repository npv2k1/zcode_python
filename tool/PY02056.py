

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input().split()))
max_rev = -1
index_rev = []
check = False
for i in range(n):
    for j in range(m):
        if(len(arr[i][j]) >= 2 and arr[i][j] == arr[i][j][::-1] and int(arr[i][j]) > max_rev):
            max_rev = int(arr[i][j])
            index_rev = []
            index_rev.append([i, j])
            check = True
        elif(int(arr[i][j]) == max_rev):
            index_rev.append([i, j])
if(not check):
    print('NOT FOUND')
else:
    print(max_rev)
    for i in index_rev:
        print(f'Vi tri [{i[0]}][{i[1]}]')
