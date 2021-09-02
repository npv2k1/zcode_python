import re
t = int(input())
for tt in range(t):
    n = re.search(r'[0-3]|[5-6]|[8-9]', input())
    if n:
        print('NO')
    else:
        print('YES')
