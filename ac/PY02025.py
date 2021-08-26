n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = sorted(list(set(a)))
B = sorted(list(set(b)))

for i in A:
    if(i in B):
        print(i, end=' ')
print()
for i in A:
    if i not in B:
        print(i, end=' ')
print()
for i in B:
    if i not in A:
        print(i, end=' ')
