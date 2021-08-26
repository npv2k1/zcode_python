t = int(input())
for tt in range(t):
    n = input()
    res = []
    current_char = n[0]
    num_char = 0
    for i in n:
        if(current_char == i):
            num_char += 1
        else:
            res.append(str(num_char)+current_char)
            num_char = 1
            current_char = i
    res.append(str(num_char)+current_char)
    print(''.join(res))
