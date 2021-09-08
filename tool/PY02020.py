n = int(input())
res = []
res += map(float, input().split())
avg_point = 0
c = 0
min_res = min(res)
max_res = max(res)
for i in res:
    if(i != min_res and i != max_res):
        avg_point += i
        c += 1


print("%.2f" % (avg_point/c))
