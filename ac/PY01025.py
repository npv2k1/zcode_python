n = input()
n = n[::-1]
res = []
for i in range(len(n)):
    res.append(n[i])
    if((i+1) % 3 == 0 and i < len(n)-1):
        res.append(',')

print(''.join(res[::-1]))
