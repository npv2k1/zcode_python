import sys
n = input()
dict_a = {}
for i in range(0, len(n), 2):
    tmp =int(n[i:i+2])
    if(tmp < 10):
        continue
    if(dict_a.get(tmp, -1) == -1):
        dict_a[tmp] = 1
    else:
        dict_a[tmp] += 1
for (key, value) in dict_a.items():
    print(key, value)