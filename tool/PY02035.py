n = input()
k = int(input())
dict_a = {}
for i in range(0, len(n), 2):

    tmp = int(int(n[i:i+2]))
    if(tmp < 10):
        continue
    if(dict_a.get(tmp, -1) == -1):
        dict_a[tmp] = 1
    else:
        dict_a[tmp] += 1

ok = False
res = sorted(dict_a.items(), key=lambda x: x[0])
for (key, value) in res:
    if(value >= k):
        print(key, value)
        ok = True
if(not ok):
    print("NOT FOUND")
