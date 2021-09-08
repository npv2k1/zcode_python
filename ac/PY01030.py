import math
n,k = list(map(int,input().split()))
res=[]
for i in range(10**(k-1),10**(k),1):
    if(math.gcd(n,i)==1):
        res.append(i)
for i in range(0,len(res),10):
    print(' '.join(map(str,res[i:i+10])))
