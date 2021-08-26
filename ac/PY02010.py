while True:
    n = int(input())
    if(n == 0):
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    max_arr = max(arr)
    min_arr = min(arr)
    if(max_arr == min_arr):
        print('BANG NHAU')
    else:
        print(min_arr, max_arr)
