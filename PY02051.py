n = int(input())
res = [0]*n
B = []
for i in range(n):
    B.append(list(map(int, input().split())))

# B = [[0, 3, 6, 7],
#      [3, 0, 5, 6],
#      [6, 5, 0, 9],
#      [7, 6, 9, 0]]
# B=[[0,2],[2,0]]


row_sum = []
for i in range(n-1):
    row_sum.append(sum(B[i][i+1:]))
d = row_sum[n-2]
for i in range(n-3, -1, -1):
    res[i] = (row_sum[i]-d-res[i+1])//(n-i-1)
res[n-1] = B[n-1][0]-res[0]
res[n-2] = B[n-2][0]-res[0]
print(' '.join(map(str, res)))
