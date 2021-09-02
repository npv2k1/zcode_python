def solve(n: str):
    n = n.strip()
    step = 0
    while True:
        s = 0
        for i in n:
            s += ord(i)-ord('0')
        n = str(s)
        step += 1
        if(len(n) == 1):
            break
    return step


print(solve(input()))
# đề ảo vl dấu '-' cũng cho vào cộng