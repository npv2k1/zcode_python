import re
n = map(int, input().split())
res = []
for i in range(n):
    string_in = input().lower()
    res += re.findall(r'\w+', string_in)
dict_s = {}
for i in res:
    if(dict_s.get(i, -1) == -1):
        dict_s[i] = 1
    else:
        dict_s[i] += 1

res = sorted(dict_s.items(), key=lambda x: (-x[1], x[0]))
for i in res:

    if(i[1] >= k):
        print(' '.join(map(str, i)))
