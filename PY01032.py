def symmetry(a):

    n = len(a)
    flag = 0
    if n % 2:
        mid = n//2 + 1
    else:
        mid = n//2
    start1 = 0
    start2 = mid
    while(start1 < mid and start2 < n):

        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False
def fromDeci(base, inputNum):
    res = []
    index = 0
    while (inputNum > 0):
        res.append(str(inputNum % base))
        inputNum = int(inputNum / base)
    if(symmetry(res)):
        return True
    return False


a, b, m = list(map(int, input().split()))
arr = range(b,a-1,-1)
for base in range(2, m+1):
    arr_tmp = []
    for i in arr:
        if(fromDeci(base, i)):
            arr_tmp.append(i)
    arr = arr_tmp
    if(len(arr) == 0):
        break
print(len(arr))
