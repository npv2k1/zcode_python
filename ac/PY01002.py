# PHÉP CỘNG
inp = input().strip()
s = inp.split('=')
a, b = list(map(int, s[0].split('+')))
res = int(s[1])
if(a+b == res):
    print('YES')
else:
    print('NO')
