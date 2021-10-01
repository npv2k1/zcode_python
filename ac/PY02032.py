n = input()
arr = set()

for i in range(0, len(n), 2):

    tmp = int(int(n[i:i+2]))
    if(tmp < 10):
        continue
    arr.add(tmp)

arr = sorted(list(arr))
print(' '.join(map(str, arr)))
