t = int(input())
for tt in range(1,t+1):
    
    a=list(input())
    b=list(input())
    a.sort()
    b.sort()
    print(f'Test {tt}: ',end='')
    if(a==b):
        print('YES')
    else:
        print('NO')
    
