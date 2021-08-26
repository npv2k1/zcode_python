t = int(input())
while t:
    n = input()
    for i in range(0, len(n), 2):
        print(n[i]*int(n[i+1]), end='')
    print()
    t -= 1
