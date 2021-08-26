import re


def solve(n):
    arr_688 = list(filter(None, n.split('688')))
    arr_68 = []
    arr_6 = []
    for i in arr_688:
        tmp = list(filter(None, i.split('68')))
        for j in tmp:
            arr_68.append(j)
    for i in arr_68:
        tmp = list(filter(None, i.split('6')))
        for j in tmp:
            arr_6.append(j)
    if len(arr_6) == 0:
        return 'YES'
    else:
        return 'NO'


print(solve(input()))
