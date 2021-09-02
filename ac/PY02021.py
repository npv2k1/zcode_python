t = int(input())
for tt in range(t):
    n, m, k = list(map(int, input().split()))
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_c = list(map(int, input().split()))

    i, j, z = [0]*3
    ok = True
    while(not(i >= n or j >= m or z >= k)):
        if(arr_a[i] == arr_b[j] and arr_b[j] == arr_c[z]):
            print(arr_a[i], end=' ')
            i += 1
            j += 1
            z += 1
            ok = False
        else:
            tmp = max(arr_a[i], arr_b[j], arr_c[z])
            if(arr_a[i] < tmp):
                i += 1
            if(arr_b[j] < tmp):
                j += 1
            if(arr_c[z] < tmp):
                z += 1
    if(ok):
        print('NO', end='')
    print()
