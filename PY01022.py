def solve(n: str):
    n = n.strip()
    n = n.lstrip('-')
    step = 0
    while True:
        s = 0
        for i in n:
            s += int(i)
        n = str(s)
        step += 1
        if(len(n) == 1):
            break
    return step


print(solve(input()))
