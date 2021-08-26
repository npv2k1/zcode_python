while True:
    arr = list(map(int, input().split()))
    if(arr.count(0) == 4):
        break
    count = 0
    while len(set(arr)) > 1:
        tmp = [0]*4
        for i in range(4):
            tmp[i] = abs(arr[i]-arr[(i+1) % 4])
        arr = tmp
        # print(arr)
        count += 1
    # print(arr)
    print(count)
