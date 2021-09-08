import sys
n = int(input())
arr = list(map(int, input().split()))

current = sys.maxsize
min_step = sys.maxsize

for i in arr:
    step = sum(map(lambda x: abs(x-i), arr))
    if(step < min_step):
        min_step = step
        current = i
print(min_step, current)
