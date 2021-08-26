t = int(input())


def check(s):
    for i in range(0, len(s)-1):
        if(int(s[i]) > int(s[i+1])):
            print('NO')
            return
    print('YES')
    return


while t:
    check(input())
    t -= 1
