t = int(input())


def check(arr_a, arr_b):
    for i in range(len(arr_a)):
        if(arr_a[i] > arr_b[i]):
            print('NO')
            return
    print('YES')


while t:
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_a.sort()
    arr_b.sort()
    check(arr_a, arr_b)

    t -= 1
