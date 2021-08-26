n = input()
while True:
    s = int(n[:len(n)//2])+int(n[len(n)//2:])
    print(s)
    n = str(s)
    if(len(n)==1):
        break
