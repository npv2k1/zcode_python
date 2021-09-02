n = int(input())
arr = []
while(len(arr) < n):
    arr += list(map(int, input().split()))

chan = []
chan_index = []
le = []
le_index = []
for i in range(len(arr)):
    if(arr[i] % 2 == 0):
        chan.append(arr[i])
        chan_index.append(i)
    else:
        le.append(arr[i])
        le_index.append(i)
chan.sort()

le.sort(reverse=True)
# print(chan)
# print(le)
res = [0]*n
for i in range(len(chan)):
    res[chan_index[i]] = chan[i]
for i in range(len(le)):
    res[le_index[i]] = le[i]
print(' '.join(map(str, res)))
# vl input có thể nhiểu hon 1 dòng WTF
