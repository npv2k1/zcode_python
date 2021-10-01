n = int(input())
res = [0]*n
B = []
for i in range(n):
    B.append(list(map(int, input().split())))
if(n == 2):
    print(1, 1)
else:
    row_sum = []
    for i in range(n-1):
        row_sum.append(sum(B[i][i+1:]))

    d = row_sum[n-2]
    for i in range(n-3, -1, -1):
        res[i] = (row_sum[i]-d-sum(res))//(n-i-1)
        # print(row_sum[i])
    res[n-1] = B[n-1][0]-res[0]
    res[n-2] = B[n-2][0]-res[0]
    print(' '.join(map(str, res)))

# # make test
# import random
# n=random.randint(2,50)
# arr=[]
# for i in range(n):
#     arr.append(random.randint(0, 100))
# b = [[0 for k in range(n)] for l in range(n)]
# for i in range(n):
#     for j in range(n):
#         if(i!=j):
#             b[i][j]=arr[i]+arr[j]
# # print(arr)
# # print(b)
# with open('input.txt','w') as f:
#     f.write(f'{n}\n')
#     for i in b:
#         f.write(' '.join(map(str,i))+'\n')
# with open('dest.txt', 'w') as f:
#     f.write(' '.join(map(str, arr))+'\n')
