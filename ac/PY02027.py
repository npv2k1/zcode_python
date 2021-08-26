import re
t = int(input())
arr = []
for tt in range(t):
    s = input()
    tmp_arr = re.split('[a-zA-Z]', s)
    for i in tmp_arr:
        if(i):
            arr.append(int(i))
arr.sort()
for i in arr:
    print(i)
