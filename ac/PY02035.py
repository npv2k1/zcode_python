n = input()
k = int(input())
d = {}
for i in range(0, len(n), 2):
    tmp = int(int(n[i:i+2]))
    if(tmp < 10):
        continue
    if(d.get(tmp, -1) == -1):
        d[tmp] = 1
    else:
        d[tmp] += 1

ok = False
res = sorted(d.items(), key=lambda x: x[0])
for (key, value) in res:
    if(value >= k):
        print(key, value)
        ok = True
if(not ok):
    print("NOT FOUND")
