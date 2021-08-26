t = int(input())


def check(n):
    s = int(n[0])
    for i in range(1, len(n)):
        s += int(n[i])
        if(abs(int(n[i])-int(n[i-1])) != 2):
            print('NO')
            return
    if(s % 10 == 0):
        print('YES')
    else:
        print('NO')


while t:
    n = input()
    check(n)
    t -= 1
