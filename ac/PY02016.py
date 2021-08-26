t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    f_arr = {}
    for i in arr:
        if f_arr.get(i, -1) == -1:
            f_arr[i] = 1
        else:
            f_arr[i] += 1
    max_f = 0
    value = 0
    for (key, val) in f_arr.items():
        if val > max_f:
            max_f = val
            value = key
    if(max_f > n//2):
        print(value)
    else:
        print('NO')

    t -= 1
