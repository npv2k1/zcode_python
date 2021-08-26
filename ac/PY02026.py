n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = sorted(list(set(a)))
B = sorted(list(set(b)))
if(A == B):
    print('YES')
else:
    print('NO')
