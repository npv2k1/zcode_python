arr = []
while len(arr) < 10:
    arr = arr + list(map(int, input().split()))
arr = list(map(lambda x: x % 42, arr))

print(len(set(arr)))
