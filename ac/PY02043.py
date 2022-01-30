for t in range(int(input())):
    n = input()
    k = input()
    len_k = len(k)
    c = 0
    tmp = ""
    i = 0
    while i < len(n):
        tmp = n[i:i+len_k]
        if(tmp == k):
            i += len_k+1
            c += 1
        else:
            i += 1
        tmp = ''
    print(c)
