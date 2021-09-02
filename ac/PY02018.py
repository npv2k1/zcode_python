n = int(input())
arr = list(map(int, input().split()))
# s = sum(arr)
# target = (n+1)*(n+2)//2
# print(int(abs(target-s)))
arr.sort()
ok=False
for i in range(0,n-1,1):
    if(arr[i+1]-arr[i]>1):
        print(arr[i]+1)
        ok=True
        break
if(not ok):
    print(arr[n-1]+1)

# ddm  bài ảo vcl test ngu như bò.