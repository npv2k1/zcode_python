t = int(input())
while t:
    n = input()
    if(n[len(n)-2:] == '86'):
        print("YES")
    else:
        print("NO")
    t -= 1
