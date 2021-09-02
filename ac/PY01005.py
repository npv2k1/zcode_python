n = input().strip()
c = n.count('4') + n.count('7')
if(c == 4 or c == 7):
    print('YES')
else:
    print('NO')
