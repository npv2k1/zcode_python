n, m = map(int, input().split())
tickets = list(map(int, input().split()))
res = {}
for i in tickets:
    if(res.get(i, -1) == -1):
        res[i] = 1
    else:
        res[i] += 1

kq = sorted(res.items(), key=lambda x: (-x[1], x[0]))
# print(kq)
check = False
f_max = kq[0][1]
for i in kq:
    if(i[1] != f_max):
        print(i[0])
        check = True
        break
if(not check):
    print('NONE')
